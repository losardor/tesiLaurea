for beta in $(LC_NUMERIC=C seq 0.003 0.001 0.05); 
	do 
	echo $beta ; python NG.py -b $beta; 
done
