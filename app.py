"""
Run App
"""
from app.main import create_app

from config import settings

app = create_app()

if __name__ == "__main__":
    app.run(debug=settings.DEBUG, port=settings.PORT, host=settings.HOST)
