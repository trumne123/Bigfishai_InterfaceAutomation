from Config.Conftest import *


@pytest.mark.usefixtures('session_test')
@pytest.mark.usefixtures('pre_class_test')
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
    def test02_content_list(self):
        print('完成content_list测试!')

    # 下载音频
    def test03_download_audio(self):
        print('完成download_audio测试!')

    # 上传音频评测
    def test04_speech_evaluation_report(self):
        print('完成speech_evaluation_report测试!')

    # 提交作答记录
    def test05_commit(self):
        print('完成commit测试!')

    # 获取用户作答记录
    def test06_get_user_record(self):
        print('完成get_user_record测试!')

    # 获取排行榜详情
    def test07_get_ranking_detail(self):
        print('完成get_ranking_detail测试!')
