# Given a string, return a string where for every char in the original, there are 
# two chars.

def double_char(str):
  x = ""
  for i in range(len(str)):
    x = x + 2*str[i]
  return x


# Return the number of times that the string "hi" appears anywhere in the given string.

def count_hi(str):
  count = 0
  for i in range(len(str)-1):
    if str[i] == 'h' and str[i+1] == 'i':
      count += 1
  return count
  

# Return True if the string "cat" and "dog" appear the same number of times in the given
# string.

def cat_dog(str):
  count_cat = 0
  count_dog = 0

  for i in range(len(str)-2):
      if str[i:i+3] == 'cat':
          count_cat += 1
          
  for i in range(len(str)-2):
      if str[i:i+3] == 'dog':
          count_dog += 1

  return count_cat == count_dog
  
  
