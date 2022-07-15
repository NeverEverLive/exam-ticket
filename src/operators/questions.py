from src.models.question import Question, QuestionSchema


def create_question(data):
    serializer = QuestionSchema()
    data = serializer.dump(data)

    new_answer = Question().fill(**data)
    new_answer.save()

    output_data = {
        'success': True,
        'message': 'Question created'
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
