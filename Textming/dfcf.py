import requests
from lxml import etree
from snownlp import SnowNLP
import pandas as pd
import tushare as ts
import time as tm

code = ts.get_hs300s()['code']



for i in code[1:]:   
    go = False
    df_ = pd.DataFrame([],columns=[['time','text','wlyq']])
    for page in range(1,9999):
        try:
            url = 'http://guba.eastmoney.com/list,'+str(i)+',f_'+str(page)+'.html'
            html  = requests.get(url)
            html = etree.HTML(html.text)
            #data = html.xpath('//*[@id="articlelistnew"]/div/span/a')
            
            
            #for i in data:
            #    try:
            #        prob = SnowNLP(i.text).sentiments 
            #        print(prob)
            #    except:--
            #        continue
            
            time = html.xpath('//span[@class="l6"]/text()')[1:]
            text = html.xpath('//span[@class="l3"]/a/text()')
            df = pd.DataFrame([],columns=[['time','text']])
            df['time'] = time
            df['text'] = text
            df['wlyq'] = df.text
            df['wlyq'] = df['wlyq'].applymap(lambda x:SnowNLP(x).sentiments)
            df_ = pd.concat([df_,df],axis=0)
            print ('get',str(i),'++++',str(page))
            
            if list(df.time[-2:-1].values[0])[0][:2] == '02' and go == False:
                go = True
                cout = 0
            if cout >=50 and list(df.time[-2:-1].values[0])[0][:2] == '02' and go ==True:
                break
            cout += 1
        except:
            continue
    df_.to_csv(i+'.csv')

