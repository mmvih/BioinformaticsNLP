#To run code in linux: for f in newABxmlpapers/*/*; do python yesitsder.py $f listofbacteriaslookingfor.txt outputfilename.txt; done
#where newABxmlpapers/*/* is the directory where all the papers are filed in

import xml.etree.ElementTree as et
import sys

def xmlparsing(pdf, empty):
	tree = et.parse(pdf)
	root = tree.getroot()
	for item in list(root.iter('p')):
		item = list(item.itertext())
		empty.append(' '.join(item))


def main():
	
	para = [];
	xmlparsing(sys.argv[1], para)
		
	#PARSING OUT PARAGRAPHS FROM THE ARTICLE - Includes paragraphs from the Abstract, Introduction, Methods and Analysis, and Results and Discussion
	article_paragraphs = ' '.join(para)
	#print article_paragraphs

	#MAKING SPECIES LIST
	with open(sys.argv[2], 'r') as input:
                bactlist = []
                for line in input:
                        line = line.rstrip()
                        bactlist.append(line)
	
	
	
	bactpaper = [bacteria for bacteria in bactlist if bacteria in article_paragraphs]
	print sys.argv[1]

	#APPENDS PMC IDENTITY AND BACTERIAS IF MENTIONED
	with open(sys.argv[3], 'a') as outfile:
		if bactpaper:
			outfile.write("%s\t" % sys.argv[1])
			outfile.write("%s" % bactpaper)
			outfile.write("\n")
	outfile.close()	


main()	


