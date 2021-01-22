
def text_cleaning(text):
    text=str(text).lower()#convert to lower case letters
    spl_char_text=re.sub(r'[^ a-z]','',text)# removing special characters
    tokens=nltk.word_tokenize(spl_char_text)#tokenization
    lema=wordnet.WordNetLemmatizer()#lemmatisation
    tags_list=pos_tag(tokens,tagset=None)#parts of speech
    lema_words=[]
    for token,pos_token in tags_list:
        if pos_token.startswith('V'):#VERB
            pos_val='v'
        elif pos_token.startswith('J'):#Adjective
            pos_val='a'
        elif pos_token.startswith('R'):#ADVERB
            pos_val='r'
        else:
            pos_val='n'#Noun
        lema_token=lema.lemmatize(token,pos_val)
        lema_words.append(lema_token)

    return " ".join(lema_words)
