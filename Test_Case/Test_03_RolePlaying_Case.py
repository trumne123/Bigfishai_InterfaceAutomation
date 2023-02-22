import json
import time
import pytest
import requests
from Command.DealJson import *
from Command.DealAudioFile import *
from Command.Support_function import *
from requests_toolbelt import MultipartEncoder


@pytest.mark.usefixtures('pre_class_test')
class Test_RolePlaying:
    # 新用户登录
    @pytest.mark.skip('pass')
    def test01_new_login(self):
        json_data = []
        request_data = read_data(filepath_variable_path['testData'] + 'login.yaml')
        request_url = request_data['url']
        for user_phone in create_role_user():
            request_data['param']['telephone'] = user_phone
            request_param = request_data['param']
            response = requests.post(url=request_url, json=request_param)
            json_data.append(response.json())
        get_token(json_data)
        print('完成新用户登录')

    # 班级码查询班级
    @pytest.mark.parametrize('case_data', read_data(filepath_variable_path['RolePlayingCase'] + 'test02_klass.yaml'))
    def test02_klass(self, case_data):
        request_url = case_data['url']
        access_token = list(query_data(f'select value from linked_data where title = "custom_token"')[0][0])
        print(access_token)
        print(type(access_token))
        # for token in access_token:
            # case_data['header']['Authorization'] = 'Token ' + token
            # request_header = case_data['header']
            # response = requests.get(url=request_url, headers=request_header)
            # print('完成查询klass')
            # print(response.json())
            # print(token)

    # 加入班级
    @pytest.mark.skip('pass')
    @pytest.mark.parametrize('case_data', read_data(filepath_variable_path['RolePlayingCase'] + 'test03_bind_klass.yaml'))
    def test03_bind_klass(self, case_data):
        request_url = case_data['url']
        access_token = query_data(f'select value from linked_data where title = "custom_token"')[0][0]
        for token in access_token:
            case_data['header']['Authorization'] = 'Token ' + token
            request_header = case_data['header']
            case_data['param']['realname'] = create_realname()
            request_param = case_data['param']
            response = requests.get(url=request_url, params=request_param, headers=request_header)
            print(response.request.url)
            print(response.request.body)
            print(response.json())

    # 创建小组
    @pytest.mark.skip('pass')
    @pytest.mark.parametrize('user_phone', create_role_user())
    def test01_group(self, user_phone):
        json_data = []
        request_url = read_data(filepath_variable_path['DubbingShowCase'] + 'test01_competition.yaml')
        request_param = {
            'telephone': user_phone,
            'verify_code': '209394',
            'wechar_info2_id': '',
            'apple_info_id': 0
        }
        response = requests.post(url=request_url, json=request_param)
        json_data.append(response.json())
        get_token(json_data)
        print('完成登录，获取token')

    # 根据小组码获取小组信息
    def test02_get_by_code(self):
        print('完成get_by_code测试！')

    # 修改小组(加入小组，退出小组，解散小组)
    def test03_group_edit(self):
        print('完成group_edit测试！')

    # 获取小组信息(加入小组后)
    def test04_group_id(self):
        print('完成group_id测试！')

    # 加载角色扮演内容
    def test05_redirect_type_5(self):
        print('完成redirect_type_5测试！')

    # 试听下载活动所有原音
    def test06_download_audio(self):
        print('完成download_audio测试！')

    # 修改小组(加入小组，退出小组，解散小组)
    def test07_group_edit(self):
        print('完成group_edit测试！')

    # 发起配音评测
    def test08_speech_evaluation_report(self):
        print('完成speech_evaluation_report测试！')

    # 提交配音
    def test09_commit(self):
        print('完成commit测试！')

    # 获取用户作答记录
    def test10_get_user_record_5(self):
        print('完成get_user_record_5测试！')

    # 获取小组排行榜详情
    def test11_get_ranking_detail_group(self):
        print('完成get_ranking_detail_group测试！')

    # 查询小组排行榜详情
    def test12_get_ranking_detail(self):
        print('完成get_ranking_detail测试！')
