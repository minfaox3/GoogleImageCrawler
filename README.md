# GoogleImageCrawler
Download results of all "google image search"'s images.  
This program not use google api, so can download images more than 100!

Japanese README↓  
https://github.com/minfaox3/GoogleImageCrawler/edit/master/README_ja.md

## Attention
Use in accordance with the laws of your country.

## Language and third party module
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

## Installation
* Download and install google-chrome-stable from official site or install from package manager.
  * ArchLinux  
    `yay -S google-chrome`
  * Ubuntu  
    `sudo apt install google-chrome-stable`
* Download Chrome driver from https://chromedriver.chromium.org/downloads and create path to extracted binary.
  * Choose most near to your chrome version.  
    You can check version from cli.  
    `google-chrome-stable -v`
* Install requirements package for execute gic.py.
  * Follow this command in local GoogleImageClawler repository  
   `pip install -r requirements.txt`
* That's all!

## Options
| option | description | Type | Default |
|-----------:|:------------:|:------------:|:------------:|
| -s, --sentence | Sets entence what you want to search. | String | google |
| -d, --delay | Sets delay for scrolling. | Unsigned Integer | 1 |
| -o, --output-directory | Sets output directory. | String | images |
| -dh, --do-html | This option will output result of img tags as "[SENTENCE].html".But images will not output. You can use only "True" or "False".| String | false |
| -ss, --scroll-speed | Sets scroll px per delay. | Unsigned Integer | 2000 |
| -gl, --geolocation | Sets geolocation code. Default is blank because Google guess it from ip or get from your account settings. It can affect search results. It will affect search results. | String | blank |
| -it, --image-type | Sets image type. Valid types are "clipart", "face", "lineart", "stock", "photo", "animated". | String | blank |
| -sp, --safe-parameter | Sets safe parameter. Valid parameters are "off", "medium", "high". | String | off |

## References
* Geolocation codes https://developers.google.com/custom-search/docs/xml_results_appendices#countryCodes
