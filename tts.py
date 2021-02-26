from  gtts import gTTS

import os

myText = "hello saif"

language = 'en'

output = gTTS(text = myText,lang = language,slow = False)

output.save("gg.mp3")


os.system("start gg.mp3")