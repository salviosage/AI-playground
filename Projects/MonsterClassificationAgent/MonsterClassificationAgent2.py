


class MonsterClassificationAgent:

    def generalize(self, gen, attributes):
        if len(gen) == 0:
            gen = attributes
        else:
            for attribute, value in attributes.items():
                if gen[attribute] != value:
                    gen[attribute] = "any"
        return gen

    def check_monster(self, gen, new_attributes):
        for attribute, value in new_attributes.items():
            if gen[attribute] != value and gen[attribute] != "any":
                return False
        return True

    def solve(self, samples, new_monster):
        gen = dict()
        for monster, is_positive in samples:
            if is_positive:
                gen = self.generalize(gen, monster)
        return self.check_monster(gen, new_monster)