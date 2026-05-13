import time
import random
import logging
import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def search_students(
    driver,
    query="student",
    grad_years=["2024", "2025"]
):

    query_text = (
        f"{query} graduating {' '.join(grad_years)}"
    )

    search_url = (
        "https://www.linkedin.com/search/results/people/"
        f"?origin=GLOBAL_SEARCH_HEADER&keywords={query_text}"
    )

    logging.info(
        f"Opening: {search_url}"
    )

    driver.get(search_url)

    time.sleep(10)

    return True


def scroll_page(driver):

    last_height = driver.execute_script(
        "return document.body.scrollHeight"
    )

    while True:

        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

        time.sleep(4)

        new_height = driver.execute_script(
            "return document.body.scrollHeight"
        )

        if new_height == last_height:
            break

        last_height = new_height


def go_to_next_page(driver):

    try:

        time.sleep(3)

        # Scroll fully down first
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

        time.sleep(3)

        next_selectors = [

            # Main LinkedIn pagination next button
            "//button[@aria-label='Next']",

            # Alternative next button
            "//button[contains(@aria-label,'Next')]",

            # Sometimes it's a span/button combo
            "//span[text()='Next']/ancestor::button",

            # Pagination numeric next
            "//li[contains(@class,'artdeco-pagination__indicator--number')]/following-sibling::li[1]//button"
        ]

        next_button = None

        for xpath in next_selectors:

            try:

                buttons = driver.find_elements(
                    By.XPATH,
                    xpath
                )

                for btn in buttons:

                    if (
                        btn.is_displayed()
                        and btn.is_enabled()
                    ):

                        next_button = btn
                        break

                if next_button:
                    break

            except:
                pass

        if not next_button:

            logging.info(
                "No more pages found."
            )

            return False

        logging.info(
            "Clicking next page button..."
        )

        driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            next_button
        )

        time.sleep(2)

        driver.execute_script(
            "arguments[0].click();",
            next_button
        )

        time.sleep(8)

        return True

    except Exception as e:

        logging.error(
            f"Pagination error: {e}"
        )

        return False


def get_profile_urls(
    driver,
    max_pages=20
):

    urls = []

    for page in range(max_pages):

        logging.info(
            f"Scanning page {page + 1}"
        )

        # ==================================================
        # SLOW HUMAN-LIKE SCROLL
        # ==================================================

        for _ in range(15):

            driver.execute_script(
                "window.scrollBy(0, 1200);"
            )

            time.sleep(
                random.uniform(2, 4)
            )

        time.sleep(5)

        # ==================================================
        # GET PROFILE LINKS
        # ==================================================

        links = driver.find_elements(
            By.XPATH,
            "//a[contains(@href,'/in/')]"
        )

        logging.info(
            f"Found {len(links)} raw links."
        )

        for link in links:

            try:

                href = link.get_attribute("href")

                if href:

                    clean_url = href.split("?")[0]

                    if (
                        "linkedin.com/in/" in clean_url
                        and clean_url not in urls
                    ):

                        urls.append(clean_url)

            except:
                pass

        logging.info(
            f"Collected {len(urls)} unique profile URLs."
        )

        # ==================================================
        # NEXT PAGE
        # ==================================================

        moved = go_to_next_page(driver)

        if not moved:

            logging.info(
                "Pagination finished."
            )

            break

    return urls


def extract_profile_details(
    driver,
    profile_url
):

    details = {
        "Full Name": "N/A",
        "LinkedIn URL": profile_url,
        "Email ID": "N/A",
        "Phone Number": "N/A"
    }

    try:

        logging.info(
            f"Opening profile: {profile_url}"
        )

        driver.get(profile_url)

        time.sleep(random.uniform(5, 8))

        # ==================================================
        # NAME
        # ==================================================

        try:

            name = driver.find_element(
                By.TAG_NAME,
                "h1"
            ).text.strip()

            details["Full Name"] = name

        except:
            pass

        # ==================================================
        # CONTACT INFO
        # ==================================================

        try:

            contact_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//a[contains(@href,'overlay/contact-info')]"
                    )
                )
            )

            driver.execute_script(
                "arguments[0].click();",
                contact_button
            )

            time.sleep(3)

            # EMAIL
            try:

                email_element = driver.find_element(
                    By.XPATH,
                    "//section[contains(@class,'ci-email')]//a"
                )

                email = email_element.text.strip()

                if "@" in email:

                    details["Email ID"] = email

            except:
                pass

            # PHONE
            try:

                phone_element = driver.find_element(
                    By.XPATH,
                    "//section[contains(@class,'ci-phone')]//span"
                )

                details["Phone Number"] = (
                    phone_element.text.strip()
                )

            except:
                pass

        except:
            pass

        # ==================================================
        # BACKUP EMAIL EXTRACTION
        # ==================================================

        if details["Email ID"] == "N/A":

            page_text = driver.page_source

            emails = re.findall(
                r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(?:com|edu|org|net|in|io)\b',
                page_text
            )

            blocked_words = [
                "linkedin",
                ".png",
                ".jpg",
                ".jpeg",
                ".svg",
                "2x",
                "privacy",
                "terms",
                "policy"
            ]

            valid_emails = []

            for email in emails:

                lower_email = email.lower()

                if not any(
                    word in lower_email
                    for word in blocked_words
                ):

                    valid_emails.append(email)

            if valid_emails:

                details["Email ID"] = valid_emails[0]

    except Exception as e:

        logging.error(
            f"Profile extraction failed: {e}"
        )

    return details


def collect_valid_profiles(
    driver,
    target_count=5
):

    final_results = []

    urls = get_profile_urls(driver)

    logging.info(
        f"Total profile URLs collected: {len(urls)}"
    )

    checked = 0

    for profile_url in urls:

        if len(final_results) >= target_count:
            break

        checked += 1

        logging.info(
            f"Checking profile {checked}"
        )

        details = extract_profile_details(
            driver,
            profile_url
        )

        email = details["Email ID"]

        if (
            email != "N/A"
            and ".png" not in email
            and ".jpg" not in email
            and "linkedin" not in email
        ):

            logging.info(
                f"VALID EMAIL FOUND: {email}"
            )

            final_results.append(details)

        else:

            logging.info(
                "No valid email found."
            )

    logging.info(
        f"Collected {len(final_results)} valid emails."
    )

    return final_results