import re
import string
from nltk.util import ngrams
import os
import csv
import pandas

def ngramsoutput(cleaned,n):
	print("*******************")
	store =[]
	a = []
	ngramss = ngrams(cleaned.split(),n)
	for i in ngramss:
		# writefile.write(str(i))
		print(str(i))
		# a.append(str(i))
	# store.append(a)
	# # print(store)
	# lettercount = len(cleaned)
	# arr = cleaned.split(" ")
	# wordcount = len(arr)
	# store.append(lettercount)
	# store.append(wordcount)

	# with open('database.csv', 'w', encoding='utf-8') as csv_file:
	# 	csv_writer = csv.writer(csv_file,delimiter=',')
	# 	# csv_writer.writerow(column)
	# 	csv_writer.writerow(store)

filenames=[]
# column = ["cleaned text", "lettercount", "wordcount"]
for file in os.listdir("D:/nlp"):
    if file.endswith(".txt"):
        file = (os.path.join(file))
        filenames.append(file)
print(filenames)
for i in range(len(filenames)):
	currentfile = open(filenames[i],'r',encoding='utf-8')
	# writefile =open(filenames[i],'a',encoding='utf-8')

	contents =currentfile.read()
	cleaned =re.sub(r'\[\[(?:[^\]|]*\|)?([^\]|]*)\]\]', r'\1', contents)
	for char in string.punctuation:
	    cleaned = cleaned.replace(char, ' ')
	cleaned = re.sub(' +', ' ', cleaned)
	cleaned= cleaned.rstrip("\n")
	cleaned = re.sub("^\d+\s|\s\d+\s|\s\d+$", " ", cleaned)
	cleaned = re.sub(r"\b\d+\b", "", cleaned)
	# writefile.write(cleaned)
	ngramsoutput(cleaned,2)
	# p = pandas.read_csv('database.csv', delimiter = ',')
	# print(p.shape)



	


	# ngramss = ngrams(cleaned.split(),2)
	# for i in ngramss:
	# 	print(i)
	# 	writefile.write(str(i))
    


