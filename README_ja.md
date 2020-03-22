# GoogleImageCrawler
「Google画像検索」のすべての画像の結果をダウンロードすることがきます。  
また、GoogleのAPIを使用していないため100枚を超えて画像をダウンロードすることが可能です。

English README↓  
https://github.com/minfaox3/GoogleImageCrawler/

## 注意
あなたの国の法律に従ってください。

## 言語とサードパーティーのモジュール
* python 3.7
* beautifulsoup4 4.8.2
* certifi 2019.11.28
* chardet 3.0.4
* idna 2.9
* python-magic 0.4.15
* requests 2.23.0
* selenium 3.141.0
* soupsieve 2.0
* urllib3 1.25.8

## 使用方法
* google-chrome-stableを公式サイトからダウンロードしてインストールするかパッケージマネージャーからインストールしてください。
  * ArchLinux  
    `yay -S google-chrome`
  * Ubuntu  
    `sudo apt install google-chrome-stable`
* https://chromedriver.chromium.org/downloads からChrome Driverをダウンロードして解凍してできたバイナリファイルへとパスを通してください。
  * あなたの現在使用しているChromeのヴァージョンに最も近いものを選んでください。  
    コマンドラインからも以下のように調べることができます。  
    `google-chrome-stable -v`
* gic.pyを使用するために必要なんモジュールをインストールします。
  * 下記のコマンドをローカルのGoogleImageClawlerリポジトリ内で実行してください。  
   `pip install -r requirements.txt`
* 以上です！

## オプション
| オプション | 説明 | 型 | 省略時 |
|-----------:|:------------:|:------------:|:------------:|
| -s, --sentence | 検索したい文章(単語でも可)を設定します。 | 文字列 | google |
| -d, --delay | スクロールを何秒毎にするか設定します。 | 非負整数 | 1 |
| -o, --output-directory | 画像の出力先ディレクトリを設定します。 | 文字列 | images |
| -dh, --do-html | This option will output result of img tags as "[SENTENCE].html".But images will not output. You can use only "True" or "False".| 文字列 | false |
| -ss, --scroll-speed | [DELAY]毎に何pxスクロールするかを設定します。 | 非負整数 | 2000 |
| -gl, --geolocation | 国コードを設定します。省略時が空白なのはGoogleがあなたのIPから推測するかアカウント設定から設定されます。これは検索結果に影響が与えます。 | 文字列 | 空白 |
| -it, --image-type | 手に入れたい画像の見た目を設定します。使用可能なのは"clipart", "face", "lineart", "stock", "photo", "animated"です。 | 文字列 | 空白 |
| -sp, --safe-parameter | セーフサーチのパラメータを設定します。使用可能なのは"off", "medium", "high". | 文字列 | off |

## 参考
* 国コード https://developers.google.com/custom-search/docs/xml_results_appendices#countryCodes
