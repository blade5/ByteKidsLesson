from selenium import webdriver
import time
import requests
import json
from bs4 import BeautifulSoup
import re


def autoOpenWebPage():
    webDriver = webdriver.Chrome('webdriver/chromedriver')
    webDriver.get("https://www.tsinghua.edu.cn/")

    webDriver.maximize_window()
    scrollPage(webDriver)

    webDriver.find_element_by_xpath('//*[@title="清华新闻"]').click()
    time.sleep(1)
    return webDriver


def scrollPage(webDriver):
    # 将滚动条下拉至最低
    js = "return action=document.body.scrollHeight"
    new_height = webDriver.execute_script(js)
    for i in range(0, new_height, 150):
        webDriver.execute_script('window.scrollTo(0, %s)' % (i))
        time.sleep(0.5)


def getArticleElements(webDriver):
    req = requests.get(webDriver.current_url)
    soup = BeautifulSoup(req.content, 'html.parser')
    articleDiv = soup.find('div', class_='side')
    articleElements = articleDiv.find_all('li')
    return articleElements


def processArticles(articleElements):
    articles_list = []
    for article in articleElements:
        articleTime = article.find('div', class_='time')
        articleText = article.find('div', class_='name')
        articleLink = article.find('a')

        articleImage = article.find('div', class_='img')
        src = articleImage['style']
        result = re.search("'(.*)'", src)
        print(result.group(1))

        url = requests.get('https://www.tsinghua.edu.cn' + result.group(1))

        filename = result.group(1).split('/')[-1]
        with open('WebCrawler/' + filename, 'wb') as f:
            f.write(url.content)

        articles_list.append(dict(
            time=articleTime.string,
            text=articleText.string,
            link=articleLink['href']
        ))
    return articles_list


def writeContent():
    with open('WebCrawler/results.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(articlesContent, indent=4, ensure_ascii=False))


driver = autoOpenWebPage()
articles = getArticleElements(driver)
articlesContent = processArticles(articles)
writeContent()
