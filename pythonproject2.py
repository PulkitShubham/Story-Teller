import pyttsx3
import random

when=["a long time ago ","yesterday ","in another dimension ","in the future ","a year ago "]
who=["john ","joey ","albert ","ross  ","chandler  "]
where=["walking through tunnel,","in the dark night,","in the middle of forest,","on the bank of river,","near quiet lake,"]
found=["sparkling stone  ","cursed ring  ","old heritage  ","kings sword  ","magical wand  "]
happen=["he was feeling low  ","he was amazed  ","he didn't expected that  ","he was in shock  ","he was confused  "]
after=["it was the turning point in his life  ","magic changed everthing  ","it turned out to be a curse to him  "]
end=[" everthing ends well  ","but he believed in work hard  "]

engine = pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
rate=engine.getProperty("rate")
engine.setProperty("rate", 150)
engine.say("welcome to the story zone listener, enjoy your story")
engine.say(random.choice(when)  + random.choice(who) + ' returning from work' + random.choice(where) + 'found the ' + random.choice(found) + random.choice(happen)+'after that,'+random.choice(after)+random.choice(end))
engine.runAndWait()

