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
首先是從twitter上申請一個api

而我將keyword設定 “k” "b"

設定兩個keyword搜尋的資料量也比較多比較快一點

本來輸入較為稀少的英文字

則搜尋的時間就增加很多

###3. Method

#### Getting Twitter API first

1. 申請Twitter帳號
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

##### 以下是config的內容 
下面各個“ ” 則是輸入自己申請到的api

分別將他們個個輸入即可




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
		
		keywords => [" "] // 輸入你要的keyword
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