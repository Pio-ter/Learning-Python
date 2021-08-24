chanels={'google':'1480','email':'300','natural traffic':'440','tv spot':'700'}
print(chanels['email'])
chanelsUpdate={'natural traffic':'520','news':'600'}
chanels.update(chanelsUpdate)
print(chanels)
print(chanels.keys())
chanels.pop('email')
print(chanels)
