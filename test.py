import requests
import pandas as pd

baseurl = "https://rickandmortyapi.com/api/"
endpoint ="character"

def main_request(baseurl,endpoint,x):
    r = requests.get(baseurl+endpoint+f'?page={x}')
    return r.json()
def get_pages(response):
    pages = response['info']['pages']
    return pages
def parse_json(response):
    chrlist = []
    for item in response['results']:
        id  = item['id']
        name = item['name']
        size = len(item['episode'])
        dic = {
            'id':id,
            'name':name,
            'no_episode':size
        }
        chrlist.append(dic)
    return chrlist
    


data = main_request(baseurl,endpoint,1)
mlist =[]
pages= get_pages(data)
for i in range(1,pages+1):
    print(i)
    mlist.extend(parse_json(main_request(baseurl,endpoint,i)))

df = pd.DataFrame(mlist)
print(df.head(),df.tail())
df.to_csv('character_list.csv',index=False)