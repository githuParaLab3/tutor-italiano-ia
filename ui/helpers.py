import os
import re
import uuid
from gtts import gTTS

def clean_text_for_speech(text):
    if not text:
        return ""
    text = re.sub(r'\*(\*?)(.*?)\1\*', r'\2', text)
    text = re.sub(r'#+\s', '', text)
    text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)
    return text

def text_to_speech(text, lang='it'):
    cleaned_text = clean_text_for_speech(text)
    if not cleaned_text:
        return None
    
    temp_dir = "temp_audio"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
        
    try:
        tts = gTTS(text=cleaned_text, lang=lang, slow=False)
        filename = os.path.join(temp_dir, f"{uuid.uuid4()}.mp3")
        tts.save(filename)
        return filename
    except Exception as e:
        print(f"Erro no gTTS: {e}")
        return None