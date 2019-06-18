# encoding=utf8
import sys ,os
import requests
sys.path.append(os.getcwd())
from plugins.slack_driver import SlackDriver

# 初期化
sk = SlackDriver()
API_URL = 'http://192.168.8.85:85/'

response = requests.get( API_URL + 'todo' )
print(response)
sk.slack_call( response.text )
