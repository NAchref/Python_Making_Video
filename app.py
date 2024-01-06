from dotenv import load_dotenv
import random
import os
import openai
from gtts import gTTS
from moviepy.editor import *
import moviepy.video.fx.crop as crop_vid
load_dotenv()

# Ask for video information (title,content)
title = input("\nEnter the name of the video >  ")
option = input('Do you want AI to generate content? (yes/no) >  ')

if option == 'yes':
    # Generate content using OpenAI API
    theme = input("\nEnter the theme of the video >  ")

    ### MAKE .env FILE AND SAVE YOUR API KEY ###
    openai.api_key = os.environ["OPENAI_API"]
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=f"Generate content on - \"{theme}\"",
        temperature=0.7,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response.choices[0].text)

    yes_no = input('\nIs this fine? (yes/no) >  ')
    if yes_no == 'yes':
        content = response.choices[0].text
    else:
        content = input('\nEnter >  ')
else:
    content = input('\nEnter the content of the video >  ')


# Create the directory where the video will be generated

if os.path.exists('generated') == False:
    os.mkdir('generated')



# Generate speech for the video
speech = gTTS(text=content, lang='en', tld='ca', slow=False)
speech.save("generated/speech.mp3")

gp = random.choice(["1", "2"])
start_point = random.randint(1, 480)
audio_clip = AudioFileClip("generated/speech.mp3")

if (audio_clip.duration + 1.3 > 58):
    print('\nSpeech too long!\n' + str(audio_clip.duration) + ' seconds\n' + str(audio_clip.duration + 1.3) + ' total')
    exit()

print('\n')