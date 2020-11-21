from pydub import AudioSegment
from pydub.playback import play

print('coloque o seu audio na pasta do script')
mp3 = input('Qual o nome do arquivo: ')

song = AudioSegment.from_mp3(f"{mp3}.mp3")
play(song)
