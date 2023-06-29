import random
import datetime
import time
import hashlib as hashlibrary
starting_time=time.time()
#importing and reading json file
print("----------------JSON FILE IMPORTED IN PYTHON--------------------")
import json as js
jsonFilePath = r'F:\Uni of Liv\Introduction to Programming\Python Assignment\political-emails.json'
with open(jsonFilePath) as email_file:
    email_data = js.load(email_file)
#Checking and verifying data format
"""print(type(email_data))
print(email_data[0]) #to check first element of json file
#to organise the email data in an much more organised and readable manner
for i in email_data[0]:
    print (i,"-",email_data[0][i])
"""
flag=1
while flag:
    try:
        A=input("Please enter 'A' or 'a' or '1' to display output of TASK A or Enter 'E' or 'e' to execute the whole programme: ")
        if A!='1' and A!='A' and A!='a' and A!='e' and A!='E':
            raise IOError("INPUT ERROR !")
    except IOError as m:
        print(m)
    else:
        flag=0
#---------------------------------------------------------------TASK A-------------------------------------------------------------------#
print()
print("----------------------------------------------------------------------------------TASK A-----------------------------------------------------------------------------------")
print()
if A=='1'or A=='a'or A=='A' or A=='E' or A=='e':
    print(len(email_data))
"""
Since our data is classified as 'list' and each element is an email, so we use 'len' function to count the length of the list.
Hence, the code above (line 13) gives out the total number of political emails in the json file
"""
key_check=list(email_data[0].keys())
if A=='1'or A=='a'or A=='A' or A=='E' or A=='e':
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
#--------------------------------------------------------------TASK B--------------------------------------------------------------------#
print()
if A!='E' and A!='e':
    B=input("Please enter 'B' or 'b' or '2' to display output of TASK B: ")
print("----------------------------------------------------------------------------------TASK B-----------------------------------------------------------------------------------")
print()
if A=='E' or A=='e' or B=='2'or B=='b'or B=='B':
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
if A!='E' and A!='e':
    C=input("Please enter 'C' or 'c' or '3' to display output of TASK C: ")
print("----------------------------------------------------------------------------------TASK C-------------------------------------------------------------------------------------")
print()
#------------------------------------------------------------------TASK C1---------------------------------------------------------------------#
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

#--------------------------------------------------------------TASK C2---------------------------------------------------------------------#
def genesis_block():
    genesis_block={'Block Index':1,'Transaction Time Stamp':str(datetime.datetime.now()),'Transaction Data':"This is the Genesis Block of email transactions",'Proof of Work':1,'Hash of Previous Block':hashlibrary.sha256("000".encode()).hexdigest()}
    create_chain(genesis_block)
#--------------------------------------------------------------TASK C3-----------------------------------------------------------------------#
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
#---------------------------------------------------------------TASK C4----------------------------------------------------------------#
for k in range(120):
    mine_block(random.randint(0,405))
#to check if our blockchain is complete and working successfully
if A=='E' or A=='e' or C=='3'or C=='c'or C=='C':
    for z in chain:
        print(z)
print()
print(" Programme Duration: %s seconds   "% (time.time() - starting_time))
print("------------------------------------------------------------------------------THANK YOU------------------------------------------------------------------------------")
#--------------------------------------------------------------------*******-------------------------------------------------------------------#
"""                                                                 
                                                                    OUTPUT
                                                                    
----------------JSON FILE IMPORTED IN PYTHON--------------------
Please enter 'A' or 'a' or '1' to display output of TASK A or Enter 'E' or 'e' to execute the whole programme: E

----------------------------------------------------------------------------------TASK A-----------------------------------------------------------------------------------

406
['email_id', 'sender_name', 'email', 'subject', 'datetime', 'email_content']
Keys are identical

----------------------------------------------------------------------------------TASK B-----------------------------------------------------------------------------------

a2981b38880b19db5eaaa6dd70a80f5fb85cffcb4e2e72171d2dff6f57dfa7b2
a2981b38880b19db5eaaa6dd70a80f5fb85cffcb4e2e72171d2dff6f57dfa7b2
f48a77fb8a999126bb84054a70f2fdb9bfaa474ce1fd5267fab74dbed22c643c
'hashvalue1' and 'hashvalue2' are identical
'hashvalue1' and 'hashvalue3' are not identical

----------------------------------------------------------------------------------TASK C-------------------------------------------------------------------------------------

{'Block Index': 1, 'Transaction Time Stamp': '2022-12-08 19:17:14.071742', 'Transaction Data': 'This is the Genesis Block of email transactions', 'Proof of Work': 1, 'Hash of Previous Block': '2ac9a6746aca543af8dff39894cfe8173afba21eb01c6fae33d52947222855ef'}
{'Block Index': 2, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 71742), 'Transaction Data': '15/12/2019 17:36, 121', 'Proof of Work': 1021, 'Hash of Previous Block': '47f733122573470e6fcd0b67f850f5708077a7447dfef07567bfa3fd9c05f291'}
{'Block Index': 3, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 72741), 'Transaction Data': '28/08/2019 06:00, 88', 'Proof of Work': 8122, 'Hash of Previous Block': 'a0cadd2bdeeb558b23a24a52472dc577e341268c6737fa05af481e4ae0fadb22'}
{'Block Index': 4, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 81749), 'Transaction Data': '28/10/2019 14:25, 105', 'Proof of Work': 5487, 'Hash of Previous Block': '1731e06de6503d1a08526e579db621eb922bb842788a9d3c95ed6855c14a93bf'}
{'Block Index': 5, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 86824), 'Transaction Data': '26/02/2020 09:10, 137', 'Proof of Work': 851, 'Hash of Previous Block': 'caa7160998035bd1fc41f5381063cbf549613b378d542ed15f77e5b81190a10d'}
{'Block Index': 6, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 87827), 'Transaction Data': '13/07/2020 09:50, 181', 'Proof of Work': 12595, 'Hash of Previous Block': '861e82f2f76da7d8820279638fac1acd0ebccbad5fc4896fa9fb58f5b64ee811'}
{'Block Index': 7, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 101824), 'Transaction Data': '12/07/2018 16:09, 30', 'Proof of Work': 6261, 'Hash of Previous Block': '82c816b187b80a98541eb945d77a479fd8b58d4d472d60e99a54f1d7ad3f829e'}
{'Block Index': 8, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 108818), 'Transaction Data': '22/06/2020 15:20, 174', 'Proof of Work': 221, 'Hash of Previous Block': '4eca6449126c13130c9776599f1ad718ab936f16b9d015db157baa45b6090606'}
{'Block Index': 9, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 108818), 'Transaction Data': '26/02/2020 18:16, 135', 'Proof of Work': 1121, 'Hash of Previous Block': 'fbe5c39488705bf9b962fe92ceae7657595128b65c7c929ae6a95590ff604a28'}
{'Block Index': 10, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 109828), 'Transaction Data': '23/02/2018 08:06, 215', 'Proof of Work': 11475, 'Hash of Previous Block': '36b7fbcc1c24bfe1ecc9a0ac35345d245c49754ba7723bbda381b9c68f819a5e'}
{'Block Index': 11, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 121742), 'Transaction Data': '10/06/2019 05:31, 70', 'Proof of Work': 695, 'Hash of Previous Block': '3ca74e4c919bd221e6b9c834a5a6811eba6f504527c1557fdcd1e5f9b3931d05'}
{'Block Index': 12, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 122745), 'Transaction Data': '26/02/2020 14:02, 325', 'Proof of Work': 5163, 'Hash of Previous Block': '27c8792202eebf7c1bac3d728bc33d26fb5311efd96186fabdc83540aef3cfa0'}
{'Block Index': 13, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 128756), 'Transaction Data': '25/11/2019 10:46, 310', 'Proof of Work': 13850, 'Hash of Previous Block': '3d4cf942b10a19929fbebe6978c8893d9da10bd7e75478e3ae9618a90fe97bb1'}
{'Block Index': 14, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 143285), 'Transaction Data': '26/06/2019 13:42, 278', 'Proof of Work': 1949, 'Hash of Previous Block': 'ded80758445210e69283e8cfef11814397248dadc9632a238fd90c0799ad217f'}
{'Block Index': 15, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 145366), 'Transaction Data': '31/08/2019 13:15, 92', 'Proof of Work': 19644, 'Hash of Previous Block': 'cae82476aad6118af0941a66d07036774c43d9adac317aaab5e600f8d57da8b4'}
{'Block Index': 16, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 165276), 'Transaction Data': '24/08/2019 11:31, 288', 'Proof of Work': 9352, 'Hash of Previous Block': '39a2924248a06a2a8faece8eb1a276d6b29844daeb5b778a51ecc9be2956aa01'}
{'Block Index': 17, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 174276), 'Transaction Data': '14/10/2020 16:36, 386', 'Proof of Work': 2990, 'Hash of Previous Block': '87795afe62d90917a64fe6c5ba605090ddc6ec78237b77e7e04b4fc9c2203ab4'}
{'Block Index': 18, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 177276), 'Transaction Data': '28/08/2018 05:43, 37', 'Proof of Work': 2363, 'Hash of Previous Block': 'a3a8b4383eeabeaf30e1b87e2afa905fa1eb43eb3270a3aa7f09100563557327'}
{'Block Index': 19, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 180276), 'Transaction Data': '28/02/2020 11:25, 327', 'Proof of Work': 8, 'Hash of Previous Block': 'f7ca64a8b48fbd5921a1811096513d6651a427969ee8c2bcf881abfb94d9d735'}
{'Block Index': 20, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 180276), 'Transaction Data': '23/05/2019 06:30, 62', 'Proof of Work': 1699, 'Hash of Previous Block': '41243581e8201c7680986da209cfde28a235719443567be2f87135f4c2d1cd3f'}
{'Block Index': 21, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 181276), 'Transaction Data': '28/06/2018 09:00, 236', 'Proof of Work': 852, 'Hash of Previous Block': '13118937a642426f7ac1775202772a65b94dbffb3302599acab84d85f052ce24'}
{'Block Index': 22, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 182276), 'Transaction Data': '05/10/2019 04:13, 100', 'Proof of Work': 3139, 'Hash of Previous Block': '85c9779ae4ec34547e8b2b30ef2942f2c8415987b1dbba3ff44d4a6b8092bf23'}
{'Block Index': 23, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 186364), 'Transaction Data': '25/11/2019 13:05, 116', 'Proof of Work': 3205, 'Hash of Previous Block': '78e2002b7893f650ceb5390aa2ebdd791e1b567aadc9e6744cd01e7b91d3860a'}
{'Block Index': 24, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 189366), 'Transaction Data': '26/04/2020 18:39, 337', 'Proof of Work': 2130, 'Hash of Previous Block': '5664168b2edfad625bcbd95fa6b8016636dd9308457afa005de0a68060022f8d'}
{'Block Index': 25, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 191364), 'Transaction Data': '01/11/2016 09:33, 363', 'Proof of Work': 2682, 'Hash of Previous Block': '968a4bdcb981eb8b9792ec0b342db2484208e9dc6221aec1ec5321df22627187'}
{'Block Index': 26, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 194366), 'Transaction Data': '06/07/2020 15:38, 355', 'Proof of Work': 2663, 'Hash of Previous Block': 'fb8fdb10e0741eb353ca1ce7c1f32ef55cfafab5dcce71813c76ae99817ef43e'}
{'Block Index': 27, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 196361), 'Transaction Data': '03/12/2018 16:12, 55', 'Proof of Work': 6852, 'Hash of Previous Block': '902bdcaeee3791fede6b0718a43d8adcf77678403dcff15ab6f80965a6205d47'}
{'Block Index': 28, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 203367), 'Transaction Data': '25/12/2019 11:20, 317', 'Proof of Work': 1349, 'Hash of Previous Block': 'a41c7b71c2cb2a131cd7acb5cb99875b67cc4e758517e8ef31f5990ac85bc05e'}
{'Block Index': 29, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 205367), 'Transaction Data': '01/11/2016 14:43, 189', 'Proof of Work': 2498, 'Hash of Previous Block': 'ca828732ff8eda5dd3c366c7193a12384f3e9ae675014b8d0b1ddcd9a3e5ad38'}
{'Block Index': 30, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 207276), 'Transaction Data': '03/12/2019 09:03, 313', 'Proof of Work': 9819, 'Hash of Previous Block': '9e49d2a10bb0d89ee061de3b7826193bbfc422e37024dca4e666e7e919a8a4ad'}
{'Block Index': 31, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 217276), 'Transaction Data': '09/04/2020 16:45, 147', 'Proof of Work': 7241, 'Hash of Previous Block': '561a18dfee1c33cbe81e3efe862ef57ccc94b4489487326f4f3506fc9a6ceda7'}
{'Block Index': 32, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 224277), 'Transaction Data': '30/09/2017 15:57, 3', 'Proof of Work': 1364, 'Hash of Previous Block': '82f6f10d8227f75b87da7eaa3b613f1cb8dbade3f37bde7acfb9a5ffff5ee700'}
{'Block Index': 33, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 226277), 'Transaction Data': '15/01/2020 12:04, 321', 'Proof of Work': 7061, 'Hash of Previous Block': '63feb8e548af9023cb2fb6224428fa5c6497dc5d7aa348871fcba12048a05f87'}
{'Block Index': 34, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 233277), 'Transaction Data': '30/04/2020 16:50, 156', 'Proof of Work': 7878, 'Hash of Previous Block': 'a4f049acd7e5208429b1679bf6ce03b2fa1ad90e05f46ebd1918c306ae98c1c3'}
{'Block Index': 35, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 241784), 'Transaction Data': '03/11/2017 08:58, 6', 'Proof of Work': 274, 'Hash of Previous Block': '1aeee8afcafb7c6d5ee84cc1332f46e8f76de93da1f9498005b84116901e3a55'}
{'Block Index': 36, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 241784), 'Transaction Data': '09/04/2020 16:45, 147', 'Proof of Work': 8418, 'Hash of Previous Block': '53906976109389907058484f4a726919a38157e87e918472f670a446e966698c'}
{'Block Index': 37, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 250973), 'Transaction Data': '07/01/2019 06:56, 57', 'Proof of Work': 364, 'Hash of Previous Block': '88e10364aaae85477e074eb50f91c6b506f1b7b5f995232912abcd600143a81e'}
{'Block Index': 38, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 250973), 'Transaction Data': '12/06/2020 13:01, 351', 'Proof of Work': 13840, 'Hash of Previous Block': '4add478b773821ba4c5db87305f966adce4d2e0e107473efb5b8d35af7bb6d45'}
{'Block Index': 39, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 265310), 'Transaction Data': '26/06/2018 08:23, 232', 'Proof of Work': 3256, 'Hash of Previous Block': '5c640a87081975c06bca4461339f7b11b730e2a12ac4de121b7a63caee5979fd'}
{'Block Index': 40, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 268310), 'Transaction Data': '06/09/2020 06:25, 199', 'Proof of Work': 73, 'Hash of Previous Block': '36e890551a8604aec1f83dc6206233691ba43d3e06d9411594e9db01da22dea2'}
{'Block Index': 41, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 268310), 'Transaction Data': '15/04/2017 08:18, 78', 'Proof of Work': 2225, 'Hash of Previous Block': '436e276f37c691b72ebeb84daafc396bc8d89c1a0a475c44ce37aa123d97f869'}
{'Block Index': 42, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 270602), 'Transaction Data': '26/10/2017 13:02, 398', 'Proof of Work': 4104, 'Hash of Previous Block': 'fa432dda6088ae51bd117b6343d4ca09dfc84a6cc9aac9bf6157ac9779c28d10'}
{'Block Index': 43, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 274061), 'Transaction Data': '28/02/2020 11:25, 327', 'Proof of Work': 56, 'Hash of Previous Block': '152aad7cc658814e650472986f7c0081eefe32efdbb50c8091503bc12890ea68'}
{'Block Index': 44, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 274061), 'Transaction Data': '26/07/2017 14:23, 393', 'Proof of Work': 3532, 'Hash of Previous Block': '0f9dfea23d57208ab4a2b70236000e867f76920351465e9b6d88e4e4a23140db'}
{'Block Index': 45, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 277403), 'Transaction Data': '27/08/2020 06:57, 374', 'Proof of Work': 6365, 'Hash of Previous Block': 'd79b15622d996686a4829bd312e398d68615ac94a808f9380d6dc18a5355904b'}
{'Block Index': 46, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 284953), 'Transaction Data': '04/03/2019 12:53, 265', 'Proof of Work': 2464, 'Hash of Previous Block': 'e89f0daf518bb7d2a740763d173dff17eabd4fdf056035607bdce1a88f0f84e6'}
{'Block Index': 47, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 286953), 'Transaction Data': '04/07/2020 13:03, 179', 'Proof of Work': 15673, 'Hash of Previous Block': '6f6ba1c216da14e78d34d86a82bb64ea3eea47b65e1b8884b4f110c39a9d5502'}
{'Block Index': 48, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 302953), 'Transaction Data': '19/11/2019 08:04, 304', 'Proof of Work': 1330, 'Hash of Previous Block': '844f04999d4101df4eeffe7aafabb399289f5d639eabff22977356159934037c'}
{'Block Index': 49, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 303953), 'Transaction Data': '19/04/2019 19:15, 266', 'Proof of Work': 7914, 'Hash of Previous Block': '936de39aaaf80fa47701e6e6e989864f07f12a0f65ccb392ec23b2208b2e3d07'}
{'Block Index': 50, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 312953), 'Transaction Data': '15/04/2017 08:18, 78', 'Proof of Work': 8922, 'Hash of Previous Block': '742dd20aae593621f63bc6e600a22146fd2b531ed335ae1adf563fd1e3c0732e'}
{'Block Index': 51, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 321278), 'Transaction Data': '28/12/2017 12:37, 405', 'Proof of Work': 7813, 'Hash of Previous Block': '7ceb49aa557267de1bf5e711d8ec766b8bc985657f30944d0495e38a84121023'}
{'Block Index': 52, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 330653), 'Transaction Data': '21/09/2020 10:48, 378', 'Proof of Work': 805, 'Hash of Previous Block': 'd72c44b1183ce4ca7daa8d69681d18ac1adf7f3983e174bb0421a9ec5f355759'}
{'Block Index': 53, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 331653), 'Transaction Data': '31/12/2019 18:52, 123', 'Proof of Work': 5369, 'Hash of Previous Block': 'a76954c486e0d5a16f2cf3b74890ac4809ecddeba83d8127f2b52991c19258f2'}
{'Block Index': 54, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 336653), 'Transaction Data': '19/10/2019 10:56, 297', 'Proof of Work': 3397, 'Hash of Previous Block': '6ae6521e8d26e8ecb53e0b45072a3f866538651e952ba5cd0df1fb561bba1c0b'}
{'Block Index': 55, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 340354), 'Transaction Data': '29/10/2016 18:41, 187', 'Proof of Work': 6280, 'Hash of Previous Block': '5459d190412e66fd1391d3215c4b3577a90e666072e7558730b926f3e32cea4c'}
{'Block Index': 56, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 346354), 'Transaction Data': '07/01/2019 09:15, 56', 'Proof of Work': 2957, 'Hash of Previous Block': 'e48d8c3638f47cbd3f9617125afb929ff916ace47fccb6c73106f2e4d961e435'}
{'Block Index': 57, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 349354), 'Transaction Data': '21/08/2020 09:14, 368', 'Proof of Work': 5229, 'Hash of Previous Block': '5043ec9e8c2c7db57d75ff9820c8520c7d222b29e98a33a07f5e695f67e143a6'}
{'Block Index': 58, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 354354), 'Transaction Data': '27/10/2019 13:11, 104', 'Proof of Work': 52, 'Hash of Previous Block': '8d7681bf10686cfd798f35523b4d22ace52173d1a7bc3a3d75a47b7652155c70'}
{'Block Index': 59, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 354354), 'Transaction Data': '17/12/2017 07:28, 403', 'Proof of Work': 2831, 'Hash of Previous Block': '1f91152de0ff3dd73ce9649f500ea315b8507d867b0604f988f3afe284e89aec'}
{'Block Index': 60, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 357445), 'Transaction Data': '14/11/2019 16:30, 303', 'Proof of Work': 1490, 'Hash of Previous Block': 'ca1c93403570c1af1a29ea558ca201423aee9c928d53ff84231476472c94d7d4'}
{'Block Index': 61, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 359445), 'Transaction Data': '19/11/2019 09:50, 113', 'Proof of Work': 3782, 'Hash of Previous Block': 'f1de12cb87f19daacef69c2f3b674da624828a6f31cfc2e5da21a1e08f90caa8'}
{'Block Index': 62, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 363548), 'Transaction Data': '25/08/2020 07:43, 372', 'Proof of Work': 5801, 'Hash of Previous Block': 'af4c493de25f9f78668c32e04b073b1c8542659074f94fd39dfdecda97a00d3d'}
{'Block Index': 63, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 369709), 'Transaction Data': '11/02/2020 17:36, 132', 'Proof of Work': 1638, 'Hash of Previous Block': 'b366dc69846edb95296aa68c9862f068fa5f86d3a3da69b34e4675b63ca9da7e'}
{'Block Index': 64, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 370910), 'Transaction Data': '02/05/2020 17:25, 339', 'Proof of Work': 6680, 'Hash of Previous Block': 'ca3a3a8f076fdd0d665dc88abfbbc4f507b78e83094591dee19a613e5fa3277e'}
{'Block Index': 65, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 378453), 'Transaction Data': '15/09/2018 07:05, 249', 'Proof of Work': 32, 'Hash of Previous Block': 'd24a9caccd877207106b2e74d315c23c4331be8589878846de02693502981d7e'}
{'Block Index': 66, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 378453), 'Transaction Data': '03/12/2018 16:12, 55', 'Proof of Work': 1112, 'Hash of Previous Block': '3263d26f2ef9f07b72a6f959ed5d8f971cf0fa3699143239338610fdea90287e'}
{'Block Index': 67, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 379453), 'Transaction Data': '14/07/2020 16:00, 357', 'Proof of Work': 181, 'Hash of Previous Block': 'a1e111c21429ca308030b7bb2c61b571ec0fa6d6c35ad6abda19b19bd3c9efe6'}
{'Block Index': 68, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 379453), 'Transaction Data': '29/07/2019 07:27, 83', 'Proof of Work': 2418, 'Hash of Previous Block': '68ddd358208445e597c1793799f9aa3c856831aae95da00815c322926521fe94'}
{'Block Index': 69, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 381453), 'Transaction Data': '22/11/2019 14:04, 309', 'Proof of Work': 2288, 'Hash of Previous Block': '999a76d1ec00de87421c1efda97d6b759ae2c52ff6e3e3d1cf1b44c3a63748be'}
{'Block Index': 70, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 383453), 'Transaction Data': '23/08/2020 12:24, 369', 'Proof of Work': 676, 'Hash of Previous Block': 'd94c4f1742de4df87589c0a9ee3a7e18752233ba0e78062ee266eb9eacf2e927'}
{'Block Index': 71, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 384453), 'Transaction Data': '08/06/2017 16:01, 388', 'Proof of Work': 4433, 'Hash of Previous Block': 'ae3b692243e0bcc7a2ea6054adce247d1ec5b972c18a9893444ff9d65eab9e5f'}
{'Block Index': 72, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 388749), 'Transaction Data': '14/05/2017 07:35, 67', 'Proof of Work': 263, 'Hash of Previous Block': 'fc2267a75670afc4a4b34900d0ac9fff51f1fde7e66c90eb235be1ef94caf8f0'}
{'Block Index': 73, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 389766), 'Transaction Data': '30/06/2020 06:41, 177', 'Proof of Work': 2566, 'Hash of Previous Block': '3042230ed65cc7915ee5779c8e68c36fc592416349e52a2ff40e742420f6b6b3'}
{'Block Index': 74, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 391839), 'Transaction Data': '30/12/2017 06:45, 213', 'Proof of Work': 5673, 'Hash of Previous Block': '2b38045981a6dab265576bfc0ba9a3ada988effcfda566a5f1517a60974767c6'}
{'Block Index': 75, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 397833), 'Transaction Data': '13/07/2020 09:50, 181', 'Proof of Work': 2604, 'Hash of Previous Block': '90d06602c8c6c6cc266dddb14515da70135cca68627f855494b4ada5c6ed5bac'}
{'Block Index': 76, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 399833), 'Transaction Data': '18/06/2018 13:20, 25', 'Proof of Work': 4977, 'Hash of Previous Block': '9869f5641b888444782282023c484f69203a31e811ca759ed14f653c692551c5'}
{'Block Index': 77, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 405833), 'Transaction Data': '22/08/2020 15:37, 370', 'Proof of Work': 2803, 'Hash of Previous Block': '5277e7add83d12d01ffe6a26ba62f2e2abc0356e1bd05820c08a7b78ebb636bd'}
{'Block Index': 78, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 408833), 'Transaction Data': '11/02/2020 17:36, 132', 'Proof of Work': 9244, 'Hash of Previous Block': '0b27c00fe202f1e8d12a5224472e1146af99c97356ee70bf0258b89a61e01225'}
{'Block Index': 79, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 417979), 'Transaction Data': '13/09/2017 15:16, 206', 'Proof of Work': 5616, 'Hash of Previous Block': '26d08e36b5129448b665169a069f36b10ac287b5dba74acc61c0a2cef238cb8f'}
{'Block Index': 80, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 423980), 'Transaction Data': '29/09/2017 10:46, 4', 'Proof of Work': 2800, 'Hash of Previous Block': '70c667f3229ae1c3cabff130c2921e6af92434d318c68a4bea5590f5cbc06e76'}
{'Block Index': 81, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 426980), 'Transaction Data': '15/01/2020 18:06, 129', 'Proof of Work': 1721, 'Hash of Previous Block': 'f583fc32b12f57f93769b8aef817c43756f16fb7c3f4e29223514dda8c421d66'}
{'Block Index': 82, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 427980), 'Transaction Data': '22/02/2020 16:47, 324', 'Proof of Work': 990, 'Hash of Previous Block': '8a3753323d07607cc3bead8fde65ff9301f0798567bc4945fe9bcf715e709747'}
{'Block Index': 83, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 428980), 'Transaction Data': '15/07/2019 07:52, 77', 'Proof of Work': 499, 'Hash of Previous Block': 'da3cf814e973e02ecee2ac0cf77b2d5ac7a9312c4abc72131a3df0e827440c55'}
{'Block Index': 84, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 429980), 'Transaction Data': '08/05/2018 09:09, 19', 'Proof of Work': 12231, 'Hash of Previous Block': 'cdd9b6c1c1c1fb5a18769b3b1372b99079a71e1248acdee22db6ef054f4b499f'}
{'Block Index': 85, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 442840), 'Transaction Data': '18/04/2017 08:05, 281', 'Proof of Work': 1227, 'Hash of Previous Block': 'a0735ef8c0883c36f29a32a801d9fa1cd32313e58adfde4bd812cb3f8b249140'}
{'Block Index': 86, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 444910), 'Transaction Data': '15/10/2020 08:05, 384', 'Proof of Work': 9028, 'Hash of Previous Block': '95670ecafa7c40156a8ef1b059301dcaa406e2cf7077989d0d4e482c2b45a67f'}
{'Block Index': 87, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 453393), 'Transaction Data': '16/12/2019 14:02, 120', 'Proof of Work': 911, 'Hash of Previous Block': 'c981eccc671477ca3752a79a1e2ef11c52d971f84b480ec64ece26c996181c8e'}
{'Block Index': 88, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 454449), 'Transaction Data': '30/06/2019 16:37, 280', 'Proof of Work': 2383, 'Hash of Previous Block': '5570034b2d2195ffe15cc98ca99c512e0e5d2e738bc1d442e66f9eaae3a1dfbc'}
{'Block Index': 89, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 456518), 'Transaction Data': '25/09/2019 06:13, 292', 'Proof of Work': 5762, 'Hash of Previous Block': 'c9d6225383fddb1337bf11f869a6c3999e0f6deb88c83514dc7b7d0099e2c674'}
{'Block Index': 90, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 462677), 'Transaction Data': '19/05/2018 07:29, 21', 'Proof of Work': 3035, 'Hash of Previous Block': '2dd125739acf032f4789e5e364007d561401cfd2e6fc9560167b0445873edde9'}
{'Block Index': 91, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 465930), 'Transaction Data': '18/06/2018 13:20, 25', 'Proof of Work': 9689, 'Hash of Previous Block': 'f9a1f52cc101ec34bda38d452c457eb1e697ade8a61278980f9382fae98f0113'}
{'Block Index': 92, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 475320), 'Transaction Data': '18/01/2018 12:36, 11', 'Proof of Work': 93, 'Hash of Previous Block': 'e21ee4933ee94ccbf04a38edd2d36ae06ab583cb0932238c089746e093977950'}
{'Block Index': 93, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 476363), 'Transaction Data': '22/01/2020 14:29, 322', 'Proof of Work': 2893, 'Hash of Previous Block': '172510e7fc8bcf12222ff60b4f082a33422deb9049dd59648aa5a3b51aab3bb1'}
{'Block Index': 94, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 478438), 'Transaction Data': '18/06/2018 13:20, 25', 'Proof of Work': 1175, 'Hash of Previous Block': 'f8d883f9c93df69cd571ed90c445451d05e1ec9c01ae20923de750c00c81e3c1'}
{'Block Index': 95, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 480504), 'Transaction Data': '04/06/2019 13:34, 69', 'Proof of Work': 2796, 'Hash of Previous Block': 'ee784dde7b7a768a5f7ef577dbd1aa441f04797d971c07e4e8c83cd04ea62aa3'}
{'Block Index': 96, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 482797), 'Transaction Data': '07/01/2019 06:56, 57', 'Proof of Work': 1210, 'Hash of Previous Block': 'dc37c34fedd8c037530c50670a7818b9b39fe8f13dcb3ccea920c6f45e0f0817'}
{'Block Index': 97, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 484842), 'Transaction Data': '17/12/2020 08:56, 252', 'Proof of Work': 17141, 'Hash of Previous Block': 'bcd890df5156e772c77302e23cf602e19fdd2f3a0f41ec822ab8a8cbf2a7764e'}
{'Block Index': 98, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 502750), 'Transaction Data': '17/07/2020 13:24, 359', 'Proof of Work': 3295, 'Hash of Previous Block': '83780d3b04b413d7c1f8d761cb7d2a8e004212739233cd85945b15718908c938'}
{'Block Index': 99, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 505749), 'Transaction Data': '07/10/2018 08:30, 44', 'Proof of Work': 4978, 'Hash of Previous Block': '7eaa8238080aa48a9201bef3a250f38706dca9573cb803d6e827f303e814183b'}
{'Block Index': 100, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 510958), 'Transaction Data': '19/11/2019 16:26, 114', 'Proof of Work': 11514, 'Hash of Previous Block': 'b0b45ef7687fea0cc38310d1648ae4b566ab92598b4f34776f136f54b7ce405d'}
{'Block Index': 101, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 522187), 'Transaction Data': '16/06/2020 14:51, 171', 'Proof of Work': 473, 'Hash of Previous Block': 'd43254727be46966170019e0272f988448dc07d45fec63afb0fc759625b2b5da'}
{'Block Index': 102, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 522187), 'Transaction Data': '20/09/2018 17:12, 250', 'Proof of Work': 3330, 'Hash of Previous Block': '5b3af1845eb6cf6a718119a8fd5d4b43f4ba569acd668be65f1bfdf2436e2bbc'}
{'Block Index': 103, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 525949), 'Transaction Data': '28/09/2018 17:08, 43', 'Proof of Work': 4495, 'Hash of Previous Block': '82e1d1f4c2df8d1d1a3b403d5589a7f766abab468ab077a3b8fb913ed9e3ade4'}
{'Block Index': 104, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 530475), 'Transaction Data': '04/11/2019 12:43, 107', 'Proof of Work': 1617, 'Hash of Previous Block': 'f4fb87393a21ac9c9281ce99089f6ce62c594ebcb30624b561156ad5442ab04f'}
{'Block Index': 105, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 532724), 'Transaction Data': '21/08/2020 09:14, 368', 'Proof of Work': 2900, 'Hash of Previous Block': 'e686ec3da50efbb59f33f9e789a43c7a16cf3d70273bca1620912a9cbd93efa5'}
{'Block Index': 106, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 535726), 'Transaction Data': '31/12/2019 18:52, 123', 'Proof of Work': 1235, 'Hash of Previous Block': '02193fc46149b657987c3654fc5f42f8b211fcff374d09c6f5bc5dd810a6fd66'}
{'Block Index': 107, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 536726), 'Transaction Data': '25/08/2020 07:43, 372', 'Proof of Work': 959, 'Hash of Previous Block': 'a3995ad6c06ff341a8857aef75d7c152153227094ca19d8c57bef267e09815e3'}
{'Block Index': 108, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 536726), 'Transaction Data': '05/10/2019 11:45, 295', 'Proof of Work': 7756, 'Hash of Previous Block': '954cb9445ae75d1cbf53795219f5a61d781a7f104314519304cfe3617fda89ea'}
{'Block Index': 109, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 545340), 'Transaction Data': '30/08/2018 11:11, 247', 'Proof of Work': 326, 'Hash of Previous Block': 'd36fadbb9d7f8b34d1e6590a433640595e51a745d9c1597270903647fda37f4b'}
{'Block Index': 110, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 545340), 'Transaction Data': '25/12/2019 11:20, 317', 'Proof of Work': 847, 'Hash of Previous Block': 'f80996fb083b825a3a7b5569544e63b8af6b140812ee1fa20b009c53af949a0b'}
{'Block Index': 111, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 546340), 'Transaction Data': '25/11/2019 13:05, 116', 'Proof of Work': 182, 'Hash of Previous Block': '21ec747064e9ce06b415dccadf4e08342dfc46e8412845d21d1d7ce392402982'}
{'Block Index': 112, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 547340), 'Transaction Data': '07/09/2019 03:31, 95', 'Proof of Work': 1959, 'Hash of Previous Block': 'a06677c064dcd40b739afacc034495ba7c3013cbffe7ad2a0a85fb960bd2a116'}
{'Block Index': 113, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 548340), 'Transaction Data': '28/02/2017 07:47, 302', 'Proof of Work': 8174, 'Hash of Previous Block': '19e2bde8d7c6d289f83e43d078a57025b1e87e8770c96f47b71803ed261e1f8a'}
{'Block Index': 114, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 557341), 'Transaction Data': '08/06/2017 16:01, 388', 'Proof of Work': 7668, 'Hash of Previous Block': '4b68d5f738c568597f4bd3e54d175bbbed7ce1d0043e2539f01f243239819c02'}
{'Block Index': 115, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 564426), 'Transaction Data': '28/08/2018 10:17, 36', 'Proof of Work': 150, 'Hash of Previous Block': '9661d7137268d0faf3f6ac218e16bdc8db57dd3bed6280fe4ecda508f6612d65'}
{'Block Index': 116, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 564426), 'Transaction Data': '23/06/2018 11:12, 230', 'Proof of Work': 3973, 'Hash of Previous Block': 'b79cc1beb48a048c28cc9cc0c8b70a08dfdf7d23b8d9a97aee51a25216428fe0'}
{'Block Index': 117, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 568427), 'Transaction Data': '12/07/2020 17:31, 183', 'Proof of Work': 4488, 'Hash of Previous Block': 'd1a91340ed2cc798dce6422f1e4c73dc26fbe87b1b5163ee200aa47bc7ecc2f6'}
{'Block Index': 118, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 573340), 'Transaction Data': '25/02/2020 19:21, 326', 'Proof of Work': 2339, 'Hash of Previous Block': '9d9a5a5667236b4966b18031585ad330419a5d955c9a8d1debe68e848307c81b'}
{'Block Index': 119, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 575422), 'Transaction Data': '30/06/2020 06:41, 177', 'Proof of Work': 8358, 'Hash of Previous Block': '57e82ebbd56ef6ce7802242dec785b21b62f95f9132299d1844c81d1f3d75357'}
{'Block Index': 120, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 583340), 'Transaction Data': '23/07/2018 12:35, 240', 'Proof of Work': 848, 'Hash of Previous Block': '31c4de41068810f69411437a72af404ec3c85c447499f3b0a1fe69a22ca5ce15'}
{'Block Index': 121, 'Transaction Time Stamp': datetime.datetime(2022, 12, 8, 19, 17, 14, 584340), 'Transaction Data': '11/03/2018 16:58, 16', 'Proof of Work': 103, 'Hash of Previous Block': '7b3c9f71ac1fa95b23671fc79198d8d5407159fd486abdaa9f5800142e42883f'}

 Programme Duration: 1.682161569595337 seconds   
------------------------------------------------------------------------------THANK YOU------------------------------------------------------------------------------

Process finished with exit code 0

"""
