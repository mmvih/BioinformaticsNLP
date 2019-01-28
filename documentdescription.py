      Show Dotfiles  Show Owner/Mode
File Explorer
/projects/academic/mjbuck/Buck_Lab_Members/madhuriv/
#Before compiling this code, must type in terminal command line:
	#module load python/anaconda-4.3.1
	#module load snlp
	#conda list nltk


import sys
import ast
import nltk
from nltk.probability import FreqDist
from nltk.collocations import *
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import sexpr_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import xml.etree.ElementTree as et


def xmlparsing(pdf, empty):
	tree = et.parse(pdf)
	root = tree.getroot()
	for item in list(root.iter('p')):
		item = list(item.itertext())
		empty.append(' '.join(item))

def main():
	
        para = []
	xmlparsing(sys.argv[1], para)

	#PARSING OUT PARAGRAPHS FROM THE ARTICLE
        token = PunktSentenceTokenizer()
	article_paragraphs = ' '.join(para)
	#print article_paragraphs

        #PARSING OUT SENTENCES FROM THE PARAGRAPHS
        word = word_tokenize(article_paragraphs)
	word = [w.lower() for w in word if len(w) > 3]		
	word = [w for w in word if w not in stopwords.words('english')] 	

	fdist = nltk.probability.FreqDist(word)
	#print fdist.most_common()
	#print fdist.keys()
	numwords = len(word)
	setwords = len(set(word))
	relativefreq = [fdist.freq(item) for item in set(word)]
	average = reduce(lambda x, y: x + y, relativefreq) / float(len(relativefreq))		
		
	lexicaldiversity = (float((numwords/setwords)))/100
	#print lexicaldiversity, type(lexicaldiversity)
	#outp = []
	outp = [item.encode("utf-8") for item in sorted(fdist.keys()) if fdist.freq(item)/lexicaldiversity > 1]
	#for item in sorted(fdist.keys()):
	#	if fdist.freq(item)/lexicaldiversity > 1:
	#		outp.append(item)
	print outp
	
	
	if not outp:
		with open(sys.argv[2], 'a') as outfile:
			outfile.write("%s \t NO SIGNIFICANT WORDS \n" % sys.argv[1])
	else:
		with open(sys.argv[2], 'a') as outfile:
			outfile.write("%s \t %s \n" % (sys.argv[1], outp))
	outfile.close()	
	
main()	
