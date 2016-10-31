#def 
import cPickle as pk
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.colors as cm
import numpy as np
import random
from pathlib2 import Path

DEBUG = 0
COMPLETE = 0
ERDOS    = 1; ERDOS_p = 0.5
GRID2D   = 2
GRID2DBAND = 3
GRID2DBAND_p = 0.01
BARABASI = 4; BARABASI_M = 4
GRIDONMAP = 5
SHOW = 2

def Play(f, T=1000000, name="game.dat", prob=1):
    '''
    Folk play T timesteps of the naming game. The name variable
    contains the name of the file where the data will be stored.
    If prob is not 1 function stocastically updated with probability = prob 
    on a success.
    '''


    name=namegiving(name)
    target = open(name, "w")
    #for x in range(len(time[::10])):
    #    target.write(str(time[10*x])+"\t"+str(different_words[10*x])+"\t"+str(numberofWords[10*x])+"\n")
    time=0
    target.write(str(0)+"\t")
    different_words=0
    target.write(str(different_words)+"\t")
    numberofWords=0
    target.write(str(numberofWords)+"\n")
    couples=[]
    clustering=[]
    seentimes=[100, 1000, 10000, 100000, 1000000, 1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000, 20000000, 30000000, 40000000, 99999999]


    for i in range(T):
        
        if i in seentimes:
            print i
            if SHOW==2:
                try:
                    nodeColor=[]
                    for x in f.topology.G.nodes():
                        if f.topology.G.node[x]['agent'].dict != []:
                            nodeColor.append(int(f.topology.G.node[x]['agent'].dict[0]))
                        else:
                            nodeColor.append(0)
                    nodeColor=[float(color)/max(nodeColor) for color in nodeColor]
                except:
                    print "the topolgy is complete and has no grid to print"


                if f.topology.tipo == GRIDONMAP:
                    fig=plt.figure(figsize=(16,12))
                    fig.patch.set_facecolor('#F8F8ff')
                    ax=plt.subplot(111)
                    elarge=[(u,v) for (u,v,d) in f.topology.G.edges(data=True) if d['weight'] >=0.05]
                    esmall=[(u,v) for (u,v,d) in f.topology.G.edges(data=True) if d['weight'] <0.05]
                    nx.draw_networkx_edges(f.topology.G, 
                        pos={i:i for i in f.topology.G.nodes()}, edgelist=elarge, 
                        width=1, alpha = 0.5)
                    nx.draw_networkx_edges(f.topology.G, 
                        pos={i:i for i in f.topology.G.nodes()}, edgelist=esmall, 
                        width=1, alpha=0.5,edge_color='b',style='dashed')
                    nx.draw_networkx_nodes(f.topology.G, 
                        pos={i:i for i in f.topology.G.nodes()}, node_color=nodeColor, 
                        node_cmap=cm.Colormap("Accent"),
                        node_size=60)
                    plt.xlabel('X_grid identifier')
                    plt.ylabel('Y_grid identifier')
                    plt.savefig("word_on_grid_time_"+str(i)) # display
            lunghezze=[len(component) for component in sorted(word_clusters(f.topology), key=len, reverse=True)]
            if len(lunghezze):
                clustering.append(float(sum(lunghezze))/len(lunghezze))
            else:
                clustering.append(0)
            print clustering[-1]


        [speaker, hearer] = f.Select()
        if f.topology.tipo==COMPLETE:
        	couples.append([speaker.id,hearer.id])
        if(hearer==None):
            #print "Che rumore fa un albero che cade in una foresta disabitata?"
            target.write(str(i+1)+"\t")
            target.write(str(different_words)+"\t")
            target.write(str(numberofWords)+"\n")
            continue


        if(speaker==None):
            print "che rumore fa il battito di una mano sola?"
            target.write(str(i+1)+"\t")
            if speaker.ndw:
                different_words=speaker.ndw
                target.write(str(speaker.ndw)+"\t")
            else:
                targe.write(str(different_words)+"\t")
            target.write(str(numberofWords)+"\n")
            continue


        if DEBUG: 
            print "speaker:", str(speaker.dict)," hearer:",str(hearer.dict)

        coupleWords=len(speaker.dict)+len(hearer.dict)
        if(len(speaker.dict) == 1 and speaker.dict == hearer.dict): 
            # trivial case
            #print "%d %d" %(i, speaker.ndw)
            target.write(str(i+1)+"\t")
            different_words=speaker.ndw
            target.write(str(different_words)+"\t")
            numberofWords+=len(speaker.dict)+len(hearer.dict)-coupleWords
            target.write(str(numberofWords)+"\n")
            continue
        

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


        target.write(str(i+1)+"\t")
        different_words=speaker.ndw
        target.write(str(different_words)+"\t")
        numberofWords+=len(speaker.dict)+len(hearer.dict)-coupleWords
        target.write(str(numberofWords)+"\n")
       
    target.close()

    differentWords=[]
    numberWords=[]
    for line in open(name, "r"):
        differentWords.append(int(line.split("\t")[1]))
        numberWords.append(int(line.split("\t")[2]))

    print len(differentWords), len(numberWords)

    if SHOW==1:
        if f.topology.tipo==COMPLETE:
            x,y=zip(*couples)
            plt.scatter(x,y)


        fig=plt.figure(figsize=(16,12))
        ax=plt.subplot(111)
        ax.spines["top"].set_visible(False)
        ax.spines["bottom"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()
        plt.xticks(fontsize=14)
        plt.tick_params(axis="both", which="both", bottom="off", top="off", 
            labelbottom="on", left="off", right="off", labelleft="on")
    
        plt.plot(range(len(differentWords)), differentWords, label='NDW')
        plt.plot(range(len(numberWords)) , numberWords, label='NW')
        plt.xlabel('Time Step')
        plt.ylabel('Number of Different Words')
        plt.legend()
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
        plt.tick_params(axis="both", which="both", bottom="off", top="off", 
            labelbottom="on", left="off", right="off", labelleft="on")
    
        plt.plot(range(len(numberWords)) , numberWords, label='NW')
        try:
            plt.plot(range(len(numberWords)), 
                [len(f.topology.G.nodes()) for i in range(len(numberWords))], 
                "--", lw=0.5, color="black", alpha=0.3)
        except:
            plt.plot(range(len(numberWords)), [8100 for i in range(len(numberWords))], 
                "--", lw=0.5, color="black", alpha=0.3)
        plt.xlabel('Time Step')
        plt.ylabel('Number of Words')
        plt.show()


        nodeColor=[]
        try:
            for x in f.topology.G.nodes():
                if f.topology.G.node[x]['agent'].dict != []:
                    nodeColor.append(int(f.topology.G.node[x]['agent'].dict[0]))
                else:
                    nodeColor.append(0)
            nodeColor=[float(color)/max(nodeColor) for color in nodeColor]
        except:
            print "the topolgy is complete and has no grid to print"

        
        if f.topology.tipo == GRIDONMAP:
            fig2=plt.figure()
            elarge=[(u,v) for (u,v,d) in f.topology.G.edges(data=True)\
             if d['weight'] >=0.05]
            esmall=[(u,v) for (u,v,d) in f.topology.G.edges(data=True)\
             if d['weight'] <0.05]
            nx.draw_networkx_edges(f.topology.G, 
                pos={i:i for i in f.topology.G.nodes()}, edgelist=elarge, 
                width=1, alpha = 0.5)
            nx.draw_networkx_edges(f.topology.G, 
                pos={i:i for i in f.topology.G.nodes()}, edgelist=esmall,
                 width=1, alpha=0.5,edge_color='b',style='dashed')
            nx.draw_networkx_nodes(f.topology.G, 
                pos={i:i for i in f.topology.G.nodes()}, node_color=nodeColor, 
                node_cmap=cm.Colormap("Accent"), node_size=20)
            plt.xlabel('X_grid identifier')
            plt.ylabel('Y_grid identifier')
            plt.show() # display


    if f.topology.tipo == GRIDONMAP:
        filename="final_grid_"+name
        with open(filename, "wb") as output:
            pk.dump(f.topology.G, output, pk.HIGHEST_PROTOCOL)
    
    elif f.topology.tipo == COMPLETE:
        print "finished game\n"
    
    else:
        if SHOW==1:
            fig2=plt.figure()
            nx.draw(f.topology.G, pos=nx.spring_layout(f.topology.G))
            plt.show() # display
        

    plt.plot(seentimes[:len(clustering)], clustering)
    plt.show()


    return (differentWords, numberWords)









def namegiving(name):
    '''
    Checks if the filename name is already in use, and if so adds (n) to the end,
    where n id the nth version of the file
    '''
    
    if Path(name).is_file():
    	if name.endswith(')'):
    		name=name[:-3]+'('+str(int(name[-2])+1)+')'
    	else:
    		name=name+'(2)'
    	if Path(name).is_file():
    		return namegiving(name)
    return name

def word_clusters(topology):
    seen={}
    for v in topology.G:
        if v not in seen:
            if topology.G.node[v]['agent'].dict != []:
                c=sp_length(topology, v, topology.G.node[v]['agent'].dict[0])
            else:
                c={}
            yield list(c)
            seen.update(c)
            
def sp_length(topology, source, word):
    seen={}
    level=0
    nextlevel={source:1}
    while nextlevel:
        thislevel=nextlevel
        nextlevel={}
        for v in thislevel:
            if v not in seen:
                seen[v]=level
                nextlevel.update({nbr:topology.G.node[nbr] for nbr in topology.G[v] if word in topology.G.node[nbr]['agent'].dict})
        level=level+1
    return seen