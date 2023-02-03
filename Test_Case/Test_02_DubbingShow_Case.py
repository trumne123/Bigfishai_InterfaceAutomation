import pytest


@pytest.mark.usefixtures('pre_class_test')
class Test_DubbingShow:
    # 查询官方指定活动
    def test01_competition(self):
        print('完成competition测试!')

    # 获取配音详情
    def test02_dubbingsrcv(self):
        print('完成dubbingsrcv测试!')

    # 下载配音秀原视频并生成上传音频
    def test04_download_video(self):
        print('完成download_video测试!')

    # 上传音频评测
    def test05_speech_evaluation_report(self):
        print('完成speech_evaluation_report测试!')

    # 预览配音
    def test06_get_ranking(self):
        print('完成get_ranking测试!')
