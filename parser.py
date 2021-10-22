from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import os
import datetime


name = ['alcohol', 'food', 'home-stuff', 'beer-cider', 'cosmetics-hygiene',
        'for-kids', 'pet-supplies', 'mkt-electronic-1077', 'mkt-clothes-shoes-and-accessories-1790']
rus_name = ["алкоголь", "еда", "для дома", "пиво", "косметика",
            "для детей", "зоотовары", "электроника", "одежда"]

shop = ['5ka', 'krasnoeibeloe', 'dixy', 'magnit-univer', 'perekrestok']
rus_shop = ["пятерочка", "красное и белое", "дикси", "перекресток"]

url_site = "https://edadeal.ru/moskva/retailers/{}?page={}&segment={}"


def from_rus_to_eng(list_names, list_rus_names, rus_name):
    return list_names[list_rus_names.index(rus_name.lower())]


class Parser:

    def __init__(self, shop=shop[0], name=name[0], url=url_site):
        self.url = url
        self.name = name
        self.shop = shop
        try:
            os.mkdir('lists')
        except:
            pass
        self.file_path = os.path.join('lists',self.shop+'_'+self.name+'_'+ str(datetime.datetime.now().day)+'.txt')


    def exists_path(self):
        if os.path.exists(self.file_path):
            self.fl = None
            return 0
        else:
            self.fl = open(self.file_path, mode='w', encoding='utf-8')
            return 1

    def get_page(self, page_number):
        if self.exists_path() == 0 and page_number==1:
            return 0
        url = self.url.format(self.shop, str(page_number), self.name)
        opts = Options()
        opts.add_argument('--headless')
        browser = Firefox(options=opts)
        browser.get(url)
        browser.implicitly_wait(4)
        if self.name == 'alcohol' or self.name == 'beer-cider':
            elems = browser.find_elements(By.XPATH, '//*[contains(text(),"Да. Мне есть 18")]')

            for elem in elems:
                print(elem)
                while (1):
                    try:
                        elem.click()
                        break
                    except:
                        pass
                break

        products_info = browser.find_elements(By.CLASS_NAME, 'b-offer__description')
        if (len(products_info)==0):
            browser.quit()
            return 0
        products_price = browser.find_elements(By.CLASS_NAME, 'b-offer__price-new')
        for i in range(len(products_info)):
            st = products_info[i].text + ' '+ products_price[i].text + '\n'
            self.fl.write(st)
        browser.quit()
        return 1

    def get_all_pages(self):
        page=1
        while True:
            if (self.get_page(page) == 0):
                break
            page = page+1
        if self.fl is not None:
            self.fl.close()
        return self.file_path


# ps = Parser(shop=from_rus_to_eng(list_names=shop, list_rus_names=rus_shop, rus_name='Красное и белое'))
ps = Parser(shop=shop[4])
ps.get_all_pages()
