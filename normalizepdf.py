      Show Dotfiles  Show Owner/Mode
File Explorer
/projects/academic/mjbuck/Buck_Lab_Members/madhuriv/CodesOralMicrobiome/
#module load python/anaconda-4.3.1
#conda list nltk
#module load snlp
#module load java/1.8.0_45
#module load NER
#python normalizepdf.py microbiome.txt habitatrootwords.txt newABxmlPapers/*/PMC*.nxml outputfilename.txt

import re
import sys
import ast
import nltk
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
from nltk.parse.stanford import StanfordDependencyParser
from nltk.probability import FreqDist
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import sexpr_tokenize
from nltk.tokenize import word_tokenize
import xml.etree.ElementTree as et

def bacteriasinpaper(microbiome):
	for line in microbiome:
		line = line.rstrip()
		line = line.split('\t')
		if sys.argv[3] == line[0]:
			return ast.literal_eval(line[1].lower())

def xmlparsing(pdf, empty):
	tree = et.parse(pdf)
	root = tree.getroot()
	for item in list(root.iter('p')):
		item = list(item.itertext())
		empty.append(' '.join(item))

def main():
	
	stemmer = SnowballStemmer("english")
	
	with open(sys.argv[1], 'r') as input:
		wholebacterias = bacteriasinpaper(input)
	
	#TOKENIZING EACH BACTERIA INTO ITS GENUS AND SPECIES SEPARATELY
	whole_bacterias = []
	for item in wholebacterias:
		whole_bacterias.append(item.replace(" ", "_"))
	bacterias = " ".join(wholebacterias)
	bacterias = bacterias.split()
	#print wholebacterias
	#print whole_bacterias	
	#print bacterias

	para = [];
        xmlparsing(sys.argv[3], para)

        #PARSING OUT PARAGRAPHS FROM THE ARTICLE
        token = PunktSentenceTokenizer()
        article_paragraphs = ' '.join(para)

        #PARSING OUT SENTENCES FROM THE PARAGRAPHS
        sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
        sent = " ".join(sent_detector.tokenize(article_paragraphs.strip(),realign_boundaries = False))
        sent = re.sub(r' \([^)]*\)','', sent)
	#propercapsent = token.tokenize(sent)
	sent = token.tokenize(sent.lower())
	word = word_tokenize(article_paragraphs)
	word = [(w.lower()) for w in word if (len(w) > 3 and w not in stopwords.words('english'))]
	#print word
	normalizeword = ([stemmer.stem(item) for item in word])

	with open(sys.argv[2], 'r') as input:
		stemmedlist = [stemmer.stem(line.rstrip()) for line in input]

	commonstems = [normalizeword.index(wordz) for wordz in normalizeword for item in stemmedlist if item == wordz]
	#print commonstems

	wordsinpaper = [word[item] for item in commonstems]
	#print wordsinpaper		

	#bacteriawords = [item.encode("utf-8") for bact in bacterias for item in word if bact == item]
	#print bacteriawords
	bacteriasent = list(set([(sentwbact.encode("utf-8")) for bact in bacterias for sentwbact in sent if bact in sentwbact]))
	#print bacteriasent
	rootsentences = list(set([(sentwroot.encode("utf-8")) for w in wordsinpaper for sentwroot in sent if w in sentwroot]))
	#print rootsentences

	bacteria_sent = []
	bacteria_sent = [(item.replace(bact, whole_bacterias[wholebacterias.index(bact)])) for item in bacteriasent for bact in wholebacterias if bact in item]
	#print bacteria_sent
	
	#fdist = nltk.probability.FreqDist(bacteriawords)
	#print fdist	
	
	path_to_jar = '/util/academic/snlp/parser_v3.8.0/stanford-parser.jar'
	path_to_models_jar = '/util/academic/snlp/parser_v3.8.0/stanford-parser-3.8.0-models.jar'
	dependency_parser = StanfordDependencyParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)


	with open(sys.argv[4], 'a') as output:
		for item in rootsentences:
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

	print sys.argv[3]
	
main()	


