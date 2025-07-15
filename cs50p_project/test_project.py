from final_project import printDS, printCS, printRS, printRR, printQR


def test_printDS():
    test_data = [
  {
    "position": "1",
    "positionText": "1",
    "points": "98",
    "wins": "5",
    "Driver": {
      "driverId": "hamilton",
      "permanentNumber": "44",
      "code": "HAM",
      "url": "http://en.wikipedia.org/wiki/Lewis_Hamilton",
      "givenName": "Lewis",
      "familyName": "Hamilton",
      "dateOfBirth": "1985-01-07",
      "nationality": "British"
    },
    "Constructors": [
      {
        "constructorId": "mclaren",
        "url": "http://en.wikipedia.org/wiki/McLaren",
        "name": "McLaren",
        "nationality": "British"
      }
    ]
  }]
    expected_result = ['', 'Position: 1', 'Driver: Lewis Hamilton',
     'Points: 98', 'Nationality: British', 'Date of Birth: 1985-01-07',
      'Constructor: McLaren', '']
    assert printDS(test_data) == expected_result


def test_printCS():
    test_data1 = [
  {
    "position": "1",
    "positionText": "1",
    "points": "172",
    "wins": "8",
    "Constructor": {
      "constructorId": "ferrari",
      "url": "http://en.wikipedia.org/wiki/Scuderia_Ferrari",
      "name": "Ferrari",
      "nationality": "Italian"
    }
  }]
    expected_result1 = ['', 'Position: 1', 'Constructor: Ferrari',
                         'Nationality: Italian', 'Points: 172', '']
    assert printCS(test_data1) == expected_result1



def test_printRS():
    test_data2 = [
  {
    "season": "2012",
    "round": "1",
    "url": "http://en.wikipedia.org/wiki/2012_Australian_Grand_Prix",
    "raceName": "Australian Grand Prix",
    "Circuit": {
      "circuitId": "albert_park",
      "url": "http://en.wikipedia.org/wiki/Melbourne_Grand_Prix_Circuit",
      "circuitName": "Albert Park Grand Prix Circuit",
      "Location": {
        "lat": "-37.8497",
        "long": "144.968",
        "locality": "Melbourne",
        "country": "Australia"
      }
    },
    "date": "2012-03-18",
    "time": "06:00:00Z"
  }]
    expected_result2 = ['', 'Round: 1', 'Season: 2012', 'Date: 2012-03-18',
                         'Grand Prix: Australian Grand Prix',
                           'Name of Circuit: Albert Park Grand Prix Circuit',
                             'Locality: Melbourne Australia', '']
    assert printRS(test_data2) == expected_result2



def test_printRR():
    test_data3 = [
  {
    "season": "2008",
    "round": "5",
    "url": "http://en.wikipedia.org/wiki/2008_Turkish_Grand_Prix",
    "raceName": "Turkish Grand Prix",
    "Circuit": {
      "circuitId": "istanbul",
      "url": "http://en.wikipedia.org/wiki/Istanbul_Park",
      "circuitName": "Istanbul Park",
      "Location": {
        "lat": "40.9517",
        "long": "29.405",
        "locality": "Istanbul",
        "country": "Turkey"
      }
    },
    "date": "2008-05-11",
    "time": "12:00:00Z",
    "Results": [
      {
        "number": "2",
        "position": "1",
        "positionText": "1",
        "points": "10",
        "Driver": {
          "driverId": "massa",
          "permanentNumber": "19",
          "code": "MAS",
          "url": "http://en.wikipedia.org/wiki/Felipe_Massa",
          "givenName": "Felipe",
          "familyName": "Massa",
          "dateOfBirth": "1981-04-25",
          "nationality": "Brazilian"
        },
        "Constructor": {
          "constructorId": "ferrari",
          "url": "http://en.wikipedia.org/wiki/Scuderia_Ferrari",
          "name": "Ferrari",
          "nationality": "Italian"
        },
        "grid": "1",
        "laps": "58",
        "status": "Finished",
        "Time": {
          "millis": "5209451",
          "time": "1:26:49.451"
        },
        "FastestLap": {
          "rank": "3",
          "lap": "16",
          "Time": {
            "time": "1:26.666"
          },
          "AverageSpeed": {
            "units": "kph",
            "speed": "221.734"
          }
        }
      }]}]
    expected_result3 = ['', 'RACE INFORMATION:', '', 'Race: 2008 Turkish Grand Prix',
                         'Location: Istanbul Turkey', 'Circuit Name: Istanbul Park',
                           'Round: 5', 'Date: 2008-05-11', '', 'RESULTS:', '', 'Finishing Position: 1',
                             'Driver: Felipe Massa', 'Nationality: Brazilian',
                               'Constructor: Ferrari', 'Starting Grid Position: 1', '']
    assert printRR(test_data3) == expected_result3

def test_printQR():
    test_data4 = [
  {
    "season": "2008",
    "round": "5",
    "url": "http://en.wikipedia.org/wiki/2008_Turkish_Grand_Prix",
    "raceName": "Turkish Grand Prix",
    "Circuit": {
      "circuitId": "istanbul",
      "url": "http://en.wikipedia.org/wiki/Istanbul_Park",
      "circuitName": "Istanbul Park",
      "Location": {
        "lat": "40.9517",
        "long": "29.405",
        "locality": "Istanbul",
        "country": "Turkey"
      }
    },
    "date": "2008-05-11",
    "time": "12:00:00Z",
    "QualifyingResults": [
      {
        "number": "2",
        "position": "1",
        "Driver": {
          "driverId": "massa",
          "permanentNumber": "19",
          "code": "MAS",
          "url": "http://en.wikipedia.org/wiki/Felipe_Massa",
          "givenName": "Felipe",
          "familyName": "Massa",
          "dateOfBirth": "1981-04-25",
          "nationality": "Brazilian"
        },
        "Constructor": {
          "constructorId": "ferrari",
          "url": "http://en.wikipedia.org/wiki/Scuderia_Ferrari",
          "name": "Ferrari",
          "nationality": "Italian"
        },
        "Q1": "1:25.994",
        "Q2": "1:26.192",
        "Q3": "1:27.617"
      }]}]

    expected_result4 = ['', 'QUALIFYING INFORMATION:', '', 'Race: 2008 Turkish Grand Prix',
                         'Location: Istanbul Turkey', 'Circuit Name: Istanbul Park',
                           'Round: 5', 'Date: 2008-05-11', '', 'RESULTS:', '', 'Quali Position: 1',
                             'Driver: Felipe Massa', 'Nationality: Brazilian',
                               'Constructor: Ferrari', '']
    assert printQR(test_data4) == expected_result4



