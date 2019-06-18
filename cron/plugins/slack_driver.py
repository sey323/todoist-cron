import sys
from slacker import Slacker
from util.load_config import Config


class SlackDriver:

    def __init__( self , _api_key = None , _usr_name = None):
        self._usr = None
        self._token = _api_key
        self._usr_name = _usr_name
        self._channel = None
        self._icon = None

        self.get_apikey()
        self.connect()

    '''
    config.jsonからAPIキーの取得
    '''
    def get_apikey( self ):
        config = Config('../../config.json')
        #config = Config('config.json') #実験用
        data = config.slack()
        self._token = data['api_key']
        self._usr_name = data['name']
        self._channel = data['channel']
        self._icon = data['icon']

    '''
    Slackに接続
    '''
    def connect( self ):
        self._usr = Slacker(self._token)
        print('Slack Connect Complete!')


    '''
    スラックに通知
    '''
    def slack_call( self , content  ):
         # 送信するユーザの決定
        channel = '#' + self._channel
        icon = ":" + self._icon + ":"
        self._usr.chat.post_message( channel , content , username = self._usr_name ,  icon_emoji=icon)
