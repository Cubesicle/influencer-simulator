# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("JohnVlogsTTV")


# The game starts here.

label start:
    c ""

    menu:
        "What kind of video should I make today?"

        "A scary video":
            jump scary

        "A prank video":
            jump prank

        "A challenge video":
            jump challenge

        "Passion video":
            
            
    
    return

label scary:
    c "Yo what's up, guys. Today we're boutta enter... The Aokigahara Forest!"
    c "This is gonna be a big deal, guys. You know why?"
    c "Cause this forest is known as the Sea of Trees, also known as..."
    c "The Japanese Suicide Forest!"
    "*scary_thump_sound_effect.wav*"
    c "This is not a freaking joke."
    "*cuts to being in forest*"
    c "Okay guys this is absolutely crazy"

    return

label prank:
    c "prank"
    return

label silly:
    c "silly"
    return