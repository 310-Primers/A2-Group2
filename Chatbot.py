from tkinter.messagebox import QUESTION


class Chatbot():
    def __init__(self, name):
        self.name = name
        print(f"""Hello! my name is {name}, what is your name?""")
        username = input()
        print("Nice to meet you, "+username+"! As your friend, how may I help you today")
        
        possiblequestions = {1: "", 2: ""}



a = Chatbot("Fred");


    



