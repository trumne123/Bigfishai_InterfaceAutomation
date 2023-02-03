from Command.DealSqlData import *


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


def update_token(case_data):
    new_token = query_data(f'select value from linked_data where title = "token"')[0][0]
    case_data['header']['Authorization'] = new_token
    return case_data
