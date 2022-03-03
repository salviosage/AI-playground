from MonsterClassificationAgent2 import MonsterClassificationAgent

def test():
    #This will run your code against the first four known test cases.
    test_agent = MonsterClassificationAgent()

    known_positive_1 = {'size': 'huge', 'color': 'black', 'covering': 'fur', 'foot-type': 'paw', 'leg-count': 2, 'arm-count': 4, 'eye-count': 2, 'horn-count': 0, 'lays-eggs': True, 'has-wings': True, 'has-gills': True, 'has-tail': True}
    known_positive_2 = {'size': 'large', 'color': 'white', 'covering': 'fur', 'foot-type': 'paw', 'leg-count': 2, 'arm-count': 4, 'eye-count': 2, 'horn-count': 0, 'lays-eggs': True, 'has-wings': True, 'has-gills': True, 'has-tail': False}
    known_positive_3 = {'size': 'huge', 'color': 'white', 'covering': 'fur', 'foot-type': 'paw', 'leg-count': 2, 'arm-count': 4, 'eye-count': 2, 'horn-count': 0, 'lays-eggs': True, 'has-wings': True, 'has-gills': False, 'has-tail': True}
    known_positive_4 = {'size': 'large', 'color': 'black', 'covering': 'fur', 'foot-type': 'paw', 'leg-count': 1, 'arm-count': 3, 'eye-count': 2, 'horn-count': 0, 'lays-eggs': True, 'has-wings': True, 'has-gills': True, 'has-tail': True}
    known_positive_5 = {'size': 'large', 'color': 'white', 'covering': 'fur', 'foot-type': 'foot', 'leg-count': 2, 'arm-count': 4, 'eye-count': 2, 'horn-count': 0, 'lays-eggs': True, 'has-wings': True, 'has-gills': False, 'has-tail': False}
    known_negative_1 = {'size': 'large', 'color': 'blue', 'covering': 'fur', 'foot-type': 'paw', 'leg-count': 2, 'arm-count': 4, 'eye-count': 2, 'horn-count': 0, 'lays-eggs': True, 'has-wings': True, 'has-gills': True, 'has-tail': True}
    known_negative_2 = {'size': 'tiny', 'color': 'red', 'covering': 'scales', 'foot-type': 'none', 'leg-count': 0, 'arm-count': 8, 'eye-count': 8, 'horn-count': 2, 'lays-eggs': False, 'has-wings': False, 'has-gills': False, 'has-tail': False}
    known_negative_3 = {'size': 'medium', 'color': 'gray', 'covering': 'fur', 'foot-type': 'foot', 'leg-count': 2, 'arm-count': 6, 'eye-count': 2, 'horn-count': 0, 'lays-eggs': True, 'has-wings': False, 'has-gills': False, 'has-tail': False}
    known_negative_4 = {'size': 'huge', 'color': 'black', 'covering': 'fur', 'foot-type': 'paw', 'leg-count': 2, 'arm-count': 6, 'eye-count': 2, 'horn-count': 2, 'lays-eggs': True, 'has-wings': True, 'has-gills': False, 'has-tail': False}
    known_negative_5 = {'size': 'medium', 'color': 'purple', 'covering': 'fur', 'foot-type': 'talon', 'leg-count': 2, 'arm-count': 4, 'eye-count': 2, 'horn-count': 0, 'lays-eggs': False, 'has-wings': False, 'has-gills': True, 'has-tail': False}

    monster_list = [(known_positive_1, True), (known_positive_2, True), (known_positive_3, True), (known_positive_4, True), (known_positive_5, True),
            (known_negative_1, False), (known_negative_2, False), (known_negative_3, False), (known_negative_4, False), (known_negative_5, False)]

    new_monster_1 = {'size': 'large', 'color': 'black', 'covering': 'fur', 'foot-type': 'paw', 'leg-count': 1, 'arm-count': 3, 'eye-count': 2, 'horn-count': 0, 'lays-eggs': True, 'has-wings': True, 'has-gills': True, 'has-tail': True}
    new_monster_2 = {'size': 'tiny', 'color': 'red', 'covering': 'scales', 'foot-type': 'none', 'leg-count': 0, 'arm-count': 8, 'eye-count': 8, 'horn-count': 2, 'lays-eggs': False, 'has-wings': False, 'has-gills': False, 'has-tail': False}
    new_monster_3 = {'size': 'large', 'color': 'gray', 'covering': 'fur', 'foot-type': 'foot', 'leg-count': 1, 'arm-count': 3, 'eye-count': 2, 'horn-count': 0, 'lays-eggs': True, 'has-wings': True, 'has-gills': False, 'has-tail': False}
    new_monster_4 = {'size': 'small', 'color': 'black', 'covering': 'scales', 'foot-type': 'paw', 'leg-count': 2, 'arm-count': 4, 'eye-count': 2, 'horn-count': 0, 'lays-eggs': True, 'has-wings': True, 'has-gills': False, 'has-tail': False}

    print(test_agent.solve(monster_list, known_positive_1))
    print(test_agent.solve(monster_list, known_positive_2))
    print(test_agent.solve(monster_list, known_positive_3))
    print(test_agent.solve(monster_list, known_positive_4))
    print(test_agent.solve(monster_list, known_negative_1))
    print(test_agent.solve(monster_list, known_negative_2))
    print(test_agent.solve(monster_list, known_negative_3))
    print(test_agent.solve(monster_list, known_negative_4))
    print(test_agent.solve(monster_list, new_monster_1))
    print(test_agent.solve(monster_list, new_monster_2))
    print(test_agent.solve(monster_list, new_monster_4))
    print(test_agent.solve(monster_list, new_monster_4))
    print(test_agent.solve(monster_list, new_monster_3))

if __name__ == "__main__":
    test()