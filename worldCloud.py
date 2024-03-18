# 產生文字雲
import  numpy
from PIL import Image # 圖片轉array陣列
import matplotlib.pyplot as plt
import wordcloud # 文字雲
from collections import Counter # 次數統計
arr =['\n', '\n', '\n', '\n', '\n', '\n', '©', ' ', '由', ' ', 'TVBS', '新聞網', ' ', '提供', '\n', ' ', '何時', '快篩', '，', '陳時中', '解答', '。', '（', '圖', '／', 'TVBS', '資料', '畫面', '）', '\n', '\n', '\n', '國內', '疫情', '爆發', '，', '快篩', '實名制', '上路', '後', '，', '民眾', '排隊', '搶', '買', '快篩', '？', '究竟', '何時', ' 需要', '使用', '快篩', '試劑', '？', '對此', '，', '指揮中心', '指揮官', '陳時中', '今', '（', '16', '）', '日', '表示', '，', '符合', '兩', '情況', '才', '要', '快篩', '，', '呼籲', '民眾', '不要', '想', '篩', '就', '篩', '，', '也', '不要', '為', '了', '心安', '就', '使用', '快篩', '。']
# 統計分詞出現次數
dictionary = Counter(arr)
print(10,dictionary)
# 移除停用詞
stopword = [' ', '，', '（', '）', '...', '。', '「', '」']  # 定義停用詞
[dictionary.pop(x, None) for x in stopword] # 存字典裡刪除停用詞
# for x in stopword:
#   dictionary.pop(x, None)

# 格式設定
font_path = 'NotoSansTC-Light.otf' # 設定字體格式
mask = numpy.array(Image.open('warning (1).png')) # 遮罩
print(18, mask)
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
wc.to_file('my_wordcloud.png')
# 顯示文字雲
# plt.imshow(wc)