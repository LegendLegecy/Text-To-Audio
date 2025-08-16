from gtts import gTTS
import pyttsx3
from moviepy.editor import AudioFileClip, concatenate_audioclips
import os
import shutil
import re



if os.path.exists("Audio"):
    shutil.rmtree("Audio/")
    os.mkdir("Audio")

if not os.path.exists("Audio"):
    os.mkdir("Audio")

if os.path.exists("Dialogues.mp3"):
    os.remove("Dialogues.mp3")



# Function for Google TTS (gTTS)
def speaker1(text, output_file, lang='en'):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("Audio/"+output_file)
    print(f"Audio saved as {output_file}")

# Function for pyttsx3 (female voice)
def speaker2(text, output_file):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Female voice
    engine.setProperty('rate', 150)  # Set speech rate
    engine.save_to_file(text, "Audio/"+output_file)
    engine.runAndWait()

# Function for pyttsx3 (male voice)
def speaker3(text, output_file):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Male voice
    engine.setProperty('rate', 150)  # Set speech rate
    engine.save_to_file(text, "Audio/"+output_file)
    engine.runAndWait()

# Function to combine MP3 files into one using moviepy
def combine_mp3_files(files_list, output_file):
    # Load the MP3 files using moviepy
    audio_list = []
    for  file in files_list:
        file = f"Audio/{file}"
        audio_list.append(AudioFileClip(file))
        
    # Concatenate the audio clips
    final_audio = concatenate_audioclips(audio_list)
    
    # Write the combined audio to an output file
    final_audio.write_audiofile(output_file)
    print(f"Combined audio saved as {output_file}")


def remove_special_characters(text):
    # Remove any character that is not a letter, number, comma, or period
    cleaned_text = re.sub(r'[^a-zA-Z0-9,\.]', '', text)
    return cleaned_text

# # Generate the individual voice files
# speaker1(text1, "voice1.mp3")
# speaker2(text2, "voice2.mp3")
# speaker3(text3, "voice3.mp3")



actor1 = "Alex"
actor2 = "Jamie"

with open("Script sample.txt" , "r") as file:
    data = file.read().replace("â€™", '').replace("â€”", '')\
                   .replace("â€˜", "'").replace("â€™", "'")\
                   .replace("â€œ", '"').replace("â€", '"')\
                   .replace("Ã©", "é").replace("Ã¢", "â")\
                   .replace("Ã", "")  # If you see incorrect isolated 'Ã'

    print(data)
    lines = data.split("\n\n")
    for i , line in enumerate( lines ):
        texts = line.split(":")[1:]
        dialogue =''
        for text in texts:
            dialogue += text
            
        character = line.split(": ")[0]
        if character == actor1:
            speaker1(dialogue , f"{i}.mp3" )
        elif character == actor2:
            speaker2(dialogue , f"{i}.mp3" )










# Combine them into one MP3
dir = os.listdir("Audio")
dir.sort(reverse=False)
print(dir)
combine_mp3_files(dir, "Dialogues.mp3")

