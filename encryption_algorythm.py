###---Encryption Algorythm--- by Jeroen Leuenberger###
###https://github.com/Jero075/Encryption-Algorythm###

###Characters_for_encryption###
#char_str = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ'
###Hash start to identify encrypted strings
#hash_start = "$#"

###Encryption function###
def encrypt(string, hash_start, hash_length, key1, key2, char_str):
    for i in range(len(string)):
        for n in range(len(char_str)):
            if string[i] == char_str[n]:
                key1 *= n+i+key2
                break
    string_hash = str(key1)
    while len(string_hash) < int(hash_length*1.5):
        string_hash += string_hash[int(len(string_hash)/key2)]
    string_hash = hex(int(string_hash)).replace("0x", "")[:hash_length]
    return(hash_start + string_hash)