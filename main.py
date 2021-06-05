import json
import urllib.request
import urllib
import requests
from urllib import request, parse
from datetime import datetime, date
from flask import jsonify, request, make_response, render_template
from flask_restful import Resource
from operator import attrgetter

class Website(Resource):
    def __init__(self):
        self.url = "https://api.harvestapp.com/v2/clients"
        self.headers = {
            "Harvest-Account-ID": "1442482",
            "Authorization": "Bearer " + "2643787.pt.x_F5KtFlvbpyDrYFfVitGqtcR5G869PEisVBXwL49LsPwKO_Mlk75gxaf_IUWc24qxmiAgcazmMkD_YUphzgMg",
            "User-Agent": "RHUX-Reminder (adam.birgenheier@rhuxanalytics.com)"
        }

    def get(self):
        try:
            request = urllib.request.Request(
                url=self.url, headers=self.headers)
            response = urllib.request.urlopen(request, timeout=5)
            responseBody = response.read().decode("utf-8")
            res = json.loads(responseBody)
            print(res)
            return res
        except PermissionError as error:
            raise error
