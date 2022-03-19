
########A PART########################
def read_line(n,text):
    #chack if the text arggument exist
    try:
        open(text)
    except:
        return "file not found" 
    #chack if n is not a int or=0 we dont have line zero
    if isinstance(n, int) ==False or n==0:
        return "invalid input detected"
    with open(text) as f:
        new_text=f.readlines()
    #if the line=n smaller then len of the line of "text" return doesn't exist 
        if len(new_text)<n:
            return "line "+ str(n) +" doesn't exist"
    return new_text[n-1] 
########B PART########################
from collections import Counter
def method_name(file):
    #chack if the file arggument exist
    try:
        open(file)
    except:
        #printing "file not found"
        print("file not found")
        listt=[]
        #and return empty list 
        return listt
    with open(file) as f:
      temp = f.read()
      text=""
      #incert the letters in the now string call "text"
      for let in temp:
        if let.isalpha() or let.isdecimal():
          text += let
        else:
          text += " "
    #list of the words in the text, creating a new dictionery "words_dict" 
    arr = text.split()
    words_dict =dict()
    #run over the arr list we created and put the value in the dictionery  
    for word in arr:
      if word not in words_dict.keys():
        words_dict[word] = len(word)
    c = Counter(words_dict)
    most_common = c.most_common(5)  # returns top 5 pairs
    #getting the keys from `most_common`:
    my_keys = [key for key, val in most_common]
    #`my_keys` holds the value of the longest words the function return text list of strings

    return(my_keys)
