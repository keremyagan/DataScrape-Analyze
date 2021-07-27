# Note
-To download Tesseract : https://github.com/UB-Mannheim/tesseract/wiki 
-After download it , add Turkish language packet when setup processing
-To reach latest selenium version , visit https://chromedriver.chromium.org/downloads

### Features

- Gets Instagram and Twitter Hashtags
- Gets Text from An Image in Post
- Analyzes Text Using Some NLTK Tools
- Saves data in Csv/Excel/Txt formats
- Don't Need to Login Instagram/Twitter Account to Scraping


# DataScrape-Analyze

![](https://camo.githubusercontent.com/38f5db5524ba43e7262dfbca1f7d3631ba127fb1596785dfd707d5fc671821c9/687474703a2f2f466f7254686542616467652e636f6d2f696d616765732f6261646765732f6d6164652d776974682d707974686f6e2e737667) 


# Instagram Scraper
It uses [InstaScrape](https://github.com/chris-greening/instascrape "InstaScrape") Library to scan hashtags. Need to create an instance to use InstagramScraper class. 
```python
from instagramscraper import InstagramHashtag
instagram=InstagramHashtag(hashtag_name,hashtag_amount)
```
 
## Get Instagram Hashtags as a list in a tuple
```python
data=instagram.hashtag_result()
```
This code returns a list in a tuple. List elements contains:
-Caption 
-Shortcode 
-Post URL
-Post Time (time to shared)
-Display Url
-Owner Id
-Is Video (Returns True/False)
-Caption2 
-Image Text (Returns If there is image , else returns "Video")
## Get Instagram Hashtags as a dictionary in a tuple
```python
data=instagram.to_dict()
```
It returns same result with hashtag_result . Difference is this function returns data as a dictionary in a tuple.
## Get Instagram Hashtags Using Property Feautures
```python
instagram=InstagramHashtag(hashtag_name,hashtag_amount)
print(instagram.post_url)
print(instagram.caption)
print(instagram.caption2)
print(instagram.image_text)
print(instagram.is_video)
print(instagram.owner_id)
print(instagram.display_url)
print(instagram.is_video)
print(instagram.post_time)
print(instagram.short_code)
```
## Save Data
```python
instagram=InstagramHashtag(hashtag_name,hashtag_amount)
result=instagram.save_csv("InstagramData")
print(result)
```
If operation is success , function returns "File Saved To {file_name} As Csv File" , else returns "An Error Occurred:{error}".
Also usable save_excel and save_txt too .
#Twitter Scraper
It uses headless selenium with Chrome . 
To use:
```python
from twitterhashtag import TwitterHastags
twitter=TwitterHastags(hashtag_name,hashtag_amount)
```
## Get Twitter Hashtags as a list in a tuple
```python
data=twitter.hashtag_results()
```
This code returns a list in a tuple. List elements contains:
-Post URL
-User name
-Username
-Text
-Display URL
-Image Text (Returns If there is image , else returns "No Image")
## Get Twitter Hashtags as a dictionary in a tuple
```python
data=twitter.to_dict()
```
It returns same result with hashtag_result . Difference is this function returns data as a dictionary in a tuple.
## Get Twitter Hashtags Using Property Feautures
```python
twitter=TwitterHastags(hashtag_name,hashtag_amount)
data=twitter.to_dict()
for d in data:
    print(d["link"]) #post url
    print(d["display_url"])
    print(d["name"])
    print(d["username"])
    print(d["text"])
    print(d["text2"]) #image text
```
## Save Data
```python
twitter=TwitterHastags(hashtag_name,hashtag_amount)
result=twitter.save_csv("TwitterData")
print(result)
```
If operation is success , function returns "File Saved To {file_name} As Csv File" , else returns "An Error Occurred:{error}".
Also usable save_excel and save_txt too .

# Word Analysis
```python
from wordanalysis import WordAnalysis
wd=WordAnalysis(sentence)
negative,positive,all_words,risk=wd.analysis()
```
# From Image To Text
```python
from imagetotext import ImagetoText
text=ImagetoText(display_url).text()
```
It downloads image as "pic1.jpg" , after reads it, deletes it.
If want to not delete picture , use:
```python
from imagetotext import ImagetoText
text=ImagetoText(display_url).download()
```





