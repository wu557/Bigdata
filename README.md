# Assignment1_data collection and presistence



## Contents


####* Data Format
####* Data Source
####* Method

###1. Data Format
JSON based format

Our target is transforming the data to JSON format.

In the code box is a sample for JSON format.

```
"data": 
    {
      "date": "2014-09-13",
      "name": "Mary Jones",
      "tweet": "Elasticsearch means full text search has never been so easy",
      "user_id": 2
    },

```

###2. Data Source
All my data is captured form twitter website

and used Elasticesearch and Logstash

###3. Method

#### Getting Twitter API first

1. 申請Twitter帳號
2. 到此網址申請API
3. Get Twitter API


#### Download the elasticsearch

Elasticsearch

可用來做全文搜尋，跨機氣叢集倉儲，內建HA

此次用法是拿來做搜尋


1. Go to Elasticsearch website to dowmload the execution file
2. Choose the Elasticsearch-2.2.1
3. Install it first.

Elasticsearch Website


<https://www.elastic.co/downloads/elasticsearch>



#### Download the logstash 

Logstash

資料解析與傳送，可接收多種來源資訊

大部份提供42種較為常見的資料處理方式



1. Go to Logstash website to dowmload the execution file
2. choose the Logstash-2.2.2
3. Install it .

Logstash Website


<https://www.elastic.co/downloads/logstash>


#### code 
- consumer_key => " 輸入你申請的key "  
- consumer_secret => "  "
- oauth_token => "  "
- oauth_token_secret => "  "
- keywords => [" 輸入你想要search的keywords"]

```
input{
	twitter{
		consumer_key => "  "
		consumer_secret => "  "
		oauth_token => "  "
		oauth_token_secret => "  "
		
		keywords => [" "]
		full_tweet => true
	}

}
output{
	elasticsearch{
		index => "twitter"
	}
	file{
		codec=>"json_lines"
		path =>["~/Documents/data.json"]
	}
}
```
#### code_output
直接將抓到的資料轉成json檔


將檔案寫在Documents


可自己決定要寫在哪。

- path=>[""].

```
file{
		codec=>"json_lines"
		path =>["~/Documents/data.json"]
	}
```