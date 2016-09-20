for beta in $(LC_NUMERIC=C seq 0.0005 0.00025 0.01); do echo $beta ; python NG.py -b $beta; done
