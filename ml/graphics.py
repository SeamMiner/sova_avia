import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plt_correct_ans(course, topic, question, id, start_date, stop_date):
    cnx = sqlite3.connect('Data/db.sqlite3') #тут путь к БД
    df = pd.read_sql_query("SELECT * FROM admin_panel_result", cnx)
    del df['id']
    plt.title("Ответы пользователя: " + str(id) + ", по курсу: " + str(course)
              + ", по теме: " + str(topic) + ", по вопросу: " + str(question))
    if id != 'all':
        df = df[df['user_id'] == id]
    if course != 'all':
        df = df[df['course_id'] == course]
    if topic != 'all':
        df = df[df['topic_id'] == topic]
    if question != 'all':
        df = df[df['question_id'] == question]
    df = df[df['pass_date'] >= start_date]
    df = df[df['pass_date'] <= stop_date]
    fig = sns.countplot(x='correct_answer', data=df)
    fig.figure.savefig('output.png')
    del(fig)
    del(df)

def plt_time(course, topic, id, start_date, stop_date):
    cnx = sqlite3.connect('Data/db.sqlite3') #тут путь к БД
    df = pd.read_sql_query("SELECT * FROM admin_panel_result", cnx)
    del df['id']
    if id != 'all':
        df = df[df['user_id'] == id]
    if course != 'all':
        df = df[df['course_id'] == course]
    if topic != 'all':
        df = df[df['topic_id'] == topic]
    df = df[df['pass_date'] >= start_date]
    df = df[df['pass_date'] <= stop_date]

    time = list(range(11))
    for i in range(1, 11):
        buf = df[df['question_id'] == i]
        time[i] = buf['spent_time'].mean()
    plt.xlabel('id вопроса')
    plt.ylabel('время [c]')
    plt.title("Время пользователя: " + str(id) + ", на тест по курсу: " + str(course)
              + ", по теме: " + str(topic))
    plt.plot(time)
    plt.savefig('output.png')
    del(df)
    del(buf)

course = 1
topic = 1
question = 'all'
id = 1
start_date = '2020-05-01'
stop_date = '2020-05-10'
plt_correct_ans(course, topic, question, id, start_date, stop_date)
