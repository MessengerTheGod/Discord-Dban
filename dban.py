import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print(' ')
    print('DBAN')
    print('YOUR')
    print('FUCKING')
    print('DISCORD')
    print('MESSAGES')
    print('LOSER')
    print('Logged in as:', client.user.name)
    print('UID:',client.user.id) 
    print('Discord version:',discord.__version__)
    print('----------')
    print('Connected to:')
    for server in client.servers:
        print(' -',server.name)

# Define commands
@client.event
async def on_message(message):
    if message.author == client.user:
        commands = []
        z = 0
        for index, a in enumerate(message.content):
            if a == " ":
                commands.append(message.content[z:index])
                z = index+1
        commands.append(message.content[z:])
        
        # MASS DELETE OWN MESSAGES
        if commands[0] == 'xc':
            if len(commands) == 1:
                async for msg in client.logs_from(message.channel,limit=9999):
                    if msg.author == client.user:   
                        try:
                            await client.delete_message(msg)
                        except Exception as x:
                            pass
            elif len(commands) == 2:
                user_id = ''
                for channel in client.private_channels:
                    if commands[1] in str(channel):
                        if str(channel.type) == 'private':
                            user_id = str(channel.id)
                async for msg in client.logs_from(discord.Object(id=user_id),limit=9999):
                    if msg.author == client.user:
                        try:
                            await client.delete_message(msg)
                        except Exception as x:
                            pass
                            
client.run("Discord Auth Token here",bot=False)