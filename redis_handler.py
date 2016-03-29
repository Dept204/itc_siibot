import redis
import os


class Redis:

    def __init__(self):
        self.r_message = redis.StrictRedis(
                host=os.environ['OPENSHIFT_REDIS_HOST'],
                port=os.environ['OPENSHIFT_REDIS_PORT'],
                db=0,
                password=os.environ['REDIS_PASSWORD'])
        self.r_usr = redis.StrictRedis(
                host=os.environ['OPENSHIFT_REDIS_HOST'],
                port=os.environ['OPENSHIFT_REDIS_PORT'],
                db=1,
                password=os.environ['REDIS_PASSWORD'])
        self.r_pass = redis.StrictRedis(
                host=os.environ['OPENSHIFT_REDIS_HOST'],
                port=os.environ['OPENSHIFT_REDIS_PORT'],
                db=2,
                password=os.environ['REDIS_PASSWORD'])
