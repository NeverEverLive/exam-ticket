from src.models.answer import Answer, AnswerSchema


def create_answer(data):
    serializer = AnswerSchema()
    data = serializer.dump(data)

    new_answer = Answer().fill(**data)
    new_answer.save()

    output_data = {
        'success': True,
        'message': 'Answer created'
    }

    return output_data

def get_answer(data):
    pass


def get_all_answers(data):
    pass


def update_answer(data):
    pass

def delete_answer(data):
    pass
