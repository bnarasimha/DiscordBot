#!/bin/python
import os
import discord
import bot_response

async def send_message(message, user_message, is_private):
    try:
        response = bot_response.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

    
def run_discord_bot():
    TOKEN= os.environ["DISCORD_TOKEN"]
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        user_message = str(message.content)
        
        await send_message(message, user_message, is_private=False)

    client.run(TOKEN)

if __name__ == '__main__':
    run_discord_bot()