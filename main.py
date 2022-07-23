import Download
import ScarpingUserPage

def main():
    listUsers = ["bbarlo", "Saint", "captaincampbell", "Fischer1997", "wilward", "trenny", "administrator", "Ambrosius_Bawerman", "kimplandz", "leslie1valhalla"]
    t = Download.DownloadHTML(listUsers)
    pathList = t.downloadHTML()
    s = ScarpingUserPage.UserPage(pathList)
    s.userPage()

if __name__ == '__main__':
    main()


