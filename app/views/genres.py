from flask import request
from flask_restx import Namespace, Resource

from app.container import genre_service

from app.dao.models.genre import GenreSchema

genre_ns = Namespace('genres')

genres_schema = GenreSchema(many=True)
genre_schema = GenreSchema()


@genre_ns.route('/')
class GenreView(Resource):
    def get(self):
        all_genres = genre_service.get_all()

        return genre_schema.dump(all_genres), 200

    def post(self):
        def post(self):
            req = request.json
            genre_service.create(req)

            return "", 201


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        genre = genre_service.get_one(gid)

        return genre_schema.dump(genre), 200

    def put(self, gid):
        req_json = request.json
        req_json['id'] = gid
        genre = genre_service.update(gid)

        return '', 204

    def patch(self, gid):
        req_json = request.json
        req_json['id'] = gid
        genre = genre_service.update(gid)
        return '', 204


def delete(self, gid):
    genre = genre_service.delete(gid)

    return '', 204
