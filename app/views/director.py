from flask import request, jsonify
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

        return directors_schema.dump(all_directors), 200

    def post(self):
        data = request.get_json()
        director_service.create(data)
        director_id= data['id']
        response = jsonify()
        response.status_code = 201
        response.headers['location'] = f'/{director_id}'
        return response


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        director = director_service.get_one(did)

        return director_schema.dump(director), 200

    def put(self,did):
        data = request.json
        data['id'] = did
        director_service.update(data,did)

        return '', 204

    def patch(self, did):
        data = request.json
        data['id'] = did
        director_service.update(data,did)
        return '', 204


    def delete(self, did):
        director_service.delete(did)

        return '', 204
