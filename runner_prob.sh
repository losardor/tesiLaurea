for prob in $(LC_NUMERIC=C seq 0.1 0.1 1); do echo $prob ; python NG.py -p $prob; done
