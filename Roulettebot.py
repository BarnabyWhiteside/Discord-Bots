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

        if message.content == ('!bets?'):
            await message.channel.send('Numbers 1 to 35, Red, Black, 1st12, 2nd12, 3rd12, 1to18, 19to36, Even, Odd, Neighbours, Thirds, Zero, Orphans')

        if message.content == ('!roulette'):

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            await message.channel.send('How much would you like to bet?')

            inputBet = await self.wait_for('message',check=is_correct)

            Bet = int(inputBet.content)

            if Bet >= 10 and Bet <=1000:

                await message.channel.send('What would you like to bet on?')

                Table = ['0', '32', '15', '19', '4', '21', '2', '25', '17', '34', '6', '27',
                        '13', '36', '11', '30', '8', '23', '10', '5', '24', '16', '33', '1', '20',
                        '14', '31', '9', '22', '18', '29', '7', '28', '12', '35', '3', '26',
                        '1st12', '2nd12', '3rd12',
                        '1to18', 'Even', 'Red', 'Black', 'Odd', '19to36'
                        'Neighbours', 'Thirds', 'Zero', 'Orphans']

                Wheel = ['0', '32', '15', '19', '4', '21', '2', '25', '17', '34', '6', '27',
                        '13', '36', '11', '30', '8', '23', '10','5', '24', '16', '33', '1', '20',
                        '14', '31', '9', '22', '18', '29', '7', '28', '12', '35', '3', '26']

                Spin = random.choice(Wheel)

                try:
                    guess = await self.wait_for('message', timeout=10.0)
                except asyncio.TimeoutError:
                    return await message.channel.send('Sorry, you took too long it was {}.'.format(Spin))

                Guess = guess.content

                if Guess == 'Even' or Guess == 'Odd':
                    if Spin == '1' or Spin == '3' or Spin == '5' or Spin == '7' or Spin == '9' or Spin == '11' or Spin == '13' or Spin == '15' or Spin == '17' or Spin == '19' or Spin == '21' or Spin == '23' or Spin == '25' or Spin == '27' or Spin == '29' or Spin == '31' or Spin == '33' or Spin == '35':
                        Outcome = 'Odd'
                    else:
                        Outcome = 'Even'

                elif Guess == '1to18' or Guess == '19-36':
                    if Spin == '1' or Spin == '2' or Spin == '3' or Spin == '4' or Spin == '5' or Spin == '6' or Spin == '7' or Spin == '8' or Spin == '9' or Spin == '10' or Spin == '11' or Spin == '12' or Spin == '13' or Spin == '14' or Spin == '15' or Spin == '16' or Spin == '17' or Spin == '18':
                        Outcome = '1to18'
                    else:
                        Outcome = '19to36'

                elif Guess == 'Red' or Guess == 'Black':
                    if Spin == '9' or Spin == '18' or Spin == '7' or Spin == '12' or Spin == '3' or Spin == '32' or Spin == '19' or Spin == '21' or Spin == '25' or Spin == '34' or Spin == '27' or Spin == '36' or Spin == '30' or Spin == '23' or Spin == '5' or Spin == '16' or Spin == '1' or Spin == '14':
                        Outcome = 'Red'
                    else:
                        Outcome = 'Black'

                elif Guess == '1st12' or Guess == '2nd12' or Guess == '3rd12':
                    if Spin == '36' or Spin == '33' or Spin == '30' or Spin == '27' or Spin == '24' or Spin == '21' or Spin == '18' or Spin == '15' or Spin == '12' or Spin == '9' or Spin == '6' or Spin == '3':
                        Outcome = '1st12'
                    elif Spin == '35' or Spin == '32' or Spin == '29' or Spin == '26' or Spin == '23' or Spin == '20' or Spin == '17' or Spin == '14' or Spin == '11' or Spin == '8' or Spin == '5' or Spin == '2':
                        Outcome = '2nd12'
                    else:
                        Outcome ='3rd12'

                elif Guess == 'Neighbours':
                    if Spin == '22' or Spin == '18' or Spin == '29' or Spin == '7' or Spin == '28' or Spin == '12' or Spin == '35' or Spin == '3' or Spin == '26' or Spin == '0' or Spin == '23' or Spin == '15' or Spin == '19' or Spin == '4' or Spin == '21' or Spin == '2' or Spin == '25':
                        Outcome = 'Neighbours'
                    else:
                        Outcome = 'lose'

                elif Guess == 'Thirds':
                    if Spin == '27' or Spin == '13' or Spin == '36' or Spin == '11' or Spin == '30' or Spin == '8' or Spin == '23' or Spin == '10' or Spin == '5' or Spin == '24' or Spin == '16' or Spin == '33':
                        Outcome = 'Thirds'
                    else:
                        Outcome = 'lose'

                elif Guess == 'Zero':
                    if Spin == '12' or Spin == '35' or Spin == '3' or Spin == '26' or Spin == '0' or Spin == '32' or Spin == '15':
                        Outcome = 'Zero'
                    else:
                        Outcome = 'lose'

                elif Guess == 'Orphans':
                    if Spin == '1' or Spin == '20' or Spin == '14' or Spin == '9' or Spin == '17' or Spin == '34' or Spin == '6':
                        Outcome = 'Orphans'
                    else:
                        Outcome = 'lose'

                else:
                    if Spin == '0':
                        Outcome = 'lose'
                    else:
                        Outcome = str(Spin)

                if guess.content == Outcome:
                    await message.channel.send('You win')
                    Winnings = 'win'
                else:
                    await message.channel.send('You lose')
                    Winnings = 'lose'

                await message.channel.send(str(Spin))
                await message.channel.send(Outcome)

                if Winnings == 'win':
                    if Outcome == 'Even' or Outcome == 'Odd':
                        Winnings = Bet+Bet
                        await message.channel.send('Here are your winnings: ' + str(Winnings))
                    elif Outcome == '1to18' or Outcome == '18to36':
                        Winnings = Bet+Bet
                        await message.channel.send('Here are your winnings: ' + str(Winnings))
                    elif Outcome == 'Red' or Outcome == 'Black':
                        Winnings = Bet+Bet
                        await message.channel.send('Here are your winnings: ' + str(Winnings))
                    elif Outcome == '1st12' or Outcome == '2nd12' or Outcome =='3rd12':
                        Winnings = (Bet*2)+Bet
                        await message.channel.send('Here are your winnings: ' + str(Winnings))
                    elif Outcome == 'Neighbours':
                        Winnings = Bet+Bet
                        await message.channel.send('Here are your winnings: ' + str(Winnings))
                    elif Outcome == 'Thirds':
                        Winnings = (Bet*2)+bet
                        await message.channel.send('Here are your winnings: ' + str(Winnings))
                    elif Outcome == 'Zero':
                        Winnings = (Bet*4)+Bet
                        await message.channel.send('Here are your winnings: ' + str(Winnings))
                    elif Outcome == 'Orphans':
                        Winnings = (Bet*4)+Bet
                        await message.channel.send('Here are your winnings: ' + str(Winnings))
                    else:
                        Winnings = (Bet*35)+Bet
                        await message.channel.send('Here are your winnings: ' + str(Winnings))
                else:
                    await message.channel.send('House wins ' + str(Bet))

            else:
                await message.channel.send('The bet is invalid\nYou must bet between 10 and 1000')

        if message.content == ('!stop'):
            await message.channel.send('Goodbye')
            await client.logout()

client = MyClient()
client.run('NTU1NTA5MTE3NzQ2MjgyNTA3.D2sNxQ.URLyVX-2I6CSBac53sg1lLDxXvg')
