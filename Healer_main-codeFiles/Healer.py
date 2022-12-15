
import openai
import pyttsx3
import speech_recognition as sr
# import os
import whisper
# please enter your own Api key its find from gpt3 playground id three dot then api key option 
#openai.api_key = os.getenv("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")
model = whisper.load_model("base")

openai.api_key = "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"

engine = pyttsx3.init()
r = sr.Recognizer()
mic= sr.Microphone()

conversation = ""
user_name = "Talha"
bot_name = "Healer"
while True:
    with mic as source:
        print("listenting....")
        r.adjust_for_ambient_noise(source,duration = 0.2)
        audio = r.listen(source)
    print("no longer listening...")
        
    try:
        user_input = r.recognize_google(audio)
        #load audio and pad/trim it to fit 30 seconds
        #user_input = result.text
        print("user input:  "+ user_input)

    except Exception as e:
        print(e)
    
    prompt = user_name + ": " + user_input + "\n" + bot_name + ": "
    conversation += prompt
    response = openai.Completion.create(
    model="text-davinci-001",
    prompt=conversation,
    temperature=0,
    max_tokens = 100
)
    response_str = response["choices"][0]["text"].replace("\n","")
    response_str = response_str.split(user_name + ": ",1)[0].split(bot_name + ": ",1 )[0]
    conversation += response_str + "\n"
    engine.say(response_str)
    engine.runAndWait()


    option = input("choose the option Y for yes N for no")
    if(option == "Y"):
        continue
    else:
        break
