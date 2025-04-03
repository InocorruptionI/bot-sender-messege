import time

import redis


redis_client = redis.Redis(host='localhost', port=6379, db=0)

redis_client.set('counter', 1)

while True:
    redis_client.incr('counter')

    time.sleep(2)
    print(redis_client.get('counter'))

    if int(redis_client.get('counter')) == 20:
        break

