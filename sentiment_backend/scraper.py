from urllib.parse import urlparse
import json
import re
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def create_driver():
    options = Options()

    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    options.add_argument(
        "--window-size=1920,1080"
    )

    options.add_argument(
        "--disable-blink-features=AutomationControlled"
    )

    return webdriver.Chrome(options=options)


def get_product_data(url):
    driver = create_driver()

    try:
        driver.get(url)

        time.sleep(3)

        # -------------------------------------------------
        # 1. Check whether the website blocks automation
        # -------------------------------------------------

        page_text = driver.find_element(
            By.TAG_NAME,
            "body"
        ).text.strip()

        blocked_messages = [
            "Access Denied",
            "Request blocked",
            "Access denied",
            "automated access",
        ]

        if any(
            message.lower() in page_text.lower()
            for message in blocked_messages
        ):
            raise Exception(
                "The website blocked automated access "
                "to this product page."
            )

        # -------------------------------------------------
        # 2. Try structured Product JSON-LD
        # -------------------------------------------------

        product = find_product_jsonld(driver)

        if product:

            product_name = str(
                product.get("name", "")
            ).strip()

            rating = get_rating(product)

            reviews = extract_jsonld_reviews(
                product
            )

            cleaned_reviews = clean_reviews(
                reviews
            )

            if cleaned_reviews:

                return {
                    "product_name":
                        product_name
                        or "Unknown Product",

                    "source":
                        urlparse(url).netloc,

                    "rating":
                        rating,

                    "reviews":
                        cleaned_reviews
                }

        # -------------------------------------------------
        # 3. Try normal HTML extraction
        # -------------------------------------------------

        product_name = extract_product_name(
            driver
        )

        rating = extract_html_rating(
            driver
        )

        reviews = extract_html_reviews(
            driver
        )

        cleaned_reviews = clean_reviews(
            reviews
        )

        if not product_name:
            product_name = "Unknown Product"

        if not cleaned_reviews:

            raise Exception(
                "Product was found, but no individual "
                "review text is available on this page."
            )

        return {
            "product_name":
                product_name,

            "source":
                urlparse(url).netloc,

            "rating":
                rating,

            "reviews":
                cleaned_reviews
        }

    finally:

        driver.quit()


# =========================================================
# JSON-LD PRODUCT EXTRACTION
# =========================================================

def find_product_jsonld(driver):

    scripts = driver.find_elements(
        By.XPATH,
        "//script[@type='application/ld+json']"
    )

    for script in scripts:

        content = script.get_attribute(
            "textContent"
        )

        if not content:
            continue

        try:

            data = json.loads(content)

        except (
            json.JSONDecodeError,
            TypeError
        ):

            continue

        candidates = (
            data
            if isinstance(data, list)
            else [data]
        )

        expanded = []

        for item in candidates:

            if (
                isinstance(item, dict)
                and isinstance(
                    item.get("@graph"),
                    list
                )
            ):

                expanded.extend(
                    item["@graph"]
                )

            else:

                expanded.append(item)

        for item in expanded:

            if not isinstance(item, dict):
                continue

            item_type = item.get("@type")

            if item_type == "Product":
                return item

            if (
                isinstance(item_type, list)
                and "Product" in item_type
            ):
                return item

    return None


def get_rating(product):

    aggregate = product.get(
        "aggregateRating"
    )

    if isinstance(
        aggregate,
        dict
    ):

        return aggregate.get(
            "ratingValue"
        )

    return None


def extract_jsonld_reviews(product):

    review_data = product.get(
        "review",
        []
    )

    if isinstance(
        review_data,
        dict
    ):

        review_data = [
            review_data
        ]

    reviews = []

    for item in review_data:

        if not isinstance(
            item,
            dict
        ):
            continue

        body = str(
            item.get(
                "reviewBody",
                ""
            )
        ).strip()

        title = str(
            item.get(
                "name",
                ""
            )
        ).strip()

        if body:

            if title:

                reviews.append(
                    f"{title}. {body}"
                )

            else:

                reviews.append(body)

    return reviews


# =========================================================
# PRODUCT NAME
# =========================================================

def extract_product_name(driver):

    selectors = [

        # Common product title selectors
        "h1",

        "[itemprop='name']",

        "[class*='product-title']",

        "[class*='product_name']",

        "[class*='product-name']",

        "[class*='productName']",

        "[class*='title']",

        "[class*='name']",
    ]

    for selector in selectors:

        try:

            elements = driver.find_elements(
                By.CSS_SELECTOR,
                selector
            )

            for element in elements:

                text = element.text.strip()

                if (
                    text
                    and 3 <= len(text) <= 200
                ):

                    return text

        except Exception:

            continue

    return ""


# =========================================================
# HTML RATING
# =========================================================

def extract_html_rating(driver):

    selectors = [

        "[itemprop='ratingValue']",

        "[class*='rating']",

        "[class*='Rating']",

        "[aria-label*='rating']",

        "[aria-label*='Rating']",
    ]

    for selector in selectors:

        try:

            elements = driver.find_elements(
                By.CSS_SELECTOR,
                selector
            )

            for element in elements:

                text = (
                    element.get_attribute(
                        "content"
                    )
                    or element.get_attribute(
                        "aria-label"
                    )
                    or element.text
                )

                if not text:
                    continue

                match = re.search(
                    r"\b([0-5](?:\.\d+)?)\s*(?:/5|out of 5)?\b",
                    text
                )

                if match:

                    return float(
                        match.group(1)
                    )

        except Exception:

            continue

    return None


# =========================================================
# HTML REVIEW EXTRACTION
# =========================================================

def extract_html_reviews(driver):

    reviews = []

    time.sleep(2)

    selectors = [

        # Structured review markup
        "[itemprop='reviewBody']",

        # Common review text classes
        "[class*='review-text']",

        "[class*='reviewText']",

        "[class*='review_body']",

        "[class*='review-body']",

        "[class*='reviewBody']",

        "[class*='comment-text']",

        "[class*='commentText']",

        # Generic review containers
        "[class*='review']",

        "[class*='Review']",

        "[id*='review']",

        "[id*='Review']",
    ]

    for selector in selectors:

        try:

            elements = driver.find_elements(
                By.CSS_SELECTOR,
                selector
            )

            for element in elements:

                text = element.text.strip()

                if is_possible_review(
                    text
                ):

                    reviews.append(text)

        except Exception:

            continue

    return reviews


# =========================================================
# REVIEW VALIDATION
# =========================================================

def is_possible_review(text):

    if not text:
        return False

    text = re.sub(
        r"\s+",
        " ",
        text
    ).strip()

    # Review should have enough content
    if len(text) < 20:
        return False

    # Ignore common headings/buttons
    ignored = [

        "reviews",

        "review",

        "write a review",

        "customer reviews",

        "all reviews",

        "ratings",

        "rating",

        "reviews and ratings",

        "customer ratings",

    ]

    if text.lower() in ignored:
        return False

    # Ignore obvious navigation/UI text
    ignored_phrases = [

        "sort by",

        "filter reviews",

        "see all reviews",

        "load more",

        "write your review",

    ]

    lower_text = text.lower()

    if any(
        phrase in lower_text
        for phrase in ignored_phrases
    ):

        return False

    return True


# =========================================================
# CLEAN REVIEWS
# =========================================================

def clean_reviews(reviews):

    cleaned = []

    seen = set()

    for review in reviews:

        review = re.sub(
            r"\s+",
            " ",
            str(review)
        ).strip()

        if not is_possible_review(
            review
        ):

            continue

        key = review.lower()

        if key in seen:
            continue

        seen.add(key)

        cleaned.append(
            review
        )

    return cleaned