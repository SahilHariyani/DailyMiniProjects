import speech_recognition as sr
import pyautogui
r = sr.Recognizer()

#selects default system mic
mic = sr.Microphone()

print('Speak something')

try:
    with mic as source:
       
        r.adjust_for_ambient_noise(source)  #to decrease the background noice
        audio = r.listen(source)

    output = r.recognize_google(audio)
except:
    print('Some Error occured')

pyautogui.click(100, 100)
pyautogui.typewrite(output)
print('done')