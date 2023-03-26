list = [1,2,3,'one','two','three']            #defining a list
no_1 = 3
no_2 = 2
dict = {'name':'Ansh', 'enroll no.':'101CTBMCS2122007', 'course':'Btech', 'age':'20'}    #defining dictionary

for k in dict.keys():
    print(k)                              #printing keys

print('---------------------------------')
for v in dict.values():
    print(v)                    #printing values

print('---------------------------------')
for k,v in dict.items():
    print(k,':',v)                        #printing key-value pairs

print('---------------------------------')
print("length of dictionary is:",len(dict))

print('---------------------------------')
print(no_1 ** no_2)                   
print('---------------------------------')
for i in list:
    print(i)                    #printing contents of list

