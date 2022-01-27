print("hello")

from ScraGet import ScraGet #import package
user = ScraGet.get_user() #create object
user.updateScratch("griffpatch") #update data
print(f"Scraget works: {user.id}") #print required info from data*

with open("test.txt", "a") as file:
  file.write("testing. look at line#\n")
