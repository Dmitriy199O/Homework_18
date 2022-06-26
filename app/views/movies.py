from flask import request
from flask_restx import Namespace, Resource

from app.container import movie_service

from app.dao.models.movie import MovieSchema

movies_ns = Namespace('movies')

movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()


@movies_ns.route('/')
class MovieView(Resource):
    def get(self):
        all_movies = movie_service.get_all()


        return movies_schema.dump(all_movies), 200

    def post(self):
        def post(self):
            req = request.json
            movie_service.create(req)

            return "", 201


@movies_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)

        return movie_schema.dump(movie), 200

    def put(self, mid):
        req_json = request.json
        req_json['id'] = mid
        movie = movie_service.update(mid)

        return '', 204

    def patch(self, mid):
        req_json = request.json
        req_json['id'] = mid
        movie = movie_service.update(mid)
        return '', 204


def delete(self, mid):
    movie = movie_service.delete(mid)

    return '', 204
