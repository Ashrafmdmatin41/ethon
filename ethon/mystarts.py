#ignore this file

from telethon import events, Button


async def start_srb(event, st):
    await event.reply(st, 
                      buttons=[
                              [Button.inline("Sᴇᴛ Tʜᴜᴍʙ", data="set"),
                               Button.inline("Rᴇᴍᴏᴠᴇ Tʜᴜᴍʙ", data="rem")],
                              [Button.url("Dᴇᴠᴇʟᴏᴘᴇʀ", url="t.me/Matiz_Owner")]])
                              
    
async def vc_menu(event):
    await event.edit("**𝖵𝖨𝖣𝖤𝖮 𝖢𝖮𝖭𝖵𝖤𝖱𝖳𝖮𝖱 𝗏1.4 😎**", 
                    buttons=[
                        [Button.inline("🧐 Iɴғᴏ", data="info"),
                         Button.inline("🫢 Oᴛʜᴇʀ Bᴏᴛs", data="source")],
                        [Button.inline("📜 Nᴏᴛᴇs", data="notice"),
                         Button.inline("⚙️ Sᴇᴛᴛɪɴɢs", data="help")],
                        [Button.url("👩‍💻 Dᴇᴠᴇʟᴏᴘᴇʀ", url="t.me/Matiz_Owner")]])
    
