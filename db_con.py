"""
Author - Declan Riddell - 2024
"""

import redis

class redisCon:
    """Class for redisJSON
    """
    def get_con():
        """Function to get the connection for redis

        Returns:
            redis.Redis: return redis obj to connect
        """
        return redis.Redis(
            host='redis-14418.c267.us-east-1-4.ec2.cloud.redislabs.com',
            port=14418,
            password='TsQjGl6KdA2PoCPTA0JSxpsbB634xhmP')