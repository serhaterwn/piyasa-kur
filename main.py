from dhooks import Webhook
import json
import time
import app

while True:
    with open('config.json','r') as f:
        birimler = json.load(f)
    try:
        dolarhook = Webhook(str(birimler['dolar']))
        dolarhook.send('**Dolar anlik olarak: **'+app.dolar.text+ ' TRY')
    except ValueError:
        pass
    try:
        eurohook = Webhook(str(birimler['euro']))
        eurohook.send('**Euro anlik olarak: **'+app.euro.text+' TRY')
    except ValueError:
        pass
    try:
        bist_100_hook = Webhook(str(birimler['bist_100']))
        bist_100_hook.send('**Bist100 anlik olarak: **'+app.bist_100.text+' TRY')
    except ValueError:
        pass
    try:
        altin_hook = Webhook(str(birimler['altin']))
        altin_hook.send('**Altin anlik olarak: **'+app.altin.text+' TRY')
    except ValueError:
        pass
    try:
        petrol_hook = Webhook(str(birimler['petrol']))
        petrol_hook.send('**Petrol anlik olarak: **'+app.petrol.text+' TRY')
    except ValueError:
        pass
    time.sleep(15)









