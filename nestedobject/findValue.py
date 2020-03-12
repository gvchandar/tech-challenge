#!/usr/bin/python
import sys

def get_in(Dict_test, key_str):
  print(" Dictionary Object is: " + str(Dict_test))
  print(" Key is: " + key_str)
  splitStringArray = key_str.split('/')
  if (len(splitStringArray) != 3):
     print("Not valid key : Enter key as a/b/c or x/y/z")
     sys.exit(1)
  print(splitStringArray)
  print(Dict_test[splitStringArray[0]][splitStringArray[1]][splitStringArray[2]])

if __name__ == '__main__':
  Data = {
    'a': {
      'b': {
        'c': 'd'
      }
    },
    'x': {
      'y': {
        'z': 'a'
      }
    }
  }
  if (len(sys.argv) == 1):
     print(" Enter key for finding value in map")
     sys.exit(1)
  get_in(Data,sys.argv[1])
