import discord

HELP_FILE = 'data/help.txt'

mode = 0

async def command_output(client, command, admin_list):
    global mode
    if command.content[1:] == 'stop':
        if command.author.id in admin_list:
            await command.channel.send('陰キャはたびに出ました')
            await client.logout()
        else:
            await command.channel.send('このコマンドを実行する権限がありません')

    if command.content[1:] == 'help':
        with open(HELP_FILE, 'r', encoding="utf-8") as f:
            await command.channel.send(f.read())
            
    if command.content[1:] == 'feedback':
        await command.channel.send('フィードバックの内容を入力してください')
        mode = 1
