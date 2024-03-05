"""
Author - Declan Riddell - 2024
"""

import http.client

class apiCon:

    headers = {
                        'x-rapidapi-host': "v3.football.api-sports.io",
                        'x-rapidapi-key': "c59e06183af6afe95c429e79b0fb0791"
                        }
    
    def get_con():
        conn = http.client.HTTPSConnection("v3.football.api-sports.io")

        headers = {
                        'x-rapidapi-host': "v3.football.api-sports.io",
                        'x-rapidapi-key': "c59e06183af6afe95c429e79b0fb0791"
                        }
        
        return conn
    
    def get_headers():

        headers = {
                        'x-rapidapi-host': "v3.football.api-sports.io",
                        'x-rapidapi-key': "c59e06183af6afe95c429e79b0fb0791"
                        }
        return headers