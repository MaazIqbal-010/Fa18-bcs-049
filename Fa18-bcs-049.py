# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:23:30 2021

@author: BHATTI
"""

import queue as Q

def Astar(graph, heuristic, start, end):
    
    #print("Function Call")
    if start not in graph:
        raise TypeError(str(start) + "Not foun in graph |")
        return
    if end not in graph:
        raise TypeError(str(end) + "Not foun in graph |")
        return
    
    heu=heuristic[start]
    queue = Q.PriorityQueue()
    queue.put((heu,0,[start]))
    #print("Before While")
    while not queue.empty():
        
        node=queue.get()
        current=node[2][len(node[2])-1]
        if end in node[2]:
            print("Path found " + str(node[2]) + " Cost = " + str(node[1]))
            break
        cost=node[1]
        for neighbour in graph[current]:
            temp = node[2][:]
            temp.append(neighbour)
            current_cost = cost + graph[current][neighbour]
            heu=heuristic[neighbour] + current_cost
            print("Visiting Node is "+ str(neighbour) +" h(n)+g(n) "+ str(heu) +" Cost is "+ str(current_cost))
            queue.put((heu, current_cost, temp))
            
            
           
def readgraph():
    mapfile = open("map.txt" , "r+")
    graph={}
    heuristic={}
    for line in mapfile:
        separator = line.split(",")
        cities=separator[0]
        heuristicValue=separator[1]
        tokens=cities.split()
        node=tokens[0]
        heuristic[str(tokens[0])]=int(heuristicValue)
        graph[node]={}
        
        
        for i in range(1, len(tokens) - 1, 2):
            graph[node][tokens[i]]=int(tokens[i + 1])
            
    return graph,heuristic

def main():
    
    graph,heu = readgraph()
    print("graph is " + str(graph))
    print("\nheuristic Value is " +str(heu))
    Astar(graph, heu, 'Oradea', 'Urziceni')
    #print("After Function Call")
    
if __name__ == "__main__":
    main()
