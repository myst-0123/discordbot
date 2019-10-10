import discord

import commands as cmd

TOKEN = '***********************************************************'
CHANNEL_ID = 000000000000000000
MY_CHANNEL_ID = 000000000000000000

my_channel = None

client = discord.Client()

@client.event
async def on_ready():
    global music
    global my_channel
    channel = client.get_channel(CHANNEL_ID)
    my_channel = client.get_channel(MY_CHANNEL_ID)
    await channel.send('陰キャが帰ってきました\n陰キャBotについて知りたいときは.helpと入力してください')

@client.event
async def on_message(message):
    global mode
    # ボットからのメッセージは無視する
    if message.author.bot:
        return

    # フィードバックの送信モード
    if cmd.mode == 1:
        await my_channel.send('フィードバックが届きました\n\n' + message.content)
        await message.channel.send('フィードバックを送信しました')
        cmd.mode = 0

    # コマンド呼び出し
    if message.content[:1] == '.':
        await cmd.command_output(client, message) 

    # あいさつ
    if message.content == 'こんにちは':
        await message.channel.send('こんにちは ' + message.author.name + ' さん')

client.run(TOKEN)
