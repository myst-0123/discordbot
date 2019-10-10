import discord

HELP_FILE = discord.File('data/help.txt')

async def command_output(client, command):
    if command.content[1:] == 'stop':
        await command.channel.send('陰キャはたびに出ました')
        await client.logout()

    if command.content[1:] == 'help':
        await command.channel.send('こちらをご覧ください', file=HELP_FILE)
