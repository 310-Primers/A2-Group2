import stanza


def processpos(msg):
    pos_VerbAux = [[word.text, word.feats] for sent in msg.sentences for word in sent.words if word.upos in "VERB AUX"]


    if len(pos_VerbAux) > 0 :
        #these list comprehension is used to extract the tense or verb form from the features(.feats) attribute from every item where "Tense=" or "VerbForm=" is in the list
        tense = [word[word.find("Tense")+6:word.find("Tense")+10] if "Tense=" in word  else None for word in [item[1] for item in pos_VerbAux]]
        verbForm = [word[word.find("VerbForm")+9: word.find("VerbForm")+12]  if "VerbForm=" in word else None for word in [item[1] for item in pos_VerbAux]]


        #this list comprehension is just used to remove any None value in our lists
        tense = [i for i in tense if i]
        verbForm = [i for i in verbForm if i]

        if("Past" in tense):
            print(f"{a.name}: It's in the past now!")
        elif("Fin" in verbForm):
            print(f"{a.name}: That's pretty cool, I hope things work out!")

    else:
        print("OkAY")