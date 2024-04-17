#ignore this file

from telethon import events, Button


async def start_srb(event, st):
    await event.reply(st, 
                      buttons=[
                              [Button.inline("SET THUMB.", data="set"),
                               Button.inline("REM THUMB.", data="rem")],
                              [Button.url("DEV", url="t.me/r4h4t_69")]])
                              
    
async def vc_menu(event):
    await event.edit("**VIDEO CONVERTOR v1.0**", 
                    buttons=[
                        [Button.inline("INFO", data="info"),
                         Button.inline("SOURCE", data="source")],
                        [Button.inline("NOTICE", data="notice"),
                         Button.inline("MAIN", data="help")],
                        [Button.url("DEVELOPER", url="t.me/SA_SYR")]])
    
