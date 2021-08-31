import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import random
import pickle

#tokenizer for urls as they are different from normal texts
def token_extracter(input):
    tokenBySlash=str(input.encode('utf-8')).split('/')
    all_tokens=[]
    for i in tokenBySlash:
        tokens=str(i).split("-")
        tokensByDot=[]
        for j in range(0,len(tokens)):
            tempTokens=str(tokens[j]).split(".")
            tokensByDot+=tempTokens
        all_tokens+=tokens+tokensByDot
    all_tokens=list(set(all_tokens))
    if 'com' in all_tokens:
        all_tokens.remove("com")
    return all_tokens

#loading the dataset
data=pd.read_csv("data.csv",',',error_bad_lines=False)
data=pd.DataFrame(data)
data=np.array(data)

#shuffling the dataset to randomness in dataset
random.shuffle(data)

# setting output as labels and corpus as urls
y=[d[1] for d in data]
corpus=[d[0] for d in data]

#tokenizing our urls into a vector matrix
vectorizer=TfidfVectorizer(tokenizer=token_extracter)
X=vectorizer.fit_transform(corpus)


#splitting training and testing dataset
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)


#using Logistic Regression 
lgs=LogisticRegression()
lgs.fit(X_train,y_train)
print(lgs.score(X_test,y_test))

#storing vectorizer and trained model for the use of server api response
pickle.dump(vectorizer,open("vectorizer.pkl","wb"))
pickle.dump(lgs,open("Url_Detection_Model.pkl","wb"))


'''X_predict=['wikipedia.com','facebood.com','famebook.com','google.com/search=bombay']
X_predict=vectorizer.transform(X_predict)
y_predict=lgs.predict(X_predict)
print(y_predict)
'''

