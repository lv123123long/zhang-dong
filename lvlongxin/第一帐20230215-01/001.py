import json
from os import makedirs
from os.path import exists
import requests
import logging
import re
from urllib.parse import urljoin
import multiprocessing
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

BASE_URL = 'https://ssr1.scrape.center'
TOPIC_PAGE = 10

RESULTS_DIR = 'results'
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)

def scrape_page(url):
    logging.info('scrape %s.............', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text      # return 代表函数的接受，，下面的就不会执行了
        logging.error('get invalid ststus code %s while scraping %s', response.status_code, url)

    except requests.RequestException:
        logging.error('error occurred while scraping %s', url, exc_info=True)   # 这个exc_info 会打印出报错详细

def scrape_index(page):
    index_url = f'{BASE_URL}/page/{page}'
    return scrape_page(index_url)

def parse_index(html):
    pattern = re.compile('<a.*?href="(.*?)".*?class="name">')     # 中间这个括号很有讲究，用来取值的匹配
    items = re.findall(pattern,  html)
    if not items:     # 判断列表是否为空，，直接not 就行  返回值为true 就是说明这个列表为空
        return []
    for item in items:
        print(item)
        detail_url = urljoin(BASE_URL, item)   # BASE_URL = 'https://ssr1.scrape.center' # /detail/99   # https://ssr1.scrape.center/detail/97
        logging.info('get detail url %s', detail_url)
        yield detail_url

def scrape_detail(url):
    return scrape_page(url)

def parse_detail(html):
    cover_pattern = re.compile('class="item.*?<img.*?src="(.*?)".*?class="cover">', re.S)
    name_pattern = re.compile('<h2.*?>(.*?)</h2>')
    categories_pattern = re.compile('<button.*?category.*?<span>(.*?)</span>.*?</button>', re.S)
    published_at_pattern = re.compile('(\d{4}-\d{2}-\d{2})\s?上映')
    drama_pattern = re.compile('<div.*?drama.*?>.*?<p.*?>(.*?)</p>', re.S)
    score_pattern = re.compile('<p.*?score.*?>(.*?)</p>', re.S)

    cover = re.search(cover_pattern, html).group(1).strip() \
    if re.search(cover_pattern, html) else None      # search 方法的作用，，就是提取里面括号匹配的值，这里只有一个

    name = re.search(name_pattern, html).group(
        1).strip() if re.search(name_pattern, html) else None
    categories = re.findall(categories_pattern, html) if re.findall(      # 有多个，所以用findall来提取，是个列表
        categories_pattern, html) else []
    published_at = re.search(published_at_pattern, html).group(
        1) if re.search(published_at_pattern, html) else None
    drama = re.search(drama_pattern, html).group(
        1).strip() if re.search(drama_pattern, html) else None
    score = float(re.search(score_pattern, html).group(1).strip()
                  ) if re.search(score_pattern, html) else None

    return {
        'cover': cover,
        'name': name,
        'categories': categories,
        'published_at': published_at,
        'drama': drama,
        'score': score
    }

def save_data(data):
    name = data.get('name')
    data_path = f'{RESULTS_DIR}/{name}.json'
    json.dump(data, open(data_path, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=2)   # ensure_ascii  False 保证中文在json里面以中文的形式出现， indent代表两行缩进
def main(page):
    index_html = scrape_index(page)
    detail_urls = parse_index(index_html)
    for detail_url in detail_urls:
        detail_html = scrape_detail(detail_url)
        data = parse_detail(detail_html)
        logging.info('get detail data %s', data)
        # 靠上面的循环，其实已经把所有的数据成功提取出来了
        logging.info('saving data to json file')
        save_data(data)
        logging.info('data saved successfully')

if __name__ == "__main__":
    pool = multiprocessing.Pool()
    pages = range(1, TOPIC_PAGE + 1)
    #   print(pages) # range(1, 11)
    pool.map(main, pages)
    pool.close()

    # 总结一下多进程，，就是把两个for循环，变成一个多进程，剩下一个for循环
    # 多进程传递的参数，就是外面这个循环的次数


    """
    本来的模样
    for page in range(1, TOPIC_PAGE + 1)
        for detail in details:
    """
