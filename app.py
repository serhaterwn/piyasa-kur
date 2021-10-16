import requests, bs4

client = requests.session()
page = client.get('https://uzmanpara.milliyet.com.tr/dolar-kuru/')
page_html = bs4.BeautifulSoup(page.text ,'html.parser')
dolar = page_html.find('span',{'id':'usd_header_son_data'})
euro = page_html.find('span',{'id':'eur_header_son_data'})
bist_100 = page_html.find('span',{'id':'imkb_header_son_data'})
altin = page_html.find('span',{'id':'gld_header_son_data'})
petrol = page_html.find('span',{'id':'petrol_header_son_data'})