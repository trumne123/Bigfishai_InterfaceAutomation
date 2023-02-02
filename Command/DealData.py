import yaml


# 读取数据
def read_data(filepath):
    try:
        f = open(filepath, 'r', encoding='utf-8')
        get_data = yaml.load(stream=f.read(), Loader=yaml.FullLoader)
        return get_data
    except Exception as e:
        print('数据读取失败', e)


# 追加写入数据
def add_data(write_data, filepath):
    try:
        f = open(filepath, 'a', encoding='utf-8')
        yaml.dump(write_data, stream=f, allow_unicode=True)
    except Exception as e:
        print('数据写入失败', e)


# 覆盖写入数据
def cover_data(write_data, filepath):
    try:
        f = open(filepath, 'w', encoding='utf-8')
        yaml.dump(write_data, stream=f, allow_unicode=True)
    except Exception as e:
        print('数据写入失败', e)
