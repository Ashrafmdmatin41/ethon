#ignore this file

from telethon import events, Button


async def start_srb(event, st):
    await event.reply(st, 
                      buttons=[
                              [Button.inline("Sᴇᴛ Tʜᴜᴍʙ", data="set"),
                               Button.inline("Rᴇᴍᴏᴠᴇ Tʜᴜᴍʙ", data="rem")],
                              [Button.url("Dᴇᴠᴇʟᴏᴘᴇʀ", url="t.me/Md_Matin_Ashraf")]])
                              
    
async def vc_menu(event):
    await event.edit("**VIDEO CONVERTOR v1.4**", 
                    buttons=[
                        [Button.inline("info.", data="info"),
                         Button.inline("SOURCE", data="source")],
                        [Button.inline("NOTICE.", data="notice"),
                         Button.inline("Main.", data="help")],
                        [Button.url("Dᴇᴠᴇʟᴏᴘᴇʀ", url="t.me/Md_Matin_Ashraf")]])
    
