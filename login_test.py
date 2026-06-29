from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ---------------- Chrome ----------------
driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 20)

# ---------------- Open Login Page ----------------
driver.get("https://cbd-courierbidz.iihdev.com/login")

# ---------------- Enter Email ----------------
email = wait.until(
    EC.visibility_of_element_located(
        (By.NAME, "email")
    )
)

email.clear()
email.send_keys("kashishqa.iihglobal@gmail.com")

# ---------------- Enter Password ----------------
password = wait.until(
    EC.visibility_of_element_located(
        (By.NAME, "password")
    )
)

password.clear()
password.send_keys("Test@123")

# ---------------- Click Login ----------------
login_btn = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit']")
    )
)

login_btn.click()

# ---------------- Wait for Dashboard ----------------
wait.until(
    EC.url_contains("/dashboard")
)

print("Login successful")

# ---------------- Screenshot ----------------
driver.save_screenshot("after_login.png")

time.sleep(5)

# driver.quit()