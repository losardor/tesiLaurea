for beta in $(LC_NUMERIC=C seq 0.001 0.001 0.01); 
	do 
	echo $beta ; 
	for i in seq 1 10 1; 
		do 
		echo; python NG.py -b $beta; 
	done
done
