#  Bu kod Instagram dan postlarning rasmlari va ularning havolalarini olish uchun Selenium kutubxonasidan foydalanadi.
import time
import urllib.request

from selenium import webdriver   # brauzer va firefox va shunga oxshganlarni ishga tushuradi
from selenium.webdriver.chrome.options import Options   # Google Chrome'ga qo‘shimcha sozlamalar berish uchun
from selenium.webdriver.common.by import By  #  HTML elementlarni turli usullar bilan tanlash
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait    #    Kutish mexanizmi  Selenium'ga kerakli elementlar yuklanishini kutish imkonini beradi.
from django.utils.crypto import get_random_string
from core.settings.develop import NUMBER_OF_INSTAGRAM_POSTS
from pathlib import Path



class InstagramScraper:
    def __init__(self,username,password):
        self.username = username
        self.password = password

        self.posts_number = NUMBER_OF_INSTAGRAM_POSTS
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # brauzer background rejimida ishlaydi
        chrome_options.add_argument("--no-sandbox") # ubuntuda ishlashi uchun
        chrome_options.add_argument("--disable-dev-shm-usage") # olingan malumotlar diskda saqlanishini taminlaydi
        chrome_prefs = {}  # chrome uchun sozlamalar saqlanadigan joy
        chrome_options.experimental_options["prefs"] = chrome_prefs # chromening maxsus sozlamalarini yuklash
        chrome_prefs["profile.default_content_settings"] = {"images":2}  # avtomaticheskiy rasmlar yuklanishini ochiramiz
        self.driver = webdriver.Chrome(options=chrome_options) 
#         webdriver.Chrome(...) → Chrome brauzerini avtomatlashtirish uchun kerak.
#         options=chrome_options → Brauzerni maxsus sozlamalar bilan ochish uchun.
        self.images = [] 
        self.wait = WebDriverWait(self.driver , 60) # yani sahifa ochilayotganda elementlar paydo bolishi vaqti


    def get_credentials(self) -> tuple:
        return self.username , self.password
    
    def scrape(self , account=None):
        try:
            self.driver.set_page_load_timeout(50) #   Selenium WebDriver orqali yuklanayotgan veb-sahifa uchun maksimal kutish vaqtini 50 soniya qilib belgilaydi.
            self.driver.set_script_timeout(10)  # JavaScript kodlarining bajarilishi uchun maksimal kutish vaqtini 10 soniya .10 soniya ichida tugamasa, Selenium xatolik chiqaradi va davom etmaydi.
            time.sleep(5)
            username , password = self.get_credentials()
            self.driver.get("https://www.instagram.com/")
            time.sleep(5)
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']"))).send_keys(username)
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR ,"input[name='password']"))).send_keys(password)
            self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME , "button[type='submit']"))).click()



             #  bular sahifaga kirgandan keyin 2 ta page ni yopib beradi
            try:
                self.wait.until(EC.element_to_be_clickable((By.XPATH , "//button[contains(text() , 'Not now')]"))).click()
            except Exception as e:
                print(e)
                pass

            try:
                self.wait.until(EC.element_to_be_clickable((By.XPATH , "//button[contains(text(),'Not now')]"))).click()
            except Exception as e:
                print(e)
                pass

            time.sleep(5)
            self.driver.get(account)

            posts = []
            links = self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME , "a"))) #   sahifadagi barcha <a> (link) teglarini yuklashni kutadi va ularni links ro‘yxatiga saqlaydi.
            images = self.wait.until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR , "img[class='x5yr21d xu96u03 x10l6tqk x13vifvy x87ps6o xh8yej3']")  # sahifadagi barcha rasm (<img>) teglarini yuklash va ularni olish uchun
                )
            )

            link_index = 0
            image_index = 0

            def link_valid(link):
                try:
                    l = link.get_attribute("href")
                    if "/p/" in l:
                        return True
                except Exception as e:
                    print(e)
                    return False
                return False
            
            def image_valid(image):
                try:
                    l = image.get_attribute("src")
                    if l:
                        return True
                except Exception as e:
                    print(e)
                    return False
                return False
            

            while link_index < len(links) and image_index < len(images):
                while link_index < len(links) and not link_valid(links[link_index]):
                    link_index+=1
                while image_index < len(images) and not image_valid(images[image_index]):
                    image_index+=1
                if link_index >= len(links) or image_index >= len(images):
                    continue
                link = links[link_index]
                image = images[image_index]
                try:
                    post = link.get_attribute('href')
                    if "/p/" in post and post not in posts:
                        posts.append(post)
                        time.sleep(5)
                        download_url = image.get_attribute('src') # rasm manzili
                        unique_id = get_random_string(length=32)
                        Path("media/images").mkdir(parents=True ,exist_ok=True)
                        filename , headers = urllib.request.urlretrieve(download_url, f"media/images/{unique_id}.jpg") # rasmni yuklab olip images fayliga saqliydi
                        if len(self.images) >= self.posts_number:  # maksimal postlar soniga yetganda function tugiydi
                            return
                        self.images.append([filename,post])
                         # filename - bu saqlangan rasm yo'li.. media/images/3a4f9c1e8d6b7a9c2d5f1a3b4e6d8c9f.jpg
                        # post - instagramdagi post sahifa  https://www.instagram.com/p/CxYz3J4A9dG/
                except Exception as e:
                    print(e)
                    pass
                link_index += 1
                image_index += 1
        except Exception as e:
            print(e)
            pass







