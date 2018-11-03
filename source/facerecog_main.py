import requests
import os

BASE_URL = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/"
SUBSCRIPTION_KEY  = "自分のSUBSCRIPTION_KEYを入力する"
GROUP_NAME = "baseball_player"

def makeGroup():
    end_point = BASE_URL + "persongroups/" + GROUP_NAME
    payload = {
        "name": GROUP_NAME
    }
    headers = {
        "Ocp-Apim-Subscription-Key" :SUBSCRIPTION_KEY
    }
    response = requests.put(
        end_point,
        headers = headers,
        json = payload
    )
    return response

def makePerson(name):
    end_point = BASE_URL + "persongroups/" + GROUP_NAME + "/persons"
    headers = {
        "Ocp-Apim-Subscription-Key" :SUBSCRIPTION_KEY
    }
    payload = {
        "name": name
    }
    response = requests.post(
        end_point,
        headers = headers,
        json = payload
    )
    return response

def addFaceToPerson(personId, imageUrl):
    end_point = BASE_URL + "persongroups/" + GROUP_NAME + "/persons/" + personId  + "/persistedFaces"
    #print(end_point)
    headers = {
        "Ocp-Apim-Subscription-Key" :SUBSCRIPTION_KEY
    }
    payload = {
        "url": imageUrl
    }
    response = requests.post(
        end_point,
        headers = headers,
        json = payload
    )
    return response

#ローカルのファイルを追加する
def addFaceToPersonByfile(personId, imagefile):
    end_point = BASE_URL + "persongroups/" + GROUP_NAME + "/persons/" + personId  + "/persistedFaces"
    headers = {
        "Content-Type" :'application/octet-stream',
        "Ocp-Apim-Subscription-Key" :SUBSCRIPTION_KEY
    }
    response = requests.post(
        end_point,
        headers = headers,
        data = imagefile
    )
    return response

def trainGroup():
    end_point = BASE_URL + "persongroups/" + GROUP_NAME + "/train"
    headers = {
        "Ocp-Apim-Subscription-Key" :SUBSCRIPTION_KEY
    }
    response = requests.post(
        end_point,
        headers = headers,
    )
    return response

def detectFace(imageUrl):
    end_point = BASE_URL + "detect"
    headers = {
        "Ocp-Apim-Subscription-Key" :SUBSCRIPTION_KEY
    }
    payload = {
        "url": imageUrl
    }
    response = requests.post(
        end_point,
        json = payload,
        headers = headers
    )
    return response

def detectFaceBylocal(imagefile):
    end_point = BASE_URL + "detect"
    headers = {
        "Content-Type" :'application/octet-stream',
        "Ocp-Apim-Subscription-Key" :SUBSCRIPTION_KEY
    }
    response = requests.post(
        end_point,
        data = imagefile,
        headers = headers
    )
    return response

def identify(faceId):
    end_point = BASE_URL + "identify"
    headers = {
        "Ocp-Apim-Subscription-Key" :SUBSCRIPTION_KEY
    }
    faceIds = [faceId]
    payload = {
        "faceIds" :faceIds,
        "personGroupId" :GROUP_NAME,
        #"maxNumOfCandidatesReturned" :maxNumOfCandidatesReturned
    }
    response = requests.post(
        end_point,
        json = payload,
        headers = headers
    )
    return response
