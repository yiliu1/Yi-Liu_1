
# Insightdata code challenge 

For this coding challenge ,I developed it in python 2.7 on my macbook pro .
I wtrie all the codes in python and tested it on my macbook.
My email :yiliu1.ubc@gmail.com

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

To run the program ,clone it and run `run.sh`.
Current directory should be `../codingmonkey`.Use `bash run.sh` or `./run.sh` to run the script. Read input from `tweet_input/tweets.txt` and write output to `tweet_output/ft1.txt`and `tweet_output/ft2.txt`.
In the `tweet_input`,there is an example file `tweets.txt`  that I put there.

# Implementation details

##### Feature 1

Clean and extract the text from the raw JSON tweets that come from the Twitter Streaming API, and track the number of tweets that contain unicode.

After running the `run.sh`script , cleaned tweets will be in `tweet_output/ft1.txt`.
Final results example :
```
......
......
I can't go back to sleep (timestamp: Fri Oct 30 15:32:56 +0000 2015)
@06Goriosi  (timestamp: Fri Oct 30 15:32:56 +0000 2015)
com as notas destes testes vou trabalhar para o mcdonalds (timestamp: Fri Oct 30 15:32:56 +0000 2015)
@esraahesham55      (timestamp: Fri Oct 30 15:32:56 +0000 2015)

4601 tweets contained  unicode.

```


##### Feature 2
Calculate the average degree of a vertex in a Twitter hashtag graph for the last 60 seconds, and update this each time a new tweet appears.

After running `run.sh`,there will be a file `ft2.txt` in `tweet_output`.
Final Results example :

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

# Note:
when running the `run.sh`,I print out the whole process .

### Thank you for reviewing 

