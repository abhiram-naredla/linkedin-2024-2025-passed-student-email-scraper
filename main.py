import os
import pandas as pd
import logging
import random
import time

from datetime import datetime
from dotenv import load_dotenv

from linkedin_login import (
    get_driver,
    login_to_linkedin
)

from scraper import (
    search_students,
    collect_valid_profiles
)

# Logging setup
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log"),
        logging.StreamHandler()
    ]
)


def main():

    load_dotenv()

    # Config
    search_query = os.getenv(
        "SEARCH_QUERY",
        "student"
    )

    target_years = os.getenv(
        "GRAD_YEARS",
        "2024,2025"
    ).split(",")

    target_email_count = int(
        os.getenv("MAX_PROFILES", 5)
    )

    logging.info(
        "--- Starting LinkedIn Student Scraper ---"
    )

    driver = get_driver()

    try:

        # LOGIN
        success = login_to_linkedin(driver)

        if not success:

            logging.error(
                "LinkedIn login failed."
            )

            return

        logging.info(
            "Login successful."
        )

        # SEARCH
        search_success = search_students(
            driver,
            query=search_query,
            grad_years=target_years
        )

        if not search_success:

            logging.error(
                "Search failed."
            )

            return

        logging.info(
            "Search completed successfully."
        )

        # COLLECT VALID EMAILS
        logging.info(
            f"Searching for {target_email_count} valid emails..."
        )

        results = collect_valid_profiles(
            driver,
            target_count=target_email_count
        )

        # SAVE RESULTS
        if results:

            os.makedirs("data", exist_ok=True)

            df = pd.DataFrame(results)

            timestamp = datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )

            output_file = (
                f"data/output_{timestamp}.csv"
            )

            df.to_csv(
                output_file,
                index=False
            )

            df.to_csv(
                "data/output.csv",
                index=False
            )

            logging.info(
                f"Saved {len(results)} valid email records."
            )

            logging.info(
                f"Output file: {output_file}"
            )

        else:

            logging.warning(
                "No valid emails found."
            )

    except KeyboardInterrupt:

        logging.warning(
            "Process interrupted by user."
        )

    except Exception as e:

        logging.critical(
            f"Main loop error: {e}"
        )

    finally:

        logging.info(
            "Closing browser..."
        )

        driver.quit()

        logging.info(
            "--- Scraping Session Completed ---"
        )


if __name__ == "__main__":

    main()