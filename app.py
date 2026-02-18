import gradio as gr
import speech_recognition as sr
import datetime

recognizer = sr.Recognizer()

def voice_assistant(audio):
    if audio is None:
        return "No audio received."

    try:
        with sr.AudioFile(audio) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)

        text = text.lower()

        # Simple rule-based responses
        if "hello" in text:
            response = "Hello! How can I help you?"
        elif "time" in text:
            response = "Current time is " + datetime.datetime.now().strftime("%H:%M")
        elif "your name" in text:
            response = "I am a simple voice assistant created using Python and Gradio."
        else:
            response = "Sorry, I don't understand that command yet."

        return f"You said: {text}\nAssistant: {response}"

    except Exception as e:
        return "Error processing audio."

iface = gr.Interface(
    fn=voice_assistant,
    inputs=gr.Audio(type="filepath"),
    outputs="text",
    title="Simple Voice Assistant",
    description="Speak into the microphone and get a response."
)

iface.launch()
