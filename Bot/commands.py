import discord

HELP_FILE = 'data/help.txt'

mode = 0

async def command_output(client, command):
    global mode
    if command.content[1:] == 'stop':
        await command.channel.send('陰キャはたびに出ました')
        await client.logout()

    if command.content[1:] == 'help':
        with open(HELP_FILE, 'r', encoding="utf-8") as f:
            await command.channel.send(f.read())
            
    if command.content[1:] == 'feedback':
        await command.channel.send('フィードバックの内容を入力してください')
        mode = 1