import db_manager
import validation
import time

def main():

    first_name = input('Please enter your first name: ')
    first_name_val = validation.name_validation(first_name)
    last_name = input('Please enter your last name: ')
    last_name_val = validation.name_validation(last_name)
    db_manager.add_user(first_name_val, last_name_val)


    print('Please enter your topic of choice by entering the corresponding number:')
    topic = input('1: Sports\n'
                  '2: Geography\n'
                  '3: Food/Drink\n')
    topic_num = validation.topic_validation(topic)
    q_ids = get_q_ids(topic_num)

    #print(a_list)

    print('Please enter the number of questions you would like to take by entering the corresponding number:')
    question_amount = input('1: 3 Questions \n'
                            '2: 5 Questions \n')
    question_amount_num = validation.question_num_validation(question_amount)
    show_q_info(topic_num, q_ids)
    get_results()

def get_q_ids(topic_num):
    question_ids = db_manager.get_question_ids(topic_num)
    return question_ids

def get_q_info(topic_num, question_ids):
    topic_name = db_manager.get_topic_by_id(topic_num)
    points_list = db_manager.get_points_for_question(question_ids)
    diff_list = db_manager.get_difficulty(question_ids)
    #correct_answers = db_manager.get_answer(question_ids)
    return topic_name, points_list, diff_list


def show_q_info(topic_num, question_ids):
    print('The quiz will begin now...')
    print('please enter the corresponding number for the multiple choice answer...\n')
    questions = db_manager.get_question_text(question_ids)
    choices = db_manager.get_choices(question_ids)
    topic_name, points, difficulty = get_q_info(topic_num, question_ids)
    correct_or_not = ''
    start = time.time()
    start = str(start)

    for question in range(len(questions)):
        print(f'Topic: {topic_name[0][0]}')
        print(f'Points available: {points[question][0]}')
        print(f'Difficulty: {difficulty[question][0]}')
        print(questions[question][0])
        score = 0



        for choice in range(len(choices[question])):
            print(f'{choice + 1}: {choices[question][choice]}')

        answer = input('Please enter answer: \n')
        answer_val = validation.answer_validation(answer)

        answer_str = choices[question][answer_val-1]
        correct_ans = db_manager.check_answer(question_ids[question][0])
        result = check_user_answer(answer_str, correct_ans)

        score = score + points_added(result, points[question][0])
        if result:
            correct_or_not = correct_or_not + 'Yes'
        else:
            correct_or_not = correct_or_not + 'No'
        end = str(time.time())


        db_manager.add_results(question_ids[question][0], score, correct_or_not,start, end)




def check_user_answer(user_ans, correct_ans):
    if user_ans != correct_ans[0]:
        print(f'\nIncorrect\n\nThe correct answer was {correct_ans[0]}\n\n')
        return False
    else:
        print('\nCorrect!\n')
        return True

def points_added(result, points):
    score = 0
    if result:
        score = score + points
    else:
        points = 0
        score = score + points
    return score

def get_results():
    res = db_manager.show_results()
    print(res)
































main()