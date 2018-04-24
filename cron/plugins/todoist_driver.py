# coding: utf-8
import sys ,os
sys.path.append( os.pardir )
from util.load_config import Config
from pytodoist import todoist
from datetime import datetime, timedelta, date


class TodoistDriver:

    def __init__( self , _token=None , _usr=None ):
        self._token = _token

        self.usr = _usr
        self.projects = None

        self.get_apikey()

    '''
    config.jsonからAPIキーの取得
    '''
    def get_apikey( self ):
        # config = Config('config.json')
        config = Config('../../config.json')

        data = config.todoist()
        self._token = data['api_key']

    '''
    todoistへの接続
    '''
    def conect( self ):
        self.usr = todoist.login_with_api_token(self._token.strip())
        projects = self.usr.get_projects()
        if self.usr:
            print('Todoist Connect complete!')
        else:
            exit()


    '''
    同期
    '''
    def sync( self ):
        self.conect()
        self.usr.sync()
        # 同期後プロジェクトを更新
        self.projects = self.usr.get_projects()


    '''
    usrのタスクの取得
    '''
    def get_usr( self ):
        self.sync()
        return self.usr


    '''
    日付が一週間以内のタスクを取得
    '''
    def get_deadline(self ):
        self.sync()
        # 日付を変えて表示するための埋め込み
        embedding_date = [
                            [-365, 0, '期限切れの'],
                            [0, 1, '今日の'],
                            [1, 3, '三日以内の'],
                            [3, 7, '今週の']]
        # 現在時刻の取得(UTC)
        now = datetime.utcnow()

        # プロジェクトごとにタスクを取得
        content = []
        for project in self.projects:
            for e in embedding_date:
                emb_content = []
                # 近い順に並び替え
                for t in sorted( [ x for x in project.get_tasks() if x.due_date_utc is not None ], key=lambda t:datetime.strptime(t.due_date_utc, '%a %d %b %Y %H:%M:%S +0000')):
                    if datetime.strptime(t.due_date_utc, '%a %d %b %Y %H:%M:%S +0000') >= now + timedelta(days=e[0]) and datetime.strptime(t.due_date_utc, '%a %d %b %Y %H:%M:%S +0000') < now + timedelta(days=e[1]):
                        emb_content.append('\n> ・'+t.date_string+'\t'+t.content)
                if len(emb_content) > 0:
                        emb_content.insert(0, '\n>#'+e[2]+'タスク:')
                content.extend(emb_content)

        return content

    '''
    プロジェクト名に含まれるタスクを取得
    '''
    def get_task(self , project_name ):
        self.sync()
        # プロジェクトごとにタスクを取得
        content = []

        for project in self.projects:
            print( project.name)
            # 個別でタスクを取得するとき
            if not project_name.lower() in project.name.lower() :
                continue;
            for i in project.get_tasks():
                content.append( i )

        return content



    '''
    タスクを探す
    '''
    def find_task( self , task_name):
        self.sync()
        projects = self.projects

        hit_project = []
        hit_task =[]

        for project in projects:
            tasks = project.get_tasks()
            for task in tasks:
                if task_name in task.content:
                    hit_project.append( project )
                    hit_task.append( task )

        return hit_project , hit_task


    '''
    プロジェクトを探す
    '''
    def find_project( self , project_name ):
        self.sync()
        projects = self.projects

        for project in projects:
            if project_name.lower() in project.name.lower():
                return project

        return None

    '''
    Complete
    '''
    def complete_task( self , task_name ):
        hit_project , hit_task = self.find_task( task_name )
        message = ''
        if len(hit_task) == 0:
            message = task_name + "が見つかりません"

            return message
        elif len(hit_task) > 1:
            message = str(len(hit_task)) + "の該当するタスクがありました\n"
            for i in range( len( hit_task ) ):
                    message = message + 'Todoist:'+ hit_project[ i ].name + '=>' + hit_task[ i ].content + '\n'

            return message
        else :
            hit_task[0].complete()
            message = '\nTodoist:'+ hit_project[ 0 ].name + '=>' + hit_task[ 0 ].content + '完了！'

            log_message = '{"type":"task_kill","task_id":' + str(hit_project[ 0 ].id) + '"project_name":"' + hit_project[ 0 ].name + '","task_name":"' + hit_task[ 0 ].content + '","date_added":"' + str(datetime.strptime(hit_task[0].date_added, '%a %d %b %Y %H:%M:%S +0000') + timedelta(hours=9)) \
                            +'","date_archive":"' + str( datetime.now()) + '"}'

            # task_log(log_message)

            return message

    '''
    タスクの追加
    '''
    def add_task( self , project_name , task_name , date = None ):
        project = self.find_project( project_name )
        if project is None:
            return 'No Project'

        task = project.add_task( task_name , date )

        log_message = '{"type":"task_add","task_id":' + str(task.id) + ',project_name":"' + project.name + '","task_name":"' + task_name + '","date_added":"' +  str(datetime.strptime(task.date_added, '%a %d %b %Y %H:%M:%S +0000') + timedelta(hours=9)) \
                            +'","date_deadline":"' +  str(datetime.strptime(task.due_date_utc, '%a %d %b %Y %H:%M:%S +0000') + timedelta(hours=9)) + '"}'

        # task_log(log_message)

        return task_name +' is Adding'
