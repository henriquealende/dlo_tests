import sounddevice as sd
import soundfile as sf
import numpy as np
import json

from PySide2.QtWidgets import QGraphicsOpacityEffect
from PySide2.QtCore import QPropertyAnimation

def readAndPlayReference(type):
    if type == "Low":
        filename = 'Resources/audios/impactLowFrequency.wav'
    elif type == "Mid":
        filename = 'Resources/audios/impactMidFrequency.wav'
    elif type == "High":
        filename = 'Resources/audios/impactHighFrequency.wav'
    reference_timeData, samplingRate = sf.read(filename, dtype = 'float32')
    sd.play(reference_timeData, samplingRate)
    status = sd.wait()

def readAndPlayTest(order, amplitude):
    filename_low = 'Resources/audios/impactLowFrequency05.wav'
    filename_mid = 'Resources/audios/impactMidFrequency10.wav'
    filename_high = 'Resources/audios/impactHighFrequency10.wav'
    filename_compressor = 'Resources/audios/VESH_2800_4189_FD.wav'
    low_impulse_timeData, _ = sf.read(filename_low, dtype='float32')
    mid_impulse_timeData, _ = sf.read(filename_mid, dtype='float32')
    high_impulse_timeData, _ = sf.read(filename_high, dtype='float32')
    compressor_timeData, samplingRate = sf.read(filename_compressor, dtype='float32')
    test_sounds = [low_impulse_timeData, mid_impulse_timeData, high_impulse_timeData]
    currentAudio = (amplitude*(test_sounds[order])+compressor_timeData)
    sd.play(currentAudio, samplingRate)
    status = sd.wait()
    if order == 0:
        currentAudioID = 'low'
    elif order ==1:
        currentAudioID = 'mid'
    else:
        currentAudioID = 'high'

def saveUserFile(ID, name, age, gender, knowledge,
        GH_L_S, GH_M_S, GH_H_S, GH_L_P, GH_M_P, GH_H_P):
    user = {
        'personal_info': {
                'name': name,
                'age': age,
                'gender': gender,
                'knowledge': knowledge
        },
        'answer': {
                'GH_Low_STAIR': GH_L_S,
                'GH_Mid_STAIR': GH_M_S,
                'GH_High_STAIR': GH_H_S,
                'GH_Low_PEST': GH_L_P,
                'GH_Mid_PEST': GH_M_P,
                'GH_High_PEST': GH_H_P
        }
    }
   
    j = json.dumps(user)
    with open(f'Results/{ID}.json', 'w') as f:
      f.write(j)
      f.close
