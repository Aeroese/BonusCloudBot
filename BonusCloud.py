import json
import time
import urllib3
import requests
import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.adapters.DEFAULT_RETRIES = 3

class BonusCloud:
    cookie = None
    def Login(Email, Password) :
        global cookie
        cookie = None
        body = json.dumps( { 'email' : Email, 'password' : Password } )
        url = 'https://console.bonuscloud.io/api/user/login/'
        r = requests.post(url = url, data = body, verify = False, cookies = cookie, timeout = 10,headers={'Content-Type':'application/json;charset=UTF-8'})
        cookie = r.cookies
        result = json.loads(r.content.decode('utf-8'))
        return result

    def GetStatus() :
        url = 'https://console.bonuscloud.io/api/bcode/get_status/'
        r = requests.get(url = url, verify = False, cookies = cookie, timeout = 10)
        result = json.loads(r.content.decode('utf-8'))
        return result

    def GetUserInfo() :
        url = 'https://console.bonuscloud.io/api/user/get_user_info/'
        r = requests.get(url = url, verify = False, cookies = cookie, timeout = 10)
        result = json.loads(r.content.decode('utf-8'))
        return result

    def GetRecommendCount() :
        url = 'https://console.bonuscloud.io/api/user/get_recommend_count/'
        r = requests.get(url = url, verify = False, cookies = cookie, timeout = 10)
        result = json.loads(r.content.decode('utf-8'))
        return result

    def GetreCommendInfo() :
        url = 'https://console.bonuscloud.io/api/user/get_recommend_info/'
        r = requests.get(url = url, verify = False, cookies = cookie, timeout = 10)
        result = json.loads(r.content.decode('utf-8'))
        return result

    def Getavaliable_list() : 
        url = 'https://console.bonuscloud.io/api/bcode/avaliable_list/'
        r = requests.get(url = url, verify = False, cookies = cookie, timeout = 10)
        result = json.loads(r.content.decode('utf-8'))
        return result

    def GetTodayRevenue() :
        now_time =datetime.datetime.now()
        yest_time = now_time + datetime.timedelta(days=-1)
        start = int(time.mktime(yest_time.timetuple())*1000)
        end = int(time.mktime(now_time.timetuple())*1000)
        print(start,end)
        url = 'https://console.bonuscloud.io/api/web/revenue/?type=account&start=' + str(start) + '&end=' + str(end)
        r = requests.get(url = url, verify = False, cookies = cookie, timeout = 10)
        result = json.loads(r.content.decode('utf-8'))
        return result

    def GetReferRevenue() :
        now_time =datetime.datetime.now()
        yest_time = now_time + datetime.timedelta(days=-1)
        start = int(time.mktime(yest_time.timetuple())*1000)
        end = int(time.mktime(now_time.timetuple())*1000)
        print(start,end)
        url = 'https://console.bonuscloud.io/api/web/revenue/?type=refer&start=' + str(start) + '&end=' + str(end)
        r = requests.get(url = url, verify = False, cookies = cookie, timeout = 10)
        result = json.loads(r.content.decode('utf-8'))
        return result

    def GetTotalRevenue() :
        url = 'https://console.bonuscloud.io/api/web/revenue/?type=all'
        r = requests.get(url = url, verify = False, cookies = cookie, timeout = 10)
        result = json.loads(r.content.decode('utf-8'))
        return result

    def GetDevicesList() :
        url = 'https://console.bonuscloud.io/api/web/devices/list/'
        r = requests.get(url = url, verify = False, cookies = cookie, timeout = 10)
        result = json.loads(r.content.decode('utf-8'))
        return result

    def GetDevicesNetInfo(MacAddress , Bcode) :
        url = 'https://console.bonuscloud.io/api/web/devices/netInfo?mac_address=' + MacAddress + '&bcode=' + Bcode
        r = requests.get(url = url, verify = False, cookies = cookie, timeout = 10)
        result = json.loads(r.content.decode('utf-8'))
        return result

