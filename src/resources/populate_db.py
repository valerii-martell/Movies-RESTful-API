import datetime
import threading

import bs4
import requests
from flask_restful import Resource

from src import db
from src.services.movie_service import MovieService
# from concurrent.futures.thread import ThreadPoolExecutor as PoolExecutor
from concurrent.futures.process import ProcessPoolExecutor as PoolExecutor


class MoviesParser:
    url = 'https://www.imdb.com/'

    def get_movies_urls(self):
        print('Getting movie urls', flush=True)
        url = self.url + 'chart/top/'
        resp = requests.get(url)
        resp.raise_for_status()

        html = resp.text
        soup = bs4.BeautifulSoup(html, features='html.parser')
        movie_containers = soup.find_all('td', class_='posterColumn')
        movie_links = [movie.a.attrs['href'] for movie in movie_containers][:10]

        return movie_links

    def parse_movies(self, movie_urls):
        movies_to_create = []
        for url in movie_urls:
            url = self.url + url
            print(f'Getting a detailed info about the movie - {url}')
            movie_content = requests.get(url)
            movie_content.raise_for_status()

            html = movie_content.text
            soup = bs4.BeautifulSoup(html, features="html.parser")
            title, _ = soup.find('div', class_='originalTitle').text.split('(')
            rating = float(soup.find('div', class_='ratingValue').strong.text)
            description = soup.find('div', class_='summary_text').text.strip()
            title_bar = soup.find('div', class_='titleBar').text.strip()
            title_content = title_bar.split('\n')
            release_date, _ = title_content[-1].split('(')
            release_date = datetime.datetime.strptime(release_date.strip(), '%d %B %Y')
            length = self._convert_time(soup.find('div', class_='subtext').time.text.strip())
            print(f'Received information about - {title}', flush=True)
            movies_to_create.append(
                {
                    'title': title,
                    'rating': rating,
                    'description': description,
                    'release_date': release_date,
                    'length': length,
                    'distributed_by': 'Warner Bros. Pictures',
                }
            )
        return movies_to_create

    @staticmethod
    def populate_db_with_movies(movies):
        return MovieService.bulk_create_movies(db.session, movies)

    @staticmethod
    def _convert_time(time: str) -> float:
        hour, minute = time.split('h')
        minutes = (60 * int(hour)) + int(minute.strip('min'))
        return minutes


class PopulateDB(Resource, MoviesParser):

    def post(self):
        t0 = datetime.datetime.now()
        movies_urls = self.get_movies_urls()
        movies = self.parse_movies(movies_urls)
        created_movies = self.populate_db_with_movies(movies)
        dt = datetime.datetime.now() - t0
        print(f'Done in {dt.total_seconds():.2f} sec.')
        return {'message': f'Database were populated with {created_movies} movies'}, 201


class PopulateDBThreads(Resource, MoviesParser):

    def post(self):
        threads = []
        movies_to_create = []
        movie_urls = self.get_movie_urls()

        t0 = datetime.datetime.now()
        for movie_url in movie_urls:
            threads.append(threading.Thread(target=self.parse_movies, args=(movie_url, movies_to_create), daemon=True))
        [t.start() for t in threads]
        [t.join() for t in threads]
        created_movies = self.populate_db_with_movies(movies_to_create)

        dt = datetime.datetime.now() - t0
        print(f"Done in {dt.total_seconds():.2f} sec.")

        return {'message': f'Database were populated with {created_movies} movies. '
                           f'Done in {dt.total_seconds():.2f} sec.'}, 201


class PopulateDBProcesses(Resource, MoviesParser):

    def post(self):
        work = []
        movie_urls = self.get_movie_urls()

        t0 = datetime.datetime.now()
        with PoolExecutor() as executor:
            for movie_url in movie_urls:
                f = executor.submit(self.parse_movies, movie_url)
                work.append(f)
        movies_to_create = [f.result() for f in work]
        created_movies = self.populate_db_with_movies(movies_to_create)

        dt = datetime.datetime.now() - t0
        print(f"Done in {dt.total_seconds():.2f} sec.")

        return {'message': f'Database were populated with {created_movies} movies. '
                           f'Done in {dt.total_seconds():.2f} sec.'}, 201

