import discord
from discord.ext import tasks
from spotify_api import add_track
import re
import os
from dotenv import load_dotenv
load_dotenv()
class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.counter = 0
        self.get_tracks.start()
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
       
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('https://open.spotify.com/track/'):
            self.counter = 0
            await message.channel.send("Adding Song")
            song = [message.content]
            add_track(song)
    @tasks.loop(seconds=5)
    async def get_tracks(self):

        channel = self.get_channel(966780512255500378)
        if self.counter == 0:
            self.counter += 1
            await channel.send("Running")
            messages = await channel.history(limit=200).flatten()
            pre_url = "https://open.spotify.com/track/" 
            
            m = []
            for msg in messages:
                if "https://open.spotify.com/track/" in msg.content:
                    result = re.findall('https:\//open\.spotify\.com\/track\/[0-9a-zA-Z]+', msg.content)
                    for r in result:
                        m.append(r)
            add_track(m)
#                    add_track(msg.content)
        elif self.counter == 1:
            self.get_tracks.stop()
            await channel.send("Waiting for new track")
    @get_tracks.before_loop
    async def before_task(self):
        await self.wait_until_ready()
client=MyClient()
client.run('DISCORD_TOKEN')

