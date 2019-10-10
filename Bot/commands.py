import discord

HELP_FILE = discord.File('data/help.txt')

mode = 0

async def command_output(client, command):
    global mode
    if command.content[1:] == 'stop':
        await command.channel.send('陰キャはたびに出ました')
        await client.logout()

    if command.content[1:] == 'help':
        await command.channel.send('こちらをご覧ください', file=HELP_FILE)

    if command.content[1:] == 'feedback':
        await command.channel.send('フィードバックの内容を入力してください')
        mode = 1