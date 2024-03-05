"""
Author - Declan Riddell - 2024
"""

import json, pandas as pd
from db_con import redisCon
from api_con import apiCon

class pythonRedis:
    """
    Python application utilizing RedisJSON to query a Football API to get some statistics

    Returns:
        NA
    """

    def teamSearch(self, inTeam):
        """Function to display a team and their home stadium

        Args:
            inTeam (str): string of the team you want to find the Average Points for
        """
        # API
        conn = apiCon.get_con()
        conn.request("GET", "/teams?search=" + inTeam, headers=apiCon.headers)
        response = conn.getresponse()
        data = response.read()
        json_data = json.loads(str(data, 'utf-8'))
        
        # RedisJSON
        r = redisCon.get_con()
        r.json().set("football:team:" + inTeam, ".", json.dumps(json_data))
        final_data = r.json().get('football:team:' + inTeam)
        datad = json.loads(final_data)

        name = datad['response'][0]['team']['name']
        venue = datad['response'][0]['venue']['name']
        print(f"\nName: {name}")
        print(f"Venue: {venue}")

    def topThree(self, df):

        """topThree will query the API for the top 3 teams from a given league and given season,
        then display the teams and add them to the DataFrame

        Args:
            df (Pandas DataFrame): DataFrame obj containing Football stats

        Returns:
            df: return the df with the current info
        """

        # API
        conn = apiCon.get_con()
        league = input("League : ")
        season = input("Season : ")
        conn.request("GET", "/standings?league=" + league + "&season=" + season, headers=apiCon.headers)
        response = conn.getresponse()
        data = response.read()
        json_data = json.loads(str(data, 'utf-8'))

        # RedisJSON
        r = redisCon.get_con()
        r.json().set("football:league:standings:" + league + ":" + season, ".", json.dumps(json_data))
        final_data = r.json().get('football:league:standings:' + league + ":" + season)
        datad = json.loads(final_data)

        # Loop through for the top 3 teams
        for i in range(0,3):
            print(str(i) + ": " + datad['response'][0]['league']['standings'][0][i]['team']['name'] + " " + str(datad['response'][0]['league']['standings'][0][i]['points']))
            df = pd.concat([df, pd.DataFrame({"teamname": [datad['response'][0]['league']['standings'][0][i]['team']['name']], "season": [str(season)], "points": [int(datad['response'][0]['league']['standings'][0][i]['points'])], "rank" : [int(datad['response'][0]['league']['standings'][0][i]['rank'])]})], ignore_index=True)
            
        print(df)
        return df
    

    def processAvgPoints(self, df, inTeam):

        """Function to process the df to aggregate a teams Average Points over the course of available data

        Args:
            df (Pandas DataFrame): DataFrame obj containing Football stats
            inTeam (str): string of the team you want to find the Average Points for
        """

        # Don't disrupt the df
        tmp = df
        tmp = tmp.loc[tmp['teamname'] == inTeam, 'points'].mean()
        print(tmp)

    def titlesWon(self, df, inTeam):

        """Function to process the df to aggregate the amount of Titles won by a given team

        Args:
            df (Pandas DataFrame): DataFrame obj containing Football stats
            inTeam (str): string of the team you want to find the Average Points for
        """

        # Don't disrupt the df
        tmp = df
        tmp = tmp.loc[tmp['teamname'] == inTeam]
        tmp = len(tmp.loc[tmp['rank'] == 1])
        print(tmp)

    def maxPoints(self, df, inTeam):

        """Function to find the Max Points earned in any season of a given team

        Args:
            df (Pandas DataFrame): DataFrame obj containing Football stats
            inTeam (str): string of the team you want to find the Average Points for
        """

        # Don't disrupt the df
        tmp = df
        tmp = tmp.loc[tmp['teamname'] == inTeam, 'points'].max()
        print(tmp)

    def menu(self, df):

        """Function for the menu driver

        Args:
            df (Pandas DataFrame): DataFrame obj containing Football stats
        """

        flag = True
        while flag:
            print(f"\n 1 - Team\n 2 - Standings\n 3 - Average Points \n 4 - Titles Won \n 5 - Max Points \n 6 - exit \n")
            choice = input("Choice: ")
            print(choice)
            if choice == '1':
                self.teamSearch(input("\nTeam:  "))
            elif choice == '2':
                df = self.topThree(df)
            elif choice == '3':
                self.processAvgPoints(df, input("\nTeam: "))
            elif choice == '4':
                self.titlesWon(df, input("\nTeam: "))
            elif choice == '5':
                self.maxPoints(df, input("\nTeam: "))
            elif choice == '6':
                flag = False
                break