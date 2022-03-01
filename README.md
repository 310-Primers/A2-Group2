# A2-Group2

# Our very own chatbot - Harvie The MovieBot

Harvie, the conversational chatbot, specializes in talking about film - movies, tv shows and celebrities. The main goal is for it to be able to handle a conversation of at least 30 turns and be able to deal with any possible input.

For now, most of the conversation is based on a series of questions being asked by the user and the bot responding back with answers from an array. We also allowed the bot to be able to ask questions to the reader.

## How to run the bot/install it
For now, we have not compiled the code to be run as an exectuble program. It currently works using a terminal/command line. We hope to change that in a following sprint cycle.

You can clone this remote repository into your own local machine and then run it by either opening `Chatbot.py` (or `code Chatbot.py` in a command line once you navigate to the local repository).You must then compiling/running the file using an IDE or using the command `python Chatbot.py` in the terminal.

Note: You will need to have Python installed on your local machine, we recommend having a version *no earlier* than **v 3.9.10**

## Code breakdown:
### Chatbot
for now the chatbot is a simple class that saves that creates an object with a name as its only attribute to identify our chatbot.

### getResponse
takes the user's input (as lowercase) and tries to identify the string as one of the keys in a dictionary of possible questions. If it matches a key, the coressponding value (the pre-written answer to the question) is returned. If not, a key error is returned and handled.

### questions
this class stores a list of questions, and our bot will randomly pick one and output it to terminal when the user inputs "ask me a question".


## Looking ahead
We would love to include the following features to our bot:
- A ui so that the user doesn't have to use a terminal
- More abilities other than just answering questions such as:
    - quizing the user on movies, tv shows,etc and displaying correct answers at end as a score (trivia mode)
    - being able to give the iMDb synopsis and ratings for a movie using an API
- deploying the bot on a website or as an executable program
- potentially changing the architecture of the software so that the bot is not rule based but instead more intelligent and capable of using NLP to interpret the user's input and give the same response to many similarly worded queries.