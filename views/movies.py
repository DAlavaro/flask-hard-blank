from flask import Flask
from flask_restx import Resource, Namespace

movie_ns = Namespace('movies')

@movie_ns.route('/')
class MoviesView(Resource):

    def get(self):
        return 'hello world'



@movie_ns.route('/int:mid')
class MoviesView(Resource):

    def get(self, mid):
        return f'hello world {mid}'