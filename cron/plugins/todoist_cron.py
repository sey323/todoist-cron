# coding: utf-8
import sys ,os
import datetime
import requests
sys.path.append(os.getcwd())

# 自作モジュールの読み込み
from util.load_config import Config

API_URL = 'http://192.168.8.85:85/'


def add_monthly():
    # 日付の取得
    today = datetime.date.today()
    after_month = today + datetime.timedelta(weeks=+4)
    # Jsonから追加するタスクを取得．
    config = Config('../config.json')
    data = config.todoist()

    for d in data['monthly']:
        response = requests.post( API_URL + 'task/' + d['project'] + \
                                            '/' + d['task'] + "_" + str(today) + \
                                            '/' + str(after_month) )


def add_weekly():
    # 日付の取得
    today = datetime.date.today()
    after_week = today + datetime.timedelta(weeks=+1)
    # Jsonから追加するタスクを取得．
    config = Config('../config.json')
    data = config.todoist()

    for d in data['weekly']:
         response = requests.post( API_URL + 'task/' + d['project'] + \
                                             '/' + d['task'] + "_" + str(today) + \
                                             '/' + str(after_week) )
