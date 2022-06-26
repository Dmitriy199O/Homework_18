from app.create_db import db
from app.dao.movie import MovieDAO
from app.dao.genre import GenreDAO
from app.dao.director import DirectorDAO
from app.dao.services.movie import MovieService
from app.dao.services.genre import GenreService
from app.dao.services.director import DirectorService

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)
