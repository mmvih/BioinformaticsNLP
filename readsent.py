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
			print sent.encode("utf-8")

			#with open(sys.argv[3], 'a') as output:
			#	output.write("%s" % sent.encode("utf-8"))
			#output.close()
			#word = word_tokenize(sent)
		        #word = [w.encode('utf-8') for w in word if len(w) > 2 and w not in stopwords.words('english')]
			#with open(sys.argv[4], 'a') as output2:
			#	output2.write("%s" % word)
			#output2.close()
	
main()	

	





