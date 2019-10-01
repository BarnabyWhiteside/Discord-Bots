import discord
import random
import asyncio

newUserMessage = "Please message @Kings if you have any questions."

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

        if message.content == ('!stop'):
            await message.channel.send('Goodbye')
            await client.logout()

    async def on_member_joinse(message, member):
        channel = get_channel(568191050909351976)
        await message.channel.send("Welcome " + member.name + "to LinC, please check #server-rules for the rules")
        await client.send_message(memeber, newUserMessage)

        role = discord.utils.get(member.server.roles, name="Gnoblins")
        await client.add_roles(member, role)
        print("Added role '" + role.name + "' to " + member.name)

client = MyClient()
client.run('NTU1NTA5MTE3NzQ2MjgyNTA3.D2sNxQ.URLyVX-2I6CSBac53sg1lLDxXvg')
