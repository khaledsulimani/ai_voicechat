# 🤖🎙️ Voice Assistant AI (Arabic) with Cohere & Python

Welcome to your Arabic Voice Assistant powered by Python and Cohere!  
This assistant listens to your voice, understands your question, gets an answer from Cohere AI, and replies back in Arabic audio.  
Perfect for hands-free Q&A, learning, or just having fun with AI in your language! 🌟

---

## 📂 Project Structure

```
robot-arm-control-panel/
│
├── voice chat ai.py      # Main Python script for the voice assistant
├── README.md             # This file
└── ...                   # (Other files/folders if any)
```

---

## 🛠️ Requirements

- Python 3.9.x (Tested on 3.9.34)
- [Anaconda Navigator](https://www.anaconda.com/products/distribution) (recommended)
- Cohere API Key ([Get yours here](https://dashboard.cohere.com/api-keys))
- Microphone (for voice input)

### 📦 Python Libraries

Install these libraries before running the assistant:

```bash
pip install speechrecognition cohere gtts pygame
```

If you have issues with `pyaudio` (required by `speechrecognition`), install it with:

```bash
conda install pyaudio
```
or
```bash
pip install pipwin
pipwin install pyaudio
```

---

## 🚀 How to Run

1. **Place your Cohere API Key**  
   Open `voice chat ai.py` and replace the string in:
   ```python
   co = cohere.Client("YOUR-API-KEY-HERE")
   ```
   with your actual Cohere API key.

2. **Start the Assistant**  
   Open Anaconda Prompt or your terminal, navigate to the project folder, and run:
   ```bash
   python "voice chat ai.py"
   ```

3. **Talk to Your Assistant!**  
   - Speak in Arabic when prompted.
   - The assistant will reply in Arabic audio.
   - To stop the conversation, just say:  
     **"اغلاق"** or **"توقف"**

---

## 🧠 How It Works

1. **🎤 Listen:**  
   The assistant listens to your voice using your microphone.

2. **📝 Recognize:**  
   Converts your speech to Arabic text using Google Speech Recognition.

3. **🤖 AI Reply:**  
   Sends your question to Cohere’s AI model and gets a smart answer in Arabic.

4. **🔊 Speak:**  
   Uses Google Text-to-Speech (gTTS) to convert the answer to audio and plays it back.

5. **🔁 Repeat:**  
   Keeps chatting until you say "اغلاق" or "توقف".

---

## 📝 Code Overview

- `listen_to_audio()`: Listens and recognizes Arabic speech.
- `get_reply_from_ai(user_input)`: Sends your question to Cohere and gets a reply.
- `play_audio_reply(text)`: Converts text to Arabic audio and plays it.
- `should_stop(command)`: Checks if you said a stop command.
- The main loop keeps the conversation going!

---

## 💡 Tips

- Make sure your microphone is working and not muted.
- You need an internet connection for both speech recognition and Cohere API.
- If you get errors with audio playback, make sure `pygame` is installed and your sound drivers are working.

---

## 🔒 Security Note

**Never share your Cohere API key publicly!**  
Keep it private and safe.

---
## 📸 Project Results

### *API key*:![صورة واتساب بتاريخ 1447-01-28 في 05 10 11_103ae8f2](https://github.com/user-attachments/assets/062f4839-f331-4fbd-84df-5cafc9f2fcfd)


### *run file*:![صورة واتساب بتاريخ 1447-01-28 في 05 37 23_b5603a47](https://github.com/user-attachments/assets/1ef5d360-6d8b-4768-90be-b6714292ab8d)


---
## *Code Explanation* 📝💻

### *voice chat ai*:
*This script listens to your Arabic speech, sends your question to Cohere AI for an answer, and replies back to you in spoken Arabic. The conversation continues until you say "اغلاق" or "توقف" to stop.*.

```py
import speech_recognition as sr
import cohere
from gtts import gTTS
import pygame
import time
import os

def listen_to_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("أنا جاهز للاستماع إليك الآن...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="ar-SA")
        print(f"سمعتك تقول: {text}")
        return text
    except sr.UnknownValueError:
        print("لم أتمكن من فهم ما قلته.")
        return None
    except sr.RequestError as e:
        print(f"حدث خطأ أثناء الاتصال: {e}")
        return None

def get_reply_from_ai(user_input):
    co = cohere.Client("L8WUxKSfUKUjddVr2ZrRYHF0Jl4znTkKxogG2eW3")
    prompt = f"قم بالإجابة على هذا السؤال باللغة العربية الفصحى:\nس: {user_input}\nج:"
    response = co.generate(
        model="command-r-plus",
        prompt=prompt,
        max_tokens=100
    )
    return response.generations[0].text.strip()

def play_audio_reply(text):
    tts = gTTS(text=text, lang="ar")
    filename = "response.mp3"
    tts.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():  # التأكد من انتهاء الصوت
        time.sleep(0.5)

    # إغلاق محرك pygame بعد الانتهاء
    pygame.mixer.quit()

    # حذف الملف بعد التشغيل
    try:
        os.remove(filename)
    except PermissionError:
        print(f"لم أتمكن من حذف الملف {filename}. قد يكون الملف قيد الاستخدام.")

def should_stop(command):
    if command and ("اغلاق" in command or "توقف" in command):
        print("وداعًا! تم إنهاء المحادثة.")
        return True
    return False

if __name__   == "__main__":
    print("مرحبًا بك! تحدث إلي، وإذا أردت إنهاء المحادثة، قل 'اغلاق' أو 'توقف'.")
    
    while True:
        user_input = listen_to_audio()
        if user_input:
            reply = get_reply_from_ai(user_input)
            print(f"الجواب: {reply}")
            play_audio_reply(reply)
            
            # تحقق إذا كان المستخدم يريد إغلاق المحادثة
            if should_stop(user_input):
                break  # إيقاف الحلقة عندما يقول المستخدم "اغلاق" أو "توقف"

```
---

## 📞 Support

If you need help, open an issue or ask in the Cohere or Python communities.

---
## 🧑‍💻 Author
- **khaled mahmoud sulaimani** – [@khaledsulimani](https://github.com/khaledsulimani)

---
Enjoy your Arabic
