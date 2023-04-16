import os
import sys
import glob
from pydub import AudioSegment

def split_wav_file(input_folder, output_dir, output_prefix, split_duration):
    # フォルダが存在することを確認
    if not os.path.isdir(input_folder):
        print(f"Input folder '{input_folder}' not found.")
        return

    # 出力ディレクトリが存在することを確認（存在しない場合は作成）
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 入力フォルダを取得する
    files = glob.glob(input_folder + "\*.wav")
    for input_file in files:

        # 入力ファイルを読み込む
        audio = AudioSegment.from_wav(input_file)
        work_filename = os.path.splitext(os.path.basename(input_file))[0]
        total_duration = len(audio)
        split_duration_mili = split_duration * 1000  # milliseconds

        # 分割
        for i in range(0, total_duration, split_duration_mili):
            start = i
            end = i + split_duration_mili
            split_audio = audio[start:end]
            split_file_name = f"{output_prefix}_{work_filename}_{i//1000}s_to_{(i+split_duration_mili)//1000}s.wav"
            split_file_path = os.path.join(output_dir, split_file_name)
            split_audio.export(split_file_path, format="wav")
            print(f"Exported '{split_file_path}'")

if __name__ == "__main__":
    input_folder= "C:\RVC\VoiceInput"  # 入力フォルダ
    output_dir = "C:\RVC\VoiceOutput"  # 分割ファイルを保存するディレクトリ
    output_prefix = "split"  # 分割ファイルのプレフィックス
    split_duration = 3  # 分割する秒数

    split_wav_file(input_folder, output_dir, output_prefix, split_duration)
