"""
Author - Declan Riddell - 2024
"""

import http.client

class apiCon:
    """Class for all API info
    """

    headers = {
                        'x-rapidapi-host': "v3.football.api-sports.io",
                        'x-rapidapi-key': "c59e06183af6afe95c429e79b0fb0791"
                        }
    
    def get_con():
        """function to get_con for API

        Returns:
            conn : returns the http.client connection info
        """
        conn = http.client.HTTPSConnection("v3.football.api-sports.io")
        return conn