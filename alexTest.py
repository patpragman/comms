import process
import sql

#Adding a user via hardcoded data. Change the username before uncommenting and running this
#sampleDict = {"username" : "hogrider69", "password" : "Password"}
#print(process.new_user(sampleDict)) # Wrapped in a print statement to get the return value


sampleDict2 = {"username" : "hogrider69", "password" : "Password469"}
# now testing user deleter. Create a user with the code above and then delete them with the code below
print(process.edit_password(sampleDict2))