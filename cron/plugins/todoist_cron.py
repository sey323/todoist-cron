# coding: utf-8
import sys ,os
sys.path.append(os.getcwd())
import datetime

# 自作モジュールの読み込み
from plugins.todoist_driver import TodoistDriver
from util.load_config import Config

todoist = TodoistDriver()


def add_monthly():
    # 日付の取得
    today = datetime.date.today()
    after_month = today + datetime.timedelta(weeks=+1)
    # Jsonから追加するタスクを取得．
    config = Config('../config.json')
    data = config.todoist()

    for d in data['monthly']:
        todoist.add_task( d['project'] , d['task'] + "_" + str(today) , after_month )

def add_weekly():
    # 日付の取得
    today = datetime.date.today()
    after_week = today + datetime.timedelta(weeks=+1)
    # Jsonから追加するタスクを取得．
    config = Config('../config.json')
    data = config.todoist()

    for d in data['weekly']:
        todoist.add_task( d['project'] , d['task'] + "_" + str(today) , after_week )
