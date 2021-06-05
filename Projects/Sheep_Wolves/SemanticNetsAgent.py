class SemanticNetsAgent:
    def __init__(self):
        #If you want to do any initial processing, add it here.
        self.goal_state = [0,0,0,0]
        self.initial_state=[0,0,0,0]
#         self.parent_node= create_node(initial_state,None,[initial_sheep,initial_wolves])
#         pass
    
    def solve(self, initial_sheep, initial_wolves):
        goal_state = [0,0,initial_sheep,initial_wolves]
        initial_state=[initial_sheep,initial_wolves,0,0]
#         print(initial_state,goal_state)
#         self.parent_node= create_node(initial_state,None,[initial_sheep,initial_wolves])
        return a_star(initial_state, goal_state)
        #Add your code here! Your solve method should receive
        #the initial number of sheep and wolves as integers,
        #and return a list of 2-tuples that represent the moves
        #required to get all sheep and wolves from the left
        #side of the river to the right.
        #
        #If it is impossible to move the animals over according
        #to the rules of the problem, return an empty list of
        #moves.
        
        pass
# Node data structure

class Node:
    def __init__(self, state, parent, operator, depth,position):
        # Contains the state of the node
        self.state = state
        # Contains the node that generated this node
        self.parent = parent
        # Contains the operation that generated this node from the parent
        self.operator = operator
        # Contains the depth of this node (parent.depth +1)
        self.depth = depth
        # position either left or right
        self.position = position
        
        self.heuristic=None
    
        
def move_left(state,sheeps=0,wolthes=0):
    new_state = state[:]
    # Sanity check
    if(sheeps==0 and wolthes==0):
        # Can't move it, return None
        return None
    
    elif(sheeps>state[2] or wolthes>state[3]):
        # Can't move it, return None
        return None
    else:
        # Swap the values.
        new_state[2] = new_state[2]-sheeps
        new_state[3] = new_state[3]-wolthes
        new_state[0] = new_state[0]+sheeps
        new_state[1] = new_state[1]+wolthes
        if new_state[0] < new_state[1] or new_state[2] < new_state[3]:
            # Can't move it, dead state return None
            return None
        return new_state
    

def move_right(state,sheeps=0,wolthes=0):
    new_state = state[:]
     # Sanity check
    if(sheeps==0 and wolthes==0):
        return None
    
    elif(sheeps>state[0] or wolthes>state[1]):
#         print(state[2])
        # Can't move it, return None
        return None
    else:
        # Swap the values.
        new_state[0] = new_state[0]-sheeps
        new_state[1] = new_state[1]-wolthes
        new_state[2] = new_state[2]+sheeps
        new_state[3] = new_state[3]+wolthes
        if new_state[0] < new_state[1] or new_state[2] < new_state[3]:
            # Can't move it, dead state return None
            return None
        
        return new_state
    

def create_node(state, parent, operator, depth=0,position='L'):
    return Node(state, parent, operator, depth,position)



def expand_node(node):
    """Returns a list of expanded nodes"""
    expanded_nodes = []
    if(node.position=='L'):
        expanded_nodes.append(create_node(move_right(node.state,0,1), node, [0,1], node.depth + 1,'R'))
        expanded_nodes.append(create_node(move_right(node.state,0,2), node, [0,2], node.depth + 1,'R'))
        expanded_nodes.append(create_node(move_right(node.state,1,0), node, [1,0], node.depth + 1,'R')) 
        expanded_nodes.append(create_node(move_right(node.state,2,0), node, [2,0], node.depth + 1,'R')) 
        expanded_nodes.append(create_node(move_right(node.state,1,1), node, [1,1], node.depth + 1,'R'))
    else:
        expanded_nodes.append(create_node(move_left(node.state,0,1), node, [0,1], node.depth + 1))
        expanded_nodes.append(create_node(move_left(node.state,0,2), node, [0,2], node.depth + 1))
        expanded_nodes.append(create_node(move_left(node.state,1,0), node, [1,0], node.depth + 1)) 
        expanded_nodes.append(create_node(move_left(node.state,2,0), node, [2,0], node.depth + 1)) 
        expanded_nodes.append(create_node(move_left(node.state,1,1), node, [1,1], node.depth + 1))
        
    # Filter the list and remove the nodes that are impossible (move function returned None)
    expanded_nodes = [node for node in expanded_nodes if node.state != None]  # list comprehension!
    return expanded_nodes


def a_star(start, goal):
    start_node=create_node(start,None,None,1,'L')
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
            item.heuristic+=(item.depth/10000)
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
    dmatch+=(state.state[0]-state.state[2] )+ (state.state[1]-state.state[3])
#             )+ (state.state[1]-state.state[3])
    state.heuristic=dmatch