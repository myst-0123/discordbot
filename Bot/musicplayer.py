import discord
import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl':  "sample_music" + '.%(ext)s',
    'postprocessors': [
        {'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
         'preferredquality': '192'},
        {'key': 'FFmpegMetadata'},
    ],
}

ydl = youtube_dl.YoutubeDL(ydl_opts)

class MusicPlayer:
    def __init__(self, voice_channel, text_channel, volume):
        self.LIST_FILE = discord.File('data/musiclist.txt')
        self.vol = volume
        self.voice_channel = voice_channel
        self.text_channel = text_channel

    async def music_player(self, message):
        if message.content[1:5] == 'list':
            await self.show_list()
        if message.content[1:5] == 'join':
            await self.join_voice_channel()
        if message.content[1:5] == 'play':
            await self.music_play(message.content[6:])
        if message.content[1:6] == 'start':
            await self.music_start()
        if message.content[1:6] == 'pause':
            await self.music_pause()
        if message.content[1:5] == 'stop':
            await self.music_stop()
        if message.content[1:7] == 'volume':
            await self.music_change_vol(float(message.content[8:]))

    async def show_list(self):
        await self.text_channel.send('曲のリストです', file=self.LIST_FILE)

    async def join_voice_channel(self):
        self.vc = await self.voice_channel.connect()

    async def music_play(self, song_name):
        try:
            if song_name[0:4] == 'http':
                if self.vc.is_playing():
                    self.vc.source = discord.FFmpegPCMAudio(ydl.add_extra_info(song_name, download=False))
                else:
                    self.vc.play(discord.FFmpegPCMAudio(ydl.add_extra_info(song_name, download=False)), after=lambda e: print('done', e))
            else:
                if self.vc.is_playing():
                    self.vc.source = discord.FFmpegPCMAudio(f'data/musics/{song_name}.mp3')
                else:
                    self.vc.play(discord.FFmpegPCMAudio(f'data/musics/{song_name}.mp3'), after=lambda e: print('done', e))

            self.vc.source = discord.PCMVolumeTransformer(self.vc.source)
            self.vc.source.volume = self.vol
        except:
            await self.text_channel.send('ボイスチャットに接続されていません!joinで接続します')

    async def music_start(self):
        try:
            print(self.vc.is_paused())
            if self.vc.is_paused():
                self.vc.resume()
        except:
            pass

    async def music_pause(self):
        try:
            if self.vc.is_playing():
                self.vc.pause()
        except:
            pass

    async def music_stop(self):
        try:
            if self.vc.is_playing or self.vc.is_paused:
                self.vc.stop()
        except:
            pass

    async def music_change_vol(self, vol):
        try:
            self.vc.source.volume = vol
            self.vol = vol
            await self.text_channel.send('音量を{}%に設定しました'.format(vol * 100))
        except:
            pass
