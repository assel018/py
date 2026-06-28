import re
import json



filename = "raw.txt"
def parse_receipt(filename):
    with open(filename, "r",encoding = "utf-8",errors="ignore") as file:
        txt = file.read()


    # Extract prices of product
    prices = re.findall(r'\d+,\d{2}', txt)
    prices = [float(price.replace(',', '.')) for price in prices]

    # Extract names of product
    product_pattern = r'\d+\.\n([^\n]+)'
    products = re.findall(product_pattern, txt)

    # Extract total
    total_match = re.search(r'Total\s+(\d+\.\d{2})', txt, re.IGNORECASE)
    total = float(total_match.group(1)) if total_match else sum(prices)

    # Extract date
    date_match = re.search(r'\d{2}[/-]\d{2}[/-]\d{4}', txt)
    date = date_match.group() if date_match else "Not found"

    # Extract time
    time_match = re.search(r'\d{2}:\d{2}(?::\d{2})?', txt)
    time = time_match.group() if time_match else "Not found"

    # Extract payment method
    payment_match = re.search(
        r'(Cash|Card|Visa|MasterCard)', txt, re.IGNORECASE)
    payment_method = payment_match.group() if payment_match else "Not found"

    # Structured output
    data = {
        "products": products,
        "prices": prices,
        "total": total,
        "date": date,
        "time": time,
        "payment_method": payment_method
    }

    print(json.dumps(data, indent=4, ensure_ascii=False))

parse_receipt(filename)