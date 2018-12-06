# Tyrone - a script built to mimic a virtual assistant

import time
import random
from random import randint
import webbrowser
import datetime
import os

action = ["Type in in what you want to do: ","Type in the desired action: ","Type something you wanna do: ","Let's do something: ","Do you wanna do something? ","What do you wanna do?: ","Choose something to do: ","Type something you wanna do: ", "Wanna do anything?: ","Wanna do something?: ","Ready to do something?: ","Let's go!: "]
roasts = ["You're so stupid, I could count your brain cells on one hand.","You're so stupid, you went to the dentist to get Bluetooth.","As a failure, you are a great success.","Come back and talk to me when your I.Q. exceeds your age.","You're the reason this country has to put directions on shampoo.","If you really spoke your mind, you'd be speechless.","Have you been shopping lately? They're selling lives, you should go get one.","You're like Monday mornings, nobody likes you.","How old are you? - Wait I shouldn't ask, you can't count that high.","The last time I saw something like you, I flushed it.","Some babies were dropped on their heads but you were clearly thrown at a wall.","Calling you an idiot would be an insult to all the stupid people.","You, sir, are an oxygen thief!","I can explain something to you, but I can’t understand it for you.","If I wanted to kill myself I'd climb your ego and jump to your IQ.","You're so ugly, when your mom dropped you off at school she got a fine for littering.","You're so ugly, you scared the crap out of the toilet","You're so dumb you got hit by a parked car","You're an idiot","Paigon","You're a wasteman!","I'd slap you, but that would be animal abuse.","Please shut your mouth when you’re talking to me.","If I had a face like yours, I'd sue my parents.","It's better to let someone think you are an idiot than to open your mouth and prove it."]
intro = ["Who are you? ","What's your name? ","You got a name or something? ","You got a name? "]
address = ["Yo ","Alright ","Alright then ","Ok ","Come on ","Come on then ","Ok then "]
facts = ["'Rhythm' is the longest English word without a vowel.","Apparently banging your head against a wall burns 150 calories a hour.","Camels have three eyelids to protect themselves from blowing sand.","The word 'queue' is the only word in the English language that is still pronounced the same way when the last four letters are removed.","'Almost' is the longest word in the English language with all the letters in alphabetical order.","Donald Duck comics were banned from Finland because he doesn't wear any pants.","Cap’n Crunch’s full name is Horatio Magellan Crunch.","More than 50% of the people in the world have never made or received a telephone call.","Coconuts kill more people in the world than sharks do. Approximately 150 people are killed each year by coconuts.","Barbie's full name is Barbara Millicent Roberts.","A sneeze can travel as fast as 100 miles per hour."]
invalid = ["Command is unavailable.","This action isn't available.","This command doesn't appear to work.","I think you've made a mistake somewhere.","Sorry, you might have made a spelling mistake.","Check for any spelling mistakes.","Check for any mistakes.","You might have made a mistake.","Sorry, that's an invalid comment.","Invalid comment.","That's an invalid comment.","This command doesn't work."]
bye = ["In a bit.","Until next time...","I'll see you later.","See ya!","Bye.","See ya later!","I bid you adieu!"]

print("What's up? I'm Tyrone.")
name = input(random.choice(intro))

names = name

time.sleep(1)

print(random.choice(address),names.capitalize(),", let's do some stuff.\n", sep ='')
time.sleep(.5)
print("But before we do anything, I should let you know that you can get help by typing 'help'.\n")

#def cls():
#    print ("\n" * 200)

def command():
    commands = input(random.choice(action)).lower()

    if commands == "help":
        print()
        print("Here are some actions / commands that might help you\n>>> Help (alt = help me)\n>>> Roast (alt = roast me)\n>>> Thanks\n>>> Clear (work in progress)\n>>> Fact\n>>> Date (date and time)\n>>> Github (alt = git)\n>>> Credits (alt = credit)\n>>> Bye\n")
        command()

    #if commands == "clear":
    #    cls()
    #    command()

    if commands == "thanks":
        print("You're welcome?\n")
        command()
        
    if commands == "date":
        today = time.strftime('%d/%m/%Y %H:%M:%S')
        print("The current date and time is",today)
        print()
        command()

    if commands == "help me":
        print()
        print("Here are some actions / commands that might help you\n>>> Help (alt = help me)\n>>> Roast (alt = roast me)\n>>> Fact\n>>> Date (date and time)\n>>> Github (alt = git)\n>>> Credits (alt = credit)\n>>> Bye\n")
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
        print(">>> _ _ _ _ - programmer (github.com/_ _ _ _ _ _ _)\n>>> Pun.me - roasts (pun.me/pages/funny-insults.php)\n")
        command()

    if commands == "credit":
        print(">>> _ _ _ _ - programmer (github.com/_ _ _ _ _ _ _)\n>>> Pun.me - roasts (pun.me/pages/funny-insults.php)\n")
        command()

    if commands == "bye":
        print(random.choice(bye))
        time.sleep(randint(2,4))
        exit()

    else:
        print(random.choice(invalid)," Please try another command.\n",sep ='')
        command()

command()
