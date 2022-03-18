import stanza
import truecase
from Chatbot import *

#stanza.download('en')

def processinput(msg):
    
    resp = ""
    nlp = stanza.Pipeline(lang = "en", processors = "tokenize,ner") # Build the pipeline, specify part-of-speech processor's batch size
    msg = truecase.get_true_case(msg)
    msg1 = nlp(msg)
    ner_workOfArt = [token.text for sentences in msg1.sentences for token in sentences.tokens]

    if len(ner_workOfArt)>0:
        for finalwords in ner_workOfArt:
            resp = resp + "I have heard about " + finalwords + " and I absolutely love it!! \n" 
            return resp
            
        
        #return resp
        #we can use the POS tagging to find out if user is speaking in past future tense and allow our bot to give a generic response based 


        #bot_input = bot_input.lower()
            #if len(ner_workOfArt)>0:
             #   print(*[f"{a.name}: I loved",*[f'{token}' for token in ner_workOfArt]])
    #doc = nlp("Barack Obama was born in Hawaii.") # Run the pipeline on the input text
    #print(doc) # Look at the result
    #print(resp)
    resp = "I have not heard of this before, but I can surely check in out!"
    return resp
    


#processinput("Barack Obama was born in Hawaii. I enjoyed watching Titanic yesterday")