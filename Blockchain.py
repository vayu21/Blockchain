import random
import datetime
import hashlib as hashlibrary
#importing and reading json file
print("----------------IMPORTING THE JSON FILE IN PYTHON--------------------")
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
print()
print("--------------------------------------------------------------------------------------TASK A----------------------------------------------------------------------------------------")
print()
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
print()
print("--------------------------------------------------------------------------------------TASK B----------------------------------------------------------------------------------------")
print()
encoded_block = str(email_data[8]).encode()
hashvalue1 = hashlibrary.sha256(encoded_block).hexdigest()
print(hashvalue1)

encoded_block = str(email_data[8]).encode()
hashvalue2 = hashlibrary.sha256(encoded_block).hexdigest()
print(hashvalue2)

encoded_block = str(email_data[10]).encode()
hashvalue3 = hashlibrary.sha256(encoded_block).hexdigest()
print(hashvalue3)

#Checking the identicality of the hash values
if hashvalue1==hashvalue2:
    print("'hashvalue1' and 'hashvalue2' are identical")
else: print("'hashvalue1' and 'hashvalue2' are not identical")

if hashvalue1==hashvalue3:
    print("'hashvalue1' and 'hashvalue3' are identical")
else: print ("'hashvalue1' and 'hashvalue3' are not identical")
print()
print("--------------------------------------------------------------------------------------TASK C----------------------------------------------------------------------------------------")
print()
#------------------------------------------------------------------TASK C1------------------------------------------------------------------------#
#creating a dictionary function
#block_dict={'Block Index':,'Transaction Time Stamp':,'Transaction Data':,'Proof of Work':,'Hash of Previous Block':}
chain=[]
def create_block(index,timestamp,data,proof,hash):
    block_dict={'Block Index':index,'Transaction Time Stamp':timestamp,'Transaction Data':data,'Proof of Work':proof,'Hash of Previous Block':hash}
    create_chain(block_dict)
    return block_dict
def create_chain(block):
    chain.append(block)

#print(create_block()) #to check if our block is returning dictionary or not

#-----------------------------------------------------------------TASK C2------------------------------------------------------------------------#
def genesis_block():
    genesis_block={'Block Index':1,'Transaction Time Stamp':str(datetime.datetime.now()),'Transaction Data':"This is the Genesis Block of email transactions",'Proof of Work':1,'Hash of Previous Block':"000"}
    create_chain(genesis_block)
#-----------------------------------------------------------------TASK C3------------------------------------------------------------------------#
def hash_value(obj):
    encoded_block = str(obj).encode()
    has = hashlibrary.sha256(encoded_block).hexdigest()
    return has
""" TO CHECK HOW TO CREATE PREVIOUS HASH OF THE BLOCK IN THE BLOCKCHAIN
genesis_block()
print(hash_value(chain[0]))
"""
to_check_proof=[]
def pow_algo(previous_proof):
    new_proof=1
    check_proof=False
    while check_proof==False:
        encoded_block = str(new_proof**5-previous_proof**3).encode()
        has1 = hashlibrary.sha256(encoded_block).hexdigest()
        if(has1[:3]=='000'):
            check_proof=True
        else:
            new_proof+=1
# To check if our new proof is already assigned to any previous block or not
    if(new_proof in to_check_proof):
        print("It's already assigned")
    else:
        to_check_proof.append(new_proof)
    return new_proof

def mine_block(i):
    #before adding a block to our blockchain, we have to check if our blockchain has genesis block or not
    if len(chain)==0:
        #if not so, then we will call genesis block funtion to add genesis block in our blockchain
        genesis_block()
    block_index=len(chain)+1
    trans_timestamp=datetime.datetime.now()
    trans_data=email_data[i]['datetime']+ ", " +email_data[i]['email_id']
    prev_hash=hash_value(chain[len(chain)-1])
    #pow= random.randint(2000,7000)
    pow=pow_algo(chain[len(chain)-1]['Proof of Work'])
    create_block(block_index,trans_timestamp,trans_data,pow,prev_hash)

"""     TO CHECK IF WE CAN ADD POLITICAL EMAIL DATA TO OUR BLOCKCHAIN
for i in range(0,4):
    mine_block(i)
for j in chain:
    print(j)
"""
#------------------------------------------------------------------TASK C4-------------------------------------------------------------------#
for k in range(121):
    mine_block(random.randint(0,405))
#to check if our blockchain is complete and working successfully
for z in chain:
    print(z)
#--------------------------------------------------------------------*******-------------------------------------------------------------------#