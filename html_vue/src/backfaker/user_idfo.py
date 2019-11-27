import requests
import json, urllib
from urllib import parse
from urllib.request import urlopen

#天气信息查询
def request1(m="GET"):
    url = "https:/127.0.0.1:5000"
    params = {
        "Time": '1 2 3 4 5',
        "ID": '1'
    }
    params = parse.urlencode(params)
    if m =="GET":
        f = urlopen("%s?%s" % (url, params))
    else:
        f = urlopen(url, params)
 
    content = f.read()
    res = json.loads(content)
    print(res)