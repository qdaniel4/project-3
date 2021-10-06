import db_manager
import validation

def main():

    first_name = input('Please enter your first name: ')
    first_name_val = validation.name_validation(first_name)
    last_name = input('Please enter your last name: ')
    last_name_val = validation.name_validation(last_name)
    db_manager.add_user(first_name_val, last_name_val)


    print('Please enter your topic of choice by entering the corresponding number:')
    topic = input('1: \n'
                  '2: \n'
                  '3: \n')
    topic_num = validation.topic_and_answer_validation(topic)

    print('Please enter the number of questions you would like to take by entering the corresponding number:')
    question_amount = input('1: 3 Questions \n'
                            '2: 5 Questions \n')
    question_amount_num = validation.question_num_validation(question_amount)

def get_q_ids(topic_num):
    question_ids = db_manager.get_question_ids(topic_num)
    return question_ids

def get_q_info(topic_num, question_ids):
    topic_name = db_manager.get_topic_by_id(topic_num)
    points_list = db_manager.get_points_for_question(question_ids)
    diff_list = db_manager.get_difficulty(question_ids)
    correct_answers = db_manager.get_answer(question_ids)
    return topic_name, points_list, diff_list, correct_answers


def show_q_info(topic_num, question_ids):
    print('The quiz will begin now...')
    print('please enter the corresponding number for the multiple choice answer...\n')
    questions = db_manager.get_question_text(question_ids)
    choices = db_manager.get_choices(question_ids)
    topic_name, points, difficulty, correct_answers = get_q_info(topic_num, question_ids)
    answer_list = []

    for question in range(len(questions)):
        print(f'Topic: {topic_name}')
        print(f'Points available: {points[question]}')
        print(f'Difficulty: {difficulty[question]}')
        print(questions[question])
        counter = 0
        for choice in range(len(choices[question])):
            print(f'{choice + 1}: {choices[question][choice]}')
        answer = input('Please enter answer')
        answer_val = validation.topic_and_answer_validation(answer)
        check_answers(answer, correct_answers)
        counter = counter + answer_val
        answer_list.append(choices[question][counter -1])

    return answer_list

def check_answers(user_answer, correct_answers):
    for answer in range(len(correct_answers)):
        if user_answer != correct_answers[answer]:
            print(f'Incorrect\nThe correct answer was {correct_answers[answer]}')
        else:
            print('Correct!')


























main()