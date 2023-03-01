import json
import time
import pytest
import requests
from Command.DealJson import *
from Command.DealAudioFile import *
from Command.Support_function import *
from requests_toolbelt import MultipartEncoder


@pytest.mark.skip('Test_ReadingShow跳过！')
# @pytest.mark.usefixtures('pre_class_test')
class Test_ReadingShow:
    # 获取商品信息
    @pytest.mark.parametrize('CaseData', read_data(filepath_variable_path['ReadingShowCase'] + 'test01_goods_info.yaml'))
    def test01_goods_info(self, CaseData):
        case_data = update_url(update_token(CaseData), 'reading')
        request_url = case_data['url']
        request_header = case_data['header']
        response = requests.get(url=request_url, headers=request_header)
        print(response.json())

    # 查询训练营内容
    @pytest.mark.parametrize('CaseData', read_data(filepath_variable_path['ReadingShowCase'] + 'test02_content_list.yaml'))
    def test02_content_list(self, CaseData):
        case_data = update_url(update_token(CaseData), 'reading')
        request_url = case_data['url']
        request_header = case_data['header']
        request_param = case_data['param']
        response = requests.post(url=request_url, headers=request_header, json=request_param)
        print(response.request.body)
        print(response.json())
        get_dubbing_info(response.json())

    # 下载音频
    # @pytest.mark.skip('pass')
    def test03_download_audio(self):
        case_data = read_data(filepath_variable_path['ReadingShowCase'] + 'test03_download_audio.yaml')
        for case_info in case_data:
            request_url = f'https://www.bigfishai.com:8300{case_info["audio_url"]}'
            response = requests.get(url=request_url)
            file_path = filepath_variable_path['DownloadAudioPath']
            file_name = str(case_info['id']) + '.mp3'
            download_file = os.path.join(file_path, file_name)
            with open(download_file, 'wb') as file_path:
                file_path.write(response.content)
            # 转换音频格式
            deal_audio(file_name)
            print(f'{case_data.index(case_info)}完成下载')

    # 上传音频评测
    # @pytest.mark.skip('pass')
    def test04_speech_evaluation_report(self):
        case_data = read_data(filepath_variable_path['ReadingShowCase'] + 'test04_speech_evaluation_report.yaml')
        for case_info in case_data:
            url = case_info['url']
            file_name = case_info['id']
            user_dubbing = query_data('select value from linked_data where title = "user_dubbing_id"')[0][0]
            competition = query_data('select value from linked_data where title = "competition_id_reading"')[0][0]
            upload_file = open(f'./MediaFile/Audio/UploadAudio/{file_name}.MP3', 'rb').read()
            file_data = {
                'res': ('audio.mp3', upload_file, 'application/octet-stream'),
                'user': '309',
                'name': case_info['title'],
                'eval_type': case_info['eval_type'],
                'audio_type': '1',
                'typeThres': '4',
                'content_type': case_info['content_type'],
                'content_type_id': file_name,
                'user_dubbing': user_dubbing,
                'competition': competition
            }
            encode_data = MultipartEncoder(fields=file_data)
            request_headers = {'Content-Type': encode_data.content_type}
            response = requests.post(url=url, headers=request_headers, data=encode_data)
            # 将二进制字符通过utf-8解码为str（当前str无法通过print函数打印出来）
            str1 = response.content.decode('utf-8')
            # 重新把str通过gbk编码为二进制字符
            bite2 = str1.encode('gbk', 'ignore')
            # 再体通过utf-8解码为str，最后转为json
            rjson = json.loads(bite2.decode('utf-8', 'ignore'))
            print(rjson)
            time.sleep(0.8)

    # 提交作答记录
    @pytest.mark.parametrize('CaseData', read_data(filepath_variable_path['ReadingShowCase'] + 'test05_commit.yaml'))
    # @pytest.mark.skip('pass')
    def test05_commit(self, CaseData):
        case_data = update_url(update_token(CaseData), 'reading')
        request_url = case_data['url']
        request_header = case_data['header']
        response = requests.get(url=request_url, headers=request_header)
        print(response.json())

    # 获取用户作答记录
    @pytest.mark.parametrize('CaseData', read_data(filepath_variable_path['ReadingShowCase'] + 'test06_get_user_record.yaml'))
    # @pytest.mark.skip('pass')
    def test06_get_user_record(self, CaseData):
        case_data = update_url(update_token(CaseData), 'reading')
        request_url = case_data['url']
        request_header = case_data['header']
        response = requests.get(url=request_url, headers=request_header)
        print(response.content)

    # 获取排行榜详情
    @pytest.mark.parametrize('CaseData', read_data(filepath_variable_path['ReadingShowCase'] + 'test07_get_ranking_detail.yaml'))
    # @pytest.mark.skip('pass')
    def test07_get_ranking_detail(self, CaseData):
        case_data = update_url(update_token(CaseData), 'reading')
        request_url = case_data['url']
        request_header = case_data['header']
        request_param = case_data['param']
        response = requests.post(url=request_url, headers=request_header, json=request_param)
        print(response.json())
