import requests # 訪問
from bs4 import BeautifulSoup # 網頁解析
import os

# 抓取網頁網址
# url = 'https://news.cnyes.com/news/cat/future'
url = 'https://today.line.me/tw/v2/tab/top?gclid=Cj0KCQjwi46iBhDyARIsAE3nVrYQoE42ilNsMR3sE99VZQEi46aIlU9gb8W_KTecyC2HI5L_gO4S1isaAmkqEALw_wcB'
re = requests.get(url)
soup = BeautifulSoup(re.text, 'html.parser')
print(soup)
# texts = soup.find_all('a', class_='_1Zdp')

# 抓取財經網頁文章內容
# def crewFinanceArticleContentText(contentUrl):
#     url = 'https://news.cnyes.com/'+contentUrl
#     re = requests.get(url)
#     soup = BeautifulSoup(re.text, 'html')
#     title =  soup.find('h1').string
#     time = soup.find('time').string
#     texts = soup.find_all('p')
#     allArticleText = ''
#     for text in texts:
#         cText = str(text.string )
#         allArticleText += cText
#     print(23, 'title ' + str(title))
#     print(24, 'time ' + time)
#     print(25, allArticleText)

# if os.path.isfile('FinancialArticles.txt'): #第N次抓
#   print("檔案存在。")
#   notCrewArticle = []
#   with open('FinancialArticles.txt', 'r') as temp_f:
#     text = []
#     for line in temp_f:
#         text.append(line)
#   for x in texts:
#         if x['href']+'\n' in text:
#             print(20, '抓過這個網址了')  # The string is found
#         else:
#             print(22, '沒抓過') # The string does not exist in the file
#             notCrewArticle.append(x['href'])
#             file = open('FinancialArticles.txt', 'a+')
#             file.write(x['href']+'\n')
#             file.close()
#   for articleUrl in notCrewArticle:
#     crewFinanceArticleContentText(articleUrl)
# else: #第一次抓
#   print("檔案不存在。")
# file = open('FinancialArticles.txt', 'w+')
# for x in texts:
#   print(45, x)
#   file.write(x['href']+'\n')
# file.close()
# with open('FinancialArticles.txt', 'r') as temp_f:
#   text = []
#   for line in temp_f:
#       text.append(line)
# for x in text:
#   url = x.strip('\n')
#   crewFinanceArticleContentText(url)
  
