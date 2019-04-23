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

def main():
	
	papersent = []
	with open(sys.argv[1], 'r') as input:
		for item in input:
			papersent.append(item)
	input.close() 
        
	print "okay"
	
	path_to_jar = '/util/academic/snlp/parser_v3.8.0/stanford-parser.jar'
	path_to_models_jar = '/util/academic/snlp/parser_v3.8.0/stanford-parser-3.8.0-models.jar'
	dependency_parser = StanfordDependencyParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)

	with open(sys.argv[2], 'a') as output:
		for item in papersent:
			output.write("%s\n" % item)
			try:
				result = dependency_parser.raw_parse(item)
				for e in result:
					result = e
					break
				output.write(result.to_dot())
			except UnicodeDecodeError:
				output.write("UnicodeDecodeError\n\n")
				continue
			except OSError:
				output.write("OSError\n\n")
				continue
			output.write("\n")

	print sys.argv[1]
	
main()	
