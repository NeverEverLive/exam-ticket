from flask import Blueprint, Response, request
from json import dumps
from src.operators.answers import create_answer
from src.operators.questions import create_question

api = Blueprint('documents', __name__)


@api.route('/', methods=["GET"])
def index():
    return Response(
        dumps({"message": "test"}),
        status=200,
        content_type='application/json'
    )


@api.post('/answer')
def create_answer_endpoint():
    data = create_answer(request.get_json())
    return Response(
        dumps(data), 
        status=201, 
        content_type='application/json'
        )
    

@api.post('/question')
def create_question_endpoint():
    data = create_question(request.get_json())
    return Response(
        dumps(data), 
        status=201, 
        content_type='application/json'
        )
