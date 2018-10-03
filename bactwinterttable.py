#python bactwinteresttable.py bacteriawinterest.txt

import sys
import ast 
from nltk.probability import FreqDist

def main():
	
	bacteriainterest = []
	with open(sys.argv[1],'r') as input:
		for row in input:
                        strippedline = row.rstrip()
			strippedline = strippedline.split('\t')
			#print strippedline[1]
			#print strippedline[2]
			bacteria = ast.literal_eval(strippedline[1])
			interested = ast.literal_eval(strippedline[2])
			for item in bacteria:
				for item2 in interested:
					string = " ".join([item,"\t",item2])
					#print string
					bacteriainterest.append(string)
	input.close()
	#for item in bacteriainterest:
	#	print item
	for item in FreqDist(bacteriainterest).most_common():
		print item
	

main()	
