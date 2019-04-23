import sys
import nltk
import re 
import ast 
import xml.etree.ElementTree as et
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import sexpr_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def xmlparsing(pdf, empty):
	tree = et.parse(pdf)
	root = tree.getroot()
	for item in list(root.iter('p')):
		item = list(item.itertext())
		empty.append(' '.join(item))


def main():
	
	para = [];
	xmlparsing(sys.argv[1], para)
	
	#PARSING OUT PARAGRAPHS FROM THE ARTICLE
	article_paragraphs = ' '.join(para)
	article_paragraphsoutput = article_paragraphs.encode('utf-8')
	articlejoined = article_paragraphs

	with open(sys.argv[2], 'r') as input:
		species = [line.rstrip() for line in input]
		speciesjoined = [item.replace(" ", "_") for item in species]
	input.close()

	articlejoined = article_paragraphs
	#print articlejoined
	#print type(articlejoined)
	
	speciesinpaper = []
	abbrev = []
	for item in species:
		if item in article_paragraphs:
			articlejoined = articlejoined.replace(item, speciesjoined[species.index(item)])
			articlejoined = articlejoined.replace(item.split(" ")[0][0] + ". " + item.split(" ")[1], speciesjoined[species.index(item)])
	
	token = PunktSentenceTokenizer()
	word = word_tokenize(articlejoined)
	word = [w.encode('utf-8') for w in word if len(w) > 2 and w not in stopwords.words('english')]
	sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
        sent = " ".join(sent_detector.tokenize(articlejoined.strip(),realign_boundaries = False))
        sent = re.sub(r' \([^)]*\)','', sent)
        sent = token.tokenize(sent)

	
	with open(sys.argv[3], 'a') as outfile1:
			outfile1.write("%s" % word)
	outfile1.close()
	
	with open(sys.argv[4], 'a') as outfile2:
                        outfile2.write("%s" % sent)
        outfile2.close()


main()	

	





