import os
import time
import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


# =========================================================
# CREATE DRIVER
# =========================================================

def get_driver():

    chrome_options = Options()

    headless_mode = os.getenv(
        "HEADLESS",
        "false"
    ).lower() == "true"

    if headless_mode:

        chrome_options.add_argument(
            "--headless=new"
        )

    chrome_options.add_argument(
        "--start-maximized"
    )

    chrome_options.add_argument(
        "--disable-blink-features=AutomationControlled"
    )

    chrome_options.add_experimental_option(
        "excludeSwitches",
        ["enable-automation"]
    )

    chrome_options.add_experimental_option(
        "useAutomationExtension",
        False
    )

    chrome_options.add_argument(
        "--disable-infobars"
    )

    chrome_options.add_argument(
        "--disable-notifications"
    )

    chrome_options.add_argument(
        "--disable-popup-blocking"
    )

    chrome_options.add_argument(
        "--no-sandbox"
    )

    chrome_options.add_argument(
        "--disable-dev-shm-usage"
    )

    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        ),
        options=chrome_options
    )

    driver.maximize_window()

    return driver


# =========================================================
# LOGIN FUNCTION
# =========================================================

def login_to_linkedin(driver):

    email = os.getenv("LINKEDIN_EMAIL")
    password = os.getenv("LINKEDIN_PASSWORD")

    try:

        logging.info(
            "Opening LinkedIn..."
        )

        driver.get(
            "https://www.linkedin.com/login"
        )

        time.sleep(8)

        # ==================================================
        # EMAIL FIELD
        # ==================================================

        email_field = None

        possible_email_fields = [

            "//input[@id='username']",

            "//input[@name='session_key']",

            "//input[@type='email']",

            "//input[contains(@autocomplete,'username')]",

            "//input[contains(@placeholder,'Email')]",

            "//input[contains(@placeholder,'email')]"
        ]

        for xpath in possible_email_fields:

            try:

                elements = driver.find_elements(
                    By.XPATH,
                    xpath
                )

                if len(elements) > 0:

                    email_field = elements[0]

                    break

            except:
                pass

        if not email_field:

            logging.error(
                "Email field not found."
            )

            return False

        logging.info(
            "Entering email..."
        )

        email_field.click()

        time.sleep(1)

        email_field.clear()

        time.sleep(1)

        email_field.send_keys(email)

        time.sleep(2)

        # ==================================================
        # PASSWORD FIELD
        # ==================================================

        password_field = None

        possible_password_fields = [

            "//input[@id='password']",

            "//input[@name='session_password']",

            "//input[@type='password']",

            "//input[contains(@placeholder,'Password')]"
        ]

        for xpath in possible_password_fields:

            try:

                elements = driver.find_elements(
                    By.XPATH,
                    xpath
                )

                if len(elements) > 0:

                    password_field = elements[0]

                    break

            except:
                pass

        if not password_field:

            logging.error(
                "Password field not found."
            )

            return False

        logging.info(
            "Entering password..."
        )

        password_field.click()

        time.sleep(1)

        password_field.clear()

        time.sleep(1)

        password_field.send_keys(password)

        time.sleep(2)

        # ==================================================
        # LOGIN BUTTON
        # ==================================================

        login_button = None

        possible_buttons = [

            "//button[@type='submit']",

            "//button[contains(.,'Sign in')]",

            "//button[contains(.,'Login')]",

            "//button[contains(.,'Continue')]"
        ]

        for xpath in possible_buttons:

            try:

                buttons = driver.find_elements(
                    By.XPATH,
                    xpath
                )

                if len(buttons) > 0:

                    login_button = buttons[0]

                    break

            except:
                pass

        if not login_button:

            logging.error(
                "Login button not found."
            )

            return False

        logging.info(
            "Clicking login button..."
        )

        driver.execute_script(
            "arguments[0].click();",
            login_button
        )

        time.sleep(15)

        logging.info(
            f"Current URL: {driver.current_url}"
        )

        # ==================================================
        # LOGIN SUCCESS CHECK
        # ==================================================

        if (
            "feed" in driver.current_url
            or "checkpoint" in driver.current_url
            or "mynetwork" in driver.current_url
        ):

            logging.info(
                "LinkedIn login successful."
            )

            return True

        logging.error(
            "LinkedIn login failed."
        )

        return False

    except Exception as e:

        logging.error(
            f"Login error: {e}"
        )

        return False