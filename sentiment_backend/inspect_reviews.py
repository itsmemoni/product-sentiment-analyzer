from scraper import create_driver
from selenium.webdriver.common.by import By
import time

url = "https://webscraper.io/test-sites/e-commerce/allinone/product/48"

driver = create_driver()

try:
    driver.get(url)
    time.sleep(3)

    print("\n========== PAGE INFO ==========")
    print("Title:", driver.title)
    print("URL:", driver.current_url)

    print("\n========== TEXT CONTAINING 'REVIEW' ==========")

    elements = driver.find_elements(
        By.XPATH,
        "//*[contains(translate(normalize-space(.), "
        "'ABCDEFGHIJKLMNOPQRSTUVWXYZ', "
        "'abcdefghijklmnopqrstuvwxyz'), 'review')]"
    )

    for i, element in enumerate(elements[:30], start=1):
        try:
            text = element.text.strip()

            if text:
                print(f"\n{i}. TAG: {element.tag_name}")
                print("TEXT:", text[:500])

        except Exception:
            pass

    print("\n========== POSSIBLE REVIEW CLASSES ==========")

    elements = driver.find_elements(
        By.CSS_SELECTOR,
        "[class*='review'], [id*='review']"
    )

    for i, element in enumerate(elements[:30], start=1):
        print(
            f"{i}. tag={element.tag_name}, "
            f"class={element.get_attribute('class')}, "
            f"text={element.text[:300]}"
        )

finally:
    driver.quit()