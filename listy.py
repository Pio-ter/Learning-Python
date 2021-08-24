hitsTitles=['Brothers in arms', 'Bohemian Rapsody', 'Stairway to heaven', 'riders on the storm', 'Wish you were here']
print(hitsTitles)

hitsTitles.append('Child in time')
hitsTitles.append('Again')
hitsTitles[2]='hotel california'
hitsTitles[0]='the sound of silence'
print(hitsTitles.index('hotel california'))
print(hitsTitles)
hitsTitles.remove('hotel california')
print(hitsTitles)
hitsTitles.insert(0, 'enjoy the silence')
print(hitsTitles)
hitsToRead = hitsTitles.copy()
hitsToRead.reverse()
hitsToRead.sort()
print(hitsToRead.pop(0))
print(hitsToRead.pop(1))
additionalSongs=['nothing compares 2u', 'Wish you were here']
hitsToRead.extend(additionalSongs)
print(hitsToRead.count('Wish you were here'))
print(hitsToRead.count('riders on the storm'))
print(hitsToRead.clear(), hitsTitles)
