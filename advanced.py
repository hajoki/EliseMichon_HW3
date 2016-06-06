# !/usr/bin/python

import re, os
from nltk.parse.stanford import StanfordParser

# method that we could not make work yet
def dependencies():
    #english_parser = StanfordParser('stanford-parser.jar', 'stanford-parser-3.6.0-models.jar')
    #english_parser.raw_parse_sents(("this is the english parser test", "the parser is from stanford parser"))                         
    parser = StanfordParser(model_path="C:\Python27\stanford-parser-full-2015-12-09\stanford-parser-3.6.0-models.jar")
    sentences = parser.raw_parse_sents(("IBlood B cells secrete PROTX1  ( s )   upon stimulation via the PROTX2.", "Furthermore ,  blocking PROTX0 or PROTX0 had no effect on the levels of PROTX2 released in response to the anti -  PROTX1 mAb."))
    print sentences

    # GUI
    for line in sentences:
        for sentence in line:
            sentence.draw()
            

def interaction_words():
    file_path = os.path.join(os.getcwd(),"dataset.sentences")
    labelsf = open('dataset.labels', 'r+')
    with open('int-keywords.txt','r+') as interactionf:
        word_list = [line.rstrip('\n') for line in interactionf]
    word_set=set(word_list)
    
    outputf = open('dataset.interaction_words.csv', 'w')
    outputf.write("words\tinteraction_word\tlabel\n")
    
    with open(file_path,'r+') as sentencesf:
        for line in sentencesf:
            # Read the label of the sentence
            label=labelsf.readline()
            
            # Find all the words between PROTX1 and PROTX2 and vice versa
            result12=re.findall("(?<=PROTX1).*(?=PROTX2)", line)
            result21=re.findall("(?<=PROTX2).*(?=PROTX1)", line)
            if result12:
                result = result12
            else:
                if result21:
                    result = result21
            
            if result:
                # Find the interaction word between PROTX1 and PROTX2 and vice versa
                phrase_set = set(result[0].split())
                inter = word_set.intersection(phrase_set)
                if inter:
                    interaction = list(inter)[0]
                else:
                    interaction = ""
                # Write the words in between, the first interaction word between, and the label separated by a tab
                outputf.write("\""+result[0]+"\"\t\""+interaction+"\"\t"+label)
            else:
                outputf.write("\"\"\t\"\"\t"+label)
                    
    sentencesf.close()
    labelsf.close()
    outputf.close()

if __name__ == "__main__":
    interaction_words()
