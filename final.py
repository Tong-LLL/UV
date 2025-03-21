import requests
import json
import threading

def get_ip_list(api_url):
    resp = requests.get(api_url)
    resp_json = resp.text
    resp_dict = json.loads(resp_json)
    ip_dict_list = resp_dict.get('data')
    return ip_dict_list


def view_ip(ip_port,url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36'
        }

    proxy = {
        'http': 'http://{}'.format(ip_port)
        }

    try:
        resp = requests.get(url,proxies=proxy,headers=headers)
        result = resp.text

    except:
        result = '此代理失效'

    print(result)

if __name__ == '__main__':

    print('请输入代理服务器：')
    api_url = input()

    url = 'https://m.dianping.com/shopshare/k5eg8hTkttyGvzjg?msource=Appshare2021&utm_source=shop_share&shoptype=10&shopcategoryid=4449&cityid=1&isoversea=0'

    ip_dict_list = get_ip_list(api_url)


    for ip_dict in ip_dict_list:
        ip_port = '{ip}:{port}'.format(ip=ip_dict.get('ip'),port=str(ip_dict.get('port')))
        print(ip_dict) 
        view_ip(ip_dict, url)                                    
                                        
