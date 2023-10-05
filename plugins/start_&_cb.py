import random
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from helper.database import db
from config import Config, Txt  

@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    user = message.from_user
    await db.add_user(client, message)                
    
    # Send an instant reply
    button = InlineKeyboardMarkup([[
        InlineKeyboardButton("🧑‍🏫 Official YouTube 🧑‍🏫", url='https://youtube.com/@techytel')
        ],[
        InlineKeyboardButton('📯 Uᴩᴅᴀᴛᴇꜱ', url='https://t.me/techytel'),
        InlineKeyboardButton('💁‍♂️ Sᴜᴩᴩᴏʀᴛ', url='https://t.me/techytelsupport')
        ],[
        InlineKeyboardButton('🎛️ Aʙᴜᴛ', callback_data='about'),
        InlineKeyboardButton('🛠️ Hᴇʟᴩ', callback_data='help'),
        InlineKeyboardButton('👨‍💻 Dᴇᴠꜱ', callback_data='dev')
    ]])
    
    if Config.START_PIC:
        await message.reply_photo(Config.START_PIC, caption=Txt.START_TXT.format(user.mention), reply_markup=button)       
    else:
        await message.reply_text(text=Txt.START_TXT.format(user.mention), reply_markup=button, disable_web_page_preview=True)
    
    # Schedule a thanks message after 8 minutes
    await asyncio.sleep(480)  # 8 minutes delay
    
    # Send the thanks message
    await send_thanks_message(client, message.chat.id)

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=Txt.START_TXT.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup([[
                InlineKeyboardButton(" 🧑‍🏫 Official YouTube 🧑‍🏫", url='https://youtube.com/@techytel')
                ],[
                InlineKeyboardButton('📯 Uᴩᴅᴀᴛᴇꜱ', url='https://t.me/techytel'),
                InlineKeyboardButton('💁‍♂️ Sᴜᴩᴩᴏʀᴛ', url='https://t.me/techytelsupport')
                ],[
                InlineKeyboardButton('🎛️ Aʙᴏᴜᴛ', callback_data='about'),
                InlineKeyboardButton('🛠️ Hᴇʟᴩ', callback_data='help'),
                InlineKeyboardButton('👨‍💻 Dᴇᴠꜱ', callback_data='dev')
            ]])
        )
    elif data == "help":
        await query.message.edit_text(
            text=Txt.HELP_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                
                InlineKeyboardButton("❓️ Hᴏᴡ Tᴏ Uꜱᴇ ❓️", url='https://youtube.com/@techytel')
                ],[
                InlineKeyboardButton("🔒 Cʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data = "start")
            ]])            
        )
    elif data == "about":
        await query.message.edit_text(
            text=Txt.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("♥︎ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ ♥︎", url="https://github.com/evertel/File-Renamer")
                ],[
                InlineKeyboardButton("🖥 Hᴏᴡ Tᴏ Mᴀᴋᴇ 🖥", url="https://youtu.be/GfulqsSnTv4")
                ],[
                InlineKeyboardButton("🔒 Cʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data = "start")
            ]])            
        )
    elif data == "dev":
        await query.message.edit_text(
            text=Txt.DEV_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("♥︎ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ ♥︎", url="https://github.com/evertel/File-Renamer")
                ],[
                InlineKeyboardButton("🖥 Hᴏᴡ Tᴏ Mᴀᴋᴇ 🖥", url="https://youtu.be/GfulqsSnTv4")
                ],[
                InlineKeyboardButton("🔒 Cʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data = "start")
            ]])          
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
            await query.message.continue_propagation()
        except:
            await query.message.delete()
            await query.message.continue_propagation()

async def send_thanks_message(client, chat_id):
    # Use the Telegraph link as the image URL
    telegraph_image_url = 'https://telegra.ph/file/e3c8ef879ff9bd79475ed.jpg'
    
    # Send a thanks message after 8 minutes
    await client.send_photo(
        chat_id,
        photo=telegraph_image_url,
        caption='Thank you for using the bot!',
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton('📯 Uᴩᴅᴀᴛᴇꜱ', url='https://t.me/techytel'),
            InlineKeyboardButton('💁‍♂️ Sᴜᴩᴩᴏʀᴛ', url='https://t.me/techytelsupport')
        ]])
    )
