import sys
import ast

def main():
	
	with open(sys.argv[1], 'r') as input:
		for paperlist in input:
			paperlist = ast.literal_eval(paperlist)
	with open(sys.argv[2], 'r') as input2:
		species = []	
		for item in input2:
			item = item.rstrip()
			species.append(item)
	
	speciesinpaper = [item for item in species if item in paperlist]
	for item in speciesinpaper:
		print item
main()	


