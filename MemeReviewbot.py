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
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content == ('!meme'):
            Score = random.randint(0,9)
            if Score == 0:
                await message.channel.send('Poor meme\n0 out of 9')
            elif Score == 1:
                await message.channel.send('meh\n1 out of 9')
            elif Score == 2:
                await message.channel.send('Its okay, I guess\n2 out of 9')
            elif Score == 3:
                await message.channel.send('Half decent\n3 out of 9')
            elif Score == 4:
                await message.channel.send('Entry level\n4 out of 9')
            elif Score == 5:
                await message.channel.send('Not bad, Not bad\n5 out of 9')
            elif Score == 6:
                await message.channel.send('Dank\n6 out of 9')
            elif Score == 7:
                await message.channel.send('Goddamn dude\n7 out 9')
            elif Score == 8:
                await message.channel.send('Im literally dying\n8 out of 9')
            else:
                await message.channel.send('Im dead\n9 out of 9')

        if message.content == ('!stop'):
            await message.channel.send('Goodbye')
            await client.logout()

client = MyClient()
client.run('NTU1NTA5MTE3NzQ2MjgyNTA3.D2sNxQ.URLyVX-2I6CSBac53sg1lLDxXvg')
