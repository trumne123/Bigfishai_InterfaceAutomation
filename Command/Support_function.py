from Command.DealSqlData import *


# 更新url
def update_url(case_data, key):
    if key == 'reading':
        compition_id = query_data(f'select value from linked_data where title = "competition_id_reading"')[0][0]
        case_data['url'] = case_data['url'].replace('competition_id', compition_id)
        return case_data
    elif key == 'dubbing':
        compition_id = query_data(f'select value from linked_data where title = "competition_id_dubbing"')[0][0]
        case_data['url'] = case_data['url'].replace('competition_id', compition_id)
        return case_data
    elif key == 'dubbing_src':
        dubbing_src = query_data(f'select value from linked_data where title = "dubbing_src"')[0][0]
        case_data['url'] = case_data['url'].replace('dubbing_src', dubbing_src)
        return case_data


# 更新token
def update_token(case_data):
    new_token = query_data(f'select value from linked_data where title = "token"')[0][0]
    case_data['header']['Authorization'] = new_token
    return case_data


def update_competition_id(case_data):
    compition_id = query_data(f'select value from linked_data where title = "competition_id_dubbing"')[0][0]
    case_data['param']['competition_id'] = compition_id
    return case_data


# 打包评测文本
def get_speech_data():
    dubbing_info_data = query_data('select dialogue_id,title from dubbing_info_data')
    speech_data = []
    for dubbing_data in dubbing_info_data:
        ad = {
            'name': dubbing_data[1],
            'typeThres': 4,
            'user': query_data('select value from linked_data where title = "user_id"')[0][0],
            'eval_type': 2,
            'audio_type': 1,
            'content_type': 1,
            'content_type_id': dubbing_data[0],
            'competition': query_data('select value from linked_data where title = "competition_id_dubbing"')[0][0]
        }
        speech_data.append(ad)
    return speech_data


def deal_score(score):
    # 计算平均分=(总分/人数)取整
    get_score = round(sum(score) / len(score))
    update_data(f'update linked_data set value = {get_score} where title = "score"')
