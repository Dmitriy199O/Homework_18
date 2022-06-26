from flask import request
from flask_restx import Namespace, Resource

from app.container import director_service

from app.dao.models.director import DirectorSchema

director_ns = Namespace('directors')

directors_schema = DirectorSchema(many=True)
director_schema = DirectorSchema()


@director_ns.route('/')
class DirectorView(Resource):
    def get(self):
        all_directors = director_service.get_all()

        return director_schema.dump(all_directors), 200

    def post(self):
        def post(self):
            req = request.json
            director_service.create(req)

            return "", 201


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        director = director_service.get_one(did)

        return director_schema.dump(director), 200

    def put(self, did):
        req_json = request.json
        req_json['id'] = did
        director = director_service.update(did)

        return '', 204

    def patch(self, did):
        req_json = request.json
        req_json['id'] = did
        director = director_service.update(did)
        return '', 204


def delete(self, did):
    director = director_service.delete(did)

    return '', 204
