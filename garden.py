# import spacy, NLP module for Python

import spacy


# create list of garden path sentences, 3 provided add 3 of your own
# GPS is a grammatically correct sentence which starts in such a way 
# that the reader is likely to misinterpret it
# ref: https://en.wikipedia.org/wiki/Garden-path_sentence

gardenpathSentences = [

"Mary gave the child a Band-Aid.",
"That Jill is never here hurts.",
"Have the students who failed the exam take the supplementary.",
"The cotton clothing is made of grows in Mississippi.",
"British Left Waffles on Falklands"

]


#  Tokenise each sentence in the list and perform named entity recognition.
# tokenise: Splitting text into words
# enitity recognitiion, process of classifying named entities found in a text
# into pre-defined categories

# load english NLP model

nlp = spacy.load('en_core_web_sm')

# Tokenize each sentence and perform named entity recognition
for sentence in gardenpathSentences:
    doc = nlp(sentence)

    # Print the entities in the sentence
    print(f'The Entities in the sentence "{sentence}" are:')

    for ent in doc.ents:
        print(f'{ent.text} ({ent.label_})')

# spacy.explain to look up entities which you dont understand, I added all

print("\nExplaining entities:\n")
print("GPE:", spacy.explain("GPE"))
print("PERSON:", spacy.explain("PERSON"))
print("NORP:", spacy.explain("NORP"))
print("ORG:", spacy.explain("ORG"))

# At the bottom of your file, write a comment about two entities that you looked up.
#  For each entity answer the following questions:
# ○ What was the entity and its explanation that you looked up?
# ○ Did the entity make sense in terms of the word associated with it?

# 1. NORP - Nationalities or religious or political groups
# Yes, its a country and people there have a nationality called british, 
# British is a NORP enitity

# 1. ORG - Companies, agencies, institutions, etc.
# Falklands is an island however it picked it up as 
# ref: https://www.falklands.gov.fk/our-history
# Falkland Islands Government
# Therefore Flaklands itself I think should be and island, aka GPE enitity
# but there was a war, so ORG applies, I think, based on actual 
# newspaper article, org is sufficcient 


