import process
import sql

#Adding a user via hardcoded data. Change the username before uncommenting and running this
#sampleDict = {"username" : "bigoldick", "password" : "Password"}
#process.new_user(sampleDict)


# This was me just testing my check_user function.
# This function normally runs as part of process.new_user
# to verify a user was added.

print(sql.check_user("serioussam"))