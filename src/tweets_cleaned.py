
# coding: utf-8


#Import  necessary libraries
import re
import json

# This is the function parsing a raw line in the textfile
def parse(line):
    """parse the raw tweeter JSON text to  cleaned tweets 
    
       Args: line (raw text line)
       Return:(timestamp,tweets,count)
              OR( -1 )   
    """
    json_text=json.loads(line)
    try :
        json_text['text']
    except:
        return -1                            #invalid line
    else:
        tweets=json_text['text']             #extract tweets
        timestamp=json_text['created_at']    #extract time
        try:
            tweets.encode('ascii')           #check if contain special unicode
        except:
            count=1                          
            tweets=tweets.encode('ascii','ignore')
            tweets=re.sub('\s',' ',tweets)   #replace \t\n to single whitespace  
        else:
            count=0
            tweets=tweets.encode('ascii','ignore')
            tweets=re.sub('\s',' ',tweets)   #replace \t\n to single whitespace
        
        return (timestamp,tweets,count)
    
    

#   output the cleaned tweets

f=open("./tweet_input/tweets.txt","r")

ft1=open("./tweet_output/ft1.txt","w")

unicode_count=0                          #total tweets containing special unicode
 
for line in f:                           # read line by line as if new tweets comes
    
    newline=parse(line)
    
    if  newline != -1:
        timestamp=newline[0]
        text=newline[1]
        count=newline[2]
        print text,  "(timestamp: %s )" %timestamp ,count
        ft1.write("%s (timestamp: %s)\n" %(text ,timestamp))
        
        unicode_count=unicode_count+newline[2]
        
    else:
        pass
    
print  "\n%d tweets contained  unicode."  %unicode_count  
ft1.write("\n%d tweets contained  unicode." %unicode_count)


f.close()
ft1.close()

