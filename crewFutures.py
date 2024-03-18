import requests # 訪問
# 資料處理套件
import pandas 
from datetime import datetime
currentDateAndTime = datetime.now()
currentTime = currentDateAndTime.strftime("%Y-%m-%d-%H%M%S")
# 抓取網頁網址
url = "https://mis.taifex.com.tw/futures/api/getQuoteList"
payload = {"MarketType":"0",
           "SymbolType":"F",
           "KindID":"1",
           "CID":"TXF",
           "ExpireMonth":"",
           "RowSize":"全部",
           "PageNo":"",
           "SortColumn":"",
           "AscDesc":"A"}
res = requests.post(url, json = payload)
data = res.json()
for x in data['RtData']['QuoteList']:
   x['CTime'] = x['CTime'][0:2]+':'+x['CTime'][2:4]+':'+x['CTime'][4:6]
df = pandas.DataFrame(data['RtData']['QuoteList'])
df = df[["DispCName", "Status", "CBidPrice1", "CBidSize1", "CAskPrice1", "CAskSize1", "CLastPrice", "CDiff", "CAmpRate", "CTotalVolume", "COpenPrice","CHighPrice","CLowPrice","CRefPrice","CTime"]]
df.columns = ['商品', '狀態', '買進', '買量', '賣出', '賣量', '成交價', '漲跌', '振幅%', '成交量', '開盤', '最高', '最低', '參考價', '時間']
print(21, df)
df.to_csv('C:/公司/ChengTeams/cyim-futures-zhou/futures_regular_trading/'+currentTime+'.csv', index=False, encoding='utf-8-sig')