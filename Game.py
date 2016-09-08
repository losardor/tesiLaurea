#def 
import matplotlib.pyplot as plt

DEBUG = 0

def Play(f, T=1000000, name="game.dat"):
    # folk f, play rounds T
    time=[]
    different_words=[]
    for i in range(T):
        [speaker, hearer] = f.Select()
        if(hearer==None):
            time.append(i+1)
            different_words.append(different_words[-1])
            continue
        #if (speaker.ndw==1 and i>f.N): 
        #    break
        if(speaker==None):
            time.append(i+1)
            if speaker.ndw:
                different_words.append(speaker.ndw)
            else:
                different_words.append(different_words[-1])
            continue
        #if (speaker.ndw==1 and i>f.N): 
        #    break
        
        if DEBUG: 
            print "speaker:",
            str(speaker.dict),
            " hearer:",
            str(hearer.dict)
        if(len(speaker.dict) == 1 and speaker.dict==hearer.dict): 
            # trivial case
            #print "%d %d" %(i, speaker.ndw)
            time.append(i+1)
            different_words.append(different_words[-1])
            continue
        
        #print speaker.id, hearer.id
        if not speaker.dict: #if empty
            w = speaker.NewWord()
            speaker.AddWord(w)
            w = speaker.ChooseWord()
        if w in hearer.dict: # success
            if DEBUG: 
                print "w:",str(w),"success"
            speaker.EraseDict()
            hearer.EraseDict()
            speaker.AddWord(w)
            hearer.AddWord(w)
        else:
            if DEBUG: 
                print "w:",str(w), "failure"
            hearer.AddWord(w)
        #print "%d %d" %(i+1, speaker.ndw)
        #if (speaker.ndw==1 and i>f.N):
        #    break
        time.append(i+1)
        different_words.append(speaker.ndw)
    fig=plt.figure()
    ax1=plt.subplot2grid((1,1),(0,0))
    plt.scatter(time, different_words, label='NDW')
    plt.xlabel('Time Step')
    plt.ylabel('Number of Different Words')
    plt.title('Number of Different Words in Time')
    ax1.grid(True)
    plt.show()
    target = open(name, "w")
    for x in range(len(time)):
        target.write(str(time[x])+"\t"+str(different_words[x])+"\n")

        
