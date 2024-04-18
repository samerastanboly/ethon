

from telethon import events, Button


async def start_srb(event, st):
    await event.reply(st, 
                      buttons=[
                              [Button.inline("𝗦𝗘𝗧 𝗧𝗛𝗨𝗠𝗕.", data="set"),
                               Button.inline("𝗥𝗘𝗠 𝗧𝗛𝗨𝗠𝗕.", data="rem")],
                              [Button.url("Ꭰᴇᴠᴇʟᴏᴘᴇʀ", url="t.me/SA_SYR")]])
                              
    
async def vc_menu(event):
    await event.edit("Vɪᴅᴇᴏ Eɴᴄᴏᴅᴇʀ", 
                    buttons=[
                        [Button.inline("INFO", data="info"),
                         Button.inline("Nᴏᴛɪᴄᴇ", data="notice")],
                        [Button.inline("Ꮇᴀɪɴ", data="help")],
                        [Button.url("Ꭰᴇᴠᴇʟᴏᴘᴇʀ", url="t.me/SA_SYR")]])
    
