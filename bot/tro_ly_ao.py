import speech_recognition 
import pyttsx3
from datetime import date, datetime


robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

while True:
    with speech_recognition.Microphone() as mic:
        print("Robot:I'm Listening")
        audio = robot_ear.listen(mic)
    print("Robot: ...")


    try:
        you = robot_ear.recognize_google(audio)
    except:
        you= ""

    print('You: ' + you)


    if you == "":
        robot_brain = "I cant here you, try again"
    elif "hello" in you:
        robot_brain = "Hi Khoi"
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
    elif "president" in you:
        robot_brain = "Joe Biden"
    elif "fuck you" in you:
        robot_brain = "Your mom fat"
    elif "fuck" in you:
        robot_brain = "Your mom fat with a bad pussy and small dick bitch"
    elif "shit" in you:
        robot_brain = "Kien is a bad dick and a suck bitch with a small bird and no balls"
    elif "dog" in you:
        robot_brain = "Dog with a big bird"
    elif "ice cream" in you:
        robot_brain = "I love bing chilling noice"
    elif "brother" in you:
        robot_brain = "He's dirty and nude and horny hah"
    elif "Villa" in you:
        robot_brain = "Dat's sucks"
    elif "monkey" in you:
        robot_brain = "mongky"
    elif "sigma" in you:
        robot_brain = "not really?"
    elif "chad" in you:
        robot_brain = "hope you're real gigachad"
    elif "chatgpt" in you:
        robot_brain = "he's sucks i ma the best"
    elif "manchester united" in you:
        robot_brain = "Ten Hag sucks lol"
    elif "stupid" in you:
        robot_brain = "Fuck you bitch"
    elif "Ass" in you:
        robot_brain = "Big ass or bad pussy?"
    elif "bye" or "Bye" in you:
        robot_brain = "Bye!"
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "Im fine thank you and you?"

    print("Robot: " + robot_brain)

    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
