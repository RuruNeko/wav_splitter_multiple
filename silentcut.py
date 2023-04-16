import os
import sys
import glob
import pydub
from pydub import AudioSegment
from pydub.silence import split_on_silence

def split_wav_file(input_folder, output_dir, output_prefix, silence_vol_thresh):
    # フォルダが存在することを確認
    if not os.path.isdir(input_folder):
        print(f"Input folder '{input_folder}' not found.")
        return

    # 出力ディレクトリが存在することを確認（存在しない場合は作成）
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    i = 0
    # 入力フォルダを取得する
    files = glob.glob(input_folder + "\*.wav")
    for input_file in files:
        i = i + 1
        # 入力ファイルを読み込む
        audio = AudioSegment.from_wav(input_file)
        work_filename = os.path.splitext(os.path.basename(input_file))[0]
        # サイレント部分分割
        min_silence_len = 100  # 無音部分の最小長さ (ミリ秒)
        chunks = split_on_silence(audio, min_silence_len=min_silence_len, silence_thresh=silence_vol_thresh)
        output_audio = AudioSegment.empty()
        for chunk in chunks:
            output_audio += chunk
        output_file_name = f"{output_prefix}_{work_filename}_{(len(audio))}ms_to_{(len(output_audio))}ms.wav"
        output_file_path = os.path.join(output_dir, output_file_name)
        output_audio.export(output_file_path, format="wav")
        print(f"Exported '{output_file_path}'")

if __name__ == "__main__":
    args = sys.argv
    input_folder= args[1]  # 入力フォルダ
    output_dir = args[2]  # 分割ファイルを保存するディレクトリ
    output_prefix = "split"  # 分割ファイルのプレフィックス
    silence_vol_thresh = -40  # 無音部分の閾値 (デシベル)

    split_wav_file(input_folder, output_dir, output_prefix, silence_vol_thresh)
