"""Vihanraghuॐ
for @catuserbot"""

import random 
import asyncio
import requests as r
from userbot import catub
from telethon import events



@catub.on(events.NewMessage(func=lambda x: x.sender_id == int(840338206)))
async def eli(event):
    if event.is_group:
            me=await event.client.get_me()
            first_name=me.first_name
            last_name=me.last_name 
            if last_name != None:
                full_name = first_name+" "+last_name
            else:
                full_name = first_name
            if "Turn: {}".format(full_name) in event.raw_text:
                try:
                    a = event.raw_text
                    i=list(a.split(" "))
                    alpha = i[-15].lower()
                    length = i[-10]
                    len_of_word = int(length)
                    Ab=[]
                    word_db = r.get('https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt').text
                    i=list(word_db.split("\r\n"))
                    for x in i:
                        if len(x)==len_of_word and x[0]==alpha:
                            Ab.append(x)   
                            word=random.choice(Ab)
                            any = await event.client.send_message(event.chat_id,word)
                            break
                                                                        
                except Exception as e:
                    await event.client.send_message(Config.PRIVATE_GROUP_BOT_API_ID, f"**#Word_error**\n`{e}`")
                    
            
           
            if "{} won".format(full_name) in event.raw_text:
                await event.client.send_message(Config.PRIVATE_GROUP_BOT_API_ID, f"**#Word_game** \n**Congo🎉** \nYou have won the game in {event.chat_id} \n**now gib party** :) \n**Made by** @Vihanraghu ")
              
