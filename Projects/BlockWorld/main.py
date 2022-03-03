from BlockWorldAgent1 import BlockWorldAgent

def test():
    #This will test your BlockWorldAgent
	#with eight initial test cases.
    test_agent = BlockWorldAgent()

    initial_arrangement_1 = [["A", "B", "C"], ["D", "E"]]
    goal=[["A", "B"],["D", "E", "C"]]
    goal_arrangement_1 = [ ["D", "E", "B"],["A", "C"]]
    goal_arrangement_2 = [["A", "B", "C", "D", "E"]]
    goal_arrangement_3 = [["D", "E", "A", "B", "C"]]
    goal_arrangement_4 = [["C", "D"], ["E", "A", "B"]]
    print(test_agent.solve(initial_arrangement_1, goal))
    print(test_agent.solve(initial_arrangement_1, goal_arrangement_1))
    print(test_agent.solve(initial_arrangement_1, goal_arrangement_2))
    print(test_agent.solve(initial_arrangement_1, goal_arrangement_3))  
    print(test_agent.solve(initial_arrangement_1, goal_arrangement_4)) ## this took long 

    initial_arrangement_2 = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
    goal_arrangement_5 = [["A", "B", "C", "D", "E", "F", "G", "H", "I"]]
    goal_arrangement_6 = [["I", "H", "G", "F", "E", "D", "C", "B", "A"]]
    goal_arrangement_7 = [["H", "E", "F", "A", "C"], ["B", "D"], ["G", "I"]]
    goal_arrangement_8 = [["F", "D", "C", "I", "G", "A"], ["B", "E", "H"]]

    print(test_agent.solve(initial_arrangement_2, goal_arrangement_5)) 
    print(test_agent.solve(initial_arrangement_2, goal_arrangement_6)) ## this took too long 
    print(test_agent.solve(initial_arrangement_2, goal_arrangement_7)) ## same shit
    print(test_agent.solve(initial_arrangement_2, goal_arrangement_8)) ## this took long

if __name__ == "__main__":
    test()