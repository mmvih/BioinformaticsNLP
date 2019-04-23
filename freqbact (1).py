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
	
	listwords = []
	with open(sys.argv[2], 'r') as input2:
		for item in input2:
			item = item.rstrip()
			listwords.append(item.lower())
	input2.close()

	fdist = nltk.probability.FreqDist(paperlist)
	for item in listwords:
		if fdist[item] > 0:
			print item, fdist[item]

main()	
