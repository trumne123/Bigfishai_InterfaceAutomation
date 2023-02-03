from Command.DealData import *
from Command.DealSqlData import *
from Command.DefinedVariable import *


# 获取token
def get_token(json):
    if json['code'] == 200:
        token = json['data']['key']
        write_data = {'token': 'Token ' + token}
        up_data = f'update linked_data set value = "{write_data["token"]}" where title = "token"'
        update_data(up_data)


# 获取用户id
def get_user_id(json):
    if json['code'] == 200:
        user_id = json['data']['id']
        write_data = {'user_id': user_id}
        up_data = f'update linked_data set value = "{write_data["user_id"]}" where title = "user_id"'
        update_data(up_data)


# 获取competition_id
def get_competition_id(json):
    if json['code'] == 200:
        dubbing_content = json['data']['result']
        for dubbing_id in dubbing_content:
            if '自动化专属朗读秀活动' in dubbing_id['title']:
                competition_id = dubbing_id['id']
                write_data = {'competition_id_reading': competition_id}
                update_reading_sql = f'update linked_data set value = "{write_data["competition_id_reading"]}" where title = "competition_id_reading"'
                update_data(update_reading_sql)
            if '自动化专属配音秀活动' in dubbing_id['title']:
                competition_id = dubbing_id['id']
                write_data = {'competition_id_dubbing': competition_id}
                update_dubbing_sql = f'update linked_data set value = "{write_data["competition_id_dubbing"]}" where title = "competition_id_dubbing"'
                update_data(update_dubbing_sql)
            if '自动化专属角色扮演活动' in dubbing_id['title']:
                competition_id = dubbing_id['id']
                write_data = {'competition_id_role_playing': competition_id}
                update_role_sql = f'update linked_data set value = "{write_data["competition_id_role_playing"]}" where title = "competition_id_role_playing"'
                update_data(update_role_sql)


# 获取dubbing_info
def get_dubbing_info(json):
    user_dubbing_id = json['data']['user_dubbing_id']
    write_data = {'user_dubbing_id': user_dubbing_id}
    up_data = f'update linked_data set value = "{write_data["user_dubbing_id"]}" where title = "user_dubbing_id"'
    update_data(up_data)
    for dubbing_info in json['data']['result']:
        title = ''
        eval_type = ''
        content_type = str(dubbing_info['content_type'])
        content_id = str(dubbing_info['id'])
        audio_url = dubbing_info['audio_url']
        if dubbing_info['content_type'] == 0:
            title = dubbing_info['title']
            eval_type = '12'
        if dubbing_info['content_type'] == 1:
            title = dubbing_info['title']
            eval_type = '13'
        elif dubbing_info['content_type'] == 2:
            title = dubbing_info['content']
            eval_type = '14'
        # 把每个原音id+原音下载链接存入test03作为用例，test03用例对该活动所有原音进行，之后处理作为上传评测录音
        write_data_to_04case = [{'id': content_id, 'audio_url': audio_url}]
        # 存入每个音频的评测入参到test04用例中
        write_data_to_05case = [{'url': 'https://www.bigfishai.com:8300/api/voice/speech_evaluation_report/',
                                 'user_dubbing': user_dubbing_id,
                                 'id': content_id,
                                 'title': title,
                                 'eval_type': eval_type,
                                 'content_type': content_type
                                 }]
        # 判断如果是第一条入参，就对用例yaml进行覆盖写入
        if json['data']['result'].index(dubbing_info) == 0:
            cover_data(write_data_to_04case, filepath_variable_path['ReadingShowCase'] + 'test03_download_audio.yaml')
            cover_data(write_data_to_05case,
                       filepath_variable_path['ReadingShowCase'] + 'test04_speech_evaluation_report.yaml')
        # 如果不是第一条，就对yaml进行追加写入
        else:
            add_data(write_data_to_04case, filepath_variable_path['ReadingShowCase'] + 'test03_download_audio.yaml')
            add_data(write_data_to_05case,
                     filepath_variable_path['ReadingShowCase'] + 'test04_speech_evaluation_report.yaml')


def get_competition_info(json):
    video_url = json['data']['video']['res']
    dubbing_src = json['data']['dubbingsrc']
    write_data = {'video_url': video_url, 'dubbing_src': dubbing_src}
    add_data(write_data, filepath_variable_path['LinkedDataPath'])
    up_data1 = f'update linked_data set value = "{write_data["video_url"]}" where title = "video_url"'
    update_data(up_data1)
    up_data2 = f'update linked_data set value = "{write_data["dubbing_src"]}" where title = "dubbing_src"'
    update_data(up_data2)


def get_dubbingsrcv_info(json):
    delete_data('truncate table dubbing_info_data')
    for i in json['data']['dialogue']:
        dialogue_id = i['id']
        title = i['title']
        start_time = i['start_timestamp']
        end_time = i['end_timestamp']
        write_data_to_yaml = [
            {'dialogue_id': dialogue_id, 'title': title, 'start_time': start_time, 'end_time': end_time}]
        if json['data']['dialogue'].index(i) == 0:
            cover_data(write_data_to_yaml, filepath_variable_path['DubbingInfoPath'])
        else:
            add_data(write_data_to_yaml, filepath_variable_path['DubbingInfoPath'])
        in_data = f'insert into dubbing_info_data(dialogue_id, start_time, end_time, title) value({dialogue_id}, "{start_time}", "{end_time}", "{title}")'
        insert_data(in_data)
