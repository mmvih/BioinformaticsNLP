touch sentcount.txt
for i in spesets/*
do 
	base=$(basename $i)
	sent=$(wc -l $i/bothsentbact.txt) 
	bugs=$(paste $i/names.txt)
	echo $base $bugs $sent >> sentcount.txt
done
