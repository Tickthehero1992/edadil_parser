from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


name = ['alcohol', 'food', 'home-stuff']
url_site = "https://edadeal.ru/moskva/retailers/5ka?page={}&segment={}"
file_path = "info.txt"


class Parser:

    def __init__(self, name=name[0], url=url_site, file_path=file_path):
        self.url = url
        self.name = name
        self.fl = open(file_path, mode='w', encoding='utf-8')

    def get_page(self, page_number):

        url = self.url.format(str(page_number), self.name)
        opts = Options()
        browser = Firefox(options=opts)
        browser.get(url)
        browser.implicitly_wait(4)
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
        products_price = browser.find_elements(By.CLASS_NAME, 'b-offer__price-new')
        for i in range(len(products_info)):
            st = products_info[i].text + ' '+ products_price[i].text + '\n'
            self.fl.write(st)
        browser.quit()

    def get_all_pages(self, pages=5):
        for page in range(1,pages):
            self.get_page(page)

ps = Parser()
ps.get_all_pages()