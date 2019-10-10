import discord

import commands as cmd

TOKEN = '***********************************************************'
CHANNEL_ID = 000000000000000000

client = discord.Client()

@client.event
async def on_ready():
    global music
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('陰キャが帰ってきました\n陰キャBotについて知りたいときは.helpと入力してください')

@client.event
async def on_message(message):
    if message.author.bot:
        return
        
    # コマンド呼び出し
    if message.content[:1] == '.':
        await cmd.command_output(client, message) 

    # あいさつ
    if message.content == 'こんにちは':
        await message.channel.send('こんにちは ' + message.author.name + ' さん')

client.run(TOKEN)
