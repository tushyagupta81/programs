import os
import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def scrape_full(data_in):
    for pincode in pincodes:
        for index, data in enumerate(data_in):
            asin_to_find = data[2]
            keyword = data[3]
            search_term = "+".join(keyword.split(" ")).lower()
            found_asin = False
            page = 1
            while not found_asin:
                driver.get(
                    "https://www.amazon.in/s?k=" + search_term + "&page=" + str(page)
                )
                time.sleep(1)
                try:
                    if index == 0:
                        location_ele = driver.find_element(
                            By.XPATH, '//*[@id="nav-global-location-popover-link"]'
                        )
                        location_ele.click()
                        time.sleep(1)
                        location_input = driver.find_element(
                            By.XPATH, '//*[@id="GLUXZipUpdateInput"]'
                        )
                        location_input.clear()
                        location_input.send_keys(pincode)
                        location_btn = driver.find_element(
                            By.XPATH, '//*[@id="GLUXZipUpdate"]'
                        )
                        location_btn.click()
                        time.sleep(2)
                    try:
                        divs = driver.find_elements(
                            By.CSS_SELECTOR, f'div[data-asin="{asin_to_find}"]'
                        )
                        if len(divs) == 0:
                            page += 1
                            if page > max_pages:
                                print(
                                    f"item {index} not found in {max_pages} pages on pin {pincode}"
                                )
                                output[len(output)] = {
                                    "pincode": pincode,
                                    "keyword": keyword,
                                    "asin": asin_to_find,
                                    "rank": ">96",
                                }
                                # i+=1
                                break
                        for div in divs:
                            try:
                                anchor = div.find_elements(By.TAG_NAME, "a")
                                href = anchor[0].get_attribute("href")
                                if "ref=sr_1_" in href:
                                    try:
                                        rank = int(
                                            href.split("ref=sr_1_")[1].split("?")[0]
                                        )
                                        if page == 1:
                                            if rank <= 4 or (rank >= 21 and rank <= 24):
                                                break
                                                # print("div was sponso")

                                            if rank <= 20:
                                                rank -= 4
                                                # print("rank adjusted")
                                            elif rank > 24 and rank <= 56:
                                                rank -= 8
                                                # print("rank adjusted")

                                        if page == 2:
                                            if (rank >= 49 and rank <= 52) or (
                                                rank >= 69 and rank <= 72
                                            ):
                                                break

                                            if rank <= 68:
                                                rank -= 4
                                                # print("rank adjusted")
                                            elif rank > 72 and rank <= 104:
                                                rank -= 8
                                                # print("rank adjusted")

                                    except:
                                        rank = href.split("ref=sr_1_")[1].split("?")[0]

                                    output[len(output)] = {
                                        "pincode": pincode,
                                        "keyword": keyword,
                                        "asin": asin_to_find,
                                        "rank": rank,
                                    }
                                    # i+=1
                                    found_asin = True
                                    print(f"item {index} found on pin {pincode}")
                            except:
                                print("anchor error")
                                page += 1
                                if page > max_pages:
                                    print(
                                        f"item {index} not found in {max_pages} pages on pin {pincode}"
                                    )
                                    output[len(output)] = {
                                        "pincode": pincode,
                                        "keyword": keyword,
                                        "asin": asin_to_find,
                                        "rank": ">96",
                                    }
                                    # i+=1
                                    break
                    except:
                        page += 1
                        if page > max_pages:
                            print(
                                f"item {index} not found in {max_pages} pages on pin {pincode}"
                            )
                            output[len(output)] = {
                                "pincode": pincode,
                                "keyword": keyword,
                                "asin": asin_to_find,
                                "rank": ">96",
                            }
                            # i+=1
                            break
                except:
                    print("cannot find change location btn")
                    output[len(output)] = {
                        "pincode": pincode,
                        "keyword": keyword,
                        "asin": asin_to_find,
                        "rank": "-",
                    }
                    # i+=1
                    time.sleep(1)
                    break


options = Options()
# options.add_argument("--headless=new")
options.add_argument("--incognito")
path = os.getcwd() + "/chromedriver"
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
pincodes = ["110001", "700001", "400008", "560056"]
max_pages = 2
data_in = eval(
    requests.get(
        "https://script.google.com/macros/s/AKfycbw8A731qtF2FdmTWfGhCC5cEkun_MeUnmhmjklGAP2VQRRiv19GrPF1YuBxHBi0TS6B/exec?sheet=6.%20NEW-+Keyword+Ranking"
    ).text
)
data_in = data_in[1:]
time.sleep(2)
output = {}


start_time = time.time()
scrape_full(data_in)
print("--- %s seconds ---" % (time.time() - start_time))


# for index,data in enumerate(data_in):
#     scrape_page(data,index)

r = requests.post(
    "https://script.google.com/macros/s/AKfycbxugMsk0xHYo1-Fz3HIkgc9b6M9OtvjNjyMbymKVctiz1Cw1w7S6xmgSr497AXP8o0j/exec?type=ranking&sheet=EB_RANK",
    json=output,
)
r.text
