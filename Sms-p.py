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
    
    response_1 = requests.post(url, json=message_data, headers=request_headers)
    # print(f"Response Status Code: {response.status_code}")
    # print(f"Response Body: {response.text}")
    return response_1.json()


def get_cached_code(phone_number):
    return redis_client.get(phone_number)

response_2 = send_sms(api_key, phone_number, message)

if response_2.get("code") == 1:
   print(f" Message succcessfully sent to   {phone_number}  ")
else:
   print(f"Error sending SMS to  {phone_number}: {response_2.get('message')}")


# گرفتن کد ورودی کاربر برای تایید
user_code = input("Please enter the code you received: ")


# مقایسه کد وارد شده با کد کش شده
cached_code = get_cached_code(phone_number)
if cached_code and cached_code.decode('utf-8') == user_code:
   print("you have successfully logged in!")
else:
   print("The code entered is incorrect.Login failed!")






