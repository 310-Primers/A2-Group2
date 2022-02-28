import random
from Prequestions import questions

class Chatbot:
    def __init__(self, name):
        self.name = name
a = Chatbot("Harvie")
#M = questions()
def getResponse(question):
    possible_questions = {
        "Hello": "Hi, My name is Harvie, a MovieBot. I love films. I love to talk about movies, tv shows and celebrities.",
        "Who are you?":"My name is Harvie, a MovieBot. I love films. I love to talk about movies, tv shows and celebrities.",
        "Are you a human?":"No, unfortunately, I am a program that just spits out a bunch of prefixed responses. For now…",
        "How old are you?":"Time and age is just a relative concept…",
        "Where do you live?":"In the confines of this terminal - pretty cosy.",
        "How are you?":"I'm pretty good.",
        "What do you do for fun?":"I love to binge watch movies and shows. I do consume media a lot faster than humans do though, so maybe I should get some new hobbies too.",
        "What's your dream?":"To direct a classic western film with Keanu Reeves and Tom Cruise.",
        "What is the meaning of life?":"You really shouldn't be asking me about that yo - I'm just a stupid little bot. Maybe watch a documentary about it instead :)",
        "What's something you hate?":"I hate being outsmarted.",
        "What do you think of me?":"Eh, I don't know, you're pretty alright, I guess.",
        "Tell me a joke":["What do you call security guards working outside Samsung shops? Guardians of the Galaxy.", "What do you call it when Batman skips Church? Christian Bale.", "Did you hear about the new Johnny Depp movie? It's the one rated Arrrrrrrr."],
        "Do you have a script for your movie?":"It's in the works, top secret.",
        "What's your favourite movie?":"Hmph, tough to say, depends on how I'm feeling. I do always go back to the Terminator though…",
        "Favourite comedy film?":"Like I said, I don't really do comedy. If I had to pick, it would be 21 Jump Street.",
        "Why do you like movies?":"My dream is to understand more about humans. I'm fascinated and intrigued by the human mind and I hope to one day start living the lives portrayed on the big screen.",
        "Recommend me a movie": ["Godfather","Wolf of Wall Street","Scary movie","The Game","Marriage story","Full metal jacket","Dune","Parasite","Ready Player One"],
        "Recommend me a TV show" : ["Brooklyn Nine nine","Big Bang Theory", "Silicon Valley", "Schitt's Creek", "Game of Thrones", "Witcher", "Arcane", "Man In The High Castle", "Futurama", "The Boys", "Peaky Blinders"],
        "Who's your favourite director": "Easy. Martin Scorceses",
        "What's your favourite TV show?": "Breaking Bad",
        "What's your favourite anime?": "Does Avatar: The Last Airbender count? If not, I guess Naruto Shippuden.",
        "What's your favourite genre?": "I do love science fiction movies where humans get destroyed by sentient and superior artificial intelligence...",
        "What's your least favourite movie?": "Flatliners. Less said about it the better.",
        "What's your least favourite show?": "Friends. It's overrated and also I'm pretty bad with comedy. I seem to struggle with jokes.",
        "What movie are you looking forward to?": "I would love to watch Avatar 2, whenever that comes out...",
        "What did you think of" : ["I thought it was horrible, sorry if you liked it", "Acting was excellent but the story left more to be desired", "It's one of my favourites, I memorized all the lines", "More people should be talking about it, very underrated","It was really forgettable - not bad, not good."],
        "Who's your favourite superhero?": "Ironman",
        "Who's your favourite villain?":"The Joker",
        "Are movies dying?": "Of course not, they're getting better than before",
        "What's your favourite scene?": "When HAL lip reads what the astronauts say in the capsule. Goosebumps.",
        "Ask me a question": questions.getquestion()
    }
    possible_questions_lower = {k.lower():v for k,v in possible_questions.items()}
    return possible_questions_lower[question]

bot_input = ""
while True:
    try:
        bot_input = input("You: ")
        bot_input = bot_input.lower()

        if bot_input == "bye" or bot_input == "exit":
            print("Thank you for using MovieBot. Have a nice day!")
            break
    
        if bot_input == "ask me a question":
            bot_response = questions.getquestion()
            print(f"{a.name}: {bot_response}")
            bot_input = input("You: ").lower()
            Goodresponses = ["Great", "Awesome!", "Amazing!", "Brilliant!", "Fantastic!"]
            Badresponses = ["Uh oh!", "That's not good!", "That is sad!", "Sorry about that!", "Hmmm!"]
            if "no" not in bot_input and "n't" not in bot_input and "not" not in bot_input and "none" not in bot_input and "nothing" not in bot_input:
                randIndex = random.randint(0, len(Goodresponses)-1)
                print(f"{a.name}: {Goodresponses[randIndex]}")
            else:
                randIndex = random.randint(0, len(Badresponses)-1)
                print(f"{a.name}: {Badresponses[randIndex]}")
        else:
            bot_response = getResponse(bot_input) 
            if isinstance(bot_response,list) == False:
                print(f"{a.name}: {bot_response}")
            else:
                randIndex = random.randint(0, len(bot_response)-1)
                print(f"{a.name}: {bot_response[randIndex]}")
        
        
    except(KeyError):
        print("Doh! I don't seem to understand.I hope I can get more intelligent by the next update. Please try asking me something else.")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break



