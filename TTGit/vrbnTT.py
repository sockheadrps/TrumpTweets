import nltk
from nltk import word_tokenize
from collections import *
import numpy as np
import matplotlib.pyplot as plt

##Constants##
file_path = "NaturalTweets.txt" #location of .txt with tweets
pos_type = 'NNP' #Part of speech type to search for


#This function takes file_path of .txt file. It reads the file and stores the contents of file into in a tokenized list
def process_content(file_path):
	with open(file_path, "r", encoding='utf-8') as f:
		trumpTweets = f.read()
	tokens = word_tokenize(trumpTweets)
	return tokens
	

#This function takes in a nltk.pos_tag() object and a POS to identify by
def catch_pos_counter_obj(posTagged, pos_type):
	compiledWords =''
	c = Counter
	output_list = []
	for i in range(0,len(posTagged)): #for i in rnage (index 0 through length of posTagged)
		if posTagged[i][1] == pos_type: #if at current loops position i, look at index 1 in touple (word, NLTKTAG <-)
			compiledWords +=((posTagged[i][0]) + ' ') #if is NNP(pos_type), print the word at touple index 0, (-> word, NLTKTAG)
			output_list.append((posTagged[i][0]))
			c.update(posTagged[i][0])
	co = Counter()
	for word in output_list:
		co[word] += 1
	return co

#This function plots the frequency of words using collections counter object 
def plot_stuff(counterObj):
	x_list = []
	y_list = []
	list_30_common = (list(Counter(counterObj).most_common(30)))
	for i in range(0,len(list_30_common)):
		x = list_30_common[i][0]
		x_list.append(x)
		y = list_30_common[i][1]
		y_list.append(y)
	print(x_list)
	print(y_list)

	plt.barh(np.arange(len(x_list)), y_list)

	plt.yticks(range(len(x_list)), x_list,)
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('Graph for\n' + pos_type)
	plt.legend()
	plt.show()

#process the file into a a tokenized object
tokenized_tweets = process_content(file_path)
#Make a counter object out of a particular type of POS. Hard coded in function to return the 30 most common of the POS type
posCounterObj = catch_pos_counter_obj(nltk.pos_tag(tokenized_tweets), pos_type)
#Plot our counter object by word and frequency of use
plot_stuff(posCounterObj)