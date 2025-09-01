import re
import io
import os

from elevenlabs import Voice, VoiceSettings, save
from elevenlabs.client import ElevenLabs
from pydub import AudioSegment

os.environ["PATH"] = r"C:\ffmpeg\ffmpeg-2025-08-25-git-1b62f9d3ae-full_build\bin;" + os.environ.get("PATH","")

AudioSegment.converter = r"C:\ffmpeg\ffmpeg-2025-08-25-git-1b62f9d3ae-full_build\bin\ffmpeg.exe"
AudioSegment.ffprobe   = r"C:\ffmpeg\ffmpeg-2025-08-25-git-1b62f9d3ae-full_build\bin\ffprobe.exe"


client = ElevenLabs(
    api_key="sk_4d06a2e63fae7541f6acbee8dc58a37097bef9726a59bd50"
)

try:
    with open('interview_script.txt', 'r', encoding='utf-8') as f:
        script_lines = f.readlines()
except FileNotFoundError:
    print("Error: 'interview_script.txt' not found. Please make sure the script file exists.")
    exit()

conversation = AudioSegment.empty()
print("Starting conversational audio generation...")

for line in script_lines:
    line = line.strip()
    if not line:
        continue

    voice_id_to_use = None
    voice_settings_to_use = None
    speaker_name = ""

    if line.startswith("Sarah Jenkins:"):
        speaker_name = "Sarah Jenkins"
        text_to_generate = line.replace("Sarah Jenkins:", "").strip()
        voice_id_to_use = '21m00Tcm4TlvDq8ikWAM' # "Rachel"
        voice_settings_to_use = VoiceSettings(
            stability=0.6, similarity_boost=0.85, style=0.0, use_speaker_boost=True
        )

    elif line.startswith("Dr. Alex Carter:"):
        speaker_name = "Dr. Alex Carter"
        text_to_generate = line.replace("Dr. Alex Carter:", "").strip()
        voice_id_to_use = 'CwhRBWXzGAHq8TQ4Fs17' 
        voice_settings_to_use = VoiceSettings(
            stability=0.5, similarity_boost=0.75, style=0.0, use_speaker_boost=True
        )

    if voice_id_to_use and text_to_generate:
        print(f"Generating audio for {speaker_name}...")
        
        audio_data = client.text_to_speech.convert(
            text=text_to_generate,
            voice_id=voice_id_to_use,
            model_id='eleven_multilingual_v2',
            voice_settings=voice_settings_to_use
        )
        
        audio_bytes = b"".join(audio_data)
        
        line_audio = AudioSegment.from_file(io.BytesIO(audio_bytes), format="mp3")
        
        conversation += line_audio

print("\nSaving final conversation to 'conversation.mp3'...")
conversation.export("conversation.mp3", format="mp3")

print("✅ Audio generation complete.")
