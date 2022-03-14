print("hello")

from ScraGet import ScraGet #import package
user = ScraGet.get_user() #create object
user.updateScratch("griffpatch") #update data
print(f"Scraget works: {user.AboutMe}") #print required info from data*

with open("text.txt", "a") as file:
  file.write("testing. look at line#\n")

  
with open("index.html", "w") as file:
  file.write("""<!DOCTYPE html>
<html>
  <head><title>test</title></head>
  <body>
  {}
  </body>
</html>
""".format(user.AboutMe))
