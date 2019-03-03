from pyexcel_ods import get_data
import requests
import json

data = get_data("/Users/b-macbook/Desktop/krimewatch 2.ods")


parameters = {
  "crime": "assault",
  "days": 30,
  "time": -1
}

def generateDatapoints(parameters):
    string = "new google.maps.LatLng("
    outstring = ""
    for x in range(parameters["days"]):
        if x == 0:
            continue
        if parameters["time"]==-1:
            outstring += string + str(data['Sheet1'][x][4]) + "," + str(data['Sheet1'][x][5]) + "),\n"
        else:
            if parameters["time"]==int(data['Sheet1'][x][2][0:2]):
                outstring += string + str(data['Sheet1'][x][4]) + "," + str(data['Sheet1'][x][5]) + "),\n"
    return outstring


hi = generateDatapoints(parameters)
print(hi)
