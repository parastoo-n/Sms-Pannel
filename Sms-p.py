import requests
import redis
import random

# تنظیمات Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

#اطلاعات API
api_key = "SjxROC1gzoyMuZsX7nZiPUB7ae7pkaooI2L3HjkK1GXCNMpx"


# گرفتن شماره تلفن از کاربر
phone_number = input("input your cellphone: ")