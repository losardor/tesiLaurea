#def 
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
    for i in range(T):
        [speaker, hearer] = f.Select()
        if(hearer==None):
            #print "Che rumore fa un albero che cade in una foresta disabitata?"
            time.append(i+1)
            different_words.append(different_words[-1])
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
            continue
        #if (speaker.ndw==1 and i>f.N): 
        #    break
        
        if DEBUG: 
            print "speaker:",
            str(speaker.dict),
            " hearer:",
            str(hearer.dict)
            
        if(len(speaker.dict) == 1 and speaker.dict == hearer.dict): 
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
    if SHOW==1:
        fig=plt.figure()
        ax1=plt.subplot2grid((1,1),(0,0))
        plt.scatter(time, different_words, label='NDW')
        plt.xlabel('Time Step')
        plt.ylabel('Number of Different Words')
        plt.title('Number of Different Words in Time')
        ax1.grid(True)
        plt.show()
        nodeColor=[]
        for x in f.topology.G.nodes():
                if f.topology.G.node[x]['agent'].dict != []:
                    nodeColor.append(int(f.topology.G.node[x]['agent'].dict[0]))
                else:
                    nodeColor.append(0)
        if f.topology.tipo==GRIDONMAP:
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
        elif f.topology.tipo == COMPLETE:
            print "finished game\n"
        else:
            fig2=plt.figure()
            colors = cm.rainbow(np.linspace(0, 1, len(nodeColor)))
            nx.draw(f.topology.G, pos=nx.spring_layout(f.topology.G))
            plt.show() # display

    target = open(name, "w")
    for x in range(len(time)):
        target.write(str(time[x])+"\t"+str(different_words[x])+"\n")

        
