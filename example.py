
from encryption_algorythm import encrypt

hash_start = "$#"
char_str = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ'
hash_length = 52
key1 = 1
key2 = 2

string = input("Encrypt: ")

print(encrypt(string, key1, key2, char_str, hash_start, hash_length))
