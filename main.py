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
    # can you query  the database for the unique question topics, and use that to display the list of choices? 
    topic = input('1: Sports\n'
                  '2: Geography\n'
                  '3: Food/Drink\n')
    topic_num = validation.topic_validation(topic)
    q_ids = get_q_ids(topic_num)

    #print(a_list)

    print('Please enter the number of questions you would like to take by entering the corresponding number:')
    # query the database for the number of questions available for the topic chosen.
    # allow the user to choose any number between 1 and the questions available 
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

    # there is a lot happening in this method - could it be broken into smaller parts? 

    # Storing the questions, choices, and other info in parallel lists is very error prone, and it's hard
    # to understand what the code is doing - for example, it's not immediately obvious what data 
    # topic_name[0][0] may be refering to. 
    # Another approach is making a Question class - one question has the ID, text, correct answer, wrong answers... 
    # then you can pass Question objects, or lists of Question objects, around the program. 
    # See example solution 

    questions = db_manager.get_question_text(question_ids)
    choices = db_manager.get_choices(question_ids)
    # these are lists - use plural names - topic_names, difficulties etc. 
    topic_name, points, difficulty = get_q_info(topic_num, question_ids)
    correct_or_not = ''
    start = time.time()
    start = str(start)  # store this as a number, it will make it much easier to calculate the duration 

    # on topic_name - does this need to be a list? All questions should be on the same topic 

    # if you do need to loop over two or more lists, you can use zip,
    # for question, topic, point_value, difficulty_value, id in zip(questions, topic_name, points, difficulty, question_ids):
    #     print(f'Topic: {topic[0]}')
    #     print(f'Points available: {point_value[0]}')
    #     print(f'Difficulty: {difficulty_value[0]}')
    #     print(question[0])
    #     score = 0
    #  etc....

    # The [0] that you have to do for all of the lists, is because you are returning row objects or lists 
    # of row objects from the DB and those work in the same way as tuples
    # this code would be cleaner if the DB code did more processing and only returned the data needed 

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
            correct_or_not = correct_or_not + 'Yes'  # this is causing text like "YesYesYesYesYes" to be written to the DB
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
    # more work needed here - show the required data, format and present neatly
    print(res)
































main()