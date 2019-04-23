module load python/anaconda-4.3.1
conda list nltk

for f in spesets/*
do
	num=$(basename $f)
	touch bothsentbact.txt
	touch bothwordbact.txt
	for w in $f/sent*
	do 
		echo $w		
		python readsent.py $w $f/names.txt >> bothsentbact.txt 
		python readword.py $w $f/names.txt >> bothwordbact.txt
	done
	if [ "$(wc -l < bothsentbact.txt)" -gt 0 ]; then
		cat bothsentbact.txt
		cat bothwordbact.txt
		mv bothsentbact.txt $f
		mv bothwordbact.txt $f
	else
		echo "removing $f"
		rm bothsentbact.txt
		rm bothwordbact.txt
		rm -rf $f
	fi

done	


