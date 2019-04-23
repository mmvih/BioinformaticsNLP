mkdir spesets
while read species 
do
	var=','  read -ra ADDR <<< "$species"
	varzero="${ADDR[0]%,}"
	varone="${ADDR[1]%,}"
	vartwo="${ADDR[2]%,}"
	ls SpeciesP3/$varone > text1set.txt
	ls SpeciesP3/$vartwo > text2set.txt
	comm -12 text1set.txt text2set.txt > common.txt
	if [ "$(wc -l < common.txt)" -gt 0 ]; then
		mkdir spesets/$varzero
		while read paps
			do
				cp SpeciesP3/$varone/"$paps" spesets/$varzero
		done < common.txt
		echo $varone >> names.txt
		echo $vartwo >> names.txt
		mv names.txt spesets/$varzero
		mv common.txt spesets/$varzero
	else
		rm common.txt
	fi 
	rm text1set.txt
	rm text2set.txt
	echo $varzero

done < bactsets.txt

ls spesets/ > setbactused.txt





