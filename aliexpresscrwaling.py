from selenium import webdriver
import bs4
from time import sleep
from selenium.webdriver.common.by import By
import pandas as pd
import math
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="~/ChromeProfile"'
driver = webdriver.Chrome(chrome_driver, options=chrome_options)
url = input()

driver.get(url)
soup = bs4.BeautifulSoup(driver.page_source, 'lxml')  #

driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
sleep(1)

##상품명
title = soup.select_one('h1.product-title-text').text

##대표이미지
major_img_src = driver.find_element(By.CSS_SELECTOR, 'div.images-view-item').find_element(By.CSS_SELECTOR, 'img').get_attribute('src')
major_img_src = major_img_src.replace('_50x50.jpg_.webp','?type=m510')

##추가이미지
view_img_all_p = driver.find_elements(By.CSS_SELECTOR, 'div.images-view-item')

view_img_all = ''
for view_img in view_img_all_p[1:]:
    view_img_all = view_img_all + view_img.find_element(By.CSS_SELECTOR, 'img').get_attribute('src') + '\n'

view_img_all = view_img_all.replace('_50x50.jpg_.webp','?type=m510')
#print(option_image_name_all)
#print(price_all)

######배송######
##배송비용 누르기(모든 배송 보기위한것
sleep(1)
driver.find_element(By.XPATH, r'//*[@class="product-dynamic-shipping"]').click()


##모든 배송비용
all_shipping_charges = driver.find_elements(By.CSS_SELECTOR, 'div.dynamic-shipping')


sleep(3)
##추가 옵션 클릭
for ship_chk in all_shipping_charges[0:]:
    if 'AliExpress Standard Shipping' or 'AliExpress Selection Shipping' not in ship_chk.text:

            if driver.find_elements(By.CSS_SELECTOR, 'button.comet-btn comet-btn-text _3djqy'):
                      print('추가 클릭')
                      driver.find_element(By.CSS_SELECTOR, 'button.comet-btn comet-btn-text _3djqy').click()
                      sleep(1)


##각각의 배송비용
for ship in all_shipping_charges[0:]:
    if 'AliExpress Standard Shipping' or 'AliExpress Selection Shipping' in ship.text:
        #print('Standard Shipping')
        ship_pice_array = ship.find_elements(By.CSS_SELECTOR, 'strong')
        for ship_pice_text in ship_pice_array[0:]:
            ship_pice_text = ship_pice_text.text
            if '무료 배송' in ship_pice_text:
            #print(ship_pice_text)
                ship_pice = '0'
                ship_pice = int(ship_pice)
            elif '5일 배송' in ship_pice_text: 
                print()
            else:
                ship_pice_text_change1 = ship_pice_text.replace('배송:₩ ','')
                ship_pice_text_change2 = ship_pice_text_change1.replace(',','')
                ship_pice = int(ship_pice_text_change2)
                #print('가격')
                #print(ship_pice)
    else:
        #print('not')
        sleep(1)
        

##배송비 닫기
sleep(1)
driver.find_element(By.XPATH, r'//*[@class="comet-icon comet-icon-close "]').click()
sleep(1)


##옵션 이미지
optional_image_all = driver.find_elements(By.CSS_SELECTOR, 'div.sku-property-image')
option_top_code = '<div class="se-component se-text se-l-default" id="SE-0796e3d9-00b5-47a3-bbf8-b32bcf946d54"><div class="se-component-content"><div class="se-section se-section-text se-l-default"><div class="se-module se-module-text"><!-- SE-TEXT { --><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-41e79b12-a5fb-4e49-9b6c-525ce21f9b34"><span style="" class="se-fs- se-ff-   " id="SE-316e23b7-5b2c-4a62-9749-e1861a5ab894"></span></p><!-- } SE-TEXT --><!-- SE-TEXT { --><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-2a7644d9-9cb0-4dcf-8ac6-b2d0089f4f83"><span style="" class="se-fs-fs30 se-ff-   " id="SE-a7e4c928-67a5-41e3-b5d6-2686442d0a09"><b>옵션 설명</b></span></p><!-- } SE-TEXT --><!-- SE-TEXT { --><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-0c2e5182-e11d-4e42-a041-c488f99ec359"><span style="" class="se-fs- se-ff-   " id="SE-526b1649-5224-4da4-bf6d-44131b2cc600"> </span></p><!-- } SE-TEXT --></div></div></div></div>'
option_bottom_code = '<div class="se-component se-horizontalLine se-l-default" id="SE-947f3b33-cd44-49b0-99a9-5c375a9770a3"><div class="se-component-content"><div class="se-section se-section-horizontalLine se-l-default se-section-align-center"><div class="se-module se-module-horizontalLine"><hr class="se-hr"></div></div></div></div><div class="se-component se-text se-l-default" id="SE-1f8b7851-9ad8-4cdd-9e57-dac0ce484fb4"><div class="se-component-content"><div class="se-section se-section-text se-l-default"><div class="se-module se-module-text"><!-- SE-TEXT { --><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-2e68f8cd-4233-4702-9689-46e1a82301b8"><span style="" class="se-fs-fs30 se-ff-   " id="SE-ca7a8937-3200-4f3d-89e8-d7eb6f81f6b0"><b>상세 페이지</b></span></p><!-- } SE-TEXT --><!-- SE-TEXT { --><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-2bfcf5ae-710a-4b53-8255-2c4cb53ab097"><span style="" class="se-fs- se-ff-   " id="SE-87258472-71dc-4537-beb2-0d09a1a78503"></span></p><!-- } SE-TEXT --><!-- SE-TEXT { --><p class="se-text-paragraph se-text-paragraph-align- " style="" id="SE-21887640-2ddd-45b6-8431-0e3413f38ae7"><span style="" class="se-fs- se-ff-   " id="SE-f714936e-6724-44e5-a06a-98215a05a066"></span></p><!-- } SE-TEXT --></div></div></div></div>'



option_imange_number = len(optional_image_all)
option_box_number = math.trunc(option_imange_number / 2)

plus = 0

option_box_inner = ''
    
 
for num_box in range(option_box_number):
    
    option_box_img1 = optional_image_all[plus].find_element(By.CSS_SELECTOR,'img').get_attribute('src')
    option_box_img1 = option_box_img1.replace('_50x50.jpg_.webp','')
    option_box_name1 = optional_image_all[plus].find_element(By.CSS_SELECTOR,'img').get_attribute('alt')
    plus = plus + 1

    option_box_img2 = optional_image_all[plus].find_element(By.CSS_SELECTOR,'img').get_attribute('src')
    option_box_img2 = option_box_img2.replace('_50x50.jpg_.webp','')
    option_box_name2 = optional_image_all[plus].find_element(By.CSS_SELECTOR,'img').get_attribute('alt')    
    plus = plus + 1    

    option_box_inner = option_box_inner + '<div class="se-component se-table se-l-default __se-component" id="SE-a2fc2af0-3782-4ced-a52c-400e871f0e6f"><div class="se-component-content"><div class="se-section se-section-table se-l-default se-section-align-" style="width: 100%;"><div class="se-table-container"><table class="se-table-content" style=""><tbody><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 50.0%; height: 40.0px;  "><div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-ceb48d99-aee3-4819-8f2f-b21d754f36cf"><span class="se-ff- se-fs- se-inline-image"><a class="se-module se-module-image __se_image_link __se_link" onclick="return false;" data-linktype="img" data-linkdata="{&quot;id&quot;:&quot;SE-f76bf252-0686-44c5-9d4c-e64ce0228bcf&quot;,&quot;src&quot;:&quot;https://shop-phinf.pstatic.net/20221025_80/1666657266643KfDbq_JPEG/67793109357474814_1355538267.jpg&quot;,&quot;originalWidth&quot;:&quot;233&quot;,&quot;originalHeight&quot;:&quot;214&quot;,&quot;linkUse&quot;:&quot;false&quot;,&quot;link&quot;:&quot;&quot;}" area-hidden="true"><img class="se-inline-image-resource" src="' + option_box_img1 + '?type=w860" data-src="' + option_box_img1 + '?type=w860" alt="" style="max-width: 233px"></a></span></p></div>   </td><td class="se-cell" colspan="1" rowspan="1" style="width: 50.0%; height: 40.0px;  "><div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-9c060709-660d-44aa-811a-41f86102e6a5"><span class="se-ff- se-fs- se-inline-image"><a class="se-module se-module-image __se_image_link __se_link" onclick="return false;" data-linktype="img" data-linkdata="{&quot;id&quot;:&quot;SE-7bd5bc46-2006-42f9-9f27-1d4e0179cde9&quot;,&quot;src&quot;:&quot;https://shop-phinf.pstatic.net/20221025_253/166665726859548xEk_JPEG/67793111306445847_1087617158.jpg&quot;,&quot;originalWidth&quot;:&quot;233&quot;,&quot;originalHeight&quot;:&quot;214&quot;,&quot;linkUse&quot;:&quot;false&quot;,&quot;link&quot;:&quot;&quot;}" area-hidden="true"><img class="se-inline-image-resource" src="' + option_box_img2 + '?type=w860" data-src="' + option_box_img2 + '?type=w860" alt="" style="max-width: 233px"></a></span></p></div></td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 50.0%; height: 40.0px;  "><div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-1636234a-5c7a-4d41-a039-db63a99b4508"><span style="" class="se-fs-fs24 se-ff-   " id="SE-96f59a24-f1dd-41c6-ac59-cdb07a478cb5"><b>'+ option_box_name1 + '</b></span></p></div></td><td class="se-cell" colspan="1" rowspan="1" style="width: 50.0%; height: 40.0px;  "><div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-3b30c690-bd3d-4b56-a3f2-2eadce3797d3"><span style="" class="se-fs-fs24 se-ff-   " id="SE-7e35a739-d215-4417-b320-6ed9a7a99d5e"><b>' + option_box_name2 + '</b></span></p></div>               </td></tr></tbody></table></div></div></div><script type="text/data" class="__se_module_data" data-module="{&quot;type&quot;:&quot;v2_table&quot;, &quot;id&quot; : &quot;SE-a2fc2af0-3782-4ced-a52c-400e871f0e6f&quot;, &quot;data&quot;: { &quot;columnCount&quot; : &quot;2&quot; }}"></script></div>'

if len(optional_image_all) % 2 != 0:   
    option_box_img1 = optional_image_all[plus].find_element(By.CSS_SELECTOR,'img').get_attribute('src')
    option_box_img1 = option_box_img1.replace('_50x50.jpg_.webp','')
    option_box_name1 = optional_image_all[plus].find_element(By.CSS_SELECTOR,'img').get_attribute('alt')      
    
    option_box_inner = option_box_inner + '<div class="se-component se-table se-l-default __se-component" id="SE-a2fc2af0-3782-4ced-a52c-400e871f0e6f"><div class="se-component-content"><div class="se-section se-section-table se-l-default se-section-align-" style="width: 100%;"><div class="se-table-container"><table class="se-table-content" style=""><tbody><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 50.0%; height: 40.0px;  "><div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-ceb48d99-aee3-4819-8f2f-b21d754f36cf"><span class="se-ff- se-fs- se-inline-image"><a class="se-module se-module-image __se_image_link __se_link" onclick="return false;" data-linktype="img" data-linkdata="{&quot;id&quot;:&quot;SE-f76bf252-0686-44c5-9d4c-e64ce0228bcf&quot;,&quot;src&quot;:&quot;https://shop-phinf.pstatic.net/20221025_80/1666657266643KfDbq_JPEG/67793109357474814_1355538267.jpg&quot;,&quot;originalWidth&quot;:&quot;233&quot;,&quot;originalHeight&quot;:&quot;214&quot;,&quot;linkUse&quot;:&quot;false&quot;,&quot;link&quot;:&quot;&quot;}" area-hidden="true"><img class="se-inline-image-resource" src="' + option_box_img1 + '?type=w860" data-src="' + option_box_img1 + '?type=w860" alt="" style="max-width: 233px"></a></span></p></div>   </td><td class="se-cell" colspan="1" rowspan="1" style="width: 50.0%; height: 40.0px;  "><div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-9c060709-660d-44aa-811a-41f86102e6a5"><span class="se-ff- se-fs- se-inline-image"><a class="se-module se-module-image __se_image_link __se_link" onclick="return false;" data-linktype="img" data-linkdata="{&quot;id&quot;:&quot;SE-7bd5bc46-2006-42f9-9f27-1d4e0179cde9&quot;,&quot;src&quot;:&quot;https://shop-phinf.pstatic.net/20221025_253/166665726859548xEk_JPEG/67793111306445847_1087617158.jpg&quot;,&quot;originalWidth&quot;:&quot;233&quot;,&quot;originalHeight&quot;:&quot;214&quot;,&quot;linkUse&quot;:&quot;false&quot;,&quot;link&quot;:&quot;&quot;}" area-hidden="true"></a></span></p></div></td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 50.0%; height: 40.0px;  "><div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-1636234a-5c7a-4d41-a039-db63a99b4508"><span style="" class="se-fs-fs24 se-ff-   " id="SE-96f59a24-f1dd-41c6-ac59-cdb07a478cb5"><b>'+ option_box_name1 + '</b></span></p></div></td><td class="se-cell" colspan="1" rowspan="1" style="width: 50.0%; height: 40.0px;  "><div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-3b30c690-bd3d-4b56-a3f2-2eadce3797d3"><span style="" class="se-fs-fs24 se-ff-   " id="SE-7e35a739-d215-4417-b320-6ed9a7a99d5e"><b></b></span></p></div>               </td></tr></tbody></table></div></div></div><script type="text/data" class="__se_module_data" data-module="{&quot;type&quot;:&quot;v2_table&quot;, &quot;id&quot; : &quot;SE-a2fc2af0-3782-4ced-a52c-400e871f0e6f&quot;, &quot;data&quot;: { &quot;columnCount&quot; : &quot;2&quot; }}"></script></div>'


option_box_end = option_top_code + option_box_inner + option_bottom_code





#print(optional_image_all)

##옵션 가격 및 판매가 구하기
price_all = ''
option_image_name_all = ''
first_price = int(0)

for option_image in optional_image_all[0:]:
    option_image.click()
    option_image_name = option_image.find_element(By.CSS_SELECTOR, 'img').get_attribute('alt')

    ##옵션 이름 전부
    option_image_name_all = option_image_name_all + option_image_name + ','


    ##상품가격
    if driver.find_elements(By.CSS_SELECTOR, 'span.product-price-value'):
        price_txt = driver.find_element(By.CSS_SELECTOR, 'span.product-price-value').text       
    elif driver.find_elements(By.CSS_SELECTOR, 'span.uniform-banner-box-price'):
        price_txt = driver.find_element(By.CSS_SELECTOR, 'span.uniform-banner-box-price').text

    price_origin = price_txt
    #print(price_origin)
    price_change1 = price_origin.replace('₩ ','')
    price = price_change1.replace(',','')
    
    price_int = int(price) 
    price_add_ship_origin = price_int + ship_pice
    
    ##판매가
    price_add_ship = price_add_ship_origin * 1.4
    
    ##판매가 정수
    price_add_ship_round = round(price_add_ship, -2)

    ##내 수익
    price_my_money = price_add_ship - price_add_ship_origin

    if price_my_money < 6000:
        price_add_end = 6000 + price_add_ship_origin
    else:
        price_add_end = price_add_ship_round

    price_add_end = math.ceil(price_add_end)
    price_add_end = round(price_add_end,-2)

    price_add_end = price_add_end - first_price
 
    if optional_image_all[0] == option_image:
        price_all = price_all + '0' + ','
        first_price = price_add_end
    else:
        price_add_end = str(price_add_end)
        price_all = price_all + price_add_end + ','


##옵션없는 경우 판매가
if first_price == 0:
    if driver.find_elements(By.CSS_SELECTOR, 'span.product-price-value'):
        first_price_txt = driver.find_element(By.CSS_SELECTOR, 'span.product-price-value').text       
    elif driver.find_elements(By.CSS_SELECTOR, 'span.uniform-banner-box-price'):
        first_price_txt = driver.find_element(By.CSS_SELECTOR, 'span.uniform-banner-box-price').text

    first_price = first_price_txt
    first_price = first_price.replace('₩ ','')
    first_price = first_price.replace(',','')
    first_price = int(first_price)
    first_price_add_ship = first_price + ship_pice
    price_add_end = first_price_add_ship * 1.4
    
    ##내 수익
    price_my_money = price_add_end - first_price

    if price_my_money < 6000:
        first_price = 6000 + first_price
    else:
        first_price = price_add_end

    first_price = math.ceil(first_price)
    first_price = round(first_price,-2)


###상세이미지 수집
##상세이미지 있는 개요 찾기
find_outline = driver.find_elements(By.CSS_SELECTOR, 'span.tab-inner-text')

just_calculator = 1
exel_data=[]
img_src_all = '<center><div class="se-viewer se-theme-default" lang="ko-KR"><div><img src="https://shop-phinf.pstatic.net/20221011_150/1665498732083sdHXH_JPEG/66634565892921623_1423703771.jpg?type=w860" data-src="https://shop-phinf.pstatic.net/20221011_150/1665498732083sdHXH_JPEG/66634565892921623_1423703771.jpg?type=w860" alt="" class="se-image-resource"></div><br>' + option_box_end


##상세이미지 있는 개요 찾아서 누르기
for b in find_outline[0:]:
    #print(b.text)


    if just_calculator == 5:
          sleep(1)
          b.click()
          sleep(1)
          print('ajsfhkdjfhjskfhjkfhaskjfhdkjhfakjhsakjfhsfjkhasfkdsjfhskjfhsdkfkj')
          img_all_1 = driver.find_element(By.CSS_SELECTOR, 'div.product-overview').find_elements(By.CSS_SELECTOR, 'p')
          for img_all_2 in img_all_1[0:]:
            if img_all_2.find_elements(By.CSS_SELECTOR, 'img'):
                for img_src in img_all_2.find_elements(By.CSS_SELECTOR, 'img')[0:]:
                    img_src_all = img_src_all + '<div><img style="display:block;" src="'+ img_src.get_attribute('src') + '?type=w860" alt="" class="se-image-resource">></div>'      


    sleep(1)


    just_calculator = just_calculator+1

print('타이틀')
print(title)
print()
print('판매가')
print(first_price)
print()
print('옵션가격 전부')
print(price_all)
print()
print('옵션들 이름')
print(option_image_name_all)
print()
print('대표이미지')
print(major_img_src)
print()
print('추가이미지')
print(view_img_all)
print()
print('상세페이지 url')
print(img_src_all)
print()
print('배송비')
print(ship_pice)



#exel_data_easy = []

#exel_data_easy.append({
#               'id' : '',
#               '상세설명':img_src_all,
#               '상품명' : title,
#               '판매가' : '',
#               '옵션값' : option_image_name_all,
#               '옵션가' : price_all,
#            })


#exel_data.append({
#               '판매자 상품코드' : '',
#               '카테고리코드' : '50003307',
#               '상세설명':img_src_all,
#               '상품명' : title,
#               '상품상태' : '신상품',
#               '판매가' : '',
#               '부가세' : '과세상품',
#               '재고수량' : '999',
#               '옵션형태' : '조합형',
#               '옵션값' : '',
#               '옵션가' : '',
#               '옵션 재고수량' : ''
#            })

#df = pd.read_excel('SupermarketSales.xlsx')
#df_exel = df
#pd.DataFrame(exel_data_easy).to_excel('aliex.xlsx',index=False)