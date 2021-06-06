import Questions


def user_questionnaire():
    user_answer = []
    for q in Questions.question_list:
        user_answer.append(q.ask())
    return user_answer


print(user_questionnaire())
