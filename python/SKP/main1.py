def find_all_hobbyists(hobby, hobbies):
    li = []
    names = hobbies.keys()
    for i in names:
        if hobby in hobbies[i]:
            li.append(i)
    return li


if __name__ == "__main__":
    hobbies = {
        "Steve": ['Fashion', 'Piano', 'Reading'],
        "Patty": ['Drama', 'Magic', 'Pets'],
        "Chad": ['Puzzles', 'Pets', 'Yoga']
    }

    print(find_all_hobbyists('Yoga', hobbies));