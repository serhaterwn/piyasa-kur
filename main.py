from dhooks import Webhook
import requests, bs4
import json
import time

while True:
    client = requests.session()
    page = client.get('https://uzmanpara.milliyet.com.tr/dolar-kuru/')
    page_html = bs4.BeautifulSoup(page.text ,'html.parser')
    dolar = page_html.find('span',{'id':'usd_header_son_data'})
    euro = page_html.find('span',{'id':'eur_header_son_data'})
    bist_100 = page_html.find('span',{'id':'imkb_header_son_data'})
    altin = page_html.find('span',{'id':'gld_header_son_data'})
    petrol = page_html.find('span',{'id':'petrol_header_son_data'})
    with open('config.json','r') as f:
        birimler = json.load(f)
    try:
        dolarhook = Webhook(str(birimler['dolar']))
        dolarhook.send('**Dolar anlik olarak: **'+dolar.text+ ' TRY')
    except ValueError:
        pass
    try:
        eurohook = Webhook(str(birimler['euro']))
        eurohook.send('**Euro anlik olarak: **'+euro.text+' TRY')
    except ValueError:
        pass
    try:
        bist_100_hook = Webhook(str(birimler['bist_100']))
        bist_100_hook.send('**Bist100 anlik olarak: **'+bist_100.text+' TRY')
    except ValueError:
        pass
    try:
        altin_hook = Webhook(str(birimler['altin']))
        altin_hook.send('**Altin anlik olarak: **'+altin.text+' TRY')
    except ValueError:
        pass
    try:
        petrol_hook = Webhook(str(birimler['petrol']))
        petrol_hook.send('**Petrol anlik olarak: **'+petrol.text+' TRY')
    except ValueError:
        pass
    time.sleep(60)









