import requests
import json

class DVB:
    def __init__(self):
        self.api = 'http://widgets.vvo-online.de/abfahrtsmonitor/Abfahrten.do'

def getDepartures(stop):
    api = DVB().api
    params = {'hst':stop,'raw':False}
    r = requests.get(api, params=params)
    if r.status_code == 200:
        
        linedata = dict()
        entry = 0
        for elem in r.json():
            time = int(elem[2])

            if time > 1 and time < 45:
                linedata[entry] = dict()
                linedata[entry]['linenumber'] = elem[0]
                linedata[entry]['stop'] = elem[1]
                linedata[entry]['time'] = time
                entry += 1
            
            if entry >= 8:
                break

        return linedata
    else:
        return r.status_code

def getDirection(stop, linenumber):
    api = DVB().api
    params = {'hst':stop,'raw':False}
    r = requests.get(api, params=params)
    
    if r.status_code == 200:
        i = 0
        data = []
        
        for elem in r.json():
            data.append(elem)
            i += 1
        
        linedata = dict()
        entry = 0
        for elem in data:
            if elem[0] == linenumber:
                try:
                    int(elem[2])
                except ValueError:
                    elem[2] = 0
                
                if int(elem[2]) > 1 and int(elem[2]) < 45:
                    linedata[entry] = dict()
                    linedata[entry]['linenumber'] = elem[0]
                    linedata[entry]['stop'] = elem[1]
                    linedata[entry]['time'] = elem[2]
                    entry += 1

            if entry >= 4:
                break

        return linedata
    else:
        return r.status_code

print(getDirection('Tharandter Straße', '7'))
