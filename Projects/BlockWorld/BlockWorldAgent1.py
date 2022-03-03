import heapq

def memoize(fn, slot=None, maxsize=32):
    if slot:
        def memoized_fn(obj, *args):
            if hasattr(obj, slot):
                return getattr(obj, slot)
            else:
                val = fn(obj, *args)
                setattr(obj, slot, val)
                return val
    else:
        @functools.lru_cache(maxsize=maxsize)
        def memoized_fn(*args):
            return fn(*args)

    return memoized_fn

class Problem(object):

    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        raise NotImplementedError

    def result(self, state, action):
        raise NotImplementedError

    def goal_test(self, state):
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal

    def path_cost(self, c, state1, action, state2):
        return c + 1

class BlocksWorld(Problem) :
    def __init__(self, initial, goal):
        Problem.__init__(self, initial, goal)
        self.initial = initial
        self.goal = goal

    def result(self, state, action):
        state_list = list(state)
        source_stack = action[0]
        destination_stack = action[1]
        moved_block = 0
        for block in state_list[source_stack]:  
            moved_block = block
        if len(state[source_stack]) != 1:  
            new_stack = []
            for iterator in range(len(state[source_stack])-1):
                new_stack.append(state[source_stack][iterator])  
            state_list.append(tuple(new_stack))  

        if destination_stack != ' ':   
            state_list.remove(state[destination_stack]) 
            state_list.append(state[destination_stack] + (moved_block, ))  
        else:
            state_list.append((moved_block, ))

        state_list.remove(state[source_stack]) 

        state_list.sort(key=lambda stack: len(stack))
        return tuple(state_list)

    def actions(self, state):
        actions_list = []
        for stack in state:

            for other_stack in state:
                if other_stack != stack:
                    actions_list.append((state.index(stack), state.index(other_stack)))  

            if len(stack) != 1:
                actions_list.append((state.index(stack), ' '))  

        return actions_list

    def goal_test(self, state):
        for stack in state:
            if stack not in self.goal:
                return False
        return True




class BlocksWorldH2(BlocksWorld):
    def h(self, node):
        sum = 0
        for stack in node.state:
            for other_stack in self.goal:
                if stack[0] in other_stack:
                    goal_stack = other_stack
                    break
            for block in stack:
                block_position = stack.index(block)
                if block in goal_stack:
                    if block_position == goal_stack.index(block):
                        continue
                sum = sum + len(stack) - block_position
                for iterator in range(block_position, len(stack)):
                    stack_block = stack[iterator]
                    stack_position = stack.index(stack_block)
                    if stack_position != 0:  # If there are blocks below stack_block in the current state
                        for other_stack in self.goal:
                            if stack_block in other_stack:
                                other_position = other_stack.index(stack_block)
                                if other_position != 0:  # If there are blocks below stack_block in the goal state
                                    for iterator_2 in range(0, stack_position):
                                        other_block = stack[iterator_2]
                                        if other_block in other_stack:
                                            if other_stack.index(other_block) < other_position:
                                                sum = sum + 1
                                                break
        return sum
class PriorityQueue:
    def __init__(self, order='min', f=lambda x: x):
        self.heap = []

        if order == 'min':
            self.f = f
        elif order == 'max':  # now item with max f(x)
            self.f = lambda x: -f(x)  # will be popped first
        else:
            raise ValueError("order must be either 'min' or max'.")

    def append(self, item):
        heapq.heappush(self.heap, (self.f(item), item))

    def extend(self, items):
        for item in items:
            self.heap.append(item)

    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)[1]
        else:
            raise Exception('Trying to pop from empty PriorityQueue.')

    def __len__(self):
        return len(self.heap)

    def __contains__(self, item):
        return (self.f(item), item) in self.heap

    def __getitem__(self, key):
        for _, item in self.heap:
            if item == key:
                return item

    def __delitem__(self, key):
        self.heap.remove((self.f(key), key))
        heapq.heapify(self.heap)





class Node:

    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node {}>".format(self.state)

    def __lt__(self, node):
        return self.state < node.state

    def expand(self, problem):
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        next_node = problem.result(self.state, action)
        return Node(next_node, self, action,
                    problem.path_cost(self.path_cost, self.state,
                                      action, next_node))

    def solution(self):
        return [node.action for node in self.path()[1:]]

    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        return hash(self.state)


def best_first_graph_search(problem, f): 
    f = memoize(f, 'f')
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier = PriorityQueue('min', f)
    frontier.append(node)
    explored = set()

    while frontier:

        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                incumbent = frontier[child]
                if f(child) < f(incumbent):
                    del frontier[incumbent]
                    frontier.append(child)

    return None


def astar_search(problem, h=None):
    """A* search is best-first graph search with f(n) = g(n) + h(n)."""
    h = memoize(h or problem.h, 'h')
    return best_first_graph_search(problem, lambda n: n.path_cost + h(n))



class BlockWorldAgent:
    def __init__(self):
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
     
        initialstate= tuple(tuple(var) for var in initial_arrangement if var)
        goalstate= tuple(tuple(var) for var in goal_arrangement if var)
        problem3 = BlocksWorldH2(initialstate, goalstate)
        astar = astar_search(problem3)
        path=[]
        current=astar
        astar_solution = astar.solution()
        astar_path = astar.path()
        for iterator in range(1, len(astar_path)):
            state = astar_path[iterator-1].state
            action = astar_solution[iterator - 1]

            if action[1] != ' ':
                path.append(tuple((state[action[0]][-1], state[action[1]][-1])))
            else:
                path.append(tuple((state[action[0]][-1], "Table")))
        return path
       
