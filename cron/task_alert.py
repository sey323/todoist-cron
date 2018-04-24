# encoding=utf8
import sys ,os
sys.path.append(os.getcwd())
from plugins.todoist_driver import TodoistDriver
from plugins.slack_driver import SlackDriver

# 初期化
sk = SlackDriver()
todoist = TodoistDriver()

content = todoist.get_deadline()
send_text = "現在のタスクを通知します．\n"
for i in content:
        send_text += str(i)

sk.slack_call( send_text )
