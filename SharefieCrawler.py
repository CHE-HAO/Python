import requests
from bs4 import BeautifulSoup


start = 1
end = 1000

for i in range(start, end):

    url = 'https://www.sharefie.net/post/{0}'.format(i)
    # print(url)

    resp = requests.get(url)
    # print(resp)

    if resp.status_code == 200:

        soup = BeautifulSoup(resp.text, 'html.parser')
        # print(soup)

        not_found = soup.select("div#maincont div.pagenotfound")
        # print(not_found)

        if len(not_found) == 0:

            try:
                selector = soup.select("div#maincont div#postcontent img")
                # print(selector)

                for select in selector:

                    img = select["data-src"]
                    if img.startswith("http"):
                        print(img)

            except KeyError:
                continue
