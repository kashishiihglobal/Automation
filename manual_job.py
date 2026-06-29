from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# ---------- Helper ----------
def slow_type(element, text, delay=0.1):
    for char in text:
        element.send_keys(char)
        time.sleep(delay)

# ---------- Browser ----------
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.maximize_window()
wait = WebDriverWait(driver, 20)

# ---------- Login ----------
driver.get("https://cbd-courierbidz.iihdev.com/login")

email = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@type='email']")
    )
)

slow_type(email, "kashishiih@yopmail.com")

password = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@type='password']")
    )
)

slow_type(password, "Test@123")

login_btn = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit']")
    )
)

login_btn.click()

print("Login successful")

time.sleep(5)

# ---------- Manual Job Page ----------
driver.get(
    "https://cbd-courierbidz.iihdev.com/create-job?mode=manual"
)

# ---------- Pickup Address ----------
pickup = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "pickupAddress")
    )
)

pickup.clear()
pickup.send_keys("872 Oldham Rd, Rochdale")

time.sleep(2)

pickup.send_keys(Keys.ARROW_DOWN)
pickup.send_keys(Keys.ENTER)

print("Pickup selected")

# ---------- Delivery Address ----------
delivery = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "deliveryAddress")
    )
)

delivery.clear()
delivery.send_keys("966 Carmarthen Rd, Swansea")

time.sleep(5)

delivery.send_keys(Keys.ARROW_DOWN)
delivery.send_keys(Keys.ENTER)

print("Delivery selected")

# ---------- Pickup & Delivery Date/Time ----------

print("Opening Drop-off Calendar...")

dropoff_btn = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "(//button[@aria-haspopup='dialog'])[3]")
    )
)

driver.execute_script("arguments[0].scrollIntoView({block:'center'});", dropoff_btn)
time.sleep(1)

ActionChains(driver).move_to_element(dropoff_btn).pause(1).click().perform()

print("Drop-off Calendar Opened")

time.sleep(2)

dropoff_date = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='28' and not(@disabled)]")
    )
)

driver.execute_script("arguments[0].scrollIntoView(true);", dropoff_date)
time.sleep(1)

driver.execute_script("arguments[0].click();", dropoff_date)

print("Drop-off Date Selected")

time.sleep(2)

# Close Drop-off Calendar
ActionChains(driver).send_keys(Keys.ESCAPE).perform()

time.sleep(2)

# Pickup Time
try:
    popup_buttons[0].click()

    pickup_date = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[text()='27']")
        )
    )

    pickup_date.click()

    print("Pickup date selected")

except Exception as e:
    print("Pickup date already selected:", e)


# Delivery Date



# ---------- Delivery Date ----------

delivery_date_btn = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "(//button[@aria-haspopup='dialog'])[3]")
    )
)

driver.execute_script(
    "arguments[0].scrollIntoView({block:'center'});",
    delivery_date_btn
)

time.sleep(1)

driver.execute_script(
    "arguments[0].click();",
    delivery_date_btn
)

print("Delivery calendar opened")

wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//div[contains(@class,'rdp')]")
    )
)

time.sleep(1)

delivery_date = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='26']")
    )
)

driver.execute_script(
    "arguments[0].click();",
    delivery_date
)

print("Delivery date selected")

# Delivery Time
try:
    popup_buttons = driver.find_elements(
        By.XPATH,
        "//button[@aria-haspopup='dialog']"
    )

    popup_buttons[3].click()

    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[text()='ASAP']")
        )
    ).click()

    print("Delivery time selected")

except Exception as e:
    print("Delivery time selection skipped:", e)


# ---------- Pickup Time ----------

popup_buttons = driver.find_elements(
    By.XPATH,
    "//button[@aria-haspopup='dialog']"
)

popup_buttons[1].click()

time.sleep(1)

wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//*[text()='ASAP']")
    )
).click()

print("Pickup time selected")

time.sleep(2)

# ---------- Delivery Time ----------

popup_buttons = driver.find_elements(
    By.XPATH,
    "//button[@aria-haspopup='dialog']"
)

popup_buttons[3].click()

time.sleep(1)

wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//*[text()='ASAP']")
    )
).click()

print("Delivery time selected")

time.sleep(2)

# ---------- Delivery Time ----------

delivery_time_btn = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "(//button[@aria-haspopup='dialog'])[4]")
    )
)

delivery_time_btn.click()

time.sleep(1)

wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//*[text()='ASAP']")
    )
).click()

print("Delivery time selected")

time.sleep(2)

# ---------- Next ----------

next_btn = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(.,'Next')]")
    )
)

next_btn.click()

print("Next clicked")

# ---------- Next ----------
next_btn = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(.,'Next')]")
    )
)

next_btn.click()

print("Next clicked")

next_btn.click()

print("Next clicked")

time.sleep(3)

# ---------- Fill Numeric Fields ----------
number_fields = wait.until(
    EC.presence_of_all_elements_located(
        (By.XPATH, "//input[@type='number']")
    )
)

for field in number_fields:
    try:
        field.clear()
        field.send_keys("1")
    except Exception:
        pass

print(f"Filled {len(number_fields)} numeric fields")

time.sleep(2)

# ---------- Submit ----------
submit_btn = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(.,'Submit')]")
    )
)

submit_btn.click()

print("Submit clicked")

time.sleep(5)

# ---------- Skip & Publish ----------
skip_publish = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(.,'Skip & Publish')]")
    )
)

skip_publish.click()

print("Skip & Publish clicked")

time.sleep(8)

# ---------- My Loads ----------
driver.get("https://cbd-courierbidz.iihdev.com/my-loads")

print("Navigated to My Loads")

driver.save_screenshot("my_loads.png")

time.sleep(5)

# ---------- Logout ----------
try:
    profile_dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//*[contains(text(),'Kashish')]"
            )
        )
    )

    profile_dropdown.click()

    time.sleep(2)

    signout_btn = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//*[contains(text(),'Sign Out')]"
            )
        )
    )

    signout_btn.click()

    print("Logout successful")

except Exception as e:
    print("Logout locator needs adjustment:", e)

time.sleep(5)

# driver.quit()
