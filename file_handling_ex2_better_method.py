with open("index.html") as f:
    with open("output.txt","a") as w:
        page=f.read()
        link_exist=True
        while link_exist:
            pos = page.find("<a href=")
            if pos==-1:
                link_exist=False
            else:
                start=page.find("\"",pos)
                end=page.find("\"",start+1)
                url=page[start+1:end]
                w.write(url+"\n")
                page=page[end:]

