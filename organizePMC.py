      Show Dotfiles  Show Owner/Mode
File Explorer
/projects/academic/mjbuck/Buck_Lab_Members/madhuriv/
#python organizePMC.py newmicrobiomepresent.txt slurmall.txt bacteriawinterest.txt

import sys
def main():
	
	
	dict = {}
	with open(sys.argv[1],'r') as input:
        	NOPMC = []
                numlist = []
		for row in input:
                        strippedline = row.rstrip()
                        line = strippedline.split('\t')
			PMCnum = (line[0].split("/")[2])
			if 'PMC' == PMCnum[:3]:
				papernum = int(PMCnum[3:-5],10)
				numlist.append(papernum)
				#print papernum
			else:
				NOPMC.append(line[0])
			dict[papernum] = strippedline
		
		sortNOPMC = sorted([(item) for item in NOPMC])
	input.close()
	
	dict2 = {}
	with open(sys.argv[2], 'r') as input2:
		NOPMC2 = []
		numlist2 = []
		for row in input2:
			strippedline2 = row.rstrip()
			line2 = strippedline2.split('\t')
			PMCnum2 = (line2[0].split("/")[2])
			#print PMCnum2
			if 'PMC' == PMCnum2[:3]:
				papernum2 = int(PMCnum2[3:-5], 10)
				numlist2.append(papernum2)
			else:
				NOPMC2.append(line2[0])
			dict2[papernum2] = strippedline2

		sortNOPMC2 = sorted([(item) for item in NOPMC2])
	input2.close()	
	
	combineNOPMC = set(NOPMC).intersection(NOPMC2)
	sortNOPMC = sorted(set(combineNOPMC))
	#SET IS NONE BECAUSE OF FILE NAMES, YOU NEED TO RERUN YESITSDER.PY AND INCLUDE IT INTO THE OUTPUT

	combinenumlist = set(numlist).intersection(numlist2)
	sortnumlists = sorted(set(combinenumlist))
	
	with open(sys.argv[3], 'a') as output:
		for item in sortnumlists:
			#output.write("%s" % item)
			output.write("%s\t%s\n" % (dict[item], (dict2[item]).split('\t')[1]))
	output.close()

main()	
