import concurrent.futures
import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def adjust_rank(href, page):
    try:
        rank = int(href.split("ref=sr_1_")[1].split("?")[0])
        if page == 1:
            if rank <= 4 or (rank >= 21 and rank <= 24):
                return 0

            if rank <= 20:
                rank -= 4
            elif rank > 24 and rank <= 56:
                rank -= 8

        if page == 2:
            if (rank >= 49 and rank <= 52) or (rank >= 69 and rank <= 72):
                return 0

            if rank <= 68:
                rank -= 4
            elif rank > 72 and rank <= 104:
                rank -= 8

    except:
        rank = href.split("ref=sr_1_")[1].split("?")[0]

    return rank


def scrape_item(item_data):
    output = []
    for pincode in pincodes:
        driver = webdriver.Remote(
            command_executor="http://localhost:4444", options=options
        )
        # driver = webdriver.Chrome(service=service , options=options)
        asin_found = False
        page = 1
        while not asin_found:
            driver.get(
                "https://www.amazon.in/s?k="
                + item_data["keyword"]
                + "&page="
                + str(page)
            )
            if page == 1:
                try:
                    wait = WebDriverWait(driver, 10)
                    for i in range(4):
                        try:
                            wait.until(
                                EC.visibility_of_element_located(
                                    (By.ID, "glow-ingress-block")
                                )
                            )
                            break
                        except Exception as e:
                            driver.get(
                                "https://www.amazon.in/s?k="
                                + item_data["keyword"]
                                + "&page="
                                + str(page)
                            )
                            print("getting again")
                            time.sleep(1)
                    driver.find_element(By.ID, "glow-ingress-block").click()
                    wait.until(
                        EC.visibility_of_element_located((By.ID, "GLUXZipUpdateInput"))
                    )
                    location_input = driver.find_element(By.ID, "GLUXZipUpdateInput")
                    location_input.clear()
                    location_input.send_keys(pincode)
                    driver.find_element(By.ID, "GLUXZipUpdate").click()
                    time.sleep(3)

                    # driver.get("https://www.amazon.in/")
                    # location_ele = driver.find_element(By.ID, "glow-ingress-block")
                    # location_ele.click()
                    # time.sleep(1)
                    # location_input = driver.find_element(By.ID, "GLUXZipUpdateInput")
                    # location_input.clear()
                    # location_input.send_keys(pincode)
                    # driver.find_element(By.ID, "GLUXZipUpdate").click()

                except Exception as e:
                    print(e)
                    output.append(
                        {
                            "pincode": pincode,
                            "keyword": item_data["keyword"],
                            "asin": item_data["asin"],
                            "rank": "---",
                        }
                    )
                    break
            divs = driver.find_elements(
                By.CSS_SELECTOR, f'div[data-asin="{item_data["asin"]}"]'
            )
            if len(divs) == 0:
                page += 1
                if page > max_pages:
                    # print(f"item {item_data["asin"]} not found in {max_pages} pages on pin {pincode}")
                    output.append(
                        {
                            "pincode": pincode,
                            "keyword": item_data["keyword"],
                            "asin": item_data["asin"],
                            "rank": ">96",
                        }
                    )
                    break
            else:
                for div in divs:
                    try:
                        anchor = div.find_elements(By.TAG_NAME, "a")
                        href = anchor[0].get_attribute("href")
                        if "ref=sr_1_" in href:
                            rank = adjust_rank(href, page)
                            if rank == 0:
                                break

                            output.append(
                                {
                                    "pincode": pincode,
                                    "keyword": item_data["keyword"],
                                    "asin": item_data["asin"],
                                    "rank": rank,
                                }
                            )
                            asin_found = True
                            # print(f"item {item_data["asin"]} found on pin {pincode}")
                    except:
                        print("anchor error")
                        page += 1
                        if page > max_pages:
                            # print(f"item {item_data["asin"]} not found in {max_pages} pages on pin {pincode}")
                            output.append(
                                {
                                    "pincode": pincode,
                                    "keyword": item_data["keyword"],
                                    "asin": item_data["asin"],
                                    "rank": ">96",
                                }
                            )
                            break
        driver.quit()
    return output


options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--incognito")
pincodes = ["110001", "700001", "400008", "560056"]
max_pages = 2
data_in = eval(
    requests.get(
        "https://script.google.com/macros/s/AKfycbxugMsk0xHYo1-Fz3HIkgc9b6M9OtvjNjyMbymKVctiz1Cw1w7S6xmgSr497AXP8o0j/exec?sheet=EB_DATA"
    ).text
)

final = []
n = 0
for data in data_in[1:]:
    if (len(str(data[3])) > 1) and (data[4] != "#VALUE!"):
        keyw = 0
        for keyword in data[4:]:
            final.append({"asin": data[0], "keyword": keyword})
            keyw += 1
            if keyw == 28:
                break

final = final[:28]
start = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
    results = list(executor.map(scrape_item, final))
out = [item for items in results for item in items]

r = requests.post(
    "https://script.google.com/macros/s/AKfycbxugMsk0xHYo1-Fz3HIkgc9b6M9OtvjNjyMbymKVctiz1Cw1w7S6xmgSr497AXP8o0j/exec?type=ranking&sheet=EB_RANK",
    json=out,
)
print(r.text)
print(f"Done in {time.time()-start}")

# print(scrape_item({"asin": "B0CQ4TMVG9", "keyword": "copper bottle 500ml"}))
