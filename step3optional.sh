module load python/anaconda-4.3.1
conda list nltk

for f in SpeciesP3/*
do 
	bact=$(basename $f)
	echo $bact
	for w in $f/word*
	do
		echo $w
		pmc=$(basename $w)
		echo $pmc
		python freqbact.py $w $bact >> freq.txt
	done	
	mv freq.txt $f
done	


