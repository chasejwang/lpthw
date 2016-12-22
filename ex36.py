from sys import exit















def start():
    print "You are a fog prince with a golden key and a sword."
    print "You ride into the dark forest"
    print "Finding out two ways: a cave and a road to Glory riverside."
    print "Which way you would to go, my prince?"

    choice = raw_input(" >")

    if "cave" in choice:
        case()
    elif "riverside" in choice:
        Glory_riverside()
    else:
        shame("You lost interest moving forward. On the road, you find a fat princess, \nyou two fall in love with each other.")
