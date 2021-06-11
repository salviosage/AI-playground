def bfs(start, goal):
    """Performs a breadth first search from the start state to the goal"""
    # A list (can act as a queue) for the nodes.
    goal=goal
    start_node=create_node(start,None,None,0,0)
    fringe=[]
    fringe.append(start_node)
    current=fringe.pop(0)
    path=[]
    while(current.state!=goal):
        fringe.extend(expand_node(current))
        current=fringe.pop(0)
    while(current.parent!=None):
        path.insert(0,current.operator)
        current=current.parent
    return path
    pass


def dfs(start, goal, depth=10):
    start_node=create_node(start,None,None,0,0)
    fringe_stack=Stack()
    fringe_stack.push(start_node)
    current=fringe_stack.pop()
    path=[]
    while(current.state!=goal):
        temp=expand_node(current)
        for item in temp:
            fringe_stack.push(item)
        current=fringe_stack.pop()
        if(current.depth>10):
            return None
    while(current.parent!=None):
        path.insert(0,current.operator)
        current=current.parent
    return path



def uniform_cost(start,goal):
    start_node=create_node(start,None,None,0,0)
    fringe=[]
    path=[]
    fringe.append(start_node)
    current=fringe.pop(0)
    while(current.state!=goal):
        temp=expand_node(current)
        for item in temp:
            item.depth+=current.depth
            fringe.append(item)
        fringe.sort(key =lambda x: x.depth)
        current=fringe.pop(0)
    while(current.parent!=None):
        path.insert(0,current.operator)
        current=current.parent
    return path


def greedy(start,goal):
    start_node=create_node(start,None,None,0,0)
    fringe=[]
    path=[]
    fringe.append(start_node)
    current=fringe.pop(0)
    while(current.state!=goal):
        fringe.extend(expand_node(current))
        for item in fringe:
            h(item,goal)
        fringe.sort(key =lambda x: x.heuristic)
        current=fringe.pop(0)
    while(current.parent!=None):
        path.insert(0,current.operator)
        current=current.parent
    return path

