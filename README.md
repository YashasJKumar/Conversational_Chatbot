
# Conversational Chatbot

This is a conversational chatbot built using a combination of various tools and technologies to create a seamless and interactive experience. The chatbot utilizes speech recognition, natural language processing, translation, and text-to-speech capabilities to interact with users in their preferred languages.

![image](https://i.pinimg.com/originals/aa/29/c3/aa29c30acb037c359bff34f60f6fb0df.gif)

## Features

- **Speech Recognition**: Captures and transcribes user speech using OpenAI Whisper through Groq Cloud.
- **Natural Language Processing**: Uses Llama 3 to understand and respond to user queries.
- **Translation**: Translates the chatbot's responses to the user's preferred language using Google Translate and Deep-Translator.
- **Text-to-Speech**: Converts the translated text responses back to speech using gTTS.
- **Web Interface**: Built with Streamlit for a user-friendly web interface.

## Tools and Technologies

- **Streamlit**: For creating the web interface.
- **SpeechRecognition**: To capture and recognize speech input.
- **Groq**: For utilizing OpenAI Whisper to transcribe speech.
- **GoogleTrans**: For translating text.
- **Deep-Translator**: An alternative translator to ensure accuracy and language coverage.
- **gTTS (Google Text-to-Speech)**: For converting text responses to speech.
- **PyAudio**: To handle audio input and output.
- **OpenAI Whisper**: For accurate speech-to-text transcription.
- **Llama 3**: For processing and generating responses to user queries.

## Setup and Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/YahasJKumar/Conversational_Chatbot.git
   cd Conversational_Chatbot
   ```

2. **Create and Activate a Virtual Environment**
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure Groq Cloud**
   - Sign up and set up an account on [Groq Cloud](https://console.groq.com/keys).
   - Obtain API keys and necessary credentials.
   - Update the Groq Cloud configuration in your project settings.
   - Go to Line 18.on your main.py & place your API-KEY

5. **Run the Streamlit App**
   ```sh
   streamlit run main.py
   ```

## Detailed Procedure

1. **Speech Input and Recognition**
   - The user speaks into the microphone.
   - `SpeechRecognition` captures the audio input.
   - The audio is sent to Groq Cloud where OpenAI Whisper transcribes the speech to text.

2. **Processing User Queries**
   - The transcribed text is sent to Llama 3.
   - Llama 3 processes the text and generates a relevant response.

3. **Translation of Responses**
   - The generated response is translated to the user's preferred language using `googletrans` and `deep-translator`.

4. **Text-to-Speech Conversion**
   - The translated text is converted to speech using `gTTS`.
   - `PyAudio` plays the audio response back to the user.

## Usage

- Navigate to the local URL provided by Streamlit after running the app.
- Speak into your microphone to interact with the chatbot.
- The chatbot will listen, understand, translate, and respond to your queries in your preferred language.

## Contributing

Contributions are welcome! Please create a pull request with detailed information on the changes.
