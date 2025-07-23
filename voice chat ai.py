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
