# encoding=utf8
import sys ,os
sys.path.append(os.getcwd())
from plugins.todoist_cron import add_monthly
from plugins.slack_driver import SlackDriver

add_monthly()
# 初期化
sk = SlackDriver()

# 一応スラックに通知
sk.slack_call( '今月のタスクを追加しました．' )
