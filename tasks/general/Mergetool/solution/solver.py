#!/usr/bin/env python3
import hashlib
import string
import re


if __name__ == "__main__":
  dictionary = dict()
  alphabet = string.ascii_lowercase + string.digits + "_{}"

  flag = ""

  for char in alphabet:
    dictionary[hashlib.sha1(char.encode()).hexdigest()] = char

  with open("flag.txt", 'r') as file:
    for line in file:
      lst = re.split("\W+", line)
      for word in lst:
        try:
          int(word, 16)
          flag += dictionary[word]
        except:
          pass

  print(flag)