import requests
from login import*
import time
check ='http://jwxt.jiangnan.edu.cn/jndx/xs_main.aspx?xh=1040513341'
targetpage = 'http://jwxt.jiangnan.edu.cn/jndx/xscjcx.aspx'
backpage = 'http://jwxt.jiangnan.edu.cn/jndx/xscjcx.aspx?xh=1040513341&xm=%D5%C5%F6%CE%B3%BF&gnmkdm=N121605'
param={'gnmkdm':'N121605',
       'xh':'1040513341',
       'xm':'ÕÅöÎ³¿'
}
s = requests.session()
s = loginin(s)
target =s.get(url= backpage).content
f= open('target.html','wb')
f.write(target)

data={'__EVENTARGUMENT':'',
    '__EVENTTARGET':'',
    'btn_zcj':'ÀúÄê³É¼¨',
      '_VIEWSTATE':'',
    'ddlXN':'',
    'ddlXQ':'',
    'ddl_kcxz':'',
    'hidLanguage':''
    }