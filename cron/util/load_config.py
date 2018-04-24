# coding: utf-8
import json

# Jsonファイルの読み込み用のクラス
class Config:

    def __init__( self , _filename = "config.json"):
        self._filename = _filename
        self._data = self.load_json()

    def load_json( self ):
        f = open( self._filename )
        json_data = json.load( f )

        f.close()
        return json_data

    def slack( self ):
        return self._data["slack"]

    def todoist(self):
        return self._data["todoist"]

#config = Config()
#print(config.todoist())
#print(config.toggl())
