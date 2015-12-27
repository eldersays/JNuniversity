import requests
import re
from STEP1 import*
checkcodepage = 'http://jwxt.jiangnan.edu.cn/jndx/CheckCode.aspx'
firstpage = 'http://jwxt.jiangnan.edu.cn/jndx/default2.aspx'
mainpage = 'http://jwxt.jiangnan.edu.cn/jndx/xs_main.aspx?xh=1040513341'
contentpage = 'http://jwxt.jiangnan.edu.cn/jndx/content.aspx'

headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
           'Connection':'keep-alive',
           'Host':'202.195.144.163',
           'Referer':'http://202.195.144.163/jndx/xs_main.aspx?xh=1040513341',
           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0'
            }

def loginin(sess):
    sess.headers.update(headers)
    defaultpage = sess.get(url= firstpage).content
    view = str(defaultpage)
    view = re.search(r'VIEWSTATE" value=".*?\" />',view).group(0)
    view =re.sub('VIEWSTATE" value=\"','',view)
    view = re.sub('\" />','',view)
    checkcode =sess.get(url=checkcodepage).content
    pic = open('newpic.gif','wb')
    pic.write(checkcode)
    pic.close()
    checkcod_key = recpic()
    idata={
    'RadioButtonList1':'Ñ§Éú',
    'Button1' :'',
    '__VIEWSTATE':view,
    'TextBox1':'1040513341',
    'TextBox2':'33070219950714351X',
    'TextBox3':checkcod_key,
    'lbLanguage':''
    }
    sess.post(url=firstpage,data=idata)
    return sess

