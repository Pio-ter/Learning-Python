stupid=False
looksGood=False
rich=True

if stupid and looksGood and rich:
    print('I am happy man')
elif rich and (stupid or looksGood):
    print('still happy')
else:
    print('not happy')
