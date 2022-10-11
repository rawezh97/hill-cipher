word = input("the cipehr :")
key = "ddcf"
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

word_index = []
key_index = []

for i in word:
    if i.isalpha():
        word_index.append(alphabet.index(i))
for i in key:
    if i.isalpha():
        key_index.append(alphabet.index(i))

#print ("word_index : ",word_index)
#print ("key_index : ",key_index)

reverse_key = 0
deter_key = (key_index[0]*key_index[3]) - (key_index[1]*key_index[2])
#print(deter_key)
for rev in range(0,deter_key):
    check = (deter_key * rev)/26
    mod = (check - int(check)) * 26
    if round(mod) == 1 :
        reverse_key = rev 
#print (reverse_key)

adj_key = [key_index[3]*reverse_key,((key_index[1]*-1)+26)*reverse_key,((key_index[2]*-1)+26)*reverse_key,key_index[0]*reverse_key]
#print(adj_key)

full_key = []
for mod in adj_key:
    if mod >26 :
        num = mod/26
        mod = (num - int(num))*26
    full_key.append(round(mod))
#print("reverse_key(full) :",full_key)



partetion_of_wordIndex = [] # we must split the entier word to the 2 alphabet per list or per part
def two(paramet):
    x = 0
    y = 2
    index_length = len(paramet)
    if index_length % 2 == 0 :   # if this stattment be ture then taht men it is even else it is be odd
        z = index_length/2
        for part in range(0,int(z)):                               #chonyate lekdanaka
            partetion_of_wordIndex.append(paramet[x:y])         #[------>]    [ bo xwarawa]
            encodeing(full_key, partetion_of_wordIndex[part])  #[ 2   3 ]    [ 4 ]
            x += 2                                              #[ 55 24 ]    [ 5 ]
            y += 2                                              # wata [2*4 + 3*5]
        print("word_index_two :",partetion_of_wordIndex)        # wata [55*4 + 24*5]
    else :
        print("you need extra latter")

altire_word = []
def encodeing(list1,list2):
    keyword = list1
    latter = list2
    w = list1[0] * list2[0]
    g = list1[1] * list2[1]
    if (w+g)>26:
        new_latter = (w+g)/26
    else:
        new_latter = (w+g)
    first = round((new_latter - int(new_latter)) *26) 
    hg = list1[2] * list2[0]
    hj = list1[3] * list2[1]
    if (hg+hj)>26:
        new_latter2 = (hg+hj)/26
    else:
        new_latter2 = (hg+hj)
    secound = round((new_latter2 - int(new_latter2)) *26)
    #print(first)
    #print(alphabet[first])
    altire_word.append(alphabet[first])
    altire_word.append(alphabet[secound])
    #print(secound)
    #print(alphabet[secound])

two(word_index)
print("the plain text : " , end="") 
for i in altire_word:
    print(i , end="")
print("")


st = "abcdefg"
h = ' '.join(format(ord(x), 'b') for x in st)
print(h)



binary = ['1100001','1100010','1100011']

def BinaryToDecimal(binary):
     
    # Using int function to convert to
    # string  
    string = int(binary, 2)
     
    return string
for h in binary:
         
    # Driver's code
    # initializing binary data
    bin_data =h
    
    # print binary data
    print("The binary value is:", bin_data)
    
    # initializing a empty string for
    # storing the string data
    str_data =' '
    
    # slicing the input and converting it
    # in decimal and then converting it in string
    for i in range(0, len(bin_data), 7):
         
        # slicing the bin_data from index range [0, 6]
        # and storing it in temp_data
        temp_data = bin_data[i:i + 7]
          
        # passing temp_data in BinarytoDecimal() function
        # to get decimal value of corresponding temp_data
        decimal_data = BinaryToDecimal(temp_data)
          
        # Decoding the decimal value returned by
        # BinarytoDecimal() function, using chr()
        # function which return the string corresponding
        # character for given ASCII value, and store it
        # in str_data
        str_data = str_data + chr(decimal_data)
    
    # printing the result
    print("The Binary value after string conversion is:",
           str_data)