import os

from src import app

if __name__ == "__main__":
    port = os.environ.get('PORT', 8000)
    app.run(debug=True, host='0.0.0.0')

