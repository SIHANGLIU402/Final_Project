#!/usr/bin/env python
# coding: utf-8

# In[17]:


import string
#using defaultdict
from collections import defaultdict

class Project:
    def __init__(self, dic, inp):
        self.dic = dic
        self.inp = inp

    #opening file
    def open_file():
        while True:
            try:
                f = open(input("Input file name here: "), "r")
            except FileNotFoundError:
                print("file not found, please try again")
            else:
                print("file exists")
                return f
                break

    def read_data(self):
        ls = []
        self.dic = defaultdict(set)
        ctr = 0
        while True:
            # implementing line number in ctr
            ctr += 1
            data = f.readline()
            # EOF reached
            if len(data) == 0:
                break
            # translating to lower
            data = data.lower()
            # removing punctuations and apostrophes
            data = data.translate(str.maketrans('', '', string.punctuation))
            # storing words in a list
            ls = data.split(" ")
            # using defaultdict as set, that's why using add method
            for w in ls:
                self.dic[w].add(ctr)
        return dict(self.dic)


    def find_cooccurrence(self):
        #read input into words seperated by spaces
        input_word = self.inp.split(' ')
        result = set()
        print('The co-occurance for: '+', '.join(input_word))
        #interating through the input words
        for i in input_word:
            #change all input into lower cases and remove all punctuation
            i = i.lower()
            i = i.translate(str.maketrans('', '', string.punctuation))
            #print None if the input is empty
            if not self.inp:
                print('Lines: None.')
            #print None if the input is not in the dictionary
            elif i not in self.dic:
                print ('Line: None.')
                return
            #find the occurance of input words and store into a data set
            else:
                if len(result) == 0:
                    result.update(self.dic[i])
                else:
                    result.intersection_update(self.dic[i])
        print ('Lines:',', '.join(str(lnum) for lnum in result))

def main():
    f = Project.open_file()
    dic = Project.read_data(f)
    inp = ''
    #This will keep iterate until q is entered
    while True:
        inp = input('Enter space-separated words: ')
        if inp=='q':
            break
        Project.find_cooccurrence(dic, inp)
    

if __name__ == '__main__':
    main()


# In[12]:




