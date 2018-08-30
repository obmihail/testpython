# -*- coding: utf-8 -*-
#test <img src=x onerror=alert()>
#<![CDATA[<img src=x onerror=alert()>]]>
#<![CDATA[<a href="javascript:alert()" src=x onerror=alert()>]]>LINK</a>
import requests
r = requests.get('https://yaqs.googleplex.com/eng')
print r
print r.url
print r.text