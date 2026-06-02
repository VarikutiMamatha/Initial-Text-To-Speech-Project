from elevenlabs.client import ElevenLabs
from elevenlabs import save

client = ElevenLabs(
    api_key="sk_14b9e92e2b9483ace2c4fcc0e6544f2926d31037cfd6a5ec"
)

audio = client.text_to_speech.convert(
    text="My name is Mamatha Reddy Varikuti. I am currently pursuing my B.Tech in Computer Science and Engineering. I have knowledge of Python basic web development concepts. I have worked on projects such as a Student Management System and an Expired Product Detector, which helped me improve my programming and problem-solving skills.",
    voice_id="Yt5IIrEExjWQrAhWiBa6",
    model_id="eleven_multilingual_v2"
)

save(audio, "output.mp3")

print("Audio saved successfully!")