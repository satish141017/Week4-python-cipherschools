# with open("index.html") as f:
#     with open("output.txt","a") as w:
#         for line in f.readlines():
#             if "<a href=" in line:
#                 pos = line.find("<a href=")
#                 start=line.find("\"",pos)
#                 end=line.find("\"",start+1)
#                 w.write(line[start+1:end]+"\n")
    