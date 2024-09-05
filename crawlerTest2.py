import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# path = 'https://www.musinsa.com/snap/1237570978707323432'
path = 'https://www.musinsa.com/snap/profile/snap?profile_id=1234726971656693004&snap_id=1268021161197507776'

driver = webdriver.Chrome()
driver.get(path)
time.sleep(1)


print()
print('////////////////////////////////////////')

# element = driver.find_element(By.CSS_SELECTOR, '//*[@id="commonLayoutContainer"]/main/div/div[3]/div/div/div')
# //*[@id="commonLayoutContainer"]/main/div/div[3]/div/div/div/div[1]
cnt = 10
idx = 1
ex = 0
Y = 0
while(idx <= cnt):
    # # 방향키로 스크롤
    # driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    # time.sleep(1)

    Y += 200
    driver.execute_script(f"window.scrollTo(0, {Y})")
    driver.implicitly_wait(2)

    try:
        parent = driver.find_element(By.XPATH, f'//*[@id="commonLayoutContainer"]/main/div/div[3]/div/div/div')
        child = parent.find_elements(By.XPATH, './/div[@data-index]')

        for c in child:
            dataIndex = int(c.get_attribute("data-index"))
            print(f'data-index: {dataIndex}')

            list = c.find_element(By.XPATH,
                                  f'//*[@id="commonLayoutContainer"]/main/div/div[3]/div/div/div/div[{dataIndex+1}]/div/div[5]')
            print(list.text)
            print()
            idx += 1

        # p = driver.find_element(By.XPATH, f'//*[@id="commonLayoutContainer"]/main/div/div[3]/div/div/div/div[{idx}]')
        # print(idx)
        # print(p)
        # print(p.size['height'])
        list = p.find_element(By.XPATH, f'//*[@id="commonLayoutContainer"]/main/div/div[3]/div/div/div/div[{idx}]/div/div[5]')
        print(list.text)
        print()
        idx += 1

        Y += p.size['height']
        driver.execute_script(f"window.scrollTo(0, {Y})")
        driver.implicitly_wait(2)

    except:
        ex += 1

