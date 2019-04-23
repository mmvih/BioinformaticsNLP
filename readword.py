import sys
import nltk
import re 
import ast 
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import sexpr_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def main():
	
	with open(sys.argv[1], 'r') as input:
		for item in input:
			paperlist = ast.literal_eval(item)
	input.close()
	
	with open(sys.argv[2], 'r') as input2:
		species = [line.rstrip() for line in input2]
	input2.close()

	word = [] 
	for sent in paperlist:
		if species[0] in sent and species[1] in sent:
			word = word_tokenize(sent)
		        word = [(w.lower()).encode("utf-8") for w in word if (len(w) > 2 and w not in stopwords.words('english')) and w.encode("utf-8") not in species]
			word.extend(species)
			print word
main()	

	





