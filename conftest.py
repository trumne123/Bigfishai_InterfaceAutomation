import os
import pytest
import requests
from Command.DealJson import *
from Command.DealData import *
from Command.Support_function import *
from Command.DefinedVariable import *


# 项目开始前事件：删除缓存、获取登录token、获取用户信息,项目结束后自动退出登录，释放token
@pytest.fixture(scope='session', autouse=True)
def session_test():
    delete_json_file()
    # login()
    # get_user_info()
    # get_competition_list()
    # yield
    # login_out()


# 批量删除音频文件，测试class开始进行
@pytest.fixture(scope='class')
def pre_class_test():
    download_audio_path = './MediaFile/Audio/DownloadAudio/'
    upload_audio_path = './MediaFile/Audio/UploadAudio/'
    download_video_path = './MediaFile/Video/DownloadVideo/'
    # 删除下载音频文件
    for download_audio_file in os.listdir(download_audio_path):
        os.remove(download_audio_path + download_audio_file)
    # 删除上传音频文件
    for upload_file in os.listdir(upload_audio_path):
        os.remove(upload_audio_path + upload_file)
    # 删除下载视频
    for download_video_file in os.listdir(download_video_path):
        os.remove(download_video_path + download_video_file)


# 删除json缓存
def delete_json_file():
    temp_path = './Test_Result/temp/'
    # 删除json文件
    for delete_file in os.listdir(temp_path):
        os.remove(temp_path + delete_file)
    print('删除缓存')


# 登录获取token
def login():
    case_data = read_data(filepath_variable_path['testData'] + 'login.yaml')
    request_url = case_data['url']
    request_param = case_data['param']
    response = requests.post(url=request_url, json=request_param)
    get_token(response.json())
    print('完成登录，获取token')


# 获取user_id
def get_user_info():
    case_data = update_token(read_data(filepath_variable_path['testData'] + 'get_user_info.yaml'))
    request_url = case_data['url']
    request_header = case_data['header']
    response = requests.get(url=request_url, headers=request_header)
    get_user_id(response.json())
    print('获取用户id')


# 获取官方活动列表
def get_competition_list():
    case_data = update_token(read_data(filepath_variable_path['testData'] + 'list_user_1.yaml'))
    request_url = case_data['url']
    request_header = case_data['header']
    request_param = case_data['param']
    response = requests.get(url=request_url, headers=request_header, params=request_param)
    get_competition_id(response.json())
    print('获取官方活动列表')


def login_out():
    case_data = update_token(read_data(filepath_variable_path['testData'] + 'login_out.yaml'))
    request_url = case_data['url']
    request_headers = case_data['header']
    response = requests.get(url=request_url, headers=request_headers)
    print('退出登录' + response.text)
