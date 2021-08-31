data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']
for error in data:
    elements = error.split(":")
   # print(elements[0].upper(), elements[1])
    if elements[0] =='Error':
        print(elements[1].upper())
    else:
        print(elements[1])

