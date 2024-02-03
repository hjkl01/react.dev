# selenium

### selenium

```python
import random
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS


options = webdriver.ChromeOptions()
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'
options.add_argument(f'user-agent={UA}')

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# 没有配置环境变量的话需要填写Chromedriver的路径：webdriver.Chrome(executable_path="***")
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# 去掉window.navigator.webdriver字段，防止被检测出是使用selenium
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})
```

### selenium-wire

```python
import os
import time
import random
from urllib.parse import quote

from seleniumwire.utils import decode
from seleniumwire import webdriver
from user_agent import generate_user_agent


from loguru import logger


def selenium_wire_search(shopname, city):
    if os.path.exists(f"logs/{city}/{shopname}.json"):
        print(f"crawled {shopname} {city}")
        return False

    cities = {"beijing": "2", "shanghai": "1", "guangzhou": "4", "shenzhen": "7"}

    # driver = webdriver.Chrome()

    options = webdriver.ChromeOptions()
    UA = generate_user_agent(device_type="smartphone")
    options.add_argument(f"user-agent={UA}")
    driver = webdriver.Chrome(chrome_options=options)

    # Go to the Google home page
    shopname_url = quote(shopname, "utf-8")
    url = f"https://m.dianping.com/shoplist/{cities[city]}/search?from=m_search&keyword={shopname_url}"
    driver.get(url)

    # Access requests via the `requests` attribute
    for request in driver.requests:
        if request.response:
            if "module" in request.url:
                print(request.response.status_code)
                print(request.params, request.body)
                print(request.response.headers)
                # print(request.ws_messages)
                # print(request.body)
                data = request.response.body
                try:
                    if "Content-Encoding" not in request.response.headers.keys():
                        logger.warning("this request is error")
                        continue
                    body = decode(data, request.response.headers.get("Content-Encoding", "gzip"))
                    print(len(body))
                    if not os.path.exists(f"logs/{city}"):
                        os.mkdir(f"logs/{city}")

                    with open(f"logs/{city}/{shopname}.json", "w") as file:
                        file.write(body.decode("utf-8"))
                    logger.info(f"save success {shopname} {city}")
                    break
                except Exception as err:
                    logger.error(err)

    driver.quit()
    return True


def main():
    with open("logs/dianping_shops.txt", "r", encoding="utf-8") as file:
        shops = [s.strip() for s in file.readlines()]

    cities = {"beijing": "2", "shanghai": "1", "guangzhou": "4", "shenzhen": "7"}
    for shopname in shops:
        print(shopname)
        for city in list(cities.keys()):
            temp = selenium_wire_search(shopname, city)
            if temp:
                time_sleep = random.randint(5, 10)
            else:
                time_sleep = 0
            print(time_sleep)
            time.sleep(time_sleep)


if __name__ == "__main__":
    main()
```
