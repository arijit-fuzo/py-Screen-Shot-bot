import pyscreenshot

import time

from audioplayer import AudioPlayer

for i in range(6,1,-1):
    print(f"ScreenShot will bw taken in {i} seconds",)
    time.sleep(1)
image = pyscreenshot.grab()
player = AudioPlayer('beep-07a.mp3')
player.play()
#image.show()
image_name = input("What's the img name?\n")
image_name = "".join([image_name,".png"])
image.save(image_name)