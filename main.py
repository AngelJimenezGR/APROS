#Developer Angel Jimenez

from gtts import gTTS
import os
from time import ctime
import time
import sys
import datetime
import goslate

"""
    Esto es un ejemplo de como puede llegar a ser
    el asistente personal que se va a desarrollar
"""


def welcome():

    try:
        audio1 = 'Hola Angel'
        audio2 = '¿Que quieres hacer hoy?'
        tts = gTTS(audio1+audio2, lang='es')
        tts.save('sudo Audio/welcomeeeee.mp3')
        os.system('sudo Audio/welcome.mp3')
    except os.error as e:
        print(e)



def speak(audio):

    print(audio)
    tts = gTTS(audio, lang='es')
    tts.save('hello.mp3')
    print('Respondiendo....\n')

    # se introduce el comando para reproducir el audio que se ha guardado
    os.system('hello.mp3')

def request(data):

    gs = goslate.Goslate()

    respuesta = ''
    if data.lower() == 'pescar':
        respuesta = '¿A que sitio quieres ir a pescar?'
        speak(respuesta)
    elif data.lower() == 'que dia es hoy':
        respuesta = datetime.datetime.now().strftime('%A')
        speak('Hoy es ' + gs.translate(respuesta, 'es'))
    elif data.lower() == 'salir':
        respuesta = 'Te echare de menos Angel'
        speak(respuesta)
    else:
        speak('Lo siento no te he entendido')



# Inicio del Asistente personal-----------------------------------------

welcome()

mensaje = input('--> ')
request(mensaje)





