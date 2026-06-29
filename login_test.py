from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 20)

driver.get("https://cbd-courierbidz.iihdev.com/login")

# ---------------- Email ----------------
email = wait.until(
    EC.element_to_be_clickable((By.ID, "email"))
)

email.clear()

for ch in "kashishiih@yopmail.com":
    email.send_keys(ch)
    time.sleep(0.08)

# ---------------- Password ----------------
password = wait.until(
    EC.element_to_be_clickable((By.ID, "password"))
)

password.clear()

for ch in "Test@123":
    password.send_keys(ch)
    time.sleep(0.08)

time.sleep(1)

# Login Button
login_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
)
login_btn.click()

print("Login successful")

# ---------- Wait for Dashboard ----------
time.sleep(5)

# ---------- Open Profile Dropdown ----------
profile_dropdown = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "//*[contains(text(),'Kashish')]"
        )
    )
)

profile_dropdown.click()

print("Profile dropdown opened")

time.sleep(2)

# ---------- Click Sign Out ----------
signout_btn = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "//*[contains(text(),'Sign Out')]"
        )
    )
)

signout_btn.click()

print("Sign Out clicked")

# ---------- Verify Logout ----------
time.sleep(5)

print("Current URL after logout:", driver.current_url)

# ---------- Close Browser ----------
driver.quit()