def getline(thefile, thelinenum):
	if thelinenum<1: return ""
	for currentline, line in enumerate(open(thefile, "rU")):
		if currentline == thelinenum: return line
	return ""

