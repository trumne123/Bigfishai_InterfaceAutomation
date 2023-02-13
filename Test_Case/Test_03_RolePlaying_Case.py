import json
import time
import pytest
import requests

import conftest
from Command.DealJson import *
from Command.DealAudioFile import *
from Command.Support_function import *
from requests_toolbelt import MultipartEncoder


@pytest.mark.usefixtures('pre_class_test')
class Test_RolePlaying:
    # 创建小组
    def test01_group(self):
        conftest.custom_login('15702264620', '15702264621')

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
