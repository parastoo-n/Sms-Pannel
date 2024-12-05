import requests
import redis
import random

# تنظیمات Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

#اطلاعات API
api_key = "SjxROC1gzoyMuZsX7nZiPUB7ae7pkaooI2L3HjkK1GXCNMpx"


# گرفتن شماره تلفن از کاربر
phone_number = input("input your cellphone: ")

#گرفتن کد6رقمی
code = str(random.randint(100000, 999999))
print(f"Generated code_login: {code}")


#کش کردن کد در ردیس برای 5دقیقه(300ثانیه)
cashed_code =  redis_client.setex(phone_number, 300, code) 

#محتوای پیامک 
message = f"LOGIN CODE: {code}"

#ارسال پیامک
def send_sms(api_key, phone_number, message):
    url = "https://api.sms.ir/v1/send" 

    message_data = {
                   "MobileNumbers": [phone_number],
                   "Messages": [message],
                   "LineNumber": "3000773290",
                  }
    
    request_headers = {
              'Content-Type': 'application/json',
              'X-API-KEY': api_key
             }
    
    response = requests.post(url, json=message_data, headers=request_headers)
    # print(f"Response Status Code: {response.status_code}")
    # print(f"Response Body: {response.text}")
    return response.json()






