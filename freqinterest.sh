module load python/anaconda-4.3.1
conda list nltk

for f in spesets/*
do 
	bact=$(basename $f)
	echo $bact
	for w in $f/bothword*
	do
		echo $w
		python freqwordsinterested.py $w speciesjoined.txt > otherbact.txt 
	done	
	mv otherbact.txt $f
done	


