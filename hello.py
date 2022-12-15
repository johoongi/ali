from selenium import webdriver
import bs4
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='./chromedriver')
url = 'https://ko.aliexpress.com/item/1005003532002013.html?spm=a2g0o.productlist.main.9.1dfc3d69ET0mSh&algo_pvid=39f9302f-87dc-4a44-a7c7-69a469b51a97&aem_p4p_detail=202211221840042777596532759600010473948&algo_exp_id=39f9302f-87dc-4a44-a7c7-69a469b51a97-4&pdp_ext_f=%7B%22sku_id%22%3A%2212000026882707774%22%7D&pdp_npi=2%40dis%21KRW%218022.0%2114.0%21%21%21%21%21%4021227d8316691712040986526d076e%2112000026882707774%21sea&curPageLogUid=R8P7QhlcDWjX&ad_pvid=202211221840042777596532759600010473948_5&ad_pvid=202211221840042777596532759600010473948_5'

driver.get(url)
soup = bs4.BeautifulSoup(driver.page_source, 'lxml')  #

driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
sleep(1)


title = soup.select_one('h1.product-title-text').text
list2 = soup.select('div.sku-property-image > img')


driver.find_element(By.XPATH, r'//*[@class="product-dynamic-shipping"]').click()
#driver.find_elements(By.CSS_SELECTOR, 'div.dynamic-shipping').click()
sleep(1)

list3 = driver.find_elements(By.CSS_SELECTOR, 'div.dynamic-shipping')



for a in list3[0:]:
    print(a.text)
    #print(a)
    print()

driver.find_element(By.XPATH, r'//*[@class="comet-icon comet-icon-close "]').click()
sleep(1)


#driver.find_element(By.XPATH, r'//*[@class="tab-inner-text"]').click()

#driver.find_element(By.XPATH, r'//*[@class="tab-lists avoid-user-select"]]').click()
list4 = driver.find_elements(By.CSS_SELECTOR, 'span.tab-inner-text')
#list3 = soup.select('div.comet-modal-body _1yog9')

#_1lP57 _2f4Ho


print(list2)
print()


fg = 1
exel_data=[]
img_src_all = ''
Product_code = ''
for b in list4[0:]:
    print(b.text)
    #print(a)

    if fg == 5:
          b.click()
          print('asd')
          img_all = driver.find_element(By.CSS_SELECTOR, 'div.product-overview').find_elements(By.CSS_SELECTOR, 'img')
  
          for img_src in img_all[0:]:
                   img_src_all = img_src_all + '<div><img style="display:block;" src="'+ img_src.get_attribute('src') + '"></div>'      


    sleep(1)


    fg = fg+1

#print(list4)
print(img_src_all)

exel_data.append({
               '판매자 상품코드' : Product_code,
               '카테고리코드' : '50003307',
               '상세설명':img_src_all,
               '상품명' : title,
               '상품상태' : '신상품',
               '판매가' :
            })
