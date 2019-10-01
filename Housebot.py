import discord
import random
import asyncio

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):

        strWinnings = str()

        if message.author.id == self.user.id:
            if message.content == 'bank ' + strWinnings:
                await message.channel.send('you have banked ' + strWinnings)
            else:
                return

        if message.content == '!test':
            input = random.randint(1,100)       #in place of game
            strWinnings = str(input)
            await message.channel.send('bank ' + strWinnings)

        if message.content == '!test2':
            await message.channel.send('anything else')

        if message.content == ('!stop'):
            await message.channel.send('Goodbye')
            await client.logout()

client = MyClient()
client.run('NTU1NTA5MTE3NzQ2MjgyNTA3.D2sNxQ.URLyVX-2I6CSBac53sg1lLDxXvg')
