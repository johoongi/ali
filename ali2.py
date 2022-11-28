from selenium import webdriver
import bs4
from time import sleep
from selenium.webdriver.common.by import By
import pandas as pd
import math
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import aliexpresscrwaling as ali_p

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="~/ChromeProfile"'
driver = webdriver.Chrome(chrome_driver, options=chrome_options)
url = input()


driver.get(url)
soup = bs4.BeautifulSoup(driver.page_source, 'lxml')  #



###메인 실행
wait = input()

all_product = driver.find_elements(By.XPATH, r'//*[@class="' +wait+ '"]')

print(len(all_product))
smartsore_exel = []
cal_number = 0

for product_seperate in all_product[0:]:
    product_seperate.click()
    
    url_product = product_seperate.get_attribute('href')
    
    ##열린탭으로 전환
    driver.switch_to.window(driver.window_handles[-1])
 
    sleep(4)
    cal_number = cal_number + 1
    print(cal_number)
    
    try:
      attribute_ali_product = ali_p.seperate_product(driver)
      print('ok all is good')

      ##스마트스토어
      smartsore_exel.append({
                   '판매자 상품코드' : '',
                   '카테고리코드':'',
                   '상품명' : attribute_ali_product[0],
                   '상품상태' : '신상품',
                   '판매가' : attribute_ali_product[1],
                   '부가세' : '과세상품',
                   '재고수량' : '999',
                   '옵션형태' : '조합형',
                   '옵션명' : '모델\n옵션',
                   '옵션값' : 'AJK2673800\n' + attribute_ali_product[2],
                   '옵션가' : '0\n' + attribute_ali_product[3],
                   '옵션 재고수량' : '999',
                   '직접입력 옵션' : '',
                   '추가상품명' : '',
                   '추가상품값' : '',
                   '추가상품가' : '',
                   '추가상품 재고수량' : '',
                   '대표이미지' : attribute_ali_product[4],
                   '추가이미지' : attribute_ali_product[5],
                   '상세설명' : attribute_ali_product[6],
                   '브랜드' : '',
                   '제조사' : '',
                   '제조일자' : '',
                   '유효일자' : '',    
                   '원산지코드' : "'0200037",    
                   '수입사' : '아므미 협력사',    
                   '복수원산지여부' : '',    
                   '원산지 직접입력' : '',    
                   '미성년자 구매' : 'Y',    
                   '배송비 템플릿코드' : '',    
                   '배송방법' : '택배‚ 소포‚ 등기',    
                   '택배사코드' : '',    
                   '배송비유형' : '무료',    
                   '기본배송비' : '',    
                   '배송비 결제방식' : '',    
                   '조건부무료-\n상품판매가 합계' : '',    
                   '수량별부과-수량' : '',    
                   '구간별-\n2구간수량' : '',    
                   '구간별-\n3구간수량' : '',    
                   '구간별-\n3구간배송비' : '',    
                   '구간별-\n추가배송비' : '',    
                   '반품배송비' : '15000',    
                   '교환배송비' : '30000',    
                   '지역별 차등 배송비' : '',    
                   '별도설치비' : '',    
                   '상품정보제공고시 템플릿코드' : '',    
                   '상품정보제공고시\n품명' : '', 
                   '상품정보제공고시\n모델명' : '', 
                   '상품정보제공고시\n인증허가사항' : '', 
                   '상품정보제공고시\n제조자' : '', 
                   'A/S 템플릿코드' : '', 
                   'A/S 전화번호' : '02-0000-0000', 
                   'A/S 안내' : '02-0000-0000', 
                   '현재 url(이건 삭제하고 복붙)' : attribute_ali_product[7]
                })
    except:
      print('오류')
    
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


##스마트스토어
pd.DataFrame(smartsore_exel).to_excel('smartsore.xlsx',index=False)