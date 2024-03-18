import requests # 訪問
from bs4 import BeautifulSoup # 網頁解析
import jieba
from collections import Counter # 次數統計

# 抓取網頁網址
url = 'https://www.msn.com/zh-tw/news/living/%E6%B0%91%E7%9C%BE%E6%90%B6%E5%BF%AB%E7%AF%A9%E4%BD%95%E6%99%82%E7%94%A8-%E9%99%B3%E6%99%82%E4%B8%AD%E5%88%97-%E5%BF%85%E7%AF%A92%E6%83%85%E6%B3%81-%E5%88%A5%E7%AF%A9%E5%BF%83%E5%AE%89/ar-AAXjyKa?ocid=msedgntp&cvid=57c44830a3dc431ab1a9be6e0560d999'
re = requests.get(url)
soup = BeautifulSoup(re.text, 'html.parser')
texts = soup.find_all('p')
# print(texts)
text = texts[0].text
print(text)
# 設定分詞資料庫
jieba.set_dictionary('dict.txt.big.txt')

# 將自己常用的詞加入字典
jieba.load_userdict('finance_dict.txt')

# 新增及刪除常用詞
jieba.add_word('陳時中') # 加入陳時中
jieba.add_word('快篩') # 加入快篩
# jieba.del_word('元') # 刪除元

# 斷句方式
# 用jieba.lcut(text, cut_all=False)直接返回list
# segs = jieba.cut(text, cut_all=True) # 全切模式 切的很碎
# segs = jieba.cut(text, cut_all=False) # 預設模式
seg_list = jieba.lcut(text, cut_all=False) # lcut直接返回list
print(seg_list)
# 統計分詞出現次數
dictionary = Counter(seg_list)
# 移除停用詞
stopword = [' ', '，', '（', '）', '...', '。', '「', '」']  # 定義停用詞
[dictionary.pop(x, None) for x in stopword] # 存字典裡刪除停用詞