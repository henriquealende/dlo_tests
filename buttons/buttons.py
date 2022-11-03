from widget import *
from processing.processing import *
import random as rd
import numpy as np


class UI_Buttons():
    def __init__(self):
        super(UI_Buttons, self).__init__()

    def nextHome(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.register_page)
        fadeIn = QGraphicsOpacityEffect(self.ui.register_page)
        self.animation = QPropertyAnimation(fadeIn, b"opacity")
        self.ui.register_page.setGraphicsEffect(fadeIn)
        self.animation.setDuration(1000)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

    def nextRegister(self):
        genderCheck = False
        knowledgeCheck = False
        nameCheck = False
        ageCheck = False
        self.name = self.ui.username.text()
        if len(self.name) != 0:
            nameCheck = True
        if self.ui.maleRadioButton.isChecked():
            self.gender = "Male"
            genderCheck = True
        elif self.ui.femaleRadioButton.isChecked():
            self.gender = "Female"
            genderCheck = True
        self.age = self.ui.userage.text()
        if len(self.age) != 0:
            ageCheck = True
        if self.ui.expertRadioButton.isChecked():
            self.knowledge = "Expert"
            knowledgeCheck = True
        elif self.ui.laypersonRadioButton.isChecked():
            self.knowledge = "Female"
            knowledgeCheck = True

        if nameCheck and genderCheck and ageCheck and knowledgeCheck:

            self.randomlist = rd.sample(range(0, 5), 5)
            self.amplitude = (rd.randint(6,10))/10
            self.amplitudeChangeStaircase = self.amplitude/20
            self.amplitudeChangePest = 2

            self.progress = 0
            self.orderAudio = 0
            self.negativeAnswerCheck = False
            self.positiveAnswerCheck = False
            self.ProgressBarValue(self.progress)
            self.ui.testSoundButton.setEnabled(True)
            self.gainHistory = []

            self.ui.stackedWidget.setCurrentWidget(self.ui.reference_page)
            fadeIn = QGraphicsOpacityEffect(self.ui.reference_page)
            self.animation = QPropertyAnimation(fadeIn, b"opacity")
            self.ui.reference_page.setGraphicsEffect(fadeIn)
            self.animation.setDuration(1000)
            self.animation.setStartValue(0)
            self.animation.setEndValue(1)
            self.animation.start()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Atenção')
            msg.setText('Preencha todos os campos do cadastro')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()


    def playReferenceSound(self, freq):
        readAndPlayReference(freq)
        self.ui.referenceSoundButtonLow.setChecked(True)
        if (self.ui.referenceSoundButtonLow.isChecked() and
                self.ui.referenceSoundButtonMid.isChecked() and
                self.ui.referenceSoundButtonHigh.isChecked()):
            self.ui.readyButton.setEnabled(True)

    def startTest(self):
        self.ui.test_page.setGraphicsEffect(None)
        self.ui.stackedWidget.setCurrentWidget(self.ui.test_page)
        fadeIn = QGraphicsOpacityEffect(self.ui.test_page)
        self.animation = QPropertyAnimation(fadeIn, b"opacity")
        self.ui.test_page.setGraphicsEffect(fadeIn)
        self.animation.setDuration(1000)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

    def playTestSound(self):
        self.currentAudioID = readAndPlayTest(self.randomlist[self.orderAudio], self.amplitude)
        self.ui.positiveButton.setEnabled(True)
        self.ui.negativeButton.setEnabled(True)
        self.ui.testSoundButton.setDisabled(True)
        self.gainHistory = np.append(self.gainHistory, self.amplitude)


    def positiveAnswer(self):
        self.ui.positiveButton.setEnabled(False)
        self.ui.negativeButton.setEnabled(False)
        self.ui.testSoundButton.setDisabled(False)        
        if self.negativeAnswerCheck:
            self.amplitude = self.amplitude/(0.5*self.amplitudeChangePest)
        else:
            self.amplitude = self.amplitude/self.amplitudeChangePest
        if len(self.gainHistory) > 15:
            self.ui.nextStepButton.setEnabled(True)
            self.ui.positiveButton.setEnabled(False)
            self.ui.negativeButton.setEnabled(False)
            self.ui.testSoundButton.setDisabled(True)        
        self.positiveAnswerCheck = True
        self.negativeAnswerCheck = False

    def negativeAnswer(self):
        self.ui.positiveButton.setEnabled(False)
        self.ui.negativeButton.setEnabled(False)
        self.ui.testSoundButton.setDisabled(False)
        if self.positiveAnswerCheck:
            self.amplitude = self.amplitude*(0.5*self.amplitudeChangePest)
        else:
            self.amplitude = self.amplitude*self.amplitudeChangePest
        if len(self.gainHistory) > 15:
            self.ui.nextStepButton.setEnabled(True)
            self.ui.positiveButton.setEnabled(False)
            self.ui.negativeButton.setEnabled(False)
            self.ui.testSoundButton.setDisabled(True)        
        self.positiveAnswerCheck = False
        self.negativeAnswerCheck = True

    def nextStepTest(self):
        self.progress += 16
        self.ProgressBarValue(self.progress)
        self.amplitude = self.gainHistory[0]

        self.ui.test_page.setGraphicsEffect(None)
        fadeIn = QGraphicsOpacityEffect(self.ui.circularProgressBarBase)
        self.animation = QPropertyAnimation(fadeIn, b"opacity")
        self.ui.circularProgressBarBase.setGraphicsEffect(fadeIn)
        self.animation.setDuration(1000)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()
        self.ui.nextStepButton.setEnabled(False)
        self.ui.testSoundButton.setEnabled(True)
        if self.currentAudioID == '125':
            self.GH_125 = self.gainHistory
        elif self.currentAudioID == '250':
            self.GH_250 = self.gainHistory
        elif self.currentAudioID == '500':
            self.GH_500 = self.gainHistory
        elif self.currentAudioID == '2000':
            self.GH_2000 = self.gainHistory
        elif self.currentAudioID == '4000':
            self.GH_4000 = self.gainHistory
        elif self.currentAudioID == '8000':
            self.GH_8000 = self.gainHistory
        self.gainHistory = []

        if self.orderAudio >= 4:
            self.ui.circularProgressBarBase.setGraphicsEffect(None)
            self.ui.stackedWidget.setCurrentWidget(self.ui.final_page)
            fadeIn = QGraphicsOpacityEffect(self.ui.final_page)
            self.animation = QPropertyAnimation(fadeIn, b"opacity")
            self.ui.final_page.setGraphicsEffect(fadeIn)
            self.animation.setDuration(1000)
            self.animation.setStartValue(0)
            self.animation.setEndValue(1)
            self.animation.start()
        else:
            self.orderAudio += 1
            self.ui.step_label.setText("etapa " + str(self.orderAudio + 1))

    def idUserChange(self):
        self.idUser = self.ui.idUserLine.text()
        if len(self.idUser) != 0:
            self.ui.quitButton.setEnabled(True)
        else:
            self.ui.quitButton.setEnabled(False)

    def closeApp(self):
        saveUserFile(self.idUser, self.name, self.gender, self.age, self.knowledge,
                self.GH_125, self.GH_250, self.GH_500, self.GH_2000,
                self.GH_4000, self.GH_8000)
        self.close()

    def closeAll(self):
        self.close()

    def minimizeApp(self):
        self.showMinimized()



