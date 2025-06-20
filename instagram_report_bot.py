from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Credentials (use test accounts only)
USERNAME = 'hukkum925'
PASSWORD = 'hackerbro'
TARGET_USERNAME = 'manik_now'

# Chrome setup
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
# options.add_argument("--headless")  # Optional for CLI-only use

driver = webdriver.Chrome(options=options)

def login():
    print("[*] Logging into Instagram...")
    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(10)
    driver.find_element(By.NAME, 'username').send_keys(USERNAME)
    driver.find_element(By.NAME, 'password').send_keys(PASSWORD + Keys.RETURN)
    time.sleep(10)
    print("[+] Login successful.")

def report_account():
    print(f"[*] Navigating to @{TARGET_USERNAME}'s profile...")
    driver.get(f'https://www.instagram.com/{TARGET_USERNAME}/')
    time.sleep(15)

    print("[*] Opening report menu...")
    try:
        buttons = driver.find_elements(By.TAG_NAME, "button")
        for button in buttons:
            if "Options" in button.get_attribute("aria-label") or button.text == "⋯":
                button.click()
                break
        time.sleep(25)

        print("[*] Clicking 'Report'...")
        driver.find_element(By.XPATH, '//button[contains(text(), "Report")]').click()
        time.sleep(20)

        print("[*] Selecting reason 'It’s inappropriate'...")
        driver.find_element(By.XPATH, '//button[contains(text(), "It’s inappropriate")]').click()
        time.sleep(16)

        print("[*] Selecting sub-reason 'Spam'...")
        driver.find_element(By.XPATH, '//button[contains(text(), "Spam")]').click()
        print("[+] One report sent (educational use only).")
    except Exception as e:
        print(f"[!] Report attempt failed: {e}")

def main():
    try:
        login()
        for i in range(5):
            print(f"\n--- Report Attempt {i+1}/5 ---")
            report_account()
            time.sleep(5)  # Pause to reduce detection risk
    except Exception as e:
        print(f"[!] Error: {e}")
    finally:
        driver.quit()
        print("[*] Finished all report attempts.")

if __name__ == "__main__":
    main()
