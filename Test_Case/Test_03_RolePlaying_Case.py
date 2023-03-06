import json
import time
import pytest
import requests
from Command.DealJson import *
from Command.DealAudioFile import *
from Command.Support_function import *
from requests_toolbelt import MultipartEncoder


# @pytest.mark.usefixtures('pre_class_test')
# @pytest.mark.skip('Test_RolePlaying跳过！')
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
    @pytest.mark.skip('pass')
    @pytest.mark.parametrize('case_data', read_data(filepath_variable_path['RolePlayingCase'] + 'test02_klass.yaml'))
    def test02_klass(self, case_data):
        request_url = case_data['url']
        for token in get_access_token(0):
            case_data['header']['Authorization'] = 'Token ' + token
            request_header = case_data['header']
            response = requests.get(url=request_url, headers=request_header)
            print(response.json())
        print('完成查询klass')

    # 加入班级
    @pytest.mark.skip('pass')
    @pytest.mark.parametrize('case_data', read_data(filepath_variable_path['RolePlayingCase'] + 'test03_bind_klass.yaml'))
    def test03_bind_klass(self, case_data):
        request_url = case_data['url']
        for token in get_access_token(0):
            case_data['header']['Authorization'] = 'Token ' + token
            request_header = case_data['header']
            case_data['param']['realname'] = create_realname()
            request_param = case_data['param']
            response = requests.get(url=request_url, params=request_param, headers=request_header)
            print(response.json())
        print('完成加入班级')

    # 创建小组
    @pytest.mark.skip('pass')
    @pytest.mark.parametrize('case_data', read_data(filepath_variable_path['RolePlayingCase'] + 'test04_group.yaml'))
    def test04_group(self, case_data):
        request_data = update_competition_id(case_data, 'role')
        access_token = get_access_token(1)
        request_url = request_data['url']
        request_param = request_data['param']
        request_data['header']['Authorization'] = 'Token ' + access_token
        request_header = request_data['header']
        response = requests.post(url=request_url, headers=request_header, json=request_param)
        get_group_info(response.json())
        print(response.json())
        print('完成group测试')

    # 根据小组码获取小组信息
    @pytest.mark.skip('pass')
    @pytest.mark.parametrize('case_data', read_data(filepath_variable_path['RolePlayingCase'] + 'test05_get_by_code.yaml'))
    def test05_get_by_code(self, case_data):
        request_data = update_group_code(update_competition_id(case_data, 'role'))
        request_url = request_data['url']
        request_param = request_data['param']
        access_token = get_access_token(2)
        request_data['header']['Authorization'] = 'Token ' + access_token
        request_header = request_data['header']
        response = requests.post(url=request_url, headers=request_header, json=request_param)
        print(response.json())
        print('完成get_by_code测试！')

    # 修改小组(加入小组，退出小组，解散小组)
    @pytest.mark.skip('pass')
    @pytest.mark.parametrize('case_data', read_data(filepath_variable_path['RolePlayingCase'] + 'test06_group_edit.yaml'))
    def test06_group_edit(self, case_data):
        request_data = update_group_id(case_data)
        request_url = request_data['url']
        request_param = request_data['param']
        access_token = get_access_token(2)
        request_data['header']['Authorization'] = 'Token ' + access_token
        request_header = request_data['header']
        response = requests.post(url=request_url, headers=request_header, json=request_param)
        print(response.json())
        print('完成group_edit测试！')

    # 获取小组信息(加入小组后)
    @pytest.mark.parametrize('case_data', read_data(filepath_variable_path['RolePlayingCase'] + 'test07_group.yaml'))
    def test07_group_id(self, case_data):
        request_data = update_group_id(case_data)
        request_url = request_data['url']
        access_token = get_access_token(1)
        request_data['header']['Authorization'] = 'Token ' + access_token
        request_header = request_data['header']
        response = requests.get(url=request_url, headers=request_header)
        print(response.json())
        print('完成group_id测试！')

    # 修改小组(加入小组，退出小组，解散小组)
    @pytest.mark.skip('pass')
    @pytest.mark.parametrize('case_data',
                             read_data(filepath_variable_path['RolePlayingCase'] + 'test06_group_edit.yaml'))
    def test06_group_edit(self, case_data):
        request_data = update_group_id(case_data)
        request_url = request_data['url']
        request_param = request_data['param']
        access_token = get_access_token(2)
        request_data['header']['Authorization'] = 'Token ' + access_token
        request_header = request_data['header']
        response = requests.post(url=request_url, headers=request_header, json=request_param)
        print(response.json())
        print('完成group_edit测试！')

    # 加载角色扮演内容
    def test08_redirect_type_5(self):
        print('完成redirect_type_5测试！')

    # 试听下载活动所有原音
    def test09_download_audio(self):
        print('完成download_audio测试！')

    # 修改小组(加入小组，退出小组，解散小组)
    def test10_group_edit(self):
        print('完成group_edit测试！')

    # 发起配音评测
    def test11_speech_evaluation_report(self):
        print('完成speech_evaluation_report测试！')

    # 提交配音
    def test12_commit(self):
        print('完成commit测试！')

    # 获取用户作答记录
    def test13_get_user_record_5(self):
        print('完成get_user_record_5测试！')

    # 获取小组排行榜详情
    def test14_get_ranking_detail_group(self):
        print('完成get_ranking_detail_group测试！')

    # 查询小组排行榜详情
    def test15_get_ranking_detail(self):
        print('完成get_ranking_detail测试！')
