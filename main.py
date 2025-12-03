import random
import test




def createCharacter(hero):
    hero['name'] = random.choice(test.pull_names)
    hero['level'] = 1
    hero['hp'] = 100
    hero['mp'] = 50
    hero['strength'] = 10
    hero['defense'] = 5
    hero['inventory'] = []
    return hero
    



hero = {}

def main():
    createCharacter(hero)
    print(hero)


if __name__ == "__main__":
    main()