import spacy

nlp = spacy.load("en_core_web_sm")

def process_input(user_input):
    doc = nlp(user_input)
    for token in doc:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)

def get_response(user_input):
    if "hello" in user_input.lower():
        return "Hi there!  How can I assist you?"
    elif "help" in user_input.lower():
        return "Sure, I'm here to help.  What do you need assistance with?"
    else:
        return "I'm not sure how to respond to that.  Can you rephrase?"
    


