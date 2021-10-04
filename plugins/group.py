from googletrans import Translator
from pyrogram import Client, filters
from helper.list import list
from helper.database import find_one
@Client.on_message(filters.group & filters.command(["tr"]))
async def left(client,message):
	if (message.reply_to_message):
		try:
			lgcd = message.text.split("/tr")
			lg_cd = lgcd[1].lower().replace(" ", "")
			tr_text = message.reply_to_message.text
			translator = Translator()
			translation = translator.translate(tr_text,dest = lg_cd)
			try:
				for i in list:
					if list[i]==translation.src:
						fromt = i
					if list[i] == translation.dest:
						to = i 
				await message.reply_text(f"Diterjemahkan dari **{fromt.capitalize()}** Ke **{to.capitalize()}**\n\n```{translation.text}```")
			except:
			   	await message.reply_text(f"Diterjemahkan dari **{translation.src}** Ke **{translation.dest}**\n\n```{translation.text}```")
      			
				
			
		except :
			print("error")
	else:
			 ms = await message.reply_text("Anda dapat menggunakan perintah ini dengan menggunakan balas ke pesan")
			 await ms.delete()
