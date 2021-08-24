marketing=['loyality program','client promotion','market research']
marketing.append('public relations')
print(marketing[2])
marketing.insert(1,'investor relations')
print(marketing)
emailMarketing=marketing.copy()
emailMarketing.sort()
print(emailMarketing)
internalEmails=['internal communication']
emailMarketing.extend(internalEmails)
print(emailMarketing)
print(tuple(emailMarketing))
