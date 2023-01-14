# how to copy a text from other file

with open("file1.txt","r") as rf:
    with open("file2.txt","w") as wf:
        wf.write(rf.read())
