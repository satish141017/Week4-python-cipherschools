# default  is r [wahi read wala] mode 
# todaye we learn about  w ,a ,r+ modes
# write mode
# w -- it will overwrite (means pichla uda ke nya) karta hai 
# w --  used to create new files ese nayee files ya empty files mai use karte hai
# with open("temp_file2.txt","w") as f:
#     f.write("this sentence is written with python and created with python") 

# a -- apppend text withour deleting it
with open("temp_file2.txt","a") as f:
    f.write("this sentence is append with python") 


# r+ --  it will overite text but not delete all of it bus jo iske curseer ke raste mai aye ga to last mai kese likhe phele cusor ko last mai le jao sekk method ki help se fir write kar lo
with open("temp_file2.txt","r+") as f:
    f.seek()
    f.write("this sentence is append with python") 