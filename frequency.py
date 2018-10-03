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
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import sexpr_tokenize
from nltk.tokenize import word_tokenize
import xml.etree.ElementTree as et


def xmlparsing(pdf, empty):
	tree = et.parse(pdf)
	root = tree.getroot()
	for item in list(root.iter('p')):
		item = list(item.itertext())
		empty.append(' '.join(item))

def main():
	
	#MAKING SPECIES LIST, MICROBIOMEPRESENT.TXT
	with open(sys.argv[1], 'r') as input:
            	#paperlist = []
		#microbacterialist = []
               	for line in input:
			line = line.rstrip()
                        line = line.split('\t')
			if sys.argv[2] == line[0]:
				paper = line[0]
				bacterias = line[1]			
			#paperlist.append(line[0])
			#microbacterialist.append(line[1])
	
	para = [];
	if paper == sys.argv[2]:
        	xmlparsing(sys.argv[2], para)

        	#PARSING OUT PARAGRAPHS FROM THE ARTICLE
        	token = PunktSentenceTokenizer()
        	article_paragraphs = ' '.join(para)

        	#PARSING OUT SENTENCES FROM THE PARAGRAPHS
        	sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
        	sent = " ".join(sent_detector.tokenize(article_paragraphs.strip(),realign_boundaries = False))
        	sent = token.tokenize(sent)
        	word = word_tokenize(article_paragraphs)

        	#print word
        	#print sent


		bacterias = ast.literal_eval(bacterias)
		bacterias = " ".join(bacterias)
		bacterias = bacterias.split()
		#print bacterias
		
		bacteriawords = [(item.encode("utf-8")) for bact in bacterias for item in word if bact == item]
		bacteriasent = [(sentwbact.encode("utf-8")) for bact in bacterias for sentwbact in sent if bact in sentwbact]
		#print bacteriawords  
		#print bacteriasent
		
		for item in bacteriasent:
			print item
	
		fdist = nltk.probability.FreqDist(bacteriawords)

		
		with open(sys.argv[3], 'a') as outfile:
			outfile.write("%s\t" % sys.argv[2])
			for item in bacterias:
				outfile.write("%s \t %s \t" % (item, fdist[item]))
			outfile.write("\n")
		outfile.close()	

main()	



		





