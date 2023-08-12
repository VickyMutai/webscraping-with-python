import time
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
    

options  = uc.ChromeOptions()
driver = uc.Chrome(use_subprocess=True) 

url = 'https://blog.hubspot.com/sales/famous-quotes'

# Open the URL
driver.get(url)
time.sleep(3)
quotelist = driver.find_element(By.CLASS_NAME,'hsg-featured-snippet__wrapper--content').text

output_file_path = 'output.txt'
with open(output_file_path, 'w') as output_file:
    output_file.write(quotelist)

print("Text written to", output_file_path)
