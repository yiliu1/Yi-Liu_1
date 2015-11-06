
# Insightdata code challenge 

For this coding challenge, I developed it in python 2.7 on my macbook pro.
I wtrie all the codes in python and tested it on my macbook. I hope you enjoy reading my code as much as I enjoyed writing it.
If needed, you can reach me at yiliu1.ubc@gmail.com.

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

To run the program, clone it and run `run.sh`.
Current directory should be `../codingmonkey`.Then Use `bash run.sh` or `./run.sh` to run the script.
For example ,my current directory is` /Users/yi/codingmonkey`,then in the `Terminal`, I run `bash run.sh`.

The output files are `ft1.txt` and `ft2.txt` in `tweet_output` directory.
And name of input file in `tweet_input` would be `tweets.txt`

# Implementation details

##### Feature 1

Clean and extract the text from the raw JSON tweets that come from the Twitter Streaming API, and track the number of tweets that contain unicode.

After running the `run.sh`script, cleaned tweets will be in `tweet_output/ft1.txt`.
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
When running the program,I show the entire process .
For example you can see lines like:

```
Yall stay safe my ATX peeps!! (timestamp: Fri Oct 30 15:30:22 +0000 2015 ) 0
(timestamp: Fri Oct 30 15:30:22 +0000 2015 ) 1

915 tweets contained  unicode.
feature 2 , processing...

('line:1', '2.00') ([u'news', u'trump', u'election'], datetime.datetime(2015, 10, 30, 15, 29, 44))
('line:2', '2.00') ([], datetime.datetime(2015, 10, 30, 15, 29, 44))
...
...
('line:1987', '3.66') ([u'austin', u'atxtraffic'], datetime.datetime(2015, 10, 30, 15, 30, 22))
('line:1988', '3.66') ([], datetime.datetime(2015, 10, 30, 15, 30, 22))
('line:1989', '3.66') ([], datetime.datetime(2015, 10, 30, 15, 30, 22))
('line:1990', '3.66') ([], datetime.datetime(2015, 10, 30, 15, 30, 22))
feature 2  finished
```

### Thank you for reviewing 

