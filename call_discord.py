import discord
import random

from env import developerKey, cx, search , items
from insert_db import insert_sqlite,show_recent,call_search_api

class DiscordClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        key = message.content.split(" ",1)
        if message.author == self.user:
            return

        if message.content == 'hey':
            await message.channel.send('hi')

        elif key[0]=="!google":
            if len(key)==1:
                await message.channel.send("Google Seach can't be empty")
            else:
                insert_sqlite(message.author.name, key[1])
                response = call_search_api(key[1])
                await message.channel.send(response)

        elif key[0]=="!recent":
            if len(key)==1:
                await message.channel.send("Recent search can't be empty")
            result  = show_recent(key[1],message.author.name)
            if not result:
                await message.channel.send(key[1]+' not search yat')
            await message.channel.send(result)

        else:
            rand_item = items[random.randrange(len(items))]
            await message.channel.send(rand_item)

if __name__ == '__main__':
        client = DiscordClient()
        client.run(token)