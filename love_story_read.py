with open("love_story.txt","r",encoding="utf-8") as f:
    # vs code and windows mai default encoding cp1252 hotee hai hame chnage karna padega encoding ko emojis read karne ke liye
    print(f.encoding)
    print(f.read(),end="")

# how to read files in read
# with open("file1.txt","r") as f:
#     data =f.read(3)
#     # it will read 3 word
#     while len(data)>0:
#         print(data)
#         data =f.read(3)
