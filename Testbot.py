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
        if message.author.id == 234724675215818752:
            if message.content == 'Hi everyone':
                await message.channel.send('Thats Chains!')

        if message.content ==('hello there'):
            await message.channel.send('General Kenobi')

        if message.content.startswith('!guess'):
            await message.channel.send('Guess a number between 1 and 10.')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 10)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send('Sorry, you took too long it was {}.'.format(answer))

            if int(guess.content) == answer:
                await message.channel.send('You are right!')
            else:
                await message.channel.send('Oops. It is actually {}.'.format(answer))

        if message.content == ('!calc'):
            await message.channel.send('What number would you like to start with?')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            firstNum = await self.wait_for('message', check=is_correct)

            if int(firstNum.content) <= 100 and int(firstNum.content) >= 0:
                await message.channel.send('And what is the second number?')
            else:
                await message.channel.send('I do not know that number, I can only count from 0 to 100')

            secondNum = await self.wait_for('message', check=is_correct)

            total = int(firstNum.content) + int(secondNum.content)

            if int(secondNum.content) <=100 and int(secondNum.content) >=0:
                await message.channel.send('The total is: ' + str(total))

        if message.content == ('!D4'):
            await message.channel.send(random.randint(1,4))

        if message.content == ('!D6'):
            await message.channel.send(random.randint(1,6))

        if message.content == ('!D8'):
            await message.channel.send(random.randint(1,8))

        if message.content == ('!D10'):
            await message.channel.send(random.randint(1,10))

        if message.content == ('!D12'):
            await message.channel.send(random.randint(1,12))

        if message.content == ('!D20'):
            await message.channel.send(random.randint(1,20))

        if message.content == ('!2D6'):

            D1 = random.randint(1,6)
            D2 = random.randint(1,6)
            if D1 and D2 == 1:
                await message.channel.send('Snake eyes!')
            else:
                await message.channel.send(str(D1) + ' and ' + str(D2))

        if message.content == ('!stop'):
                await client.logout()

client = MyClient()
client.run('NTU1NTA5MTE3NzQ2MjgyNTA3.D2sNxQ.URLyVX-2I6CSBac53sg1lLDxXvg')
