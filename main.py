import time
import streamlit as st
import speech_recognition as sr
import tempfile
import os
from gtts import gTTS
from groq import Groq
from deep_translator import GoogleTranslator

languages = {
    "English": "en",
    "Kannada": "kn",
    "German": "de",
    "Hindi": "hi",
    "Tamil": "ta",
    "Telugu": "te",
}
GROQ_API_KEY = "your-api-key-here"

client = Groq(api_key=GROQ_API_KEY)

recognizer = sr.Recognizer()


st.title("Conversational ChatBot")
target_lang_name = st.sidebar.selectbox("Select Target Language:", list(languages.keys()))

def recognize_audio():
    with sr.Microphone() as source:
        st.write("<span stylek='color:yellow'>Clearing the background Noise...</span>", unsafe_allow_html=True)
        recognizer.adjust_for_ambient_noise(source, duration=1)
        st.write("<span style='color:skyblue'>Say Something....!</span>", unsafe_allow_html=True)
        audio = recognizer.listen(source, timeout=5)
        st.write("<span style='color:green'>Done Recording 👍</span>", unsafe_allow_html=True)

        with open("./audio.mp3", "wb") as f:
            f.write(audio.get_wav_data())

        filename = "./audio.mp3"
        try:
            with open(filename, "rb") as file:
                transcription = client.audio.transcriptions.create(
                    file=(filename, file.read()),
                    model="whisper-large-v3",
                    prompt="Specify context.Correct spelling mistakes",  # Optional
                    response_format="json",  # Optional
                    language="en",  # Optional
                    temperature=0.0,  # Optional
                )
            spoken_text = transcription.text
            st.write("You said: ")
            st.write(spoken_text)
            return spoken_text
        except Exception:
            st.write("There was an error while trying to recognize the audio")


def translate_text(text, target_lang):
    try:
        translated_text = GoogleTranslator(source='en', target=target_lang).translate(text)
        return translated_text
    except Exception as e:
        st.write(f"Translation Error: {e}")
        return None


def prompt_llm(text, target_lang):
    formatted_text = f"{text}. Let the answer be concise , not too long"
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "user",
                "content": formatted_text
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )
    translated_text = translate_text(completion.choices[0].message.content, target_lang)
    with open("./response.txt", "w") as f:
        f.write(translated_text)


def spit_out():
        with open("./response.txt", "r") as f:
            content = f.read()
        st.write(" ")
        st.markdown(":blue[Response: ]")
        st.write(content)
        if content:
            tts = gTTS(content, lang=languages[target_lang_name])
            # tts.save("./audio.mp3")
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
                tts.save(f.name)
                audio_file = f.name

            st.audio(data=audio_file, format="audio/mpeg", autoplay=True)
            os.remove(audio_file)


if st.button("Recognize"):
    while True:
        transcribed_text = recognize_audio()
        if transcribed_text.lower() == "stop":
            st.write("Bye")
            break
        prompt_llm(transcribed_text, languages[target_lang_name])
        spit_out()
        time.sleep(10)

