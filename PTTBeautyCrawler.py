import requests
from bs4 import BeautifulSoup

# 2500 - 2510
start = 2500
end = 2510


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
URL_CHECKER = [PTT_URL, "instagram", "reurl", "twitter", "twitch",
               "miupix", "yhoo.it", "facebook", "youtube", "/bbs",
               "appledaily", "/cdn-cgi", "youthwant", "libertytimes", "html", "gif", "ppt.cc", "montagg", "goo.gl"]
print("-------------------------------")

for i in range(start, end):
    ROOT_URL = PTT_URL + ("/bbs/Beauty/index{0}.html".format(i))
    ROOT = requests.get(ROOT_URL, cookies={'over18': '1'})  # 將網頁資料GET下來
    ROOT_SOUP = BeautifulSoup(ROOT.text, "html.parser")  # 將網頁資料以html.parser
    ROOT_SOUP_SELECT = ROOT_SOUP.select("div.title a")  # 取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel
    ROOT_SOUP_LAST_PAGE_SELECT = get_last_page(ROOT_SOUP)

    # print(ROOT)
    # print(ROOT_SOUP)
    # print(ROOT_SOUP_SELECT)
    # print(ROOT_SOUP_LAST_PAGE_SELECT)

    URL_ARR = []
    for TOPIC_URLS in ROOT_SOUP_SELECT:
        URL_ARR.append(PTT_URL + TOPIC_URLS["href"])

    IMAGE_URLS = []
    for URL in URL_ARR:
        VERIFY_TITLE = True
        VERIFY_WRITER = True

        BRANCH = requests.get(URL, cookies={'over18': '1'})
        BRANCH_SOUP = BeautifulSoup(BRANCH.text, "html.parser")
        # print(BRANCH_SOUP)
        BRANCH_CONTENT_TITLE = BRANCH_SOUP.select("title")
        BRANCH_CONTENT_WRITER = BRANCH_SOUP.select("div#main-content span.article-meta-value")
        BRANCH_CONTENT_IMAGES = BRANCH_SOUP.select("div#main-container a")
        # print(BRANCH_CONTENT_TITLE)
        # print(BRANCH_CONTENT_WRITER)
        # print(BRANCH_CONTENT_IMAGES)

        if len(BRANCH_CONTENT_TITLE) > 0:
            BRANCH_CONTENT_TITLE = BRANCH_CONTENT_TITLE[0].text
            # print(BRANCH_CONTENT_TITLE)
            VERIFY_TITLE = contains(BRANCH_CONTENT_TITLE, TITLE_FILTER)

        if len(BRANCH_CONTENT_WRITER) > 0:
            BRANCH_CONTENT_WRITER = BRANCH_CONTENT_WRITER[0].text
            # print(BRANCH_CONTENT_WRITER)
            VERIFY_WRITER = contains(BRANCH_CONTENT_WRITER, WRITER_FILTER)

        if not (VERIFY_TITLE or VERIFY_WRITER):
            for CONTENT_IMAGE in BRANCH_CONTENT_IMAGES:
                url = CONTENT_IMAGE["href"]
                # print(url)
                if not contains(url, URL_CHECKER):
                    IMAGE_URLS.append(url)
        # print("================================")

    for image_url in IMAGE_URLS:
        print(image_url)

