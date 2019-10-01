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

        if message.content == ('!rules'):
            await message.channel.send("Players place their wagers on the betting spaces on the following choices: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, even, odd, under 7 and over 7. The banker then rolls the two dice and pays out accordingly on the winning betting categories. Payouts are 'for' and not 'to' which means players don't receive their stakes back if they win.")

        if message.content == ('!play'):

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            await message.channel.send('Hello ladies and gentlemen, I will act as the House today \nHow much would you like to bet?')

            betInput = await self.wait_for('message',check=is_correct)
            Bet = int(betInput.content)

            if int(betInput.content) >=10 and int(betInput.content) <=1000:

                await message.channel.send('What would you like to bet on?')

                Table = ['Odd','Under 7', '7', 'Over7', 'Even'
                        '2', '3', '4', '5', '6', '8', '9', '10', '11', '12']

                Dice1 = random.randint(1,6)
                Dice2 = random.randint(1,6)
                Total = Dice1 + Dice2

                try:
                    guess = await self.wait_for('message', timeout=10.0)
                except asyncio.TimeoutError:
                    return await message.channel.send('Sorry, you took too long')

                if guess.content == ('odd') or guess.content == ('even'):
                    if Total == 3 or Total == 5 or Total == 7 or Total == 9 or Total == 11:
                        Outcome = 'odd'
                    else:
                        Outcome = 'even'

                elif guess.content == ('under 7') or guess.content == ('over 7'):
                    if Total < 7:
                        Outcome = 'under 7'
                    elif Total > 7:
                        Outcome = 'over 7'
                    else:
                        Outcome = '7'

                else:
                    Outcome = str(Total)

                if guess.content == Outcome:
                    betCalc = 'win'
                    await message.channel.send('You win')
                else:
                    betCalc= 'lose'
                    await message.channel.send('You lose')

                await message.channel.send(str(Total))
                await message.channel.send(Outcome)

                if betCalc == 'win':
                    if Outcome == 'under 7' or Outcome == 'over 7' or Outcome == 'odd' or Outcome == 'even':
                        Winnings = Bet*2
                        await message.channel.send('Here are your winnings: ' + str(Winnings))
                    elif Outcome == '2' or Outcome == '12':
                        Winnings = Bet*30
                        await message.channel.send('Here are your winnings: ' + str(Winnings))
                    elif Outcome == '3' or Outcome == '11':
                        Winnings = Bet*15
                        await message.channel.send('Here are your winnings: ' + str(Winnings))
                    elif Outcome == '4' or Outcome == '10':
                        Winnings = Bet*10
                        await message.channel.send('Here are your winnings: ' + str(Winnings))
                    elif Outcome == '5' or Outcome == '9':
                        Winnings = Bet*7
                        await message.channel.send('Here are your winnings: ' + str(Winnings))
                    elif Outcome == '6' or Outcome == '8':
                        Winnings = Bet*6
                        await message.channel.send('Here are your winnings: ' + str(Winnings))
                    else:
                        Winnings = Bet*5
                        await message.channel.send('Here are your winnings: ' + str(Winnings))
                else:
                    await message.channel.send('House wins ' + str(Bet))
            else:
                await message.channel.send('That bet is invalid\nYou must bet between 10 and 1000')

        if message.content == ('!stop'):
            await message.channel.send('Goodbye')
            await client.logout()

client = MyClient()
client.run('NTU1NTA5MTE3NzQ2MjgyNTA3.D2sNxQ.URLyVX-2I6CSBac53sg1lLDxXvg')
