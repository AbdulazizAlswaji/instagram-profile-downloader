from selenium import webdriver
from selenium.webdriver.common.by import By
import wget
import time

driver = webdriver.Chrome()
username = #instagram username
password = # instagram user password
link = # https://www.instagram.com/tirryaq/


driver.get(link)
driver.find_element(By.CSS_SELECTOR, '[name="username"]').send_keys(username)
driver.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys(password)
driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

driver.get(link)

num = 1000
counter = 0
images = []
while counter < num:
    get_images = driver.execute_script("""
links=''; 
for (var i =0; i < document.getElementsByClassName('KL4Bh').length; i++) {
links += document.getElementsByClassName('KL4Bh')[i].children[0].src+ '||';
}
return links
""")
    for link in get_images.split('||'):
        try:
            if link in images:
                pass
            else:
                images.append(link)
                wget.download(link, 'output/' + str(counter) + '.jpg')
                counter = counter + 1
                if counter == num:
                    break
        except:
            pass
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
    time.sleep(5)
        
        
        
        
        
        
        
        
        
        