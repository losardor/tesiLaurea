#def 

DEBUG = 0

def Play(f, T=1000000):
   # folk f, play rounds T
   for i in range(T):

      [speaker, hearer] = f.Select()
      if(hearer==None): continue
      if (speaker.ndw==1 and i>f.N): break
      if DEBUG: print "speaker:",str(speaker.dict)," hearer:",str(hearer.dict)
      if(len(speaker.dict) == 1 and speaker.dict==hearer.dict): # trivial case
	 print "%d %d" %(i, speaker.ndw)
	 continue
	 
      #print speaker.id, hearer.id
      if not speaker.dict: #if empty
	 w = speaker.NewWord()
	 speaker.AddWord(w)
      w = speaker.ChooseWord()
      if w in hearer.dict: # success
	 if DEBUG: print "w:",str(w),"success"
	 speaker.EraseDict()
	 hearer.EraseDict()
	 speaker.AddWord(w)
	 hearer.AddWord(w)
      else:
	 if DEBUG: print "w:",str(w), "failure"
	 hearer.AddWord(w)
	 
      print "%d %d" %(i+1, speaker.ndw)
      if (speaker.ndw==1 and i>f.N):
	 break
