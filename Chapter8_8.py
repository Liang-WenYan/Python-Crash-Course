def make_album(name, album_name, number=''):
    if number:
        full_album = {'singer_name': name.title(), 'album': album_name.title(), 'many': number}
    else:
        full_album = {'singer_name': name.title(), 'album': album_name.title()}
    return full_album


while True:
    print("\nInput the singer's name:")
    print("\n(Enter 'quit' at any time to quit!)")
    singer_name = input()
    if singer_name == 'quit':
        break
    print("\nInput the album's name:")
    print("\n(Enter 'quit' at any time to quit!)")
    album = input()
    if album == 'quit':
        break
    print("\nHow many songs? ")
    print("\n(Enter 'quit' at any time to quit!)")
    many = input()
    if many == 'quit':
        break
    full_album = make_album(singer_name, album, many)
    print(full_album)
