# Encryption-Algorythm

!!!DO NOT use this algorythm to encrypt passwords for public projects as I am not an expert in this field!!!

An algorythym to encrypt a string of any length.

Parameters:
  - string = The string that you want to encrypt
  - key1 = Any integer value >= 1
  - key2 = Any integer value >= 2
  - char_str = The characters that should be used to encrypt the string; Any string
  - hash_start = A String that will be put in front of the hash to identify the hash (optional); Default: ""
  - hash_length = The length of the the hash (optional); Default: 128 / Any integer value >= 1 (I would recommend at least 32)

Syntax:
  encrypt(string, key1, key2, char_str, hash_start, hash_length)
