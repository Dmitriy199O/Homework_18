# from app.dao.models.movie import Movie
# from app.dao.models.genre import Genre
# from app.dao.models.director import Director
# from app.create_db import db
#
#
#
# def load_data():
#     movie_1 = Movie(title="", description="", trailer="",
#                     rating=4.5,
#                     genre_id=16, director_id=16)
#
#
#     db.create_all()
#     with db.session.begin():
#         db.session.add_all([movie_1, movie_2])
