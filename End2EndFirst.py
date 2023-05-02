from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
# products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
products = driver.find_elements(By.XPATH, "//h4[@class='card-title']/a")

for product in products:
    if "Blackberry" in product.text:
        print(product.text)
        print("Found")
        product.find_element(By.XPATH, "//a[text()='"+product.text+"']/../../../div/button").click()


driver.execute_script("window.scrollTo(0, document.body.scrollTop);")



# wait = WebDriverWait(driver, 4)
# wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".nav-link.btn.btn-primary")))
driver.find_element(By.CSS_SELECTOR, ".nav-link.btn.btn-primary").click()
driver.find_element(By.CSS_SELECTOR,".btn.btn-success").click()