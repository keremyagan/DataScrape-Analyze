from instascrape import *
from instascrape.core._mappings import _HashtagMapping, _PostMapping
from instascrape.core._static_scraper import _StaticHtmlScraper
from instascrape.scrapers.post import Post
import datetime
from imagetotext import ImagetoText
import pandas as pd
from pandas import ExcelWriter
class Hashtag(_StaticHtmlScraper):
    _Mapping = _HashtagMapping
    def get_recent_posts(self, amt: int = 71):
        """
        Return a list of recent posts to the hasthag
        Parameters
        ----------
        amt : int
            Amount of recent posts to return
        Returns
        -------
        posts : List[Post]
            List containing the recent 12 posts and their available data
        """
        posts = []
        post_arr = self.json_dict["entry_data"]["TagPage"][0]["graphql"]["hashtag"]["edge_hashtag_to_media"]["edges"]
        amount_of_posts = len(post_arr)
        if amt > amount_of_posts:
            amt = amount_of_posts
        for post in post_arr[:amt]:
            posts.append(post)
        return posts

    def _url_from_suburl(self, suburl: str) :
        return f"https://www.instagram.com/tags/{suburl}/"
   
class InstagramHashtag():
    def __init__(self,hashtag,amount):
        self.hashtag=hashtag
        self.amount=amount
        self.search_hashtag = Hashtag(f'https://www.instagram.com/explore/tags/{self.hashtag}/')
        self.list=[]
        
    def hashtag_posts(self):
        """
        Returns Posts as Object of InstagramScrape
        Don't need to use it
        """
        self.search_hashtag.scrape()
        posts=self.search_hashtag.get_recent_posts(self.amount)
        return posts
    
    def hashtag_result(self):
        """
        Returns 
        caption,shortcode,post_url,post_time,display_url,owner_id,is_video,caption2,image_text
        as a list
        """
        posts=self.hashtag_posts()
        for n,post in enumerate(posts):
            print(f"{n+1}/{len(posts)}")
            try:
                caption=str(post["node"]['edge_media_to_caption']["edges"][0]["node"]["text"])
                shortcode=str(post["node"]["shortcode"])
                post_url=str("https://www.instagram.com/p/"+str(shortcode)+"/")
                timestamp=post["node"]["taken_at_timestamp"]
                post_time=str(datetime.datetime.fromtimestamp(int(timestamp)))
                display_url=str(post["node"]["display_url"])
                owner_id=str(post["node"]["owner"]["id"])
                is_video=post["node"]["is_video"]
                caption2=str(post["node"]["accessibility_caption"])
                if not is_video:
                    text=ImagetoText(display_url).text()
                    list=[caption,shortcode,post_url,post_time,display_url,owner_id,is_video,caption2,text]
                    self.list.append(list)
                try:
                    list=[caption,shortcode,post_url,post_time,display_url,owner_id,is_video,caption2,text]
                    if list not in self.list:
                        self.list.append(list)
                except:
                    list=[caption,shortcode,post_url,post_time,display_url,owner_id,is_video,caption2,"Video"]
                    if list not in self.list:
                        self.list.append(list)   
            except:
                pass
        
        return self.list
   
    def to_dict(self):
        """
        Returns 
        caption,shortcode,post_url,post_time,display_url,owner_id,is_video,caption2,image_text
        as a dict in list
        """
        posts=self.hashtag_posts()
        for n,post in enumerate(posts):
            print(f"{n+1}/{len(posts)}")
            try:
                caption=str(post["node"]['edge_media_to_caption']["edges"][0]["node"]["text"])
                shortcode=str(post["node"]["shortcode"])
                post_url=str("https://www.instagram.com/p/"+str(shortcode)+"/")
                timestamp=post["node"]["taken_at_timestamp"]
                post_time=str(datetime.datetime.fromtimestamp(int(timestamp)))
                display_url=str(post["node"]["display_url"])
                owner_id=str(post["node"]["owner"]["id"])
                is_video=post["node"]["is_video"]
                caption2=str(post["node"]["accessibility_caption"])
                if not is_video:
                    text=ImagetoText(display_url).text()
                    dict={
                        "caption":caption,
                        "shortcode":shortcode,
                        "post_url":post_url,
                        "post_time":post_time,
                        "display_url":display_url,
                        "owner_id":owner_id,
                        "is_video":is_video,
                        "caption2":caption2,
                        "text":text
                    }
                    self.list.append(dict)
                try:
                    dict={
                        "caption":caption,
                        "shortcode":shortcode,
                        "post_url":post_url,
                        "post_time":post_time,
                        "display_url":display_url,
                        "owner_id":owner_id,
                        "is_video":is_video,
                        "caption2":caption2,
                        "text":text
                    }
                    if dict not in self.list:
                        self.list.append(dict)
                except:
                    dict={
                        "caption":caption,
                        "shortcode":shortcode,
                        "post_url":post_url,
                        "post_time":post_time,
                        "display_url":display_url,
                        "owner_id":owner_id,
                        "is_video":is_video,
                        "caption2":caption2,
                        "text":"Video"
                    }
                    if dict not in self.list:
                        self.list.append(dict)   
            except :
                pass
        
        return self.list       

    @property
    def post_url(self):
        if self.list==[]:
            self.to_dict()
        list=[]
        for i in self.list:
            list.append(i["post_url"])
        return list

    @property
    def caption(self):
        if self.list==[]:
            self.to_dict()
        list=[]
        for i in self.list:
            list.append(i["caption"])
        return list

    @property
    def short_code(self):
        if self.list==[]:
            self.to_dict()
        list=[]
        for i in self.list:
            list.append(i["shortcode"])
        return list
 
    @property
    def post_time(self):
        if self.list==[]:
            self.to_dict()
        list=[]
        for i in self.list:
            list.append(i["post_time"])
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
    def owner_id(self):
        if self.list==[]:
            self.to_dict()
        list=[]
        for i in self.list:
            list.append(i["owner_id"])
        return list

    @property
    def is_video(self):
        if self.list==[]:
            self.to_dict()
        list=[]
        for i in self.list:
            list.append(i["is_video"])
        return list

    @property
    def caption2(self):
        if self.list==[]:
            self.to_dict()
        list=[]
        for i in self.list:
            list.append(i["caption2"])
        return list

    @property
    def image_text(self):
        if self.list==[]:
            self.to_dict()
        list=[]
        for i in self.list:
            list.append(i["text"])
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
                file.write(f"Post Url:{i['post_url']}\n")
                file.write(f"Post Time:{i['post_time']}\n")
                file.write(f"Shortcode:{i['shortcode']}\n")
                file.write(f"Display Url:{i['display_url']}\n")
                file.write(f"Owner ID:{i['owner_id']}\n")
                file.write(f"Is Video:{i['is_video']}\n")
                file.write(f"Caption:{i['caption']}\n")                       
                file.write(f"Caption2:{i['caption2']}\n")
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
            
            df = pd.DataFrame(list(zip(self.post_url,self.post_time,self.short_code,self.display_url,self.owner_id,self.is_video,self.caption,self.caption2,self.image_text)),
                columns =['Post Url', 'Post Time','Shortcode','Display Url','Owner ID','Is Video','Caption','Caption2','Image Text'])
            
            writer = ExcelWriter(file_name)
            df.to_excel(writer,"InstagramData")
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
            
            df = pd.DataFrame(list(zip(self.post_url,self.post_time,self.short_code,self.display_url,self.owner_id,self.is_video,self.caption,self.caption2,self.image_text)),
                columns =['Post Url', 'Post Time','Shortcode','Display Url','Owner ID','Is Video','Caption','Caption2','Image Text']) 
            df.to_csv(file_name)
            return f"File Saved To {file_name} As Csv File"
        except Exception as err:
            return f"An Error Occurred:{err}"

    @classmethod
    def save_data(cls,df,file_type,file_name="file1",sheet_name="InstagramData"):
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
            return f"An Error Occured:{err}"