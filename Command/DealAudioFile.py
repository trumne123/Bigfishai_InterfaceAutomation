from pydub import AudioSegment
from moviepy.editor import *
from Command.DealData import *
from Command.DefinedVariable import *


# 音频格式转换为合法上传格式
def deal_audio(filename):
    audio = AudioSegment.from_file(f'./MediaFile/Audio/DownloadAudio/{filename}', 'mp3')
    audio.set_frame_rate(44100).set_channels(1).export(f'./MediaFile/Audio/UploadAudio/{filename}', format='mp3', bitrate='128k')


# 切割音频并保存为合法上传格式
def cut_audio(start_time, end_time, audio_name):
    audio = AudioSegment.from_file(filepath_variable_path['DownloadVideoPath'] + 'change_to_mp3.mp3', 'mp3')
    audio_part = audio[int(start_time): int(end_time)]
    audio_part.set_frame_rate(44100).set_channels(1).export(f'./MediaFile/Audio/UploadAudio/{audio_name}.mp3',
                                                            format='mp3', bitrate='128k')


# 视频转音频
def deal_video(filename, cut_audio_info):
    video_path = './MediaFile/Video/DownloadVideo/' + filename
    video = VideoFileClip(video_path)
    video.audio.write_audiofile('./MediaFile/Video/DownloadVideo/' + 'change_to_mp3.mp3')
    video.close()
    for i in cut_audio_info:
        # cut_audio(i['start_time'], i['end_time'], i['id'])
        cut_audio(i[1], i[2], i[0])


if __name__ == '__main__':
    audio_info = read_data(filepath_variable_path['DubbingInfoPath'])
    deal_video('123', audio_info)
