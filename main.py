from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome("/Users/joshmanik/Downloads/chromedriver 3")

    def closeBrowser(self):
        self.browser.close()

    def loginToInstagram(self):
        browser = self.browser
        browser.get("https://www.instagram.com/")
        time.sleep(2)

        # we are forced to accept cookies so we do

        accept_Cookies = browser.find_element_by_xpath(r"/html/body/div[2]/div/div/div/div[2]/button[1]")
        accept_Cookies.click()
        usernameTextBox = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
        passwordTextBox = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
        usernameTextBox.send_keys(self.username)
        passwordTextBox.send_keys(self.password)
        loginButton = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div")
        loginButton.click()
        time.sleep(5)
        notification_popup = browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
        notification_popup.click()
        time.sleep(2)


    def Get_Hashtag_photos(self,hashtag):
        browser = self.browser
        browser.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)

        listOfPictures = []
        for scroll in range(1,2):
            try:
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(0.5)
                pictureLinks = browser.find_elements_by_tag_name("a")
                for picture in pictureLinks:
                    if '/p/' in picture.get_attribute('href'):
                        if picture not in listOfPictures:
                            listOfPictures.append(picture.get_attribute('href'))
            except Exception:
                continue
        return listOfPictures




    def Like_Hashtags_photos(self, hashtag):
        browser = self.browser
        Photolinks = self.Get_Hashtag_photos(hashtag=hashtag)
        for photo in Photolinks:
            browser.get(photo)
            time.sleep(1)
            like = browser.find_element_by_class_name('fr66n')
            like.click()


if __name__ == "__main__":

    username = "username"
    password = "password"
    hashtag = "ToyotaSupra"

    Bot = InstagramBot(username=username, password=password)
    Bot.loginToInstagram()
    Bot.Like_Hashtags_photos(hashtag=hashtag)
