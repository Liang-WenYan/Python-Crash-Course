def make_album(name, album_name, number=''):
    """返回一个字典，包含歌手的姓名和专辑名，可能包含歌曲数"""
    if number:
        full_album = {'singer_name': name.title(), 'album': album_name.title(), 'many': number}
    else:
        full_album = {'singer_name': name.title(), 'album': album_name.title()}
    return full_album


print(make_album('xu song', 'bu ru chi cha qu', number=7))
print(make_album('mao bu yi', 'ping fan de yi tian'))
print(make_album('xu song', 'xun bao you xi', 8))
