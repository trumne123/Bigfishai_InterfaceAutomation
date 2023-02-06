import json
import time
import pytest
import requests
from Command.DealJson import *
from Command.DealAudioFile import *
from Command.Support_function import *
from requests_toolbelt import MultipartEncoder


@pytest.mark.usefixtures('pre_class_test')
class Test_DubbingShow:
    # 查询官方指定活动
    @pytest.mark.parametrize('CaseData', read_data(filepath_variable_path['DubbingShowCase'] + 'test01_competition.yaml'))
    def test01_competition(self, CaseData):
        case_data = update_url(update_token(CaseData), 'dubbing')
        request_url = case_data['url']
        request_header = case_data['header']
        response = requests.get(url=request_url, headers=request_header)
        print(response.json())
        get_competition_info(response.json())

    # 获取配音详情
    @pytest.mark.parametrize('CaseData', read_data(filepath_variable_path['DubbingShowCase'] + 'test02_dubbingsrcv.yaml'))
    def test02_dubbingsrcv(self, CaseData):
        case_data = update_competition_id(update_url(update_token(CaseData), 'dubbing_src'))
        request_url = case_data['url']
        request_headers = case_data['header']
        param = case_data['param']
        response = requests.get(url=request_url, headers=request_headers, params=param)
        print(response.json())
        get_dubbingsrcv_info(response.json())

    # 下载配音秀原视频并生成上传音频
    def test04_download_video(self):
        qu_data1 = 'select value from linked_data where title = "video_url"'
        request_url = f'https://www.bigfishai.com:8300{query_data(qu_data1)[0][0]}'
        response = requests.get(url=request_url)
        file_path = filepath_variable_path['DownloadVideoPath']
        qu_data2 = 'select value from linked_data where title = "competition_id_dubbing"'
        file_name = f'{query_data(qu_data2)[0][0]}.mp4'
        download_file = os.path.join(file_path, file_name)
        with open(download_file, 'wb') as file_path1:
            file_path1.write(response.content)
        cut_audio_info = query_data('select dialogue_id,start_time,end_time,title from dubbing_info_data')
        deal_video(file_name, cut_audio_info)

    # 上传音频评测
    def test05_speech_evaluation_report(self):
        case_data = get_speech_data()
        url = 'https://www.bigfishai.com:8300/api/voice/speech_evaluation_report/'
        evaluation_score = []
        for request_data in case_data:
            file_name = request_data['content_type_id']
            upload_file = open(f'./MediaFile/Audio/UploadAudio/{file_name}.MP3', 'rb').read()
            file_data = {
                'res': ('audio.mp3', upload_file, 'application/octet-stream'),
                'user': request_data['user'],
                'name': request_data['name'],
                'eval_type': str(request_data['eval_type']),
                'audio_type': str(request_data['audio_type']),
                'typeThres': str(request_data['typeThres']),
                'content_type': str(request_data['content_type']),
                'content_type_id': str(request_data['content_type_id']),
                'competition': request_data['competition']
            }
            encode_data = MultipartEncoder(fields=file_data)
            request_headers = {'Content-Type': encode_data.content_type}
            response = requests.post(url=url, headers=request_headers, data=encode_data)
            print(response.json())
            evaluation_score.append(response.json()['data']['score'])
            # 将二进制字符通过utf-8解码为str（当前str无法通过print函数打印出来）
            # str1 = response.content.decode('utf-8')
            # # 重新把str通过gbk编码为二进制字符
            # bite2 = str1.encode('gbk', 'ignore')
            # # 再体通过utf-8解码为str，最后转为json
            # rjson = json.loads(bite2.decode('utf-8', 'ignore'))
            # print(rjson)
            # print(rjson['data']['score'])
            time.sleep(0.8)
        deal_score(evaluation_score)

    # 预览配音
    def test06_get_ranking(self):
        request_url = 'https://www.bigfishai.com:8300/api/dubbing/userdubbing/get_ranking/'
        request_param = {
            "user_id": query_data('select value from linked_data where title = "user_id"')[0][0],
            "competition_id": query_data('select value from linked_data where title = "competition_id_dubbing"')[0][0],
            "score": query_data('select value from linked_data where title = "score"')[0][0]
        }
        request_headers = {'Authorization': query_data('select value from linked_data where title = "token"')[0][0]}
        response = requests.post(url=request_url, headers=request_headers, json=request_param)
        print(response.json())
