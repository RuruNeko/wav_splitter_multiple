# wav_splitter_multiple
複数ファイル一括処理に対応したフォルダ指定型  
いい感じにRVCでの学習に必要な機能が洗い出せたら、GUI作って使いやすいツールにするかもしれない  
  
# fork元  
https://github.com/Yanagi-ai/wav_splitter  
  
# 動作に必要な外部ファイル  
https://github.com/BtbN/FFmpeg-Builds/releases  
にある  
ffmpeg-master-latest-win64-gpl-shared.zip  
内のdll、exeファイルをpython実行ファイルと同フォルダ内に置く  
以下のようになる  
./main.py  
./ffmpeg.exe  
./avcodec-60.dll  
./以下省略  

# 必要なライブラリ  
requirements.txt　を参照  
インストール方法  
pip install -r requirements.txt  

# python環境とかライブラリインストールとか面倒くさい！脳死とまでは言わないけどもっと簡単に環境用意させて！  
1.Anaconda Install  
https://www.anaconda.com/products/distribution  
2.Anaconda Prompt を実行  
3.ファイルがあるドライブに移動して cd でディレクトリ移動  
例、Dドライブの d:\wav_splitter\　に解凍した場合は以下のコマンド  
cd /d d:\wav_splitter\  
4.pip install -r requirements.txt  を実行  
5.以下の「実行方法」を実行  
  
# 実行方法  
## 3秒単位で音声カット  
python main.py [input_dir] [output_dir]  
example:python main.py c:\testvoice_input c:\testvoice_output  
第一引数はインプットフォルダ  
第二引数はアウトプットフォルダを指定する  
**フォルダパスの最後に「/」「\」は不要**、これを入れると動作エラー（面倒なので自動的に除外処理とかはしていない）  

## 無音カット  
python silentcut.py [input_dir] [output_dir]  
  
# 【現在あるもの】  
・main.py  
複数ファイル一括処理に対応したフォルダ指定型  
wavを分割するためのスクリプト  
n秒ごとに.wavファイルを分割  
  
・monoral_converter.py  
ステレオ/バイノーラルのwav音声をモノラルに変換する  
学習時にモノラル音声のほうがいいかも？という仮説に基づいて作った  
  
・nosound.py  
wavが無音かどうか判断するスクリプト  
音声作品を3秒毎に分割すると、たくさんの無音ファイルが生成されたりする  
それをフィルタリングしてフォルダ分けするためのスクリプト  

・silentcut.py  
複数ファイル一括処理に対応したフォルダ指定型  
音声の無音部分をカットして出力するためのスクリプト  
具体例　ファイルAがあるとする  
"*" = 発音、"-" = 無音  
処理前  
"--**---**--"  
処理後  
"****"  
  
Q:無音判定の推奨閾値は？  
A:色々試した結果 -40前後、微調整するなら -50～-30ぐらい  
  
Q:元音声の音量がバラバラ  
A:マスタリングしてください  