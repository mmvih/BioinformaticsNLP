module load python/anaconda-4.3.1
conda list nltk

mkdir SpeciesP3
while read species; do mkdir SpeciesP3/"$species"; done < speciesjoined.txt
mkdir abxmlwords
mkdir abxmlsents

for f in abxmlpapers/*
do 
	DIREK=${f##*/}
	echo ${DIREK}
	mkdir abxmlwords/${DIREK}
	mkdir abxmlsents/${DIREK}
	
	for w in abxmlpapers/${DIREK}/*
		do
			echo $w
			PAP=$(basename $w)
			newwords=word${PAP%.*}.txt
			newsents=sent${PAP%.*}.txt
			echo $newwords
			echo $newsents
			python articlejoin.py $w specieslist.txt $newwords $newsents
			python yesbactder.py $newwords speciesjoined.txt > inter.txt
			if [ "$(wc -l < inter.txt)" -gt 0 ]; then
				cat inter.txt
				while read species
					do 
						cp $newwords SpeciesP3/"$species"
						cp $newsents SpeciesP3/"$species"
						cp $w SpeciesP3/"$species" 
				done < inter.txt
			fi
			rm inter.txt
			mv $newwords abxmlwords/${DIREK}
			mv $newsents abxmlsents/${DIREK}
		done
	
done

find SpeciesP3/ -type d -empty -delete
ls SpeciesP3/ > usedbact.txt
python setsof2.py usedbact.txt bactsets.txt








