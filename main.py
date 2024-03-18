import requests # 訪問
from bs4 import BeautifulSoup # 網頁解析
import jieba
import  numpy
from PIL import Image # 圖片轉array陣列
import os
import matplotlib.pyplot as plt
import wordcloud # 文字雲
from collections import Counter # 次數統計
import openpyxl #Excel

# 抓取網頁網址
url = 'https://news.cnyes.com/news/cat/future'
re = requests.get(url)
soup = BeautifulSoup(re.text, 'html.parser')
texts = soup.find_all('a', class_='_1Zdp')

def exportExcel(title, time,link, article, id, segList):
    wb = openpyxl.Workbook()
    sheet = wb.create_sheet("工作表1", 0)
    sheet['A1'] = '文章標題'
    sheet['A2'] = title
    sheet['B1'] = '文章連結'
    sheet['B2'] = link
    sheet['C1'] = '文章內文'
    sheet['C2'] = article
    sheet['D1'] = '文章時間'
    sheet['D2'] = time
    sheet['E1'] = '斷詞'
    index = 1
    for x in segList:
        index+=1
        sheet['E'+str(index)] = x
    wb.save('./financeArticles/'+id+'/'+ id +'.xlsx')
    print(18, title, time,link, article, id, segList)

def generateWordCloud(title, time,link, article, id):
    path= os.getcwd()
    os.makedirs(path+'/financeArticles/'+ id)
  # 設定分詞資料庫
    jieba.set_dictionary('./dict.txt.big.txt')
    # 將自己常用的詞加入字典
    jieba.load_userdict('./finance_dict.txt')
    # 新增及刪除常用詞
    # jieba.add_word('陳時中') # 加入陳時中
    # jieba.add_word('快篩') # 加入快篩
    # jieba.del_word('元') # 刪除元
    # 斷句方式
    seg_list = jieba.lcut(article, cut_all=False) # lcut直接返回list
    print(seg_list)
    # 統計分詞出現次數
    dictionary = Counter(seg_list)
    print(10,dictionary)
    # 移除停用詞
    stopword = [' ', '，', '（', '）', '...', '。', '「', '」']  # 定義停用詞
    [dictionary.pop(x, None) for x in stopword] # 存字典裡刪除停用詞
    # 產生文字雲 格式設定
    font_path = 'NotoSansTC-Light.otf' # 設定字體格式
    mask = numpy.array(Image.open('warning (1).png')) # 遮罩
    mask=(mask==0)*255 # 把舉證等於0的地方變成255 原本有數字的地方變0
    wc = wordcloud.WordCloud(background_color='white',
                            margin=2, # 文字間距
                            mask=mask, # 遮罩 有用的話則無視設定長寬
                            font_path=font_path, # 設定字體
                            max_words=200, # 取多少文字在裡面
                            width=1080, height=720, # 長寬解析度
                            relative_scaling=0.5 # 詞頻與詞大小關聯性
                            )
    # 生成文字雲
    wc.generate_from_frequencies(dictionary) # 吃入次數字典資料

    # 輸出
    wc.to_file('./financeArticles/'+ id+'/'+id+'.png')

    exportExcel(title, time,link, article, id, seg_list)

# 抓取財經網頁文章內容
def crewFinanceArticleContentText(contentUrl):
    url = 'https://news.cnyes.com/'+contentUrl
    re = requests.get(url)
    soup = BeautifulSoup(re.text, 'html')
    title =  soup.find('h1').string
    time = soup.find('time').string
    id= contentUrl.split('/')[len(contentUrl.split('/'))-1] 
    texts = soup.find_all('p')
    allArticleText = ''
    for text in texts:
        cText = str(text.string )
        allArticleText += cText
    generateWordCloud(title, time, url, allArticleText, id)

if os.path.isfile('./FinancialArticles.txt'): #第N次抓
  print("檔案存在。")
  notCrewArticle = []
  with open('./FinancialArticles.txt', 'r') as temp_f:
    text = []
    for line in temp_f:
        text.append(line)

  for x in texts:
        if x['href']+'\n' in text:
            print(101, x['href'])
            print(102, '抓過這個網址了')  # The string is found
        else:
            print(22, '沒抓過') # The string does not exist in the file
            notCrewArticle.append(x['href'])
            file = open('./FinancialArticles.txt', 'a+')
            file.write(x['href']+'\n')
            file.close()
  for articleUrl in notCrewArticle:
    crewFinanceArticleContentText(articleUrl)
else: #第一次抓
  print("檔案不存在。")
  file = open('./FinancialArticles.txt', 'w+')
  for x in texts:
    print(45, x)
    file.write(x['href']+'\n')
    file.close()
    with open('./FinancialArticles.txt', 'r') as temp_f:
        text = []
        for line in temp_f:
            text.append(line)
        for x in text:
            url = x.strip('\n')
            crewFinanceArticleContentText(url)

