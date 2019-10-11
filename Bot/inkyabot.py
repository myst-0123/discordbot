import discord

import settings
import commands as cmd
import musicplayer as mp

client = discord.Client()
setting = settings.Settings()

music = None
my_channel = None

@client.event
async def on_ready():
    global music
    global my_channel
    channel = client.get_channel(setting.CHANNEL_ID)
    voice_channel = client.get_channel(setting.VOICE_CHANNEL_ID)
    my_channel = client.get_channel(setting.MY_CHANNEL_ID)
    music = mp.MusicPlayer(voice_channel, channel)
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
        await cmd.command_output(client, message, setting.admin_list) 

    # ミュージックプレイヤーの起動
    if message.content[:1] == '!':
        await music.music_player(message)

    # あいさつ
    if message.content == 'こんにちは':
        await message.channel.send('こんにちは ' + message.author.name + ' さん')

client.run(setting.TOKEN)
