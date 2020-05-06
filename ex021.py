# DESAFIO 021 - FAÇA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA O ÁUDIO DE UM ARQUIVO MP3
from pygame import mixer, time

ouvir = input("Quer ouvir uma música? (S/N): ")
if ouvir == 's' or 'S':
    mixer.init()
    mixer.music.load('ex021.mp3')
    mixer.music.play()
    input("Parar parar aperte enter: ")
elif ouvir == 'n':
    print('Ok! Até mais!')
else:
    print('Opção inválida.')



'''while mixer.music.get_busy():
    time.Clock().tick(10)'''

'''import playsound

playsound.playsound('ex021.mp3')'''