
# coding: utf-8



#Import the necessary libraries
import re

# This is the function parsing  a raw line in the textfile
def parse(line):
    """parse the raw tweeter JSON text to  cleaned tweets 
    
       Args:raw text line 
       Return:(clean tweets , timestamp,containing other unicode) OR -1 when line is invalid
       
    """
    pattern='^(.*)created_at":"(.*)","id"(.*)"text":"(.*)","source"(.*)'
    match=re.search(pattern,line)
    if match is None:
        pass 
        return -1                             # remove datafileline
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
    if strascii==str:                                     #remove other unicode   
        count=0
    else:
        count=1
        
    strascii=re.sub('\s',' ',strascii)        # replace /n/t.etc to single whitespace
    strclean=strascii.replace('\\','')        # remove '\'
    return strclean, count 




#import necessary libraries
import datetime
import itertools 

month_map = {'Jan': 1, 'Feb': 2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7,
    'Aug':8,  'Sep': 9, 'Oct':10, 'Nov': 11, 'Dec': 12}

#This is the function to transfer the str format to python datetime format
def parse_tweet_time(s):
    """ Convert JSON time format into python datetime object,ignore time zone
    
    Args:
        s(str):date and time in JSON format
    Returns:
        datetime :datetime object 
    """
    return datetime.datetime(int(s[26:30]),
                             month_map[s[4:7]],
                             int(s[8:10]),
                             int(s[11:13]),
                             int(s[14:16]),
                             int(s[17:19]))

#This is the function to parse the tweet string lines and collect hashtags

def extract_hashtag(line):
    """Find hashtags in tweets
    Args:line(string)
         tweets including hashtags
    Return:hashtags(list)
          all hashtags in one tweet 
         
    """
    
    hashtags=re.findall(r"#(\w+)",line) #match (#hashtags,include underscore)
    hashtags=list(set(hashtags))
    
    return hashtags


def parse_hashtags(line):
    """Find hashtags from the raw JSON text
    Args:line(str)
         raw JSON text
    Return:(hashtag(list),timestamp(python date.time))   
         hashtags and datetime in one raw JSON text
    
    """
    
    parsed_line=parse(line)
    
    if parsed_line!= -1:
        text=parsed_line[1]
        timestamp=parsed_line[0]
        timestamp=parse_tweet_time(timestamp)
        hashtags=list(extract_hashtag(text))
        hashtags=set(map(lambda x:x.lower(),hashtags))  #eg.Spark is the same as spark
        hashtags=list(hashtags)
        hashtagtime=(hashtags,timestamp)
        
        if len(hashtags)>1:              # if there is no hashtags or ONE hashtag, do not creat 
                                         # node , just return empty node and timestamp      
            return hashtagtime
        else:
            return (list(),timestamp)
            
        
    else:
        pass                 # ignore the invalid line 
                          #print 'Invalid datafile line: %s' % parsed_line[1]
        return -1
    
    

# This function is to calculate the average degree of a vertex in a Twitter hashtag graph for the last 60 seconds

def timewindow(hashtag_stack,h,t):
    """ filter the timewindow hashtags in hashtag_stack
    
    Args:
         hashtag_stack is the history hashtag_stack
         a is the current hashtag
         t is the timewindow 
    Returns: 
          average degree of the current time
    """   
    totaltags=list() #total hashtags in the timewindow
    totaledges=list() #total edges in the timewindow
    
    newlist=filter(lambda x:               #filter out the hashtags inside the timewindow t
                   (h[1]-x[1]).total_seconds()<=t 
                   and (h[1]-x[1]).total_seconds()>=0 ,hashtag_stack)
    
    #total_tags is the collection of all tags
    hashtag_list=list(map(lambda x:x[0],newlist))  
    total_tags=set(reduce(lambda x,y:x+y,hashtag_list))
    
    #total_edges is the collection of all edges
    hashtag_edge_sets=list(map(lambda x:list(itertools.permutations(x[0],2)),newlist))
    total_edges=set(reduce(lambda x,y:x+y,hashtag_edge_sets))
    
    if len(total_tags)!=0:
        averagedegree=float(len(total_edges))/float(len(total_tags))
        averagedegree=round(averagedegree,2)
    
    else:
        averagedegree=0  # if there is no hashtags,I assume degree is 0
        
    return averagedegree
        
    
    
    
       
 
  # output the edges graph
    
import sys
import os
inputpath=os.getcwd()
input_path=os.path.join('tweet_input','tweets.txt')
output_path1=os.path.join('tweet_output','ft1.txt')
output_path2=os.path.join('tweet_output','ft2.txt')    
f=open(input_path,"r")
ft2=open(output_path2,"w")
hashtag_stack=list()
degreelist=list()
t=60
i=0

print  "feature 2 , processing...\n"
for line in f:
    newhashtags=parse_hashtags(line)
    i=i+1
    if newhashtags!=-1 :
        
        hashtag_stack.append(newhashtags)
        
        averagedegree=timewindow(hashtag_stack,newhashtags,t)
        degreelist.append(averagedegree)
        
        #print  ("line:%d"%i,"%.2f"%averagedegree),newhashtags
        ft2.write("%.2f\n" %averagedegree)
        
        
    else:
        pass
    
    
print "finished\n"

f.close()
ft2.close()

