from instagramscraper import InstagramHashtag
from wordanalysis import WordAnalysis
from twitterhashtag import TwitterHastags
from imagetotext import ImagetoText
from termcolor import colored
from banner import banner

while True:
    try:
        banner()
        risk_data=1
        print(colored("1-Instagram Scraper","red"))
        print(colored("2-Twitter Scraper","blue"))
        print(colored("3-Exit","green"))
        option=input(colored("Choose:","cyan"))
        if option=="1" or  option=="2":
            hashtag_name=input(colored("Please Enter Hashtag Name to Search:","magenta"))
            while True:
                try:
                    hashtag_amount=int(input(colored("Please Enter Number of Hashtag to Search:","red")))
                    break
                except:
                    print("Please Enter Valid Number.")

            while True:
                try:
                    risk_rate=float(input(colored("Please Enter Risk Rate:","white")))
                    break
                except:
                    print("Please Enter Valid Number.")
            
            if option=="1": #instagram  
                instagram=InstagramHashtag(hashtag_name,hashtag_amount)
                data=instagram.hashtag_result()
                for d in data:
                    caption,shortcode,post_url,post_time,display_url,owner_id,is_video,caption2,text=d
                    try:
                        sentence=caption+caption2+text
                    except:
                        sentence=caption+text
                    wd=WordAnalysis(sentence)
                    negative,positive,all_words,risk=wd.analysis()
                    if risk>risk_rate:
                        print(colored(risk_data,"red") ,colored(". Data","green"))
                        print(colored("Caption:","red") ,colored(caption.rstrip().lstrip(),"green"))
                        print(colored("Shortcode:","red") ,colored(shortcode,"green"))
                        print(colored("Post URL:","red") ,colored(post_url,"green"))
                        print(colored("Post Time:","red") ,colored(post_time,"green"))
                        print(colored("Display URL:","red") ,colored(display_url,"green"))
                        print(colored("Owner ID:","red") ,colored(owner_id,"green"))
                        print(colored("Is Video:","red") ,colored(is_video,"green"))
                        print(colored("Caption2:","red") ,colored(caption2.rstrip().lstrip(),"green"))
                        print(colored("Image Text:","red") ,colored(text.rstrip().lstrip(),"green"))
                        print(colored("Risk:","red") ,colored(risk,"green"))
                        print(colored("-".center(149,"-"),"blue"))
                        risk_data=risk_data+1
                                       
            elif option=="2": #twitter
                twitter=TwitterHastags(hashtag_name,hashtag_amount)
                data=twitter.hashtag_results()
                for d in data:
                    link,name,username,text,display_url,text2=d
                    try:
                        sentence=text+text2
                    except:
                        sentence=text
                    wd=WordAnalysis(sentence)
                    negative,positive,all_words,risk=wd.analysis()
                    if risk>risk_rate:
                        print(colored(risk_data,"red") ,colored(". Data","green"))
                        print(colored("Post URL:","red") ,colored(link,"green"))
                        print(colored("Display URL:","red") ,colored(display_url,"green"))
                        print(colored("Name:","red") ,colored(name,"green"))
                        print(colored("Username:","red") ,colored(username,"green"))
                        print(colored("Text:","red") ,colored(text.rstrip().lstrip(),"green"))
                        print(colored("Image Text:","red") ,colored(text2.rstrip().lstrip(),"green"))
                        print(colored("Risk:","red") ,colored(risk,"green"))
                        print(colored("-".center(149,"-"),"blue"))
                        risk_data=risk_data+1          

        
        elif option=="3": #exit
            break
        else:
            print("Please Choose Between 1-3 and Try Again.")
    
    except Exception as err:
        print(f"An Error Occured:{err}") 
