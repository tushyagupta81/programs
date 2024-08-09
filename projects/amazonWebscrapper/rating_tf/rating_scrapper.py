import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:127.0) Gecko/20100101 Firefox/127.0"
}
url_sheet = "https://script.google.com/macros/s/AKfycbw8A731qtF2FdmTWfGhCC5cEkun_MeUnmhmjklGAP2VQRRiv19GrPF1YuBxHBi0TS6B/exec?sheet=6.%20NEW-+Keyword+Ranking"
data_in = eval(requests.get(url_sheet).text)
asins = []
for i in range(1, len(data_in)):
    asins.append(data_in[i][2])
send = {}
asins = set(asins)
for i, asin in enumerate(asins):
    URL = "https://www.amazon.in/dp/" + str(asin)
    html_page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(html_page.content, "html.parser")

    try:
        rating_div = soup.find("div", id="averageCustomerReviews")
        rating = rating_div.find("span", class_="a-size-base a-color-base").text
        rating_count = soup.find("span", id="acrCustomerReviewText").text
    except:
        rating = "N/A"
        rating_count = "N/A"

    price_div = soup.find("div", id="corePriceDisplay_desktop_feature_div")
    price = price_div.find("span", class_="a-price-whole").text

    aplus_prema_div = soup.find("div", id="aplus_feature_div")
    aplus_middle_div = aplus_prema_div.find("div", attrs={"cel_widget_id": "aplus"})
    if aplus_middle_div:
        aplus_stat = aplus_middle_div.find("div")["class"][-1]
    else:
        aplus_stat = None

    send[i] = {
        "asin": asin,
        "price": price,
        "rating": rating,
        "rating_count": rating_count,
        "aplus_stat": aplus_stat,
    }

r = requests.post(
    "https://script.google.com/macros/s/AKfycbxugMsk0xHYo1-Fz3HIkgc9b6M9OtvjNjyMbymKVctiz1Cw1w7S6xmgSr497AXP8o0j/exec?type=rating&sheet=EB_RATING",
    json=send,
)
print(r.text)
