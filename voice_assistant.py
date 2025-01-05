import speech_recognition as sr
import wikipedia
import pyttsx4
import pywhatkit
import datetime

listener=sr.Recognizer() 
machine=pyttsx4.init()
def talk(speech):
    machine.say(speech)
    machine.runAndWait()

def input_instruction():
    talk("hello!,iam madhu,how can i assist u today?")
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio=listener.listen(source)
            instruction=listener.recognize_google(audio)
            instruction=instruction.lower()
            if instruction:
                return instruction
    except sr.UnknownValueError:
        talk("I can't understand.please repeat it again")
    except sr.RequestError:
        talk("My service is down.")
    except Exception as e:
        print("Unexpected error: {}".format(e))
    return ''

def play_madhu():
    try:
        instruction=input_instruction()
        if instruction:
            print(instruction)
            if 'play' in instruction:
                song=instruction.replace('play','')
                talk("playing" +song)
                pywhatkit.playonyt(song)
            elif 'time' in instruction:
                time = datetime.datetime.now().strftime('%I:%M %p')
                talk('current time'+time)
            elif 'date' in instruction:
                date = datetime.datetime.now().strftime('%d/%m/%Y')
                talk('date'+date)
            elif 'how are you' in instruction:
                talk('I am fine how about you')
            elif any(word in instruction for word in ['good morning','good afternoon','good evening']):
                if 'good morning' in instruction:
                    wish='good morning!,i hope u are doing well'
                elif 'good afternoon' in instruction:
                    wish='good afternoon!,how can i help u'
                elif 'good evening' in instruction:
                    wish='good evening!,what are your plans today'
                talk(wish)
                    
            elif '' in instruction:
                person=instruction.replace('','')
                info=wikipedia.summary(person,sentences=2)
                print(info)
                talk(info)
            else:
                talk('i cant hear that repeat once again')
    except Exception as e:
        print(f"unkown error occured:{e}")
play_madhu()

        