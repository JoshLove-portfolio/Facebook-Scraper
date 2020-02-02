import csv
from bs4 import BeautifulSoup

rows = []

foldername = "" #EDIT foldername TO BE THE EXACT NAME OF THE FOLDER WHERE YOUR DATA AND THIS CODE IS SAVED

with open("" % foldername, errors = "ignore") as page: 
    #EDIT THE "" TO BE THE PATH OF THE FOLDER SUCH AS C:\USER\DOCUMENTS\%s\FACEBOOK_DATA, NOTE THAT %foldername JUST FILLS IN THE FOLDER NAME FROM ABOVE. YOU'LL WANT TO
    #INCLUDE %S WHERE THE FOLDER IS IN THE PATH OR JUST DELETE %foldername AND PUT IT NORMALLY INTO THE PATH
    soup = BeautifulSoup(page, "html.parser")
    contents = soup.find("div", class_="_4t5n")
    post_list = contents.find_all("div" , class_= "uiBoxWhite")
    
    for item in post_list:
        try: 
            post = item.find("div", class_="_2pin").get_text()
        except AttributeError:
            print("post: blank")
        try: 
            timeaccessed = item.find("div", class_="_2lem").get_text()
        except AttributeError:
            print("time: none available")
        try: 
            postinfo = item.find("div", class_="_2pio").get_text()
        except AttributeError:
            print("post info: none available")
        row = {
            "post info" : postinfo, 
            "post" : post,
            "time accessed" : timeaccessed
            }
        rows.append(row)

with open("%s-all-posts.csv" % foldername, "w+") as csvfile:
    fieldnames = ["post info", "post", "time accessed"]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    
    for row in rows:
        writer.writerow(row)

