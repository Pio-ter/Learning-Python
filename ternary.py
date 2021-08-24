musclePain=True
fever=False
weaknes=True
isMan=False

if musclePain and fever and weaknes:
    print('suspicion of influenza')
else:
    print('the flu is unlikely')

if musclePain and fever and weaknes:
    print('suspicion of influenza')
elif weaknes and not (musclePain or fever):
    print('just take a rest')
else:
    print('you may be cold')

if musclePain and fever and weaknes:
     print('suspicion of influenza')
elif isMan and (musclePain or fever or weaknes):
    print('suspicion of influenza')
elif weaknes and not (musclePain or fever):
    print('just take a rest')
else:
    print('you may be cold')

isCheckCompleted=False
print('check is completed' if isCheckCompleted else 'check not done yet')  
