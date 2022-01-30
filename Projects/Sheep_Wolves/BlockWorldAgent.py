class BlockWorldAgent:
    def __init__(self):
        #If you want to do any initial processing, add it here.
        pass

    def solve(self, initial_arrangement, goal_arrangement):
        #Add your code here! Your solve method should receive
		#as input two arrangements of blocks. The arrangements
		#will be given as lists of lists. The first item in each
		#list will be the bottom block on a stack, proceeding
		#upward. For example, this arrangement:
		#
		#[["A", "B", "C"], ["D", "E"]]
		#
		#...represents two stacks of blocks: one with B on top
		#of A and C on top of B, and one with E on top of D.
		#
		#Your goal is to return a list of moves that will convert
		#the initial arrangement into the goal arrangement.
		#Moves should be represented as 2-tuples where the first
		#item in the 2-tuple is what block to move, and the
		#second item is where to put it: either on top of another
		#block or on the table (represented by the string "Table").
		#
		#For example, these moves would represent moving block B
		#from the first stack to the second stack in the example
		#above:
		#
		#("C", "Table")
		#("B", "E")
		#("C", "A")
        # pass
	    return a_star(initial_arrangement, goal_arrangement)
class Node:
    def __init__(self, state, parent, operator, depth):
        # Contains the state of the node
        self.state = state
        # Contains the node that generated this node
        self.parent = parent
        # Contains the operation that generated this node from the parent
        self.operator = operator
        # Contains the depth of this node (parent.depth +1)
        self.depth = depth
        
        self.heuristic=None

def move(state,item_to_move,item_to_move_to):
	if(item_to_move_to=="Table"):
		for item in state:
			if(item[len(item)-1]==item_to_move):
				item.pop()
		state.append([item_to_move])
		return [var for var in state if  var]
	else:
		for item in state:
			if(item[len(item)-1]==item_to_move):
				item.pop()
			elif(item[len(item)-1]==item_to_move_to):
				item.append(item_to_move)
		return [var for var in state if var]
def create_node(state, parent, operator, depth=0):
    return Node(state, parent, operator, depth)



def expand_node(node):
	# Add your code here!
	# Your expand_node method should return a list of new nodes
	expanded_nodes = []
	for n in range(len(node.state)):
		for m in range(len(node.state)):
			if(m!=n):
				expanded_nodes.append(create_node(move(node.state,node.state[n],node.state[m]),node,(node.state[n],node.state[m]),node.depth+1))
				expanded_nodes.append(create_node(move(node.state,node.state[n],"Table"),node,(node.state[n],"Table"),node.depth+1))
	return expanded_nodes


    
def a_star(start, goal):
    start_node=create_node(start,None,None,1)
    fringe=[]
    path=[]
    fringe.append(start_node)
    current=fringe.pop(0)
    explored=[]
    explored.append(start_node.state)
    while(current.state!=goal):
        new_nodes=(expand_node(current))
        new_nodes = [node for node in new_nodes if node.state not in  explored]
        explored.append([node.state for node in new_nodes if node.state != None])
        fringe.extend(new_nodes)
        for item in fringe:
            h(item)
            item.heuristic+=(item.depth/10)
        fringe.sort(key =lambda x: x.heuristic)
        if not fringe:
            return []
        current=fringe.pop(0) 


                  
    while(current.parent!=None):
        path.insert(0,tuple(current.operator))
        current=current.parent
    return path




def h(state):
    dmatch=0

    dmatch+=len(state.state)- len(goal)
    state.heuristic=dmatch

