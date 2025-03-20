from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import itertools
import requests
import json

PROXIES = [ ]

def get_ip_list():
    url = 'http://need1.dmdaili.com:7771/dmgetip.asp?apikey=46253696&pwd=dba6618ea3e462cd96ac29508e7305e0&getnum=200&httptype=1&geshi=2&fenge=1&fengefu=&operate=all'
    resp = requests.get(url)
    resp_json = resp.text
    resp_dict = json.loads(resp_json)
    ip_dict_list = resp_dict.get('data')
    return ip_dict_list

CHROMEDRIVER_PATH = "C:\Program Files\Google\Chrome\Application\chromedriver-win64\chromedriver.exe"

def set_proxy_and_refresh(proxy):

    chrome_options = Options()
    chrome_options.add_argument(f"--proxy-server=http://{proxy}")
    
    driver = webdriver.Chrome(
        service=Service(CHROMEDRIVER_PATH),
        options=chrome_options
    )
    
    try:
        driver.get("https://m.dianping.com/shopshare/k5eg8hTkttyGvzjg?msource=Appshare2021&utm_source=shop_share&shoptype=10&shopcategoryid=4449&cityid=1&isoversea=0")
        print(f"当前代理: {proxy} | 页面标题: {driver.title}")
        time.sleep(1)
    except:
        result = '此代理失效'
    finally:
        driver.quit()

if __name__ == "__main__":

    PROXIES = [ ]
    ip_dict_list = get_ip_list()

    for ip_dict in ip_dict_list:
        ip_port = '{ip}:{port}'.format(ip=ip_dict.get('ip'),port=str(ip_dict.get('port')))
        PROXIES.append(ip_port)
    
    for proxy in PROXIES:
        set_proxy_and_refresh(proxy)
        print(f"切换至下一个代理...")
