#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
import numpy as np
import random
import warnings
warnings.filterwarnings("ignore")
import string # to process standard python strings


# In[2]:


f=open('chatbot.txt','r',errors = 'ignore')
raw=f.read()
raw=raw.lower()# converts to lowercase
nltk.download('punkt') # first-time use only
nltk.download('wordnet') # first-time use only
#Data pre-processing part ( Normalization )
sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences 
word_tokens = nltk.word_tokenize(raw)# converts to list of words


# In[3]:


lemmer = nltk.stem.WordNetLemmatizer()
#creation de lexèmes
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


# In[4]:


GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "wasup"]
def greeting(sentence):
 
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


# In[5]:


from sklearn.feature_extraction.text import TfidfVectorizer


# In[6]:


from sklearn.metrics.pairwise import cosine_similarity


# In[7]:


#Part 2 : word embedding ( represtation mathematique des mots ) ici on utilise TF IDF
def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)#learning phase
    vals = cosine_similarity(tfidf[-1], tfidf)#matrice creuse pour verifier les mots donnés avec le corpus
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response


# In[ ]:


flag=True
print("Bot: Hello i'am a bot , you can ask me questions about other bots or you can type bye to leave !")
while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("ROBO: You are welcome!")
        else:
            if(greeting(user_response)!=None):
                print("ROBO: "+greeting(user_response))
            else:
                print("ROBO: ",end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        print("ROBO: Cya around !")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




