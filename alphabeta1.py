import math

count = 0

def alphaBeta(currentNode, alpha, beta):

    global count
    
    if isLeaf(currentNode):
        count = count + 1
        return int(currentNode)

    if maxNode(currentNode):
        for node in connectionElem:
            if node[0] == currentNode:
                r = alphaBeta(node[1], alpha, beta)
                alpha = max(alpha, r)
                if alpha >= beta:
                    return alpha
        return alpha

    if minNode(currentNode):
        for node in connectionElem:
            if node[0] == currentNode[0]:
                r = alphaBeta(node[1], alpha, beta)
                beta = min(beta, r)
                if beta <= alpha:
                    return beta
        return beta


def maxNode(currentNode):
    if currentNode[0] in listOfMax:
        return True
    else:
        return False

def minNode(currentNode):
    if currentNode[0] in listOfMin:
        return True
    else:
        return False
    
    
def isLeaf(currentNode):
    try:
        int(currentNode)
        return True
    
    except ValueError:
        return False

#reads in the given input from a text file
def readFile():
    with open("C:\\Users\\taylo\\Desktop\\352Assignment2\\alphabeta.txt","r") as f:
        inputLine = f.readlines()
    return inputLine #a string as a single list item [<class 'str'>]
       

def main():
    fullInput = readFile()
    #splits the input into 2 catagories (nodes that include max or min and the
    #connections with the children nodes)
    broken = fullInput[0].split(" ")

    #for both newly formed lists, it removes the first and last 3 charcters
    #and splits each list into individual nodes e.g. ['A,MAX', 'B,MIN',...
    nodes = broken[0][2:-2].split("),(") 
    connections = broken[1][2:-2].split("),(")

    global nodeElem
    nodeElem = []
    for i in range(len(nodes)):
        nodeElem.append(nodes[i].split(","))
    print("NODE ELEMENTS: ", nodeElem)

    global connectionElem
    connectionElem = []
    for i in range(len(connections)):
        connectionElem.append(connections[i].split(","))
    print("CONNECTION ELEMENTS: ", connectionElem)

    #loops through nodeElem and adds it to the max or min list
    #which can be easily referenced in the alphabeta function
    global listOfMax
    global listOfMin
    listOfMax = []
    listOfMin = []
    for i in nodeElem:
        if i[1] == "MAX":
            listOfMax.append(i[0])
        else:
            listOfMin.append(i[0])

    #passing in the root node
    print("Result", alphaBeta(connectionElem[0][0],(-1*math.inf),math.inf))
    print("Count:", count)


main()
