texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
i=0
imax=len(texts)-1
while i<=imax:
    print(texts[i], texts[i+1])
    if len(texts[i])==len(texts[i+1]):
        print('\tfound')
    i+=1
