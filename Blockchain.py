import hashlib as hashlibrary
#importing and reading json file
import json as js
jsonFilePath = r'F:\Uni of Liv\Introduction to Programming\Python Assignment\political-emails.json'
with open(jsonFilePath) as email_file:
    email_data = js.load(email_file)
#Checking and verifying data format
print(type(email_data))
print(email_data[0]) #to check first element of json file
#to organise the email data in an much more organised and readable manner
for i in email_data[0]:
    print (i,"-",email_data[0][i])
#------------------------------------------------------------------TASK A----------------------------------------------------------------------#
print(len(email_data))
"""
Since our data is classified as 'list' and each element is an email, so we use 'len' function to count the length of the list.
Hence, the code above (line 13) gives out the total number of political emails in the json file
"""
key_check=list(email_data[0].keys())
print(key_check)
for each_email in email_data:
    if key_check!=list(each_email.keys()):
        print("Keys are not identical")
        break
#To check if the above loop is fully executed till the end of the list and is not breaking in between. If not so, then the elements are identical.
if email_data.index(each_email)==len(email_data)-1:
    print("Keys are identical")
"""
The above code is meant to compare keys of each element with the keys of the first element in the list. 
It is to check whether the keys are identical or not. 
"""
#-----------------------------------------------------------------TASK B----------------------------------------------------------------------#
encoded_block = str(email_data[8]).encode()
hashvalue1 = hashlibrary.sha256(encoded_block).hexdigest()
print(hashvalue1)

encoded_block = str(email_data[8]).encode()
hashvalue2 = hashlibrary.sha256(encoded_block).hexdigest()
print(hashvalue2)

encoded_block = str(email_data[10]).encode()
hashvalue3 = hashlibrary.sha256(encoded_block).hexdigest()
print(hashvalue3)

if hashvalue1==hashvalue2:
    print("'hashvalue1' and 'hashvalue2' are identical")
else: print("'hashvalue1' and 'hashvalue2' are not identical")

if hashvalue1==hashvalue3:
    print("'hashvalue1' and 'hashvalue3' are identical")
else: print ("'hashvalue1' and 'hashvalue3' are not identical")
