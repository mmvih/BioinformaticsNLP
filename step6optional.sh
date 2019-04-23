module load python/anaconda-4.3.1
conda list nltk
module load snlp

for f in spesets/*
do 
	bact=$(basename $f)
	echo $bact
	for w in $f/bothsent*
	do
		echo $w
		python breakit.py $w broken.txt 
	done	
	mv broken.txt $f
done	


