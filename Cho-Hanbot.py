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

        if message.content == ('!stakes'):
            await message.channel.send('Max: 1000 \n Min: 10')

        if message.content == ('!play'):

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            await message.channel.send('How much would you like to bet?')

            betInput = await self.wait_for('message',check=is_correct)
            Bet = int(betInput.content)

            if Bet >= 10 and Bet <= 1000:

                await message.channel.send('What would you like to bet on?')

                Dice1 = random.randint(1,6)
                Dice2 = random.randint(2,6)
                Total = Dice1 + Dice2

                try:
                    guess = await self.wait_for('message', timeout=10.0)
                except asyncio.TimeoutError:
                    return await message.channel.send('Sorry, you took too long')

                if Total == 2 or Total == 4 or Total == 6 or Total == 8 or Total == 10 or Total == 12:
                    Outcome = 'Even'
                else:
                    Outcome = 'Odd'

                if guess.content == Outcome:
                    Outcome = 'win'
                    await message.channel.send('You win')
                else:
                    await message.channel.send('You lose')

                await message.channel.send(str(Dice1) + ' ' + str(Dice2))

                if Outcome == 'win':
                    Winnings = int(Bet.content)*2
                    await message.channel.send('Here are your winnings ' + str(Winnings))

            else:
                await message.channel.send('That bet is invalid\nYou must bet between 10 and 1000')

        if message.content == ('!stop'):
            await message.channel.send('Goodbye')
            await client.logout()

client = MyClient()
client.run('NTU1NTA5MTE3NzQ2MjgyNTA3.D2sNxQ.URLyVX-2I6CSBac53sg1lLDxXvg')
