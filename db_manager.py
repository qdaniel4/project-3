import sqlite3
import random

conn = sqlite3.connect('quiz_data_questions_db.db')

def add_user(first_name, last_name):

    insert_string = 'insert into users (user_firstname, user_lastname) values (?, ?)'

    try:
        with sqlite3.connect('quiz_data_questions_db.db') as con:
            res = con.execute(insert_string, (first_name, last_name) )
    except sqlite3.IntegrityError as e:
        print(f'Error adding user because of {e}\n')
    finally:
        con.close()



def get_topic_by_id(topic_num):

    select_string = 'select topic_name from topics where topic_id == ?'

    try:
        with sqlite3.connect('quiz_data_questions_db.db') as con:
            cursor = con.execute(select_string, (topic_num,))
            topic_name = cursor.fetchall()
    except sqlite3.IntegrityError as e:
        print(f'Error fetching topic because of {e}\n')
    finally:
        con.close()
    return topic_name


def get_question_ids(topic_num):

    select_string = 'select question_id from questions where topic_id = ?'

    try:
        with sqlite3.connect('quiz_data_questions_db.db') as con:
            res = con.execute(select_string, (topic_num,))
            question_ids = res.fetchall()
    except sqlite3.IntegrityError as e:
        print(f'Error fetching question ID because of {e}\n')
    finally:
        con.close()
    return question_ids

def get_question_text(question_ids):

    select_string = 'select question_text from questions where question_id = ?'
    q_text_list = []

    try:
        with sqlite3.connect('quiz_data_questions_db.db') as con:
            for q_text in range(len(question_ids)):
                res = con.execute(select_string, question_ids[q_text])
                question_text = res.fetchone()
                q_text_list.append(question_text)
    except sqlite3.IntegrityError as e:
        print(f'Error fetching question text because of {e}\n')
    finally:
        con.close()
    return q_text_list

def get_points_for_question(question_ids):

    select_string = 'select points from questions where question_id == ?'
    q_point_list = []

    try:
        with sqlite3.connect('quiz_data_questions_db.db') as con:
            for points in range(len(question_ids)):
                res = con.execute(select_string, question_ids[points])
                q_points = res.fetchone()
                q_point_list.append(q_points)
    except sqlite3.IntegrityError as e:
        print(f'Error fetching question points because of {e}\n')
    finally:
        con.close()
    return q_point_list

def get_difficulty(question_ids):

    select_string = 'select difficulty from questions where question_id == ?'
    q_diff_list = []

    try:
        with sqlite3.connect('quiz_data_questions_db.db') as con:
            for diff in range(len(question_ids)):
                res = con.execute(select_string, question_ids[diff])
                q_diff = res.fetchone()
                q_diff_list.append(q_diff)
    except sqlite3.IntegrityError as e:
        print(f'Error fetching question difficulty because of {e}\n')
    finally:
        con.close()
    return q_diff_list

def get_choices(question_ids):

    select_string = 'select correct_answer, wrong_answer1, wrong_answer2, wrong_answer3 from choices where choice_id = ?'
    choice_list = []

    try:
        with sqlite3.connect('quiz_data_questions_db.db') as con:
            for choice in range(len(question_ids)):
                res = con.execute(select_string, question_ids[choice])
                choices = res.fetchone()
                choice_list.append(choices)
    except sqlite3.IntegrityError as e:
        print(f'Error fetching question choices because of {e}\n')
    finally:
        con.close()
    return choice_list

def check_answer(question_id):
    select_correct = 'select correct_answer from choices where choice_id == ?'


    try:
        with sqlite3.connect('quiz_data_questions_db.db') as con:
            res = con.execute(select_correct, (question_id, ))
            correct_answer = res.fetchone()
    except sqlite3.IntegrityError as e:
        print(f'Error fetching correct answer because of {e}\n')
    finally:
        con.close()
    return correct_answer

def get_session_info():
    print()