# Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

def hello_name(name):
  return "Hello " + name + "!'"


# Given two strings, a and b, return the result of putting them together in the 
# order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".

def make_abba(a, b):
  return a + b + b + a


# The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text.
# In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given 
# tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".

def make_tags(tag, word):
  return "<" + tag + ">" + word + "</" + tag + ">" 


# Given an "out" string length 4, such as "<<>>", and a word, return a new string where the 
# word is in the middle of the out string, e.g. "<<word>>". 

def make_out_word(out, word):
  beg = out[0:2] 
  end = out[2:4]
  
  return beg + word + end


# Given a string, return a new string made of 3 copies of the last 2 chars of the original 
# string. The string length will be at least 2.

def extra_end(str):
  return 3*(str[-2:])


# Given a string, return the string made of its first two chars, so the String "Hello" yields "He".
# If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the 
# empty string "" yields the empty string "". 

def first_two(str):
  if len(str) < 2:
    return str
  else:
    return str[0:2]
  
  
# Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

def first_half(str):
   return str[0:len(str)/2]
 

# Given a string, return a version without the first and last char, so "Hello" yields "ell". 
# The string length will be at least 2.

def without_end(str):
  return str[1:-1]


# Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string 
# on the outside and the longer string on the inside. The strings will not be the same length, but 
# they may be empty (length 0).

def combo_string(a, b):
  if len(a) > len(b):
    return b + a + b
  else:
    return a + b + a
  
  
# Given 2 strings, return their concatenation, except omit the first char of each. The strings
# will be at least length 1.

def non_start(a, b):
 return a[1:] + b[1:]


# Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The
# string length will be at least 2.

def left2(str):
  return str[2:] + str[0:2]





  
