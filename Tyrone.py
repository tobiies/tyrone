# Tyrone - a script built to mimic a virtual assistant

import time
import random
from random import randint
import webbrowser
import datetime
import os

action = ["Type in what you want to do: ","Type in the desired action: ","Type something you wanna do: ","Let's do something: ","Do you wanna do something? ","What do you wanna do?: ","Choose something to do: ","Type something you wanna do: ", "Wanna do anything?: ","Wanna do something?: ","Ready to do something?: ","Let's go!: "]
roasts = ["You're so stupid, I could count your brain cells on one hand.","You're so stupid, you went to the dentist to get Bluetooth.","As a failure, you are a great success.","Come back and talk to me when your I.Q. exceeds your age.","You're the reason this country has to put directions on shampoo.","If you really spoke your mind, you'd be speechless.","Have you been shopping lately? They're selling lives, you should go get one.","You're like Monday mornings, nobody likes you.","How old are you? - Wait I shouldn't ask, you can't count that high.","The last time I saw something like you, I flushed it.","Some babies were dropped on their heads but you were clearly thrown at a wall.","Calling you an idiot would be an insult to all the stupid people.","You, sir, are an oxygen thief!","I can explain something to you, but I can’t understand it for you.","If I wanted to kill myself I'd climb your ego and jump to your IQ.","You're so ugly, when your mom dropped you off at school she got a fine for littering.","You're so ugly, you scared the crap out of the toilet","You're so dumb you got hit by a parked car","You're an idiot","Paigon.","You're a wasteman.","I'd slap you, but that would be animal abuse.","Please shut your mouth when you’re talking to me.","If I had a face like yours, I'd sue my parents.","It's better to let someone think you are an idiot than to open your mouth and prove it."]
intro = ["So who are you? ","So what's your name? ","What's your name? ","You got a name or something? ","You got a name? "]
address = ["What's up ","Hi ","Hey ","Yo ","Alright ","Alright then ","Ok ","Come on ","Come on then ","Ok then "]
facts = ["Sweden has a ski-through McDonald's","Research has shown that dogs actually like the silly, high-pitched voice their owners use to talk to them.","A report found that the free weights at the gym have 362 times more bacteria than a toilet seat.","People who think their opinions are superior to others may be most prone to overestimating their relevant knowledge and ignoring chances to learn more, a study found.","Netflix is responsible for 15% of global Internet traffic.","The 57 on Heinz ketchup bottles represents the number of varieties of pickles the company once had.","The plastic things on the end of shoelaces are called aglets.","You burn more calories sleeping than you do watching TV.","Stressed is Desserts spelled backwards.","Karoke means 'empty orchestra' in Japanese.","Cats sleep 16 to 18 hours per day.","'Rhythm' is the longest English word without a vowel.","Apparently banging your head against a wall burns 150 calories a hour.","Camels have three eyelids to protect themselves from blowing sand.","The word 'queue' is the only word in the English language that is still pronounced the same way when the last four letters are removed.","'Almost' is the longest word in the English language with all the letters in alphabetical order.","Donald Duck comics were banned from Finland because he doesn't wear any pants.","Cap’n Crunch’s full name is Horatio Magellan Crunch.","More than 50% of the people in the world have never made or received a telephone call.","Coconuts kill more people in the world than sharks do. Approximately 150 people are killed each year by coconuts.","Barbie's full name is Barbara Millicent Roberts.","A sneeze can travel as fast as 100 miles per hour."]
invalid = ["Command is unavailable.","This action isn't available.","This command doesn't appear to work.","I think you've made a mistake somewhere.","Sorry, you might have made a spelling mistake.","Check for any spelling mistakes.","Check for any mistakes.","You might have made a mistake.","Sorry, that's an invalid command.","Invalid comment.","That's an invalid comment.","This command doesn't work."]
bye = ["In a bit.","Until next time...","I'll see you later.","See ya!","Bye.","See ya later!","I bid you adieu!"]

print("What's up? I'm Tyrone.")
name = input(random.choice(intro))

names = name

time.sleep(1)

print(random.choice(address),names.capitalize(),", let's do some stuff.\n", sep ='')
time.sleep(1)
print("But before we do anything, I should let you know that you can get help by typing 'help'.\n")

def cls():
    os.system('cls')

def command():
    commands = input(random.choice(action)).lower()

    if commands == "help":
        print()
        print("Here are some actions / commands that might help you\n>>> Help (alt = help me)\n>>> Roast (alt = roast me)\n>>> Thanks\n>>> Fact\n>>> Programmer (Tobi's Github)\n>>> About\n>>> Date (date and time)\n>>> Clear (clear screen)\n>>> Github (alt = git)\n>>> Credits (alt = credit)\n>>> Bye\n")
        command()

    if commands == "clear":
        cls()
        print("Successfully cleared!\n")
        command()

    if commands == "programmer":
        print("Opening Tobi's Github...")
        webbrowser.open('https://github.com/tobiies', new=0, autoraise=True)
        print()
        command()

    if commands == "about":
        print()
        print("I'm Tyrone. I'm a Python script built to imitate a virtual assistant.")
        time.sleep(randint(2,4))
        print("You can find out more about me on my Github by typing 'Github' or 'Git'.")
        time.sleep(randint(2,4))
        print("I'm still a work in progress, so there may be some issues or kinks that need to be worked out.")
        time.sleep(randint(2,4))
        print("If you find a problem with me, you can contact my programmer / adoptive father Tobi by typing visiting my Github or typing 'programmer'.")
        time.sleep(randint(2,4))
        print("Now where were we?\n")
        time.sleep(.5)
        command()
        
    if commands == "no":
        print("YES!\n")
        command()

    if commands == "yes":
        print("NO!\n")
        command()

    if commands == "ok":
        print("Alright.\n")
        command()
    
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
        print(">>> Tobi - programmer (github.com/tobiies)\n>>> Pun.me - roasts (pun.me/pages/funny-insults.php)\n>>> Factslides - facts (factslides.com)\n")
        command()

    if commands == "credit":
        print(">>> Tobi - programmer (github.com/tobiies)\n>>> Pun.me - roasts (pun.me/pages/funny-insults.php)\n>>> Factslides - facts (factslides.com)\n")
        command()

    if commands == "bye":
        print(random.choice(bye))
        time.sleep(randint(2,4))
        exit()

    else:
        print(random.choice(invalid)," Please try another command.\n",sep ='')
        command()

command()
