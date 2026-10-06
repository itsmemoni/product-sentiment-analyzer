from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


url = "https://testingurl.dev/scraping/structured-data/product-microdata"
options = Options()

options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")


driver = webdriver.Chrome(options=options)


try:

    print("Opening page...")
    driver.get(url)

    time.sleep(5)


    # =====================================================
    # PAGE INFORMATION
    # =====================================================

    print("\n========== PAGE INFORMATION ==========")

    print("TITLE:", driver.title)

    print("URL:", driver.current_url)


    # =====================================================
    # PRODUCT INFORMATION
    # =====================================================

    print("\n========== PRODUCT INFORMATION ==========")

    product_selectors = [

        "h1",

        "h2",

        "h3",

        ".caption h4",

        ".caption h3",

        ".product-title",

        "[itemprop='name']",

        "[class*='product']",

    ]


    for selector in product_selectors:

        elements = driver.find_elements(
            By.CSS_SELECTOR,
            selector
        )

        if elements:

            print(
                f"\nSELECTOR: {selector}"
            )

            for i, element in enumerate(
                elements[:10],
                start=1
            ):

                text = element.text.strip()

                if text:

                    print(
                        f"{i}. "
                        f"TAG={element.tag_name} "
                        f"CLASS={element.get_attribute('class')}"
                    )

                    print(
                        "   TEXT:",
                        text[:500]
                    )


    # =====================================================
    # REVIEW INFORMATION
    # =====================================================

    print("\n========== REVIEW INFORMATION ==========")


    review_selectors = [

        "[itemprop='reviewBody']",

        "[class*='review']",

        "[class*='Review']",

        "[id*='review']",

        "[id*='Review']",

        "[class*='comment']",

        "[class*='Comment']",

        "[class*='feedback']",

        "[class*='Feedback']",

    ]


    for selector in review_selectors:

        elements = driver.find_elements(
            By.CSS_SELECTOR,
            selector
        )

        if elements:

            print(
                f"\nSELECTOR: {selector}"
            )

            print(
                "COUNT:",
                len(elements)
            )

            for i, element in enumerate(
                elements[:10],
                start=1
            ):

                text = element.text.strip()

                print(
                    f"\n--- ELEMENT {i} ---"
                )

                print(
                    "TAG:",
                    element.tag_name
                )

                print(
                    "CLASS:",
                    element.get_attribute(
                        "class"
                    )
                )

                print(
                    "TEXT:",
                    text[:1000]
                )


    # =====================================================
    # TEXT CONTAINING REVIEW KEYWORDS
    # =====================================================

    print(
        "\n========== REVIEW KEYWORD SEARCH =========="
    )


    body_text = driver.find_element(
        By.TAG_NAME,
        "body"
    ).text


    lines = body_text.splitlines()


    keywords = [
        "review",
        "reviews",
        "rating",
        "ratings",
        "comment",
        "comments",
    ]


    matching_lines = []


    for line in lines:

        line = line.strip()

        if not line:
            continue

        lower_line = line.lower()

        if any(
            keyword in lower_line
            for keyword in keywords
        ):

            matching_lines.append(line)


    print(
        "Matching lines:",
        len(matching_lines)
    )


    for line in matching_lines[:50]:

        print(
            "-",
            line[:500]
        )


    # =====================================================
    # JSON-LD
    # =====================================================

    print(
        "\n========== JSON-LD =========="
    )


    scripts = driver.find_elements(
        By.XPATH,
        "//script[@type='application/ld+json']"
    )


    print(
        "JSON-LD scripts:",
        len(scripts)
    )


    for i, script in enumerate(
        scripts,
        start=1
    ):

        content = script.get_attribute(
            "textContent"
        )

        if content:

            print(
                f"\n--- JSON-LD {i} ---"
            )

            print(
                content[:3000]
            )


finally:

    driver.quit()

    print(
        "\nBrowser closed."
    )