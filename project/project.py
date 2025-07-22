import requests
import sys


def main():
    try:
        if sys.argv[1] == "DS":
            user_input = input("Year: ")
            response = requests.get("https://api.jolpi.ca/ergast/f1/" + user_input + "/driverStandings.json")
            data = response.json()
            x = data.get("MRData")
            standings_table = x.get("StandingsTable")
            standings_lists = standings_table.get("StandingsLists")
            driver_standings = standings_lists[0]
            ds = driver_standings.get("DriverStandings")
            positions = printDS(ds)
            for position in positions:
                print(position)

        elif sys.argv[1] == "CS":
            user_input2 = input("Year: ")
            response2 = requests.get("https://api.jolpi.ca/ergast/f1/"+user_input2+"/constructorStandings.json")
            data2 = response2.json()
            x2 = data2.get("MRData")
            standings_table2 = x2.get("StandingsTable")
            standings_lists2 = standings_table2.get("StandingsLists")
            constructor_standings = standings_lists2[0]
            cs = constructor_standings.get("ConstructorStandings")
            positions2 = printCS(cs)
            for position2 in positions2:
                print(position2)

        elif sys.argv[1] == "RR":
            user_input3 = input("Year: ")
            user_input4 = input("Round: ")
            response3 = requests.get("https://api.jolpi.ca/ergast/f1/"+user_input3+"/"+user_input4+"/results.json")
            data3 = response3.json()
            x3 = data3.get("MRData")
            race_table = x3.get("RaceTable")
            rr = race_table.get("Races")
            positions3 = printRR(rr)
            for position3 in positions3:
                print(position3)

        elif sys.argv[1] == "RS":
            user_input4 = input("Year/Season: ")
            response4 = requests.get("https://api.jolpi.ca/ergast/f1/"+user_input4+".json")
            data4 = response4.json()
            x4 = data4.get("MRData")
            race_table4 = x4.get("RaceTable")
            rs = race_table4.get("Races")
            positions4 = printRS(rs)
            for position4 in positions4:
                print(position4)

        elif sys.argv[1] == "QR":
            user_input5 = input("Year/Season: ")
            user_input6 = input("Round: ")
            response5 = requests.get("https://api.jolpi.ca/ergast/f1/"+user_input5+"/"+user_input6+"/qualifying.json")
            data5 = response5.json()
            x5 = data5.get("MRData")
            race_table5 = x5.get("RaceTable")
            qr = race_table5.get("Races")
            positions5 = printQR(qr)
            for position5 in positions5:
                print(position5)

        else:
            print("""
    For historical data (1950 to current) on driver standings type 'DS',
    for constructor standings type 'CS',
    for race results and for each round type 'RR',
    for qualifying results for each round type 'QR',
    for race schedule type 'RS'.
    If an error is encountered the year/season or round
    may not be supported (or could be wrong) in terms of the available data,
    the supporting API could also be going through maintenance,
    apologies for the inconvenience.
    """)
    
    except Exception as e:
        print(f"Unexpected error: {e}")
            
    except IndexError:
        print("""
    For historical data (1950 to current) on driver standings type 'DS',
    for constructor standings type 'CS',
    for race results and for each round type 'RR',
    for qualifying results for each round type 'QR',
    for race schedule type 'RS'.
    If an error is encountered the year/season or round
    may not be supported (or could be wrong) in terms of the available data,
    the supporting API could also be going through maintenance,
    apologies for the inconvenience.
    """)
        
    except requests.RequestException:
        print("Error connecting to the API.")
        


def printDS(ds):
    result = []
    for item in ds:
        try:
            result.append("")
            result.append("Position: " + item.get("position", "N/A"))
            
            driver = item.get("Driver", {})
            given_name = driver.get("givenName", "Unknown")
            family_name = driver.get("familyName", "Unknown")
            result.append("Driver: " + given_name + " " + family_name)
            
            result.append("Points: " + item.get("points", "N/A"))
            result.append("Nationality: " + driver.get("nationality", "N/A"))
            result.append("Date of Birth: " + driver.get("dateOfBirth", "N/A"))
            
            constructors = item.get("Constructors", [])
            if constructors:
                result.append("Constructor: " + constructors[0].get("name", "Unknown"))
            else:
                result.append("Constructor: N/A")
            
            result.append("")
        except Exception as e:
            result.append(f"⚠️ Error with driver entry: {e}")
    return result



def printCS(cs):
    result2 = []
    for item2 in cs:
        try:
            result2.append("")
            result2.append("Position: " + item2.get("position", "N/A"))
            
            constructor = item2.get("Constructor", {})
            result2.append("Constructor: " + constructor.get("name", "Unknown"))
            result2.append("Nationality: " + constructor.get("nationality", "N/A"))
            
            result2.append("Points: " + item2.get("points", "N/A"))
            result2.append("")
        except Exception as e:
            result2.append(f"⚠️ Error with constructor entry: {e}")
    return result2



def printRR(rr):
    result3 = []
    for race in rr:
        result3.append("")
        result3.append("RACE INFORMATION:")
        result3.append("")
        result3.append("Race: " + race["season"]+" "+race["raceName"])
        result3.append("Location: " + race["Circuit"]["Location"]["locality"]+" "+race["Circuit"]["Location"]["country"])
        result3.append("Circuit Name: " + race["Circuit"]["circuitName"])
        result3.append("Round: " + race["round"])
        result3.append("Date: " + race["date"])
        result3.append("")
        result3.append("RESULTS:")
        for item3 in race["Results"]:
            result3.append("")
            result3.append("Finishing Position: " + item3["position"])
            result3.append("Driver: " + item3["Driver"]["givenName"]+" "+item3["Driver"]["familyName"])
            result3.append("Nationality: " + item3["Driver"]["nationality"])
            result3.append("Constructor: " + item3["Constructor"]["name"])
            result3.append("Starting Grid Position: " +item3["grid"])
            result3.append("")
    return result3

def printRS(rs):
    result4 = []
    for item4 in rs:
        result4.append("")
        result4.append("Round: " + item4["round"])
        result4.append("Season: " + item4["season"])
        result4.append("Date: " + item4["date"] )
        result4.append("Grand Prix: " + item4["raceName"])
        result4.append("Name of Circuit: " + item4["Circuit"]["circuitName"])
        result4.append("Locality: " +item4["Circuit"]["Location"]["locality"]+" " +item4["Circuit"]["Location"]["country"])
        result4.append("")
    return result4


def printQR(qr):
    result5 = []
    for quali in qr:
        result5.append("")
        result5.append("QUALIFYING INFORMATION:")
        result5.append("")
        result5.append("Race: "+quali["season"]+" "+quali["raceName"])
        result5.append("Location: "+quali["Circuit"]["Location"]["locality"]+" "+quali["Circuit"]["Location"]["country"])
        result5.append("Circuit Name: "+quali["Circuit"]["circuitName"])
        result5.append("Round: "+quali["round"])
        result5.append("Date: "+quali["date"])
        result5.append("")
        result5.append("RESULTS:")
        for item5 in quali["QualifyingResults"]:
            result5.append("")
            result5.append("Quali Position: " + item5["position"])
            result5.append("Driver: " + item5["Driver"]["givenName"]+" "+item5["Driver"]["familyName"])
            result5.append("Nationality: " + item5["Driver"]["nationality"])
            result5.append("Constructor: " + item5["Constructor"]["name"])
            result5.append("")
    return result5


if __name__ == "__main__":
    main()
