import requests
from lxml import etree
import time

url = "http://47.102.107.100:39012/"
session = requests.Session()


while True:
    response = session.get(url).text
    calc = etree.HTML(response).xpath("//form/div/text()")
    s=calc[0]
    s=s.split('=')
    s[0]=eval(s[0])
    s[1]=eval(s[1])
    result=(s[0]==s[1])
    if(result):
        result="true"
    else :
        result="false"
    print(result)
    data = {
        "answer": result
    }
    time.sleep(1)

    print(data)
    req = session.post(url, data=data)
    print(req.text)