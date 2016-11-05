for beta in $(LC_NUMERIC=C seq 0.003 0.001 0.013); 
	do 
	echo $beta ; python NG.py -b $beta; 
done
