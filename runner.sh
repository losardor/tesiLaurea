for beta in $(LC_NUMERIC=C seq 0.001 0.001 0.01); 
	do 
	echo $beta ; 
	for i in $(LC_NUMERIC=C seq 1 1 10);
		do 
		echo $i; python NG.py -b $beta; 
	done
done
