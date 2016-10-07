#def 
import cPickle as pk
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.cm as cm
import numpy as np
import random

DEBUG = 0
COMPLETE = 0
ERDOS    = 1; ERDOS_p = 0.5
GRID2D   = 2
GRID2DBAND = 3
GRID2DBAND_p = 0.01
BARABASI = 4; BARABASI_M = 4
GRIDONMAP = 5
SHOW = 1

def Play(f, T=1000000, name="game.dat", prob=1):
    # folk f, play rounds T
    time=[]
    different_words=[]
    numberofWords=[]
    couples=[]
    for i in range(T):
        [speaker, hearer] = f.Select()
        if f.topology.tipo==COMPLETE:
        	couples.append([speaker.id,hearer.id])
        if(hearer==None):
            #print "Che rumore fa un albero che cade in una foresta disabitata?"
            time.append(i+1)
            different_words.append(different_words[-1])
            numberofWords.append(numberofWords[-1])
            continue
        #if (speaker.ndw==1 and i>f.N): 
        #    break
        if(speaker==None):
            print "che rumore fa il battito di una mano sola?"
            time.append(i+1)
            if speaker.ndw:
                different_words.append(speaker.ndw)
            else:
                different_words.append(different_words[-1])
            numberofWords.append(numberofWords[-1])
            continue
        #if (speaker.ndw==1 and i>f.N): 
        #    break
        
        if DEBUG: 
            print "speaker:",
            str(speaker.dict),
            " hearer:",
            str(hearer.dict)
        speaker_number=len(speaker.dict)
        hearer_number=len(hearer.dict)
        sum_number=hearer_number+speaker_number
        if(len(speaker.dict) == 1 and speaker.dict == hearer.dict): 
            # trivial case
            #print "%d %d" %(i, speaker.ndw)
            time.append(i+1)
            different_words.append(different_words[-1])
            numberofWords.append(numberofWords[-1])
            continue
        
        #print speaker.id, hearer.id
        if not speaker.dict: #if empty
            w = speaker.NewWord()
            speaker.AddWord(w)
            w = speaker.ChooseWord()
        if w in hearer.dict: # success
            if DEBUG: 
                print "w:",str(w),"success"
            if random.random() < prob:
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
        speaker_number_final=len(speaker.dict)
        hearer_number_final=len(hearer.dict)
        sum_number_final=hearer_number_final+speaker_number_final
        if numberofWords==[]:
        	numberofWords.append(sum_number_final - sum_number)
        else:
        	numberofWords.append(numberofWords[-1]+(sum_number_final-sum_number))
        x,y=zip(*couples)
        plt.scatter(x,y)

    if SHOW==1:
    	fig=plt.figure(figsize=(16,12))
    	ax=plt.subplot(111)
    	ax.spines["top"].set_visible(False)
    	ax.spines["bottom"].set_visible(False)
    	ax.spines["right"].set_visible(False)
    	ax.spines["left"].set_visible(False)
    	ax.get_xaxis().tick_bottom()
    	ax.get_yaxis().tick_left()
    	plt.xticks(fontsize=14)
    	plt.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")
    	plt.plot(time, different_words, label='NDW')
    	plt.xlabel('Time Step')
    	plt.ylabel('Number of Different Words')
    	plt.title('Number of Different Words in Time')
    	plt.show()
    	fig2=plt.figure(figsize=(16,12))
    	ax2=plt.subplot(111)
    	ax2.spines["top"].set_visible(False)
    	ax2.spines["bottom"].set_visible(False)
    	ax2.spines["right"].set_visible(False)
    	ax2.spines["left"].set_visible(False)
    	ax2.get_xaxis().tick_bottom()
    	ax2.get_yaxis().tick_left()
    	plt.xticks(fontsize=14)
    	plt.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")
    	plt.plot(time, numberofWords, label='NW')
    	try:
    		plt.plot(range(len(time)), [len(f.topology.G.nodes()) for i in range(len(time))], "--", lw=0.5, color="black", alpha=0.3) 
    	except:
    		plt.plot(range(len(time)), [8100 for i in range(len(time))], "--", lw=0.5, color="black", alpha=0.3)
    	plt.xlabel('Time Step')
    	plt.ylabel('Number of Words')
    	plt.title('Number of Words in Time')
    	plt.show()
        nodeColor=[]
        try:
        	for x in f.topology.G.nodes():
        		if f.topology.G.node[x]['agent'].dict != []:
        			nodeColor.append(int(f.topology.G.node[x]['agent'].dict[0]))
                else:
                	nodeColor.append(0)
        except:
        	print "the topolgy is complete and has no grid to print"

        if f.topology.tipo == GRIDONMAP:
            fig2=plt.figure()
            colors = cm.rainbow(np.linspace(0, 1, len(nodeColor)))
            elarge=[(u,v) for (u,v,d) in f.topology.G.edges(data=True) if d['weight'] >=0.05]
            esmall=[(u,v) for (u,v,d) in f.topology.G.edges(data=True) if d['weight'] <0.05]
            nx.draw_networkx_edges(f.topology.G, pos={i:i for i in f.topology.G.nodes()}, edgelist=elarge, width=1, alpha = 0.5)
            nx.draw_networkx_edges(f.topology.G, pos={i:i for i in f.topology.G.nodes()}, edgelist=esmall, width=1, alpha=0.5,edge_color='b',style='dashed')
            nx.draw_networkx_nodes(f.topology.G, pos={i:i for i in f.topology.G.nodes()}, node_color=nodeColor, node_cmap=plt.cm.summer, node_size=20)
            plt.xlabel('X_grid identifier')
            plt.ylabel('Y_grid identifier')
            plt.title('The grid\nGenerated on the basis of given DEM')
            plt.show() # display
            filename="final_grid_"+name
            with open(filename, "wb") as output:
                pk.dump(f.topology.G, output, pk.HIGHEST_PROTOCOL)
        elif f.topology.tipo == COMPLETE:
            print "finished game\n"
        else:
            fig2=plt.figure()
            colors = cm.rainbow(np.linspace(0, 1, len(nodeColor)))
            nx.draw(f.topology.G, pos=nx.spring_layout(f.topology.G))
            plt.show() # display

    target = open(name, "w")
    for x in range(len(time)):
        target.write(str(time[x])+"\t"+str(different_words[x])+"\t"+str(numberofWords[x])+"\n")

        
