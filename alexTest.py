import process
import sql

#Adding a user via hardcoded data. Change the username before uncommenting and running this
#sampleDict = {"username" : "hogrider69", "password" : "Password"}
#print(process.new_user(sampleDict)) # Wrapped in a print statement to get the return value


# This was me just testing my check_user function.
# This function normally runs as part of process.new_user
# to verify a user was added.


# now testing password updater
process.edit_password('neofromthematrix')