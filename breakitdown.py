      Show Dotfiles  Show Owner/Mode
File Explorer
/projects/academic/mjbuck/Buck_Lab_Members/madhuriv/
#module load python/anaconda-4.3.1
#conda list nltk
#module load snlp
#module load java/1.8.0_45
#module load NER
#python breakitdown.py StaphylocococcusaureusPseudomonasaeruginosa.txt newABxmlpapers/3_Biotech/PMC3339602.nxml breakout.txt 

import os
import re
import sys
import ast
import nltk
from nltk.parse.stanford import StanfordDependencyParser
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
               	for line in input:
			line = line.rstrip()
                        line = line.split('\t')
			print line[0]
			if sys.argv[2] == line[0]:
				paper = line[0]
				bacterias = line[1]
				break
	#TOKENIZING EACH BACTERIA INTO ITS GENUS AND SPECIES SEPARATELY
	
	whole_bacterias = []
	wholebacterias = ast.literal_eval(bacterias)
	for item in wholebacterias:
		whole_bacterias.append(item.replace(" ", "_"))
	bacterias = " ".join(wholebacterias)
	bacterias = bacterias.split()

	para = [];
        xmlparsing(sys.argv[2], para)

        #PARSING OUT PARAGRAPHS FROM THE ARTICLE
        token = PunktSentenceTokenizer()
        article_paragraphs = ' '.join(para)

        #PARSING OUT SENTENCES FROM THE PARAGRAPHS
        sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
        sent = " ".join(sent_detector.tokenize(article_paragraphs.strip(),realign_boundaries = False))
        sent = token.tokenize(sent)
        word = word_tokenize(article_paragraphs)

	bacteriawords = [(item.encode("utf-8")) for bact in bacterias for item in word if bact == item]
	bacteriasent = list(set([(sentwbact.encode("utf-8")) for bact in bacterias for sentwbact in sent if bact in sentwbact]))
	
	
	bacteria_sent = []
	for item in bacteriasent:
		for bact in wholebacterias:
			if bact in item:
				indx = wholebacterias.index(bact)
				item = item.replace(bact, whole_bacterias[indx])
		bacteria_sent.append(item)
	
	fdist = nltk.probability.FreqDist(bacteriawords)
		
	path_to_jar = '/util/academic/snlp/parser_v3.8.0/stanford-parser.jar'
	path_to_models_jar = '/util/academic/snlp/parser_v3.8.0/stanford-parser-3.8.0-models.jar'
	dependency_parser = StanfordDependencyParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)


	with open(sys.argv[3], 'a') as output:
		for item in bacteria_sent:
			output.write("%s\n" % item)
			try:
				result = dependency_parser.raw_parse(item)
				dep = result.next()
				list(dep.triples())
				for itemz in list(dep.triples()):
					output.write(" ".join(str(s) for s in itemz))
					output.write("\n")	
			except UnicodeDecodeError:
				output.write("UnicodeDecodeError\n\n")
				continue
			output.write("\n")

	print sys.argv[2]
	
main()	
