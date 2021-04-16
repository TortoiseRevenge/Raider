##Built by Adam Miller for Archival Purposes
##This Library is designed to allow for easy use of the BrickSet API within Python.
##The Brickset API is designed to allow easy usage of the Brickset database, one of the best databases for Lego.
##Uses the database they have to easily get information
##
##Functions:
##
##    checkAPIKey(key)
##        Parameters:
##            key - API key, needed to access API. You can get one at https://brickset.com/tools/webservices/requestkey
##        Return:
##            Returns Status. If status = success, then it is a valid key
##
##    getKeyUsageStats(key)
##        Parameters:
##            key - Aforementioned API key
##        Return:
##            Returns Usage stats of getSets, which is the only thing watched by the API.
##
##    getSingleInstruction(key,setNum,folder)
##        Parameters:
##            key - Aforementioned API key
##            setNum - Lego Set Number (Usually 5 Numbers Long)
##            folder - Desired Folder to save instructions to
##        Return:
##            Returns Success or failure to get data
##
##    getMultipleInstructions(key,setNumList,folder)
##        Parameters:
##            key - Aforementioned API key
##            setNumList - List of Lego Set Numbers
##            folder - Desired Folder to save instructions to
##        Return:
##            List of all returns from getSingleInstructions from each specific set in list
##
##    getThemes(key):
##        Parameters:
##            key - Aforementioned API key
##        Return:
##            Returns all Lego Themes
##            
##    getSubthemes(key,theme):
##        Parameters:
##            key - Aforementioned API key
##            theme - desired Lego theme to search through
##        Return:
##            Returns all Lego Subthemes of specified theme
##
##    getThemesYear(key,theme):
##        Parameters:
##            key - Aforementioned API key
##            theme - desired Lego theme to search through
##        Return:
##            Returns years the theme was in production
##
##    getSets(key,theme):
##        Parameters:
##            key - Aforementioned API key
##            theme - desired Lego theme to search through
##        Return:
##            Returns all Lego sets of specified theme
##    








import requests
import json
import urllib.request
import os
import shutil

def checkAPIKey(key):
    parameters = {'apiKey': key}
    response = requests.get('http://brickset.com/api/v3.asmx/checkKey',params = parameters)
    response = response.text
    response = json.loads(response)
    response = response['status']
    return response

def getKeyUsageStats(key):
    parameters = {'apiKey': key}
    response = requests.get('http://brickset.com/api/v3.asmx/getKeyUsageStats',params = parameters)
    response = response.text
    return response

def getSingleInstruction(key,setNum,folder):
    parameters = {'apiKey': key, 'setNumber':setNum}
    response = requests.get('http://brickset.com/api/v3.asmx/getInstructions2',params = parameters)
    response=response.text
    response = json.loads(response)
    if(response['status'] =="success" and response['matches'] > 0):
        dirname = folder + "\\" + setNum
        try:
            os.mkdir(dirname)
        except:
            pass
        response = response['instructions']
        index = 0
        for item in response:
            url = (item['URL'])
            ind = url.rfind('/')
            a = url[ind:]
            descrip = item['description']
            descrip =descrip.replace("/","-")
            descrip = descrip.replace(" ","")
            fileName = dirname + "\\" + descrip + ".pdf"
            url = url.replace(" ","%20")
            if(os.path.isfile(fileName) == False):
                itemLoc = urllib.request.urlretrieve(url,filename=fileName)
        return("Downloads Complete for " + setNum)
    else:
        return("Brickset finds no set of number " + setNum)

def getMultipleInstructions(key,setNumList,folder):
    returnStatements = []
    for num in setNumList:
        returnStatements.append(getSingleInstruction(key,num,folder))
    return returnStatements

def getThemes(key):
    parameters = {'apiKey': key}
    response = requests.get('http://brickset.com/api/v3.asmx/getThemes',params = parameters)
    response=response.text
    return response

def getSubthemes(key,theme):
    parameters = {'apiKey': key,'Theme':theme}
    response = requests.get('http://brickset.com/api/v3.asmx/getSubthemes',params = parameters)
    response=response.text
    return response

def getThemesYear(key,theme):
    parameters = {'apiKey': key,'Theme':theme}
    response = requests.get('http://brickset.com/api/v3.asmx/getYears',params = parameters)
    response=response.text
    return response

def getSets(key,theme):
    parameters = {'apiKey': key,'userhash':'','params':"{'theme':'"+theme +"'}"}
    response = requests.get('http://brickset.com/api/v3.asmx/getSets',params = parameters)
    response=response.text
    return response
