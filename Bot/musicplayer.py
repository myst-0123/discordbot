import discord

class MusicPlayer:
    def __init__(self, voice_channel, text_channel):
        self.vol = 0.5
        self.voice_channel = voice_channel
        self.text_channel = text_channel

    async def music_player(self, message):
        self.message = message.content
        if message.content[1:5] == 'play':
            await self.music_play()
        if message.content[1:6] == 'start':
            await self.music_start()
        if message.content[1:6] == 'pause':
            await self.music_pause()
        if message.content[1:5] == 'stop':
            await self.music_stop()
        if message.content[1:7] == 'volume':
            await self.music_change_vol(float(message.content[8:]))
    
    async def music_play(self):
        song_name = self.message[6:]
        try:
            if self.vc.is_playing():
                self.vc.source = discord.FFmpegPCMAudio(f'data/musics/{song_name}.mp3')
                self.vc.source = discord.PCMVolumeTransformer(self.vc.source)
                self.vc.source.volume = self.vol
                return
            if self.vc.is_connected():
                self.vc.play(discord.FFmpegPCMAudio(f'data/musics/{song_name}.mp3'), after=lambda e: print('done', e))
                self.vc.source = discord.PCMVolumeTransformer(self.vc.source)
                self.vc.source.volume = self.vol
        except:
            self.vc = await self.voice_channel.connect()
            self.vc.play(discord.FFmpegPCMAudio(f'data/musics/{song_name}.mp3'), after=lambda e: print('done', e))
            self.vc.source = discord.PCMVolumeTransformer(self.vc.source)
            self.vc.source.volume = self.vol

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
