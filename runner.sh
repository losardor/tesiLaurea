for beta in $(LC_NUMERIC=C seq 1000000 1000000 5000000); 
	do 
	echo $beta ; python NG.py -t $beta; 
done
