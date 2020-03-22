import argparse
import base64
import os
import os.path
import queue
import time
import urllib.parse
import bs4
import magic
import requests
import selenium.webdriver
import selenium.webdriver.chrome.options
import selenium.webdriver.support.expected_conditions


def main():
    parser = argparse.ArgumentParser(description='GoogleImageCrawler options',
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-s', '--sentence', default='google', type=str, help='Sentence what you want to search. '
                                                                             'Default is "google".')
    parser.add_argument('-d', '--delay', default='1', type=int, help='Sets delay for scrolling. Default is "1" '
                                                                     'second.\nBe careful to "0" will put maximum '
                                                                     'burden on the server.')
    parser.add_argument('-o', '--directory', default='images', type=str, help='Sets output directory. Default is '
                                                                              '"images".')
    parser.add_argument('-dh', '--do-html', default='false', type=str, help='This option will print result of img tags '
                                                                            'like html.\nIf you set true then images '
                                                                            'will not output.\nDefault is "False".')
    parser.add_argument('-ss', '--scroll-speed', default=2000, type=int, help='For advanced users!\nScroll speed per '
                                                                              'delay.\nDefault is "2000"px.')
    parser.add_argument('-gl', '--geolocation', default='', type=str, help='For advanced users!\nSets geolocation '
                                                                           'code.\nDefault is blank because Google '
                                                                           'guess it from ip or get from your account '
                                                                           'settings.\nIt can affect search '
                                                                           'results.\nCode list is here\n '
                                                                           '"https://developers.google.com/custom'
                                                                           '-search/docs/xml_results_appendices'
                                                                           '#countryCodes".')
    parser.add_argument('-it', '--image-type', default='', type=str, help='For advanced users!\nSets image type.\n'
                                                                          'Default is blank.\nValid types are '
                                                                          '"clipart", "face", "lineart", "stock", '
                                                                          '"photo", "animated".')
    parser.add_argument('-sp', '--safe-parameter', default='off', type=str, help='For advanced users!\nSets safe '
                                                                                 'parameter.\nDefault is '
                                                                                 '"off".\nValid parameters are "off", '
                                                                                 '"medium", "high".')
    argv = parser.parse_args()
    delay = argv.delay
    html = argv.do_html
    directory = argv.directory
    scroll_speed = argv.scroll_speed
    gl = argv.geolocation
    it = argv.image_type
    safe = argv.safe_parameter
    if not os.path.exists(directory):
        os.makedirs(directory)
    query = argv.sentence.split()
    query = '+'.join(query)
    url = 'https://www.google.co.jp/search?tbm=isch&hl=ja&q=' + urllib.parse.quote_plus(query, encoding='utf-8')
    if gl != "":
        url += '&gl=' + gl
    if it != "":
        url += '&imgType=' + it
    if safe != "":
        url += '&safe=' + safe
    print('Starting crawl at "' + url + '".')
    options = selenium.webdriver.chrome.options.Options()
    options.add_argument('--headless')
    options.add_argument('--start-maximized')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument('--disable-extensions')
    driver = selenium.webdriver.Chrome(options=options)
    driver.get(url)
    progress_icon = queue.Queue()
    progress_icon.put('|')
    progress_icon.put('/')
    progress_icon.put('-')
    progress_icon.put('\\')
    while True:
        pi = progress_icon.get()
        progress_icon.put(pi)
        print('\r' + pi + ' ' + str(
            len(driver.find_elements_by_xpath('//img[@alt="「' + query + '」の画像検索結果"]'))) + ' images found', end='')
        time.sleep(delay)
        element = driver.find_element_by_xpath('//input[@value="結果をもっと表示"]')
        if element.is_displayed():
            element.find_element_by_xpath('//input[@value="結果をもっと表示"]').click()
        elif driver.find_element_by_xpath('//div[text()="未読はありません"]').is_displayed():
            break
        else:
            driver.execute_script('window.scrollTo(0,' + str(scroll_speed) + ');')
        scroll_speed += 2000
    soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    images = soup.select('img[alt="「' + query + '」の画像検索結果"]')
    print('\rCompleted crawl\nResult:' + str(len(images)) + ' images found')
    if html != 'true' and html != "True":
        print('Starting download images')
    for index, img in enumerate(images):
        if img.get('data-src') is not None:
            img['src'] = img['data-src']
        if html != 'true' and html != "True":
            src = str(img['src'])
            pi = progress_icon.get()
            progress_icon.put(pi)
            count = str(index + 1)
            print('\r' + pi + ' ' + count + '/' + str(len(images)), end='')
            if src.find('data:image/') != 0:
                response = requests.get(src)
                image = response.content
                with open(directory + '/' + count, 'wb') as im:
                    im.write(image)
                mime = magic.Magic(mime=True)
                ext = mime.from_file(directory + '/' + count)
                os.rename(directory + '/' + count, directory + '/' + count + '.' + ext[ext.rfind('/') + 1:])
            else:
                ext = '.' + src[src.find('/') + 1:src.find(';')]
                data = src[src.find(','):]
                with open(directory + '/' + count + ext, 'wb') as im:
                    im.write(base64.b64decode(data))
    imgs = '\n'.join(map(str, images))
    if html != 'true' and html != "True":
        print('\rComplete download images')
    if html == 'true' or html == 'True':
        print('Starting print html')
        with open(query + '.html', mode='w') as f:
            f.write(imgs)
        print('Complete print')


if __name__ == '__main__':
    main()
