import hashlib

word = input("Enter the word :")
key = "ddcf"
print ("the key :",key)
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","#"]

word_index = []
key_index = []

for i in word :
    if i.isalpha():
        word_index.append(alphabet.index(i))
for k in key:
    if k.isalpha():
        key_index.append(alphabet.index(k))

print("word_index :" ,word_index)
print("key index :"+ str(key_index))

partetion_of_wordIndex = [] # we must split the entier word to the 2 alphabet per list or per part
def two(paramet):
    x = 0
    y = 2                                   #variable = [[2,3],]
    index_length = len(paramet)
    if index_length % 2 == 0 :   # if this stattment be ture then taht men it is even else it is be odd
        z = index_length/2
        for part in range(0,int(z)):                               #chonyate lekdanaka
            partetion_of_wordIndex.append(paramet[x:y])         #[------>]    [ bo xwarawa]
            encodeing(key_index, partetion_of_wordIndex[part])  #[ 2   3 ]    [ 4 ]
            x += 2                                              #[ 55 24 ]    [ 5 ]
            y += 2                                              # wata [2*4 + 3*5]
        #print("word_index_two :",partetion_of_wordIndex)        # wata [55*4 + 24*5]
    else :
        paramet.append(0)
        index_length = len(paramet)
        z = index_length/2
        for part in range(0,int(z)):                               #chonyate lekdanaka
            partetion_of_wordIndex.append(paramet[x:y])         #[------>]    [ bo xwarawa]
            encodeing(key_index, partetion_of_wordIndex[part])  #[ 2   3 ]    [ 4 ]
            x += 2                                              #[ 55 24 ]    [ 5 ]
            y += 2                                              # wata [2*4 + 3*5]
        #print("word_index_two :",partetion_of_wordIndex)        # wata [55*4 + 24*5]

altire_word = []
def encodeing(list1,list2):
    keyword = list1
    latter = list2
    w = list1[0] * list2[0]
    g = list1[1] * list2[1]
    if (w+g)>26:
        new_latter = (w+g)/26
        new_latter = round((new_latter - int(new_latter)) *26) 
    else:
        new_latter = (w+g)

    hg = list1[2] * list2[0]
    hj = list1[3] * list2[1]
    if (hg+hj)>26:
        new_latter2 = (hg+hj)/26
        new_latter2 = round((new_latter2 - int(new_latter2)) *26)
    else:
        new_latter2 = (hg+hj)

    #print(first)
    #print(alphabet[first])
    altire_word.append(alphabet[new_latter])
    altire_word.append(alphabet[new_latter2])
    #print(secound)
    #print(alphabet[secound])
    

two(word_index)
#print(altire_word)
print("\nthe cipher text :",end="")
for i in altire_word:
    print(i , end="")
print("\n")

st = "abcdefg"
h = '\n'.join(format(ord(x), 'b') for x in st)
print(h)
hh = h.split("\n")
for i in hh:
    g = hashlib.sha224(f"{i}".encode('utf-8')).hexdigest()
    print (g)









#gg
