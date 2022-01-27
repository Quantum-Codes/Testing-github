print("hello")

from ScraGet import ScraGet #import package
user = ScraGet.get_user() #create object
user.updateScratch("griffpatch") #update data
print(user.id) #print required info from data*
