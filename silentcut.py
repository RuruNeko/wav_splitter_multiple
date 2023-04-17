import argparse
import os
import sys
import glob
import pydub
from pydub import AudioSegment
from pydub.silence import split_on_silence

def split_wav_file(input_folder, output_dir, output_prefix,min_silence_len, silence_vol_thresh):
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
        chunks = split_on_silence(audio, min_silence_len, silence_thresh=silence_vol_thresh)
        output_audio = AudioSegment.empty()
        for chunk in chunks:
            output_audio += chunk
        output_file_name = f"{output_prefix}_{work_filename}_{(len(audio))}ms_to_{(len(output_audio))}ms.wav"
        output_file_path = os.path.join(output_dir, output_file_name)
        output_audio.export(output_file_path, format="wav")
        print(f"Exported '{output_file_path}'")
        
def check_vol_thresh(silence_vol_thresh):
    if silence_vol_thresh <= -60:
        print(f"Too Low Volume '{silence_vol_thresh}'. However, the program works with this volume.The recommended value is -50 to -20.")
        print(f"無音閾値の値が低過ぎます。 '{silence_vol_thresh}'。 この値でもプログラムは動作します。推奨値は -50から-20 です。")
    elif silence_vol_thresh >= 1:
        print(f"Too High Volume '{silence_vol_thresh}'. However, the program works with this volume.The recommended value is -50 to -20.")
        print(f"無音閾値の値が高過ぎます。 '{silence_vol_thresh}'。 この値でもプログラムは動作します。推奨値は -50から-20 です。")
    else:
        print(f"Threshold is '{silence_vol_thresh}'. The recommended value is -50 to -20.")
        print(f"敷居値は '{silence_vol_thresh}' です。 推奨値は -50から-20 です。")
    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='SilentSoundCut',
                    description='Cutting Silence Multiple sounds',
                    epilog='Silence')
    parser.add_argument('-i', '--input', default='input_folder', help='入力フォルダ')
    parser.add_argument('-o', '--output', default='output_dir', help='分割ファイルを保存するディレクトリ')
    parser.add_argument('-p', '--prefix', default='split', help='分割ファイルのプレフィックス')
    parser.add_argument('-m', '--mintime', default=100, type=int, help='無音部分の最小長さ (ミリ秒)')
    parser.add_argument('-v', '--volume', default=40, type=int, help='無音部分の閾値 (デシベル)')

    args = parser.parse_args()

    input_folder = args.input
    output_dir = args.output
    output_prefix = args.prefix
    min_silence_len = args.mintime
    silence_vol_thresh = -args.volume
    print(f"Input Dir:'{input_folder}'")
    print(f"Output Dir:'{output_dir}'")
    print(f"Prefix:'{output_prefix}'")
    print(f"Min silence len:'{min_silence_len}'")
    print(f"Silence volume thresh:'{silence_vol_thresh}'")
    
    check_vol_thresh(silence_vol_thresh)
    split_wav_file(input_folder, output_dir, output_prefix,min_silence_len, silence_vol_thresh)
