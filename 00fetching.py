import requests

def FetchAndSave(url,path):
    r=requests.get(url)
    with open(path,"w", encoding="utf-8") as f:
        f.write(r.text)

url="https://www.dawn.com/"

FetchAndSave(url,"data/times.html")