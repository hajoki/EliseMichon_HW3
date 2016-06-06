# !/usr/bin/python

import re, os

def words_between():
    file_path = os.path.join(os.getcwd(),"dataset.sentences")
    labelsf = open('dataset.labels', 'r+')
    
    outputf = open('dataset.words_between.csv', 'w')
    outputf.write("words\tlabel\n")
    
    with open(file_path,'r+') as sentencesf:
        for line in sentencesf:
            # Find all the words between PROTX1 and PROTX2 and vice versa
            result12=re.findall("(?<=PROTX1).*(?=PROTX2)", line)
            result21=re.findall("(?<=PROTX2).*(?=PROTX1)", line)
            # Read the label of the sentence
            label=labelsf.readline()
            # Write the words in between and the label separated by a tab
            if result12:
                outputf.write("\""+result12[0]+"\"\t"+label)
            else:
                if result21:
                    outputf.write("\""+result21[0]+"\"\t"+label)
                else:
                    outputf.write("\"\"\t"+label)
                    
    sentencesf.close()
    labelsf.close()
    outputf.close()


if __name__ == "__main__":
    words_between()