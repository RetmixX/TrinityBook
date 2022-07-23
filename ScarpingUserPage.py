from bs4 import BeautifulSoup
import json
import dataUser

class UserPage:
    def __init__(self, pathList):
        self.__pathList = pathList

    def userPage(self):
        for i in self.__pathList:
            with open(i,"r", encoding='utf-8') as file:
                src = file.read()
            soup = BeautifulSoup(src, "lxml")

            nameUser = soup.find("div", class_="profile-container").find("a").text.strip()
            shortInfo = soup.find("ul", class_=dataUser.test).findAll("li", {"class": "list-group-item"})
            listShortInfo = [nameUser]
            DictUserPage = {}
            for i in shortInfo:
                if not len(i.text.strip().split()) == 0:
                    listShortInfo.append(" ".join(i.text.strip().split()))
            DictUserPage["Short Info"]=listShortInfo
            posts = soup.findAll("div", class_="post-container")
            postList = []
            for i in posts:
                postP = i.find("div", class_="post")["id"]
                try:
                    place = i.find("span", style="color:#9197a3").text.replace('-', '').replace('..', '').strip()
                except:
                    place = "None"

                try:
                    textp = i.find("p", dir="auto").text
                except:
                    textp = "None"
                try:
                    UrlPhoto = i.find("img", class_="image-file pointer")["src"]
                except:
                    UrlPhoto = "None"
                postList.append({
                    "Post": postP,
                    "Place": place,
                    "Post text": textp.strip(),
                    "Url photo": UrlPhoto
                })
            DictUserPage["Post"]=postList
            jsonS = json.dumps(DictUserPage, ensure_ascii=False, indent=2)
            with open(f"Json//{nameUser}.json", "w", encoding='utf-8') as file:
                file.write(jsonS)