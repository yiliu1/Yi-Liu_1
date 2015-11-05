
# coding: utf-8

# In[ ]:

#Import the necessary libraries
import re
import sys
import os

# This is the function parsing a raw line in the textfile
def parse(line):
    """parse the raw tweeter JSON text to cleaned tweets 
    
       Args: line(str)
       Return:(clean tweets , timestamp,containing other unicode) 
               OR -1 when line is invalid
       
    """
    pattern='^(.*)created_at":"(.*)","id"(.*)"text":"(.*)","source"(.*)'
    match=re.search(pattern,line)
    if match is None:
        pass 
        return -1                                       # remove datafileline
    else:
        timestamp=match.group(2)
        text=match.group(4)
        cleantext=cleanunicode(text)
        text=cleantext[0]
        count=cleantext[1]
        return timestamp,text,count
    
# This is the function to clean the unicode and remove escape character   
def cleanunicode(str):
    """clean tweets text to replace escape characte and remove special unicode
    
       Args:tweets text string
       Return clean tweets string
    """
    strascii=str.decode('unicode_escape').encode('ascii','ignore')
                                                      # leave all ASCII Unicode characters
    if strascii==str:                                 #remove other unicode   
        count=0
    else:
        count=1
        
    strascii=re.sub('\s',' ',strascii)                 # replace /n/t.etc to single whitespace
    strclean=strascii.replace('\\','')                 # remove '\'
    return strclean, count 



# output the cleaned tweets

inputpath=os.getcwd()
input_path=os.path.join('tweet_input','tweets.txt')
output_path1=os.path.join('tweet_output','ft1.txt')
output_path2=os.path.join('tweet_output','ft2.txt')
f=open(input_path,"r")

ft1=open(output_path1,"w")

unicode_count=0

for line in f:
    
    newline=parse(line)
    
    if  newline != -1:
        timestamp=newline[0]
        text=newline[1]
        print text,  "(timestamp: %s )" %timestamp
        ft1.write("%s (timestamp: %s)\n" %(text ,timestamp))
        
        unicode_count=unicode_count+newline[2]
        
    else:
        pass
    
print  "\n%d tweets contained  unicode."  %unicode_count  
ft1.write("\n%d tweets contained  unicode." %unicode_count)


f.close()
ft1.close()

