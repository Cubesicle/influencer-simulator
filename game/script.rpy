# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define john = Character("John")
define cameron = Character("Camera Man")
image emoji disintegrating = Movie(play="images/emoji disintegrating.webm")
image views = Movie(play="images/views.webm")
image john breakdance:
    "images/breakdance/frame_00_delay-0.02s.png"
    0.02
    "images/breakdance/frame_01_delay-0.02s.png"
    0.02
    "images/breakdance/frame_02_delay-0.02s.png"
    0.02
    "images/breakdance/frame_03_delay-0.02s.png"
    0.02
    "images/breakdance/frame_04_delay-0.02s.png"
    0.02
    "images/breakdance/frame_05_delay-0.02s.png"
    0.02
    "images/breakdance/frame_06_delay-0.02s.png"
    0.02
    "images/breakdance/frame_07_delay-0.02s.png"
    0.02
    "images/breakdance/frame_08_delay-0.02s.png"
    0.02
    "images/breakdance/frame_09_delay-0.02s.png"
    0.02
    "images/breakdance/frame_10_delay-0.02s.png"
    0.02
    "images/breakdance/frame_11_delay-0.02s.png"
    0.02
    "images/breakdance/frame_12_delay-0.02s.png"
    0.02
    "images/breakdance/frame_13_delay-0.02s.png"
    0.02
    "images/breakdance/frame_14_delay-0.02s.png"
    0.02
    "images/breakdance/frame_15_delay-0.02s.png"
    0.02
    "images/breakdance/frame_16_delay-0.02s.png"
    0.02
    "images/breakdance/frame_17_delay-0.02s.png"
    0.02
    "images/breakdance/frame_18_delay-0.02s.png"
    0.02
    "images/breakdance/frame_19_delay-0.02s.png"
    0.02
    "images/breakdance/frame_20_delay-0.02s.png"
    0.02
    "images/breakdance/frame_21_delay-0.02s.png"
    0.02
    "images/breakdance/frame_22_delay-0.02s.png"
    0.02
    repeat

init python:
    config.auto_voice = "voice/{id}.ogg"

# The game starts here.

label start:
    john "The name's John."
    show john neet with dissolve:
        zoom 0.75
        xalign 0.5
        yalign 0.25
    john "For so long, I've never been anything special."
    john "In fact, the only thing special about me is just how useless I am."
    hide john neet with dissolve
    john "For so long, I have nothing under my belt."
    show grades with dissolve:
        zoom 0.7
        xalign 0.5
        yalign 0.15
    john "My school life has always been lacking, with terrible grades and no social skills, I just wander around."
    hide grades with dissolve
    john "My parents have been begging me to do something with my life, yet there's nothing I want to do."
    show laptop kid with dissolve:
        xalign 0.5
        yalign 0.25
    john "That is... until I found out about the possibilities of the online world."
    hide laptop kid with dissolve
    show pewdiepie bridge with dissolve:
        xalign 0.5
        yalign 0.15
    john "I've been inspired by a lot of gaming YouTubers lately, and it gave me the incentive to make my own YouTube channel."
    hide pewdiepie bridge with dissolve
    show pengu with dissolve:
        xalign 0.5
        yalign 0.25
    john "I thought I could make a career out of it, maybe like my favorite YouTuber, Pengu."
    hide pengu with dissolve
    show r6 thumbnail with dissolve:
        xalign 0.5
        yalign 0.15
    john "Rainbow Six Siege was one of my favorite games to play, so I made dozens of clips and montages and uploaded them, hoping to become popular one day."
    hide r6 thumbnail with dissolve
    show zero views with dissolve:
        xalign 0.5
        yalign 0.15
    john "Several months have passed, and not a single person laid eyes on a single video."
    hide zero views with dissolve
    show emoji disintegrating with dissolve:
        zoom 5.0
        xalign 0.5
        yalign 0.15
    john "I'm screwed! How am I supposed to make money!?"
    hide emoji disintegrating with dissolve
    john "Maybe I can ask my rich friend how he got his money."
    john "...Wait, I can use him for my videos!"
    john "I can ask him to help me vlog!"
    show views with dissolve:
        zoom 2.0
        xalign 0.5
        yalign 0.15
    john "Vlogging crazy situations seems to garner tons of views, but where should I vlog?"
    hide views with dissolve
    john "Hmmm..."
    john "I think I know a place."
    "*cuts to the place*"

    scene bg forest lobby with dissolve
    show john waving with moveinright:
        yalign 0.0
        xalign 1.0
    john "Hello chat, today's video is gonna hit different from the usual Rainbow Six epic snipes montages I make."
    show john arms crossed with dissolve:
        zoom 2
        yalign 0.0
        xalign 0.95
    john "A good friend of mine flew me over to Japan, so I could start a new vlogging career."
    show john pointing with dissolve:
        yalign 0.0
        xalign 0.95
    john "Y'all better get ready, cause this vid's gonna be wild."
    scene black
    "*queue in epic intro*"
    $ renpy.movie_cutscene("images/epic intro.webm")

    scene bg forest entrance with dissolve
    show john arms crossed beanie with moveinleft:
        zoom 1.25
        yalign 0.0
        xalign 0.1
    john "Alright, guys. Today we're boutta enter... The Aokigahara Forest!"
    show john finger up beanie with dissolve:
        yalign 0.0
        xalign 0.1
    john "This is gonna be a big deal, guys. You know why?"
    john "Cause this forest is known as the Sea of Trees, also known as..."
    show john arms crossed beanie with dissolve:
        zoom 1.25
        yalign 0.0
        xalign 0.1
    john "The Japanese Suicide Forest!"
    "*scary_thump_sound_effect.wav*"
    show john finger up beanie with dissolve:
        yalign 0.0
        xalign 0.1
    john "This is not a freaking joke."
    scene black
    "*cuts to being in forest*"

    scene bg forest trail with dissolve
    show john hands over head beanie with dissolve:
        yalign 0.0
        xalign 0.1
    john "Okay guys this is absolutely crazy."
    show john finger up beanie with dissolve:
        yalign 0.0
        xalign 0.1
    john "So this is an ancient forest that lies at the base of Mt. Fiji."
    show john arms crossed beanie with dissolve:
        zoom 1.25
        yalign 0.0
        xalign 0.1
    cameron "It's Fuji."
    show john confused beanie with dissolve:
        yalign 0.0
        xalign 0.0
    john "Like the water?"
    cameron "Bruh."
    show john nervous beanie with dissolve:
        yalign 0.0
        xalign 0.1
    john "This place is eerie as hell, like I feel like some ghost is gonna jumpscare me."
    show john nervous beanie:
        yalign 0.0
        ease 5.0 xalign 1.0
    "*keeps walking*"
    cameron "BOO!" with hpunch
    show john nervous beanie:
        linear 0.1 yalign 0.2
        linear 0.1 yalign 0.0
        xalign 1.0
    john "Dude what the hell!?"
    cameron "*rehehehe*"
    scene black
    "*keeps walking*"
    scene bg forest body
    show john waving beanie with moveinleft:
        xalign 0.0
    "*finds some dude hanging*"
    "*scary_horror_sound_effect.wav*"
    show john horrified beanie:
        linear 0.1 yalign 0.2
        linear 0.1 yalign 0.0
    john "Holy sh**!"
    john "Oh my god guys."
    cameron "Wow."
    show john surprised beanie:
        linear 0.1 yalign 0.2
        linear 0.1 yalign 0.0
    john "That's a frickin body! Are you filming this!?"
    cameron "*keeps filming the body*"
    show john horrified beanie:
        linear 0.1 yalign 0.2
        linear 0.1 yalign 0.0
    john "Oh my god. I'm gonna break down. This is my first time seeing a dead body in real life!"
    show john breakdance:
        zoom 2.5
        yalign 0.5
    cameron "Why are you breakdancing to that information??"
    john "*refuses to elaborate*"
    show john pointing beanie with dissolve:
        zoom 1.5
        yalign 0.0
        xalign 0.0
    john "Chat, make sure you like, subscribe, and hit the bell icon to stay up to date on more videos like this."
    cameron "Bro, there's a dead guy, call the cops!"
    show john arms crossed beanie with dissolve:
        yalign 0.0
        xalign 0.0
    john "I'll be doing a giveaway this week, stay tuned!"
    cameron "BRO, THERE'S A DEAD MAN RIGHT HERE!!"
    scene bg test card
    "*cuts video*"

    return