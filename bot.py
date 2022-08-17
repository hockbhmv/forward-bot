import os 
from config import Config
from pyrogram import Client, filters

class Bot(Client): 
    def __init__(self):
        super().__init__(
            name="Forward-bot",
            api_hash=Config.API_HASH,
            api_id=Config.API_ID,
            plugins={
                "root": "plugins"
            },
            workers=30,
            bot_token=Config.BOT_TOKEN
        )
        self.userbot = None
      
    async def start(self):
        await super().start()
        if Config.SESSION_STRING:
           userbot = await self.userbot_start()
           self.userbot = userbot
           print(f"userbot {userbot.me.first_name} started")
        print(f"{self.me.first_name} is Successfully started")
    
    async def stop(self):
        await super().stop() 
        print(f'{self.me.first_name} stopped...')
    
    async def userbot_start(self):
        userbot = Client(
           api_id=Config.API_ID,
           api_hash=Config.API_HASH,
           session_string=Config.SESSION_STRING 
        )
        return await userbot.start()
