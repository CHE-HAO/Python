import requests
from bs4 import BeautifulSoup


def contains(string, filters):
    for f in filters:
        if f in string:
            return True
    return False


def get_last_page(root_soup):
    page_url = ROOT_SOUP.select("div.btn-group.btn-group-paging a")[1]["href"]
    result = page_url[17:21]
    return result


PTT_URL = 'https://www.ptt.cc'
TITLE_FILTER = ["肉特", "兇", "帥哥", "神人", "男", "三性", "選一", "公告", "投稿", "注意"]
WRITER_FILTER = ["encorek01231", "futurekeep", "ReiKuromiya"]
URL_CHECKER = [PTT_URL, "instagram", "reurl", "twitter", "twitch"]
print("-------------------------------")
ROOT = requests.get(PTT_URL + "/bbs/Beauty/index.html", cookies={'over18': '1'})  # 將網頁資料GET下來
ROOT_SOUP = BeautifulSoup(ROOT.text, "html.parser")  # 將網頁資料以html.parser
ROOT_SOUP_SELECT = ROOT_SOUP.select("div.title a")  # 取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel
ROOT_SOUP_LAST_PAGE_SELECT = get_last_page(ROOT_SOUP)

# print(ROOT)
# print(ROOT_SOUP)
# print(ROOT_SOUP_SELECT)
print(ROOT_SOUP_LAST_PAGE_SELECT)

URL_ARR = []
for TOPIC_URLS in ROOT_SOUP_SELECT:
    URL_ARR.append(PTT_URL + TOPIC_URLS["href"])

IMAGE_URLS = []
for URL in URL_ARR:
    BRANCH = requests.get(URL, cookies={'over18': '1'})
    BRANCH_SOUP = BeautifulSoup(BRANCH.text, "html.parser")
    # print(BRANCH_SOUP)
    BRANCH_CONTENT_TITLE = BRANCH_SOUP.select("title")[0].text
    BRANCH_CONTENT_WRITER = BRANCH_SOUP.select("div#main-content span.article-meta-value")[0].text
    BRANCH_CONTENT_IMAGES = BRANCH_SOUP.select("div#main-container a")
    # print(BRANCH_CONTENT_TITLE)
    # print(BRANCH_CONTENT_WRITER)
    # print(BRANCH_CONTENT_IMAGES)

    VERIFY_TITLE = contains(BRANCH_CONTENT_TITLE, TITLE_FILTER)
    VERIFY_WRITER = contains(BRANCH_CONTENT_WRITER, WRITER_FILTER)
    if not (VERIFY_TITLE or VERIFY_WRITER):
        for CONTENT_IMAGE in BRANCH_CONTENT_IMAGES:
            url = CONTENT_IMAGE["href"]
            # print(url)
            if not contains(url, URL_CHECKER):
                IMAGE_URLS.append(url)
    # print("================================")
#
# for image_url in IMAGE_URLS:
#     print(image_url)

