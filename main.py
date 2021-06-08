import heapq

import Questions
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import pairwise_distances

import xlrd
import openpyxl

# globals:
payment_question = "כמה אתה מעוניין לשלם עבור שכר לימוד בשנה?"
payment_answers = {"10,000 - 20,000": 1, "20,000 - 30,000": 2, "30,000 - 40,000": 3, "40,000 ומעלה": 4}
final_question = 'היכן אתה לומד/למדת?'
academic_institution = ""


def get_data(user_lst):
    df = pd.read_excel("train1.xlsx")
    # save results and delete from DataFrame
    results = df[final_question]
    df = df.loc[:, df.columns != final_question]
    # add current user
    user_index = df.shape[0]
    df.loc[df.shape[0]] = user_lst
    # replace payment question to integer:
    for ans in payment_answers:
        df[payment_question].replace({ans: payment_answers[ans]}, inplace=True)
    return user_index, results, df


def min_max_normalization(x, column_name):
    if x.max() != x.min():
        users_data[column_name] = (x - x.min()) / (x.max() - x.min())
    else:
        users_data[column_name] = 1


def replace_to(val_to_one, column_name):
    rest = (np.unique(
        np.delete(users_data[column_name].values, np.where(users_data[column_name].values == val_to_one)))).tolist()
    users_data[column_name].replace(rest, 0, inplace=True)
    users_data[column_name].replace({val_to_one: 1}, inplace=True)


def user_questionnaire():
    user_answer = []
    for q in Questions.question_list:
        user_answer.append(q.ask())
    return user_answer


def keep_top_k(arr, k):
    smallest = heapq.nlargest(k, arr)[-1]
    # replace anything lower than the cut off with 0
    arr[arr < smallest] = 0
    return arr


user_answers = user_questionnaire()
index, users_results, users_data = get_data(user_answers)
for i, q in enumerate(Questions.question_list):
    if q.function == "replace":
        # users_data.iloc[:, i]
        replace_to(user_answers[i], users_data.columns[i])
    else:
        min_max_normalization(users_data.iloc[:, i], users_data.columns[i])
user_similarity = 1 - pairwise_distances(users_data, metric='euclidean')

# user_similarity = keep_top_k(np.array(user_similarity[index]), 2)
