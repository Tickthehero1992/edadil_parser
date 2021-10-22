import urllib.request
import ssl
import webbrowser
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import codecs


url_site = "https://edadeal.ru/moskva/retailers/5ka?segment=alcohol"



class Parser:

    def __init__(self, url=url_site):
        self.url = url


    def get_page(self, page_number):
        # user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:90.0) Gecko/20100101 Firefox/90.0'
        # headers = {'User-Agent': user_agent}
        url = self.url.format(str(page_number))
        # gcontext = ssl.SSLContext()
        # req = urllib.request.Request(url, headers=headers)
        # response = urllib.request.urlopen(req, context=gcontext)
        # webContent = response.read()
        # with open(str(page_number)+'.html', mode='wb') as fl:
        #     fl.write(webContent)

        # data = webbrowser.get('firefox').open(url)
        # print(data)

        opts = Options()
        # opts.add_argument("--headless")
        browser = Firefox(options=opts)
        browser.get(url)
        browser.implicitly_wait(4)
        elems = browser.find_elements(By.XPATH, '//*[contains(text(),"Да. Мне есть 18")]')

        for elem in elems:
            print(elem)
            while(1):
             try:
                elem.click()
                break
             except:
                pass
            break

        products_info = browser.find_elements(By.CLASS_NAME, 'b-offer__description')
        products_price = browser.find_elements(By.CLASS_NAME, 'b-offer__price-new')
        for i in range(len(products_info)):
            print(products_info[i].text + ' '+ products_price[i].text)


        # elems = browser.find_element(By.XPATH, '//*[contains(@class,"b-offer__product-info")]')
        # print(elems)

        # browser.quit()
        # with open('page.html', 'w') as fl:
        #     fl.write(browser.page_source)
        # soup = BeautifulSoup(browser.page_source, 'lxml')
        # # print(browser.page_source)
        # print(soup.find('body'))



ps = Parser()
ps.get_page(1)