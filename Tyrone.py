# Tyrone - a script built to mimic a virtual assistant

import time
import random
from random import randint
import webbrowser
import datetime
import os
import winsound
import subprocess
import sys

translated = False

action = ["Type in what you want to do: ","Type in the desired action: ","Type something you wanna do: ","Let's do something: ","Do you wanna do something? ","What do you wanna do?: ","Choose something to do: ","Type something you wanna do: ", "Wanna do anything?: ","Wanna do something?: ","Ready to do something?: ","Let's go!: "]
roasts = ["You're so stupid, I could count your brain cells on one hand.","You're so stupid, you went to the dentist to get Bluetooth.","As a failure, you are a great success.","Come back and talk to me when your I.Q. exceeds your age.","You're the reason this country has to put directions on shampoo.","If you really spoke your mind, you'd be speechless.","Have you been shopping lately? They're selling lives, you should go get one.","You're like Monday mornings, nobody likes you.","How old are you? - Wait I shouldn't ask, you can't count that high.","The last time I saw something like you, I flushed it.","Some babies were dropped on their heads but you were clearly thrown at a wall.","Calling you an idiot would be an insult to all the stupid people.","You, sir, are an oxygen thief!","I can explain something to you, but I can’t understand it for you.","If I wanted to kill myself I'd climb your ego and jump to your IQ.","You're so ugly, when your mom dropped you off at school she got a fine for littering.","You're so ugly, you scared the crap out of the toilet","You're so dumb you got hit by a parked car","You're an idiot","Paigon.","You're a wasteman.","I'd slap you, but that would be animal abuse.","Please shut your mouth when you’re talking to me.","If I had a face like yours, I'd sue my parents.","It's better to let someone think you are an idiot than to open your mouth and prove it."]
intro = ["So who are you? ","So what's your name? ","What's your name? ","You got a name or something? ","You got a name? "]
address = ["What's up ","Hi ","Hey ","Yo ","Alright ","Alright then ","Ok ","Come on ","Come on then ","Ok then "]
facts = ["Did you know Sweden has a ski-through McDonald's?","Research has shown that dogs actually like the silly, high-pitched voice their owners use to talk to them.","A report found that the free weights at the gym have 362 times more bacteria than a toilet seat.","People who think their opinions are superior to others may be most prone to overestimating their relevant knowledge and ignoring chances to learn more, a study found.","Netflix is responsible for 15% of global Internet traffic.","The 57 on Heinz ketchup bottles represents the number of varieties of pickles the company once had.","The plastic things on the end of shoelaces are called aglets.","You burn more calories sleeping than you do watching TV.","Stressed is Desserts spelled backwards.","Karoke means 'empty orchestra' in Japanese.","Cats sleep 16 to 18 hours per day.","'Rhythm' is the longest English word without a vowel.","Apparently banging your head against a wall burns 150 calories a hour.","Camels have three eyelids to protect themselves from blowing sand.","The word 'queue' is the only word in the English language that is still pronounced the same way when the last four letters are removed.","'Almost' is the longest word in the English language with all the letters in alphabetical order.","Donald Duck comics were banned from Finland because he doesn't wear any pants.","Cap’n Crunch’s full name is Horatio Magellan Crunch.","More than 50% of the people in the world have never made or received a telephone call.","Coconuts kill more people in the world than sharks do. Approximately 150 people are killed each year by coconuts.","Barbie's full name is Barbara Millicent Roberts.","A sneeze can travel as fast as 100 miles per hour."]
welcome = ["No worries!","No problem.","Don't mention it :)","My pleasure :)","What can I say, except...","You're welcome?","Varsågod!","You're welcome?","It's a pleasure!","It's all good :)","No, thank *you*","Alright.","Ok.","Thank you for the appreciation :)"]
invalid = ["Command is unavailable.","This action isn't available.","This command doesn't appear to work.","I think you've made a mistake somewhere.","Sorry, you might have made a spelling mistake.","Check for any spelling mistakes.","Check for any mistakes.","You might have made a mistake.","Sorry, that's an invalid command.","Invalid command.","That's an invalid command.","This command doesn't work."]
bye = ["In a bit.","Until next time...","I'll see you later.","See ya!","Bye.","See ya later!","I bid you adieu!"]
dates = ["Eleesha","Merilyn","Olabode","Celestina","Maya","Tisha","Aisha","Simon","Phillip","Stu","Karie"]

winsound.PlaySound('xp.wav', winsound.SND_FILENAME)

print("What's up? I'm Tyrone.")
name = input(random.choice(intro))

time.sleep(1)

print(random.choice(address),name.capitalize(),", let's do some stuff.\n", sep ='')
time.sleep(1)
print("But before we do anything, I should let you know that you can get help by typing 'help'.\n")

def translate():
    from translate import Translator
    
    inputted = input("Type something that you want to translate: ")
    lang = input("Which language would you like to translate to? ")
    print()
    
    translator= Translator(to_lang=lang)
    translation = translator.translate(inputted)
    print("Original:\n",inputted,"\n\n","Translated:","\n",translation, sep='')
    print()
    translateagain()

def translateagain():
    again = input("Translate again? Y - Yes, N - No: ").lower()
    if again == "y":
        print()
        translate()
    else:
        print()
        print("Returning to commands...\n")
        command()

def install(package): # Package installer
    subprocess.call([sys.executable, "-m", "pip", "install", package])

def cls(): # Clear screen
    os.system('cls')

def command():
    commands = input(random.choice(action)).lower()

    translated = False
    
    if commands == "help":
        print()
        print("Here are some actions / commands that might help you\n>>> Help (alt = help me)\n>>> Riddle\n>>> Translate\n>>> Search (Google, Wikipedia, DuckDuckGo, YouTube or Custom URL)\n>>> Feedback\n>>> Tinder\n>>> Roast (alt = roast me)\n>>> Thanks\n>>> Fact\n>>> Programmer (Creator's Github)\n>>> About\n>>> Date (date and time)\n>>> Clear (clear screen)\n>>> Github (alt = git)\n>>> Credits (alt = credit)\n>>> Bye\n")
        command()
    
    if commands == "feedback":
        file = open("feedback.txt","w")
        feedback = input("Type your feedback here: ")
        file.write(feedback)
        file.close()
        print("Feedback saved! Feedback can be viewed in the Tyrone directory. Opening Paste.ee...\n")
        time.sleep(2)
        webbrowser.open("https://paste.ee/")
        command()

    if commands == "speech recognition":
        install("SpeechRecognition")
        import speech_recognition as sr
        r = sr.Recognizer()
        print()
        
        sound = sr.AudioFile('audio.wav')
        with sound as source:
            audio = r.record(source)

        print("Recognizing audio...")
        r.recognize_google(audio)

    if commands == "search":
        engine = input("\nGoogle, Wikipedia, DuckDuckGo, YouTube or Custom URL (type 'custom')?\nWhat do you want to search on?: ").lower()
        query = input("What would you like to search?: ")

        if engine == "custom":
            print("Opening ", query, "!", sep='')
            webbrowser.open(query)
        
        if engine == "wikipedia":
            print('Searching "', query.capitalize(), '" on Wikipedia...',sep='')
            webbrowser.open('https://en.wikipedia.org/wiki/'+query)
        
        if engine == "google":
            print('Searching "', query.capitalize(), '" on Google...',sep='')
            webbrowser.open('https://www.google.com/search?q='+query)
        
        if engine == "youtube":
            print('Searching "', query.capitalize(), '" on YouTube...',sep='')
            webbrowser.open('https://www.youtube.com/results?search_query='+query)

        if engine == "yt":
            print('Searching "', query.capitalize(), '" on YouTube...',sep='')
            webbrowser.open('https://www.youtube.com/results?search_query='+query)

        if engine == "duckduckgo":
            print('Searching "', query.capitalize(), '" on DuckDuckGo...',sep='')
            webbrowser.open('https://duckduckgo.com/?q='+ query +'&t=h_')
            print()

        print("\nReturning to commands...\n")
        command()

    if commands == "translate":
        print("Downloading 'Translate' package, please wait...\n")
        install("translate")
        print("Download finished!\n")
        
        print("A.) Translate\nB.) Return to commands\n")
        option = input("What would you like to do? ").lower()
        print()

        if translated == False:
            print("Here are the languages you can translate to...")
            webbrowser.open('https://en.wikipedia.org/wiki/ISO_639-1', new=0, autoraise=True)
        else:
            if option == "a":
                print()
                translate()
            else:
                print("Returning to commands...\n")
                command()
            
        translated = True
            
        if option == "a":
            print()
            translate()
        else:
            print("Returning to commands...\n")
            command()
    
    if commands == "clear":
        cls()
        print("Screen successfully cleared!\n")
        command()

    if commands == "programmer":
        print("Opening Tobi's Github...")
        webbrowser.open('https://github.com/tobiies', new=0, autoraise=True)
        print()
        command()

    if commands == "riddle":
        num = randint(1,7)
        if num == 1:
            print("The more you take, the more you leave behind. What am I?\n")
            y = input("Type 'done' once you're done: ")
            if y == "done":
                print("Footsteps.\n")
            else:
                print("Riddle cancelled.\nReturning to commands...\n")
                command()
        if num == 2:
            print("What comes once in a minute, twice in a moment, but never in a thousand years?\n")
            x = input("Type 'done' once you're done: ")
            if x == "done":
                print("The letter 'm'.\n")
            else:
                print("Riddle cancelled.\nReturning to commands...\n")
                command()
        if num == 3:
            print("A doctor and a bus driver are both in love with the same woman, an attractive girl named Sarah. The bus driver had to go on a long bus trip that would last a week. Before he left, he gave Sarah seven apples. Why?\n")
            z = input("Type 'done' once you're done: ")
            if z == "done":
                print("An apple a day keeps the doctor away!\n")
            else:
                print("Riddle cancelled.\nReturning to commands...\n")
                command()
        if num == 4:
            print("What has hands but can’t pick up anything?\n")
            w = input("Type 'done' once you're done: ")
            if w == "done":
                print("A clock.\n")
            else:
                print("Riddle cancelled.\nReturning to commands...\n")
                command()
        if num == 5:
            print("I start off dry but come out wet. I go in light and come out heavy. What am I?\n")
            v = input("Type 'done' once you're done: ")
            if v == "done":
                print("A teabag.\n")
            else:
                print("Riddle cancelled.\nReturning to commands...\n")
                command()
        if num == 6:
            print("Why didn’t the skeleton cross the road?\n")
            b = input("Type 'done' once you're done: ")
            if b == "done":
                print("He didn't have the guts.\n")
            else:
                print("Riddle cancelled.\nReturning to commands...\n")
                command()
        if num == 7:
            print("What do you call a fish with 4 eyes?\n")
            b = input("Type 'done' once you're done: ")
            if b == "done":
                print("Fiiiish.\n")
            else:
                print("Riddle cancelled.\nReturning to commands...\n")
                command()
        command()

    if commands == "about":
        print()
        print("I'm Tyrone. I'm a Python script built to imitate a virtual assistant.")
        time.sleep(randint(2,4))
        print("You can find out more about me on my Github by typing 'Github' or 'Git'.")
        time.sleep(randint(2,4))
        print("I'm still a work in progress, so there may be some issues or kinks that need to be worked out.")
        time.sleep(randint(3,6))
        print("If you find a problem with me, you can contact my programmer / adoptive father Tobi by visiting my Github or typing 'programmer'.")
        time.sleep(randint(3,6))
        print("Now where were we?\n")
        time.sleep(.5)
        command()
        
    if commands == "no":
        print("YES!\n")
        command()

    response = ["Same!","I like it!","Sounds pretty interesting.","Hmmm... Alright then.","Awesome. I like it too!","That's pretty cool!","Interesting!","Cool!","Interesting... I guess.","Eurrgh! What's that? HAHAHA!"]
    foods = ["Same!","I love that!","I think they're great!","Ok.","Cool!","I don't really like them..."]

    if commands == "tinder": # Tinder dating
        print("Loading 'Tinder Dates'...\n")
        time.sleep(randint(1,3))
        # play music
        print("Welcome to Tinder Dates, ",name.capitalize(),"!", sep= '')
        print()
        time.sleep(1)
        print("Today, your date's name is...")
        winsound.PlaySound('drum-roll.wav',winsound.SND_FILENAME) # Drum roll
        time.sleep(2)
        print(random.choice(dates))
        print()
        print("Ok, ",name.capitalize(),"! Let's go!",sep= '')
        job = input("So your date's first question is... What is your job? ")
        time.sleep(randint(1,2))
        print(random.choice(response))
        print()
        food = input("So their next question is... What's your favourite food? ")
        time.sleep(randint(1,2))
        print(random.choice(foods))
        print("\nThis seems to be going ok.")
        hobby = input("Alright then. So your date wants to know what your hobby is. What's your hobby? ")
        time.sleep(randint(1,2))
        print(random.choice(response))
        print()
        print("Ending 'Tinder Dates'. Hope you had a good date!")
        
        farewell = input("Now say goodbye to your date. Or not: ").lower()
        if farewell == "good bye" or "goodbye" or "bye":
            print("Bye ",name.capitalize(),"! Hope to see you again!\n",sep= '')
        else:
            print("Well screw you, I never liked you anyway!\n")
        command()

    if commands == "yes":
        print("NO!\n")
        command()

    if commands == "ok":
        print("Alright.\n")
        command()
    
    if commands == "thanks": # 1/3 chance of music playing
        choice = randint(1,3)
        if choice == 1:
            print(random.choice(welcome))
        if choice == 2:
            print(random.choice(welcome))
        if choice == 3:
            print("Playing 'You're Welcome' by Dwayne Johnson...")
            winsound.PlaySound('moana.wav', winsound.SND_FILENAME)
        print()
        command()

    if commands == "date":
        today = time.strftime('%d/%m/%Y %H:%M:%S')
        print("The current date and time is",today)
        print()
        command()

    if commands == "help me":
        print()
        print("Here are some actions / commands that might help you\n>>> Help (alt = help me)\n>>> Riddle \n>>> Roast (alt = roast me)\n>>> Fact\n>>> Date (date and time)\n>>> Github (alt = git)\n>>> Credits (alt = credit)\n>>> Bye\n")
        command()
    
    if commands == "roast":
        print("Thinking of a roast...")
        time.sleep(randint(1,3))
        print(random.choice(roasts))
        print()
        command()

    if commands == "roast me":
        print("Thinking of a roast...")
        time.sleep(randint(1,2))
        print(random.choice(roasts))
        print()
        command()

    if commands == "fact":
        print("Picking a random fact...")
        time.sleep(randint(1,2))
        print(random.choice(facts))
        print()
        command()

    if commands == "github":
        print("Opening Tyrone's Github...")
        webbrowser.open('https://github.com/tobiies/tyrone-ai', new=0, autoraise=True)
        print()
        command()

    if commands == "git":
        print("Opening Tyrone's Github...")
        webbrowser.open('https://github.com/tobiies/tyrone-ai', new=0, autoraise=True)
        print()
        command()

    if commands == "credits":
        print(">>> Tobi - programmer (github.com/tobiies)\n>>> Pun.me - roasts (pun.me/pages/funny-insults.php)\n>>> Factslides - facts (factslides.com)\n>>> Riddles.com - riddles (https://www.riddles.com/best-riddles)\n")
        command()

    if commands == "credit":
        print(">>> Tobi - programmer (github.com/tobiies)\n>>> Pun.me - roasts (pun.me/pages/funny-insults.php)\n>>> Factslides - facts (factslides.com)\n>>> Riddles.com - riddles (https://www.riddles.com/best-riddles)\n")
        command()

    if commands == "bye":
        print(random.choice(bye))
        winsound.PlaySound('xp-shutdown.wav', winsound.SND_FILENAME)
        exit()

    else:
        print(random.choice(invalid)," Please try another command.\n",sep ='')
        winsound.PlaySound('xp-error-sound.wav', winsound.SND_FILENAME)
        command()

command()
