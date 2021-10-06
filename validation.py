def topic_and_answer_validation(user_input):
    while user_input.isnumeric() is False or int(user_input) <= 0 or int(user_input) > 3:
        print('Please enter a whole number between 1 & 3:')
        user_input = input()
    user_input = int(user_input)
    return user_input

def question_num_validation(question_input):
    while question_input.isnumeric() is False or int(question_input) <= 0 or int(question_input) > 2:
        print('Please enter a whole number between 1 & 2:')
        question_input = input()
    question_input = int(question_input)
    return question_input

def name_validation(name):
    while name == '':
        print('This field cannot be blank: ')
        name = input()
    return name