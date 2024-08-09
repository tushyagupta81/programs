import requests
from bs4 import BeautifulSoup


# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:127.0) Gecko/20100101 Firefox/127.0"
}
url_sheet = "https://script.google.com/macros/s/AKfycbxugMsk0xHYo1-Fz3HIkgc9b6M9OtvjNjyMbymKVctiz1Cw1w7S6xmgSr497AXP8o0j/exec?sheet=EB_DATA"
data_in = eval(requests.get(url_sheet).text)
asins = []
for i in range(1, len(data_in)):
    asins.append(data_in[i][0])
send = {}
asins = set(asins)

l = len(asins)
# Initial call to print 0% progress
printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

for i, asin in enumerate(asins):
    URL = "https://www.amazon.in/dp/" + str(asin)
    html_page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(html_page.content, "html.parser")
    name = soup.find("span",id="productTitle").text

    try:
        rating_div = soup.find("div", id="averageCustomerReviews")
        rating = rating_div.find("span", class_="a-size-base a-color-base").text
        rating_count = soup.find("span", id="acrCustomerReviewText").text
    except:
        rating = "N/A"
        rating_count = "N/A"

    price_div = soup.find("div", id="corePriceDisplay_desktop_feature_div")
    if price_div:
        price = price_div.find("span", class_="a-price-whole").text
    else:
        price="N/A"

    aplus_prema_div = soup.find("div", id="aplus_feature_div")
    aplus_middle_div = aplus_prema_div.find("div", attrs={"cel_widget_id": "aplus"})
    if aplus_middle_div:
        aplus_stat = aplus_middle_div.find("div")["class"][-1]
    else:
        aplus_stat = None

    send[i] = {
        "asin": asin,
        "product_name": name,
        "price": price,
        "rating": rating,
        "rating_count": rating_count,
        "aplus_stat": aplus_stat,
    }

    printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

r = requests.post(
    "https://script.google.com/macros/s/AKfycbxugMsk0xHYo1-Fz3HIkgc9b6M9OtvjNjyMbymKVctiz1Cw1w7S6xmgSr497AXP8o0j/exec?type=rating&sheet=EB_RATING",
    json=send,
)
print(r.text)
