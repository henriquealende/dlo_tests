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
    freq = ['125', '250', '2000', '4000', '8000']
    currentImpact = eval("'Resources/audios/impact{}.wav'".format(freq[order]))
    filename_compressor = 'Resources/audios/VESH_2800_4189_FD.wav'
    impulse_timeData, _ = sf.read(str(currentImpact), dtype='float32')
    compressor_timeData, samplingRate = sf.read(filename_compressor, dtype='float32')
    currentAudio = (amplitude*(impulse_timeData)+compressor_timeData)
    sd.play(currentAudio, samplingRate)
    status = sd.wait()
    currentAudioID = str(freq[order])
    return currentAudioID

def saveUserFile(ID, name, age, gender, knowledge,
        GH_125, GH_250, GH_500, GH_2000, GH_4000, GH_8000):
    user = {
        'personal_info': {
                'name': name,
                'age': age,
                'gender': gender,
                'knowledge': knowledge
        },
        'answer': {
                'GH_125': GH_125,
                'GH_250': GH_250,
                'GH_500': GH_500,
                'GH_2000': GH_2000,
                'GH_4000': GH_4000,
                'GH_8000': GH_8000
        }
    }
   
    j = json.dumps(user)
    with open(f'Results/{ID}.json', 'w') as f:
      f.write(j)
      f.close
