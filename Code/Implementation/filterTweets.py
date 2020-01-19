import requests
from bs4 import BeautifulSoup
import sys
import pandas as pd
import csv
reload(sys)
sys.setdefaultencoding('utf8')
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen


def writeToCsvFile(dic):
    #dic = #your dictionnary
    # Creating your dataframe from your dictionnary
    # for k,v in dic:
    #     print('dictionary ',v[],k[0])
    print(dic)
    df = pd.DataFrame(dic, columns=['tweetId', 'tweetText'])
    print(df)
    # Store the data into a csv file
    df.to_csv('your_path.csv', sep=',',encoding='utf-8') # indicate the path where to store the csv file

def getTweetById(tweetId):
    all_tweets = []
    url = 'https://twitter.com/web/status/'+ tweetId #1194883952231768064
    print(url)
    data = requests.get(url)
    # print(data)
    html = BeautifulSoup(data.text, 'html.parser')
    
    timeline = html.select('.permalink-tweet-container')
    if(len(html.select('span.ProfileHeaderCard-locationText') ) > 0):
        locationHtml =  html.select('span.ProfileHeaderCard-locationText')[0].get_text().encode("utf-8")
    else:
        locationHtml = ''

    # if(timeline== None or len(timeline) == 0):
    #     with open(r'tweetsData.csv', 'a') as csvfile:
    #         fieldnames = ['id','text']
    #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #         writer.writerow({"id": tweetId, "text": ''})
     
    for tweet in timeline:
        # print(tweet)
        tweet_id = tweet.select('div.tweet')[0]['data-tweet-id']
        tweet_text = ''
        tweet_profileLocation=''
        if(tweet.select('p.TweetTextSize')[0] !=None):
            tweet_text = tweet.select('p.TweetTextSize')[0].get_text()
        else:
            if(tweet.select('div.QuoteTweet-text')[0] !=None):
                tweet_text += tweet.select('div.QuoteTweet-text')[0].get_text()
            # print('do nothing',tweet_id)
        tweet_profileLocation = locationHtml.replace('# ', '#').replace('@ ', '@').replace('\n', ' ').replace('"', '').strip()
        print(tweet_profileLocation)
        tweet_date = tweet.select('span.metadata')[0].get_text().replace('# ', '#').replace('@ ', '@').replace('\n', ' ')
        # try:
        #     tweet_text += tweet.select('div.QuoteTweet-text')[0].get_text()
        # except:
        #     print(tweet.select('div.QuoteTweet-text'))
        #     print('do nothing',tweet_id)
        # all_tweets.append({"id": tweet_id, "text": tweet_text.replace('# ', '#').replace('@ ', '@').replace('\n', ' ')})
        all_tweets.append( {"id": tweet_id, "text": tweet_text.replace('# ', '#').replace('@ ', '@').replace('\n', ' ')})

        # print(tweet_text) 
        # print(all_tweets)
        

        with open(r'tweetsData.csv', 'a') as csvfile:
            fieldnames = ['id','location','date','text']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({"id": tweet_id,'location':tweet_profileLocation.encode('utf8'),'date':tweet_date ,"text": tweet_text.replace('# ', '#').replace('@ ', '@').replace('\n', ' ')})
          

def main():
    print("python main function")
    with open('lasvegas-output-ids.txt') as f:
        content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content] 
    # print(content)
    # count = 0
    
    # getTweetById('914965004885078016')
    for id in content:
        # count = count+1
        getTweetById(id)
        # if(count==10):
        #     break

    # contents = urlopen("https://twitter.com/web/status/1122752459770929153").read()
    # print(contents)

    

if __name__ == '__main__':
    main()




