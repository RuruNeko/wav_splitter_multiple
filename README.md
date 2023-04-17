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

# python環境とかライブラリインストールとか面倒くさい！もっと簡単に環境用意させて！  
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
python silentcut.py -i [input_dir] -o [output_dir] -p prefix -m 100 -v 40  
example:python silentcut.py -i c:\testvoice_input -o c:\testvoice_output -p prefix -m 100 -v 40  
example:python silentcut.py -i c:\testvoice_input -o c:\testvoice_output
-i 無音対象とするファイル群があるフォルダを指定する  
-o 無音カットして出力したフォルダを指定する、フォルダが無い場合は作成する  
-p 分割ファイルの先頭に挿入するファイル名を指定する  
-m 無音で区切る最小限の長さを指定する。指定しない場合は 100 となる  
-v 無音と判定する閾値を指定する。指定しない場合は -40 となる  
-vのみ"正の数値"を指定することで"負の値"として閾値を設定する。具体例として 40 と指定すると -40 となる。  
  
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
"+" = 発音、"-" = 無音  
処理前  
"--++---++--"  
処理後  
"++++"  
ファイル名の左側「xxxx ms」は元音声の長さ、右側の「xxxx ms」は無音カット後の長さ、両側が長さ同一の場合はカットされていないので注意  
  
Q:無音判定の推奨閾値は？  
A:色々試した結果 -40前後、微調整するなら -50～-30ぐらい  
  
Q:元音声の音量がバラバラ  
A:マスタリングorノーマライズしてください  
  
Q:元音声にどうしてもノイズが入る、ノイズ入り音声しかない  
A:https://www.izotope.jp/jp/products/rx-10/  
もしくは  
https://www.izotope.jp/jp/products/music-production-suite-5-universal-edition/  
  
Q:ノーマライズ、マスタリングのバッチ処理は無いの？  
A:以下の2つのDAWとツール、そしてiZotope社のOzone10もしくはMPS5UEを組み合わせると大量ファイルの自動処理を実装可能  
https://www.mi7.co.jp/products/presonus/studioone/  
Audio Batch Converter  
https://www.mi7.co.jp/products/presonus/studioone/addon/  