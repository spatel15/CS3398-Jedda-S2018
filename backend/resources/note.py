from flask_restful import Resource, reqparse
from models.note import NoteModel

parser = reqparse.RequestParser()
parser.add_argument(
    'title',
    type=str,
    required=True)
parser.add_argument(
    'username',
    type=str,
    required=True)
parser.add_argument(
    'body',
    type=str,
    required=True)
parser.add_argument(
    'subject', 
    type=str,
    required=True)
parser.add_argument(
    'active',
    type=bool)

class GetNote(Resource):
    def get(self, id):
        note = NoteModel.find_by_id(id)

        if note:
            return {'note': note.json()}, 200
        return {'error': 'Note not found'}, 404

class GetNotes(Resource):
    def get(self, username):
        notes = NoteModel.find_by_username(username)

        if notes:
            return {'notes': notes.jsonlist()}, 200
        return {'error': 'No notes for this user'}, 404

class CreateNote(Resource):
    def post(self):
        args = parser.parse_args()

        if args:
            new_note = NoteModel(args)
            
            return {'message': 'Note added'}, 200
        return {'error': 'note unable to be added'}

class UpdateNote(Resource):
    def put(self, id):
        args = parser.parse_args()

        note = NoteModel.find_by_id(id)

        if note:
            note.title = args['title']
            note.subject = args['subject']
            note.body = args['body']
            note.active = args['active']

            note.save_to_db()

            return {'message': 'note updated'}, 200
        return {'error': 'note not found'}, 400


