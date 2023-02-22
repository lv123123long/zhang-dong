import requests # 请求库
import logging  # 日志输出
import re  # 正则表达式
from urllib.parse import urljoin  # url的拼接

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

BASE_URL = 'https://ssr1.scrape.center'
TOPAL_PAGE = 10

def scrape_page(url):     # 正常的请求一个页面的方法
    logging.info('scrapeing %s' %url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text                                # 返回一个页面的text全部内容
        logging.error('get invalid status code %s while scrapeing %s' %response.status_code %url)
    except requests.RequestException:
        logging.error('error occurred while scraping $s', url, exc_info=True)   # exc_info 设置为true，可以打印出报错的错误栈

def scrape_index(page):   # 爬取列表页,用一个列表页的拼接url，请求获取到的html
    index_url = f'{BASE_URL}/page/{page}'   # 通过观察得到 列表页的url拼接方式
    return scrape_page(index_url)     # 返回一个链接的所有内容text

def parse_index(html): # 解析列表页
    pattern = re.compile('<a.*?href="(.*?)".*?class="name">')    # .*?  非贪婪模式匹配任意字符串，，，，在href属性中用了分组匹配
                                                                # 这样就能在匹配结果中获取我们需要的url了
    items = re.findall(pattern, html)  # 在html中搜索出所有符合正则表达式的值
    if not items:
        return []
    for item in items:
        detail_url = urljoin(BASE_URL, item)
        logging.info('get detail url %s', detail_url)    # 每个页面拼接出10个url
        yield detail_url      # 可迭代对象，生成器，一次取一个值，，，，也相当于return 返回值

def scrape_detail(url):
    return scrape_page(url)

def parse_detail(html):
    cover_pattern = re.compile('class="item.*?<img.*?src="(.*?)')
def main():
    for page in range(1, TOPAL_PAGE + 1):
        indext_html = scrape_index(page)   # 用拼接到的url，请求到的html
        detail_urls = parse_index(indext_html)
        logging.info('detail urls %s', list(detail_urls))
# yield这里的使用值得思考，因为detail_url 从定义上来看，并不是一个列表，但是下面用list遍历出来了
if __name__ == "__main__":

    main()

