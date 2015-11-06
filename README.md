
# Insightdata code challenge 

For this coding challenge ,I developed it in python 2.7 on my macbook pro .
I wtrie all the codes in python and tested it on my macbook.

## Repo directory structure
Repo directory structure as following 

	├── README.md  
	├── run.sh  
	├── src  
	│   ├── average_degree.py  
	│   └── tweets_cleaned.py  
	├── tweet_input  
	│   └── tweets.txt  
	└── tweet_output  
	    ├── ft1.txt  
	    └── ft2.txt  

Read input from `tweet_input/tweets.txt` and write output to `tweet_output/ft1.txt`and `tweet_output/ft2.txt`.To run the program ,clone it and run `run.sh` . Use `bash run.sh` or `./run.sh`.

# Implementation details

##### Feature 1

Clean and extract the text from the raw JSON tweets that come from the Twitter Streaming API, and track the number of tweets that contain unicode.

For this part ,I used Regular expression operations to clean the raw text file .So `import re` is included.
After running the `run.sh`script , cleaned tweets will be in `tweet_output/ft1.txt`.
Final results example :
```
......
......
I can't go back to sleep (timestamp: Fri Oct 30 15:32:56 +0000 2015)
@06Goriosi  (timestamp: Fri Oct 30 15:32:56 +0000 2015)
com as notas destes testes vou trabalhar para o mcdonalds (timestamp: Fri Oct 30 15:32:56 +0000 2015)
@esraahesham55      (timestamp: Fri Oct 30 15:32:56 +0000 2015)

4949 tweets contained  unicode.

```


##### Feature 2
Calculate the average degree of a vertex in a Twitter hashtag graph for the last 60 seconds, and update this each time a new tweet appears.

In feature 2 , I used the cleaned tweets from feature 1 to extract hashtags .As the new tweet comes , it caculate the hashtags graph in the last 60 seconds .
After running `run.sh`,there will be a file `ft2.txt` in `tweet_output`.
In the file , data is like following :
```
...
...
4.80
4.17
4.17
3.71
3.71
3.71
```


```python

```
