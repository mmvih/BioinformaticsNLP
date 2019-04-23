import sys
import ast
import nltk
from nltk.probability import FreqDist

def main():
	
	paperlist = []
	with open(sys.argv[1], 'r') as input:
		for item in input:
			paperlist.extend(ast.literal_eval(item))
        input.close()

	#print paperlist
	fdist = nltk.probability.FreqDist(paperlist)
	for item in fdist.most_common():
		print item
main()	
