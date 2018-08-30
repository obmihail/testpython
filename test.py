# -*- coding: utf-8 -*-
import requests
r = requests.get('https://yaqs.googleplex.com/eng')
print r
print r.url
print r.text