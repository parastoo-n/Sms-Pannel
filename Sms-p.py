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




