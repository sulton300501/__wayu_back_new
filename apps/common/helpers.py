import io # xotirada vaqtinchalik fayl yaratish , oqish va yozish
import os #  fayl o'lchamini tekshirish , fayl mavjudligini tekshirish , va yo'lini yaratish
import re #  regex bilan ishlash 
import sys  # fayl joylashuvini olish
import PIL # pillow
import PIL.Image
import requests  # internetdan malumot olish uchun kutubxona , veb sahifalarni yuklash , API chiqarish , va malumot olish
from PIL import Image


def compress_image(image_name):
    img = Image.open(image_name)
    img = img.resize((img.width // 3 , img.height // 3) , PIL.Image.ANTIALIAS) # PIL.Image.ANTIALIAS  rasmni sifatli qilip kichiklashtrip beradi
    img.save(image_name)
    img.close()


def compress(original_file , max_size , scale):
    assert 1.1 <= scale <= 1.5 , "Scale must be between 1.1 and 1.5"
    original_file = f"{sys.path[0]}/{original_file}"

    orig_image = Image.open(original_file)  ## rasmni ochish
    cur_size = orig_image.size # rasm size ni olish

    if orig_image.format.lower() not in ["jpeg",'jpg']:  # formatlarni orasidan  izlash yoq bolsa functiondan chiqish
        return 
    
    if os.path.getsize(original_file) > 10485760:
        raise Exception("File size is too big . Max size is 10MB")
    
    if os.path.getsize(original_file) <= max_size:
        return 
    
    while True:
        cur_size = (int(cur_size[0] // scale) , int(cur_size[1] // scale))   # cur_size[0] uzunligi  cur_size[1] balandligi
        resized_file = orig_image.resize(cur_size ,Image.ANTIALIAS)

        with io.BytesIO() as file_bytes:
            resized_file.save(file_bytes , optimize=True , quality=70 , format="jpeg")
            if file_bytes.tell() <= max_size: # tell()  faylni baytlarda qaytaradi
                file_bytes.seek(0,0)  # bu yerda rasmni kichraytrilgan versiyasi bor.. # with - context manager construktsiyasi hisoblanadi.. xotirada faylni boshidan oqish uchun  .. yani faylni qayta yozishdan oldin xotiradagi faylni bioshidan boshlash kerakligi uchun kerak... seek(offset, whence) offset - faylni qayerdan boshlash kerakligini bildiradi , whence - qaysi nuqtadan boshlash kerakligini belgilaydi.. asosan 3 xil: 0 - faylni boshidan boshlash , 1-hozirgi oqilyotgan joydan , 2-faylni oxiridan boshlahs
                with open(original_file , "wb") as f_output:  #  original_file ni binary write rejimiga o'tkazad...
                    f_output.write(file_bytes.read())
                break




def get_long_lat(location) -> tuple:
    """
    return:content,status code
    example:
        error: ({}, 404),
        success: ({'long': '41.2965807', 'lat': '69.275822'}, 200)
    """
    YANDEX_PATTERN = r'"longitude":(-?\d+\.\d+),"latitude":(-?\d+\.\d+)'  # noqa
    GOOGLE_PATTERN = r"@(-?\d+\.\d+),(-?\d+\.\d+)"
    results = {}
    try:
        if re.match(r"https://yandex.\w+/?", location):  # noqa
            results['long'], results['lat'] = str(location).split('/?ll=')[-1].split('&')[0].split('%2C')
            return results, True
        elif re.match(r"https://(www.)*goo\w*[.]\w+/?", location):  # noqa
            response = requests.get(location)
            if response.status_code == 200:
                page_url = response.url
                ll = re.findall(GOOGLE_PATTERN, page_url)
                results['long'], results['lat'] = ll[0]
                return results, True
    except Exception as e:
        print(e)
        return results, False
    return results, False




# results['long'], results['lat'] = str(location).split('/?ll=')[-1].split('&')[0].split('%2C')
# https://yandex.ru/?ll=41.2965807%2C69.275822 




    
