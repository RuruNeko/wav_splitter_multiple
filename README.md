# wav_splitter_multiple
複数ファイル一括処理に対応したフォルダ指定型  
いい感じにRVCでの学習に必要な機能が洗い出せたら、GUI作って使いやすいツールにするかもしれない  
  
#fork元  
https://github.com/Yanagi-ai/wav_splitter  
  
#動作に必要な外部ファイル  
https://github.com/BtbN/FFmpeg-Builds/releases  
にある  
ffmpeg-master-latest-win64-gpl-shared.zip  
内のdll、exeファイルをpython実行ファイルと同フォルダ内に置く  
以下のようになる  
./main.py  
./ffmpeg.exe  
./avcodec-60.dll  
./以下省略  
  
#実行方法  
python main.py [input_dir] [output_dir]  
第一引数はインプットフォルダ  
第二引数はアウトプットフォルダを指定する  
** フォルダパスの最後に「/」「\」は不要**、これを入れると動作エラー（面倒なので自動的に除外処理とかはしていない）  
  
#【現在あるもの】  
・main.py  
wavを分割するためのスクリプト  
n秒ごとに.wavファイルを分割  
  
・monoral_converter.py  
ステレオ/バイノーラルのwav音声をモノラルに変換する  
学習時にモノラル音声のほうがいいかも？という仮説に基づいて作った  
  
・nosound.py  
wavが無音かどうか判断するスクリプト  
音声作品を3秒毎に分割すると、たくさんの無音ファイルが生成されたりする  
それをフィルタリングしてフォルダ分けするためのスクリプト  
  
【todo】  
・発話分析をして音声分割をしてくれるスクリプト  
n秒ごとに分割するより、発話単位で分割してくれたほうがデータセットとしての質が高まりそう  
いい感じのロジックを調整中  
