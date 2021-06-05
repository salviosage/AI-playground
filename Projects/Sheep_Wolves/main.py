from SemanticNetsAgent import SemanticNetsAgent

def test():
    #This will test  SemanticNetsAgent

    test_agent = SemanticNetsAgent()
    print(test_agent.solve(10, 4))
    print(test_agent.solve(13, 12))
    print(test_agent.solve(13, 13))
    print(test_agent.solve(14, 5))
    print(test_agent.solve(15, 3))
    print(test_agent.solve(1, 1))
    print(test_agent.solve(2, 1))
    print(test_agent.solve(4, 4))
    print(test_agent.solve(2, 2))
    print(test_agent.solve(3, 3))
    print(test_agent.solve(5, 3))
    print(test_agent.solve(5, 5))
    print(test_agent.solve(6, 2))
    print(test_agent.solve(6, 3))
    print(test_agent.solve(6, 4))
    print(test_agent.solve(6, 6))
    print(test_agent.solve(7, 3))
    print(test_agent.solve(8, 8))
    print(test_agent.solve(9, 9))

if __name__ == "__main__":
    test()