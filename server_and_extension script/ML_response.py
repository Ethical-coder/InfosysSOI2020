import pickle
import argparse
def arg():
	parser=argparse.ArgumentParser()
	parser.add_argument("-u","--url",dest="url",help="write your target mac address")
	argument=parser.parse_args()
	return argument.url


def token_extracter(input):
	tokenBySlash=str(input.encode('utf-8')).split('/')
	all_tokens=[]
	for i in tokenBySlash:
		tokens=str(i).split("-")#
		tokensByDot=[]#
		for j in range(0,len(tokens)):#
			tempTokens=str(tokens[j]).split(".")##
			tokensByDot+=tempTokens##
		all_tokens+=tokens+tokensByDot#
	all_tokens=list(set(all_tokens))
	if 'com' in all_tokens:
		all_tokens.remove("com")
	return all_tokens
url=arg()
vectorizer=pickle.load(open('./MachineLearning/vectorizer.pkl', 'rb'))
model=pickle.load(open('./MachineLearning/Url_Detection_Model.pkl', 'rb'))

y=vectorizer.transform([url])

print(model.predict(y))
