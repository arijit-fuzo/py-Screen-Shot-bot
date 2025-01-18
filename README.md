# py-Screen-Shot-bot
Here's a more concise version of the README with some emojis for a friendly touch:

---

# Screenshot & Audio Notification 📸🔊

This Python script captures a screenshot after a countdown, plays a beep sound, and lets you name the image file. It uses `pyscreenshot` for screenshots and `audioplayer` for sound notifications.

## Features ✨

- Countdown before the screenshot ⏳
- Audio notification 🔔
- Name your screenshot file 📁
- Saves as a `.png` image 🖼️

## Requirements ⚙️

Install the required libraries:

```bash
pip install pyscreenshot audioplayer
```

## How to Use 🚀

1. Run the script:

   ```bash
   python screenshot_script.py
   ```

2. The countdown starts from 6 seconds ⏰.
   
3. Once the countdown ends, the beep sound will play 🎵, and you'll be asked to name your screenshot.

4. The screenshot will be saved as a `.png` file with your chosen name.

## Example Code 💻

```python
import pyscreenshot
import time
from audioplayer import AudioPlayer

# Countdown before taking the screenshot
for i in range(6, 1, -1):
    print(f"ScreenShot will be taken in {i} seconds")
    time.sleep(1)

# Capture screenshot
image = pyscreenshot.grab()

# Play beep sound
player = AudioPlayer('beep-07a.mp3')
player.play()

# Ask for image name and save
image_name = input("What's the img name?\n")
image.save(f"{image_name}.png")
```

## License 📝

MIT License - see [LICENSE](LICENSE).

## Acknowledgements 🙏

- [pyscreenshot](https://github.com/ponty/pyscreenshot)
- [audioplayer](https://github.com/andrewrk/audioplayer)

---
