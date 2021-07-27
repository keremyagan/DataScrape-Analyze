from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from imagetotext import ImagetoText
import pandas as pd
from pandas import ExcelWriter
class TwitterHastags():
    def __init__(self,hashtag,amount=10):
        self.hashtag=hashtag
        self.amount=amount
        self.options=Options()
        self.options.headless=True  
        self.driver=webdriver.Chrome(options=self.options)
        self.hastag_link='https://twitter.com/hashtag/' + self.hashtag + '?src=hash'
        self.tweet_xpath = '//div[@data-testid="tweet"]'
        self.tweet_links_xpath = '//a[@href]' 
        self.list=[]

    def get_links(self):
        """
        Returns tweets links as a set
        """
        main_tweets = set(())
        self.driver.get(self.hastag_link)
        time.sleep(2)
        print("Getting Links.Please Wait.")
        while len(main_tweets)<self.amount:
            try:      
                tweet_link = self.driver.find_elements_by_xpath(self.tweet_links_xpath)
                elements = self.driver.find_elements_by_xpath(self.tweet_xpath)
                tweets = [tweet.get_attribute("href") for tweet in tweet_link]
                for i in tweets:
                    if '/status/' in i and '/photo/' not in i:
                        main_tweets.add(i)
                    else:
                        pass         
            except:
                pass  
            actions = ActionChains(self.driver) 
            actions.send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(1)
        return main_tweets

    def hashtag_results(self):
        """
        Returns
        post_link,nameofuser,username,post_text,display_url,image_text(if available else returns "No Image") as a tuple
        """
        main_tweets=self.get_links()
        for n,link in enumerate(main_tweets):
            try:
                print(f"{n+1}/{len(main_tweets)}")
                self.driver.get(link)
                time.sleep(1)
                try:
                    data=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[2]/div').text.splitlines()
                    if data==[]:
                        data=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div').text.splitlines()
                except:
                    data=self.driver.find_element_by_xpath('//*[@id="id__oqkmgi5kkpk"]').text.splitlines()
                name=data[0]
                username=data[1]
                display_url=""
                text=""
                text2="No Image"
                for i in data[2:]:
                    text=text+i+" "
                try:
                    urls=[]
                    images =self.driver.find_elements_by_tag_name("img")
                    urls = [img.get_attribute("src") for img in images]   
                    for url in urls:
                        if "https://pbs.twimg.com/media/" in url: #getting pic url
                            display_url=url
                            try:
                                if float(str(url).split("name=")[1].split("x")[0])!=900:
                                    #zooming to image to read text easier
                                    display_url=str(url).split("name=")[0]+"name=900x900"
                            except:
                                pass        
                            text2=ImagetoText(display_url).text()
                except :
                    pass
                
                list=[link,name,username,text,display_url,text2]
                self.list.append(list)

            except:
                pass
        
        return self.list 

    def to_dict(self):
        """
        Returns
        post_link,nameofuser,username,post_text,display_url,image_text(if available else returns "No Image") as dict in a tuple
        """
        main_tweets=self.get_links()
        for n,link in enumerate(main_tweets):
            try:
                print(f"{n+1}/{len(main_tweets)}")
                self.driver.get(link)
                time.sleep(1)
                try:
                    data=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[2]/div').text.splitlines()
                    if data==[]:
                        data=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div').text.splitlines()
                except:
                    data=self.driver.find_element_by_xpath('//*[@id="id__oqkmgi5kkpk"]').text.splitlines()
                name=data[0]
                username=data[1]
                display_url=""
                text=""
                text2="No Image"
                for i in data[2:]:
                    text=text+i+" "
                try:
                    urls=[]
                    images =self.driver.find_elements_by_tag_name("img")
                    urls = [img.get_attribute("src") for img in images]   
                    for url in urls:
                        if "https://pbs.twimg.com/media/" in url: #getting pic url
                            display_url=url
                            try:
                                if float(str(url).split("name=")[1].split("x")[0])!=900:
                                    #zooming to image to read text easier
                                    display_url=str(url).split("name=")[0]+"name=900x900"
                            except:
                                pass        
                            text2=ImagetoText(display_url).text()
                except :
                    pass
                
                dict={
                    "link":link,
                    "name":name,
                    "username":username,
                    "text":text,
                    "display_url":display_url,
                    "text2":text2
                }
                self.list.append(dict)

            except:
                pass
        
        return self.list             

    @property
    def link(self):
        if self.list==[]:
            self.to_dict()
        list=[]
        for i in self.list:
            list.append(i["link"])
        return list     

    @property
    def name(self):
        if self.list==[]:
            self.to_dict()
        list=[]
        for i in self.list:
            list.append(i["name"])
        return list    
    
    @property
    def username(self):
        if self.list==[]:
            self.to_dict()
        list=[]
        for i in self.list:
            list.append(i["username"])
        return list 
    
    @property
    def text(self):
        if self.list==[]:
            self.to_dict()
        list=[]
        for i in self.list:
            list.append(i["text"])
        return list 

    @property
    def display_url(self):
        if self.list==[]:
            self.to_dict()
        list=[]
        for i in self.list:
            list.append(i["display_url"])
        return list 

    @property
    def image_text(self):
        if self.list==[]:
            self.to_dict()
        list=[]
        for i in self.list:
            list.append(i["text2"])
        return list 
    
    def save_txt(self,file_name="file1"):
        """
        Saves data to a txt file
        Notice:If a file exist in same name of file name,data are deleting in old file ,and new data
        saves to file
        """
        file_name=file_name+".txt"
        if self.list==[]:
            self.to_dict()
        try:
            file=open(file_name,"w",encoding="utf-8")
            for i in self.list:
                file.write("-".center(99,"-"))
                file.write("\n")
                file.write(f"Post Link:{i['link']}\n")
                file.write(f"Display Url:{i['display_url']}\n")
                file.write(f"Name:{i['name']}\n")
                file.write(f"Username:{i['username']}\n")                                
                file.write(f"Text:{i['text2']}\n")
                file.write(f"Image Text:{i['text']}\n")
            file.close()
            return f"File Saved To {file_name} As Txt File"
        except Exception as err:
            return f"An Error Occurred:{err}"
        
    def save_excel(self,file_name="file1"):
        """
        Saves data to a excel file
        Notice:If a file exist in same name of file name,data are deleting in old file ,and new data
        saves to file
        """    
        try:    
            file_name=file_name+".xlsx"
            if self.list==[]:
                self.to_dict()
            
            df = pd.DataFrame(list(zip(self.link,self.display_url,self.name,self.username,self.text,self.image_text)),
                columns =['Post Url','Display Url','Name','Username','Text','Image Text'])
            
            writer = ExcelWriter(file_name)
            df.to_excel(writer,"TwitterData")
            writer.save()
            return f"File Saved To {file_name} As Excel File"
        except Exception as err:
            return f"An Error Occurred:{err}"

    def save_csv(self,file_name="file1"):
        """
        Saves data to a csv file
        Notice:If a file exist in same name of file name,data are deleting in old file ,and new data
        saves to file
        """    
        try:    
            file_name=file_name+".csv"
            if self.list==[]:
                self.to_dict()
            
            df = pd.DataFrame(list(zip(self.link,self.display_url,self.name,self.username,self.text,self.image_text)),
                columns =['Post Url','Display Url','Name','Username','Text','Image Text'])
            df.to_csv(file_name)
            return f"File Saved To {file_name} As Csv File"
        except Exception as err:
            return f"An Error Occurred:{err}"
 

    @classmethod
    def save_data(cls,df,file_type,file_name="file1",sheet_name="TwitterData"):
        """
        Saves data to a file type you selected
        Notice:If a file exist in same name of file name,data are deleting in old file ,and new data
        saves to file
        """  
        try:     
            if file_type.lower()=="excel":
                file_name=file_name+".xlsx"
                writer = ExcelWriter(file_name)
                df.to_excel(writer,sheet_name)
                writer.save()
            else:
                file_name=file_name+".csv"  
                df.to_csv(file_name) 
                
            return f"File Saved To {file_name} As {file_type} File"
        except Exception as err:
            return f"An Error Occurred:{err}"
    
    
    
       