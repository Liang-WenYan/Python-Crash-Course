def make_great(names, new_names):
    print(names)
    for name in names:
        new_name = name + " the Great"
        new_names.append(new_name)


def show_great(new_names):
    for name in new_names:
        print(name)


example_names = ['binbin', 'yanyan', 'banban']
example_new_names = []
make_great(example_names, example_new_names)
show_great(example_new_names)
