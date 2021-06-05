# import json
# import urllib.request
# import urllib
# import requests
# from urllib import request, parse
# from datetime import datetime, date
# from flask import jsonify, request, make_response, render_template
# from flask_restful import Resource
# from operator import attrgetter

# class Website(Resource):
#     def __init__(self):
#         self.url = "https://api.harvestapp.com/v2/clients"

#     def get(self):
#         try:
#             request = urllib.request.Request(
#                 url=self.url, headers=self.headers)
#             response = urllib.request.urlopen(request, timeout=5)
#             responseBody = response.read().decode("utf-8")
#             res = json.loads(responseBody)
#             print(res)
#             return res
#         except PermissionError as error:
#             raise error

#     def post(self):
#         try:
#             request = urllib.request.Request(
#                 url=self.url, headers=self.headers)
#             response = urllib.request.urlopen(request, timeout=5)
#             responseBody = response.read().decode("utf-8")
#             res = json.loads(responseBody)
#             print(res)
#             return res
#         except PermissionError as error:
#             raise error
