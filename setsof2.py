#This code takes a list returns a object list of tuples which contain all possible combinations of length 2 in a list form

import re
import sys
from itertools import combinations

def main():
	
	with open(sys.argv[1], 'r') as input:
		listitems = []
		for line in input:
			line = line.rstrip()
			listitems.append(line)
	input.close()

	comb = list(combinations(listitems, 2))
	print type(comb[0][0])
	
	with open(sys.argv[2], 'a') as output:
		count = 1;
		for item in comb:
			output.write("%s, %s, %s \n" % (count,item[0],item[1]))
			count = count + 1;
	output.close() 
		
main()	


