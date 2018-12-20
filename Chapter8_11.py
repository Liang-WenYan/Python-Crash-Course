def make_great(names, new_names):
    print("before %s" % names)
    while names:
        current_name = names.pop()
        new_names.append(current_name.title() + " the Great")
    print("after %s" % names)


def show_great(new_names):
    for name in new_names:
        print(name)


example_names = ['binbin', 'yanyan', 'banban']
print("before list: %s" % example_names)
example_new_names = []
make_great(example_names[:], example_new_names)
print("origin list: %s" % example_names)
show_great(example_new_names)
