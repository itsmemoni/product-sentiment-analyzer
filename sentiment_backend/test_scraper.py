from scraper import get_product_data

url = "https://testingurl.dev/scraping/structured-data/reviews"

print("Testing scraper...")
print("URL:", url)

try:
    data = get_product_data(url)

    print("\n========== RESULT ==========")

    print("Product Name:")
    print(data["product_name"])

    print("\nSource:")
    print(data["source"])

    print("\nRating:")
    print(data["rating"])

    print("\nNumber of Reviews:")
    print(len(data["reviews"]))

    print("\nReviews:")

    for i, review in enumerate(data["reviews"], start=1):
        print(f"{i}. {review}")

except Exception as error:
    print("\n========== ERROR ==========")
    print(error)