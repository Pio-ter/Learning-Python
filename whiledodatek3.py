text = """United Space Alliance: This company provides major support to NASA for
various projects, such as the space shuttle. One of its projects is to
create Workflow Automation System (WAS), an application designed to
manage NASA and other third-party projects. The setup uses a central
Oracle database as a repository for information. Python was chosen over
languages such as Java and C++ because it provides dynamic typing and
pseudo-code–like syntax and it has an interpreter. The result is that
the application is developed faster, and unit testing each piece is easier."""

wordLength = 6
i = 0
text1 = text.split(' ')
short = 0
long = 0
while i < len(text1):
    if len(text1[i]) <= wordLength:
       short += 1
    else:
        long += 1
    i+=1

print(short)
print(long)
