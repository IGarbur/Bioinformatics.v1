words = ["lint","cod","programming"]

def encode(words):
    one_word =""
    for i in range(len(words)):
        one_word+=str(len(words[i]))
        one_word+="#"
        one_word+=words[i]
    return one_word
''' The major problem with this is that what if the length og your word is >9
    So the whole idea is that we have to collect a whole number from starting index to # (aka while loop)
def decode(one_word):
    words = []
    index_of_length = 0
    while index_of_length < len(one_word):
        number = int(one_word[index_of_length])
        word = one_word[index_of_length+2:index_of_length+2+number]
        words.append(word)
        index_of_length = index_of_length+2+number
    return words
    '''
def decode(one_word):
    words = []
    index_of_length = 0
    while index_of_length < len(one_word):
        index = index_of_length
        number = ""
        while one_word[index]!="#" and index<len(one_word):
            number+=one_word[index]
            index+=1
        number = int(number)
        #think about an instance where you have one single digit word and one double-digit word when slising
        word = one_word[index+1 : index+1+number]
        words.append(word)
        index_of_length = index+1+number
    return words

cypher = encode(words)
print(cypher)
decyphered = decode(cypher)
print(decyphered)