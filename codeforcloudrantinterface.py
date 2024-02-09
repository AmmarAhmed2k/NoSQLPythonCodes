# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 01:36:39 2024

@author: Ammar Ahmed Siddiqui

Code to communicate with cloudant database live at account
entmax.pk@gmail.com


database name = housing

credentials below


Service credentials-1	2024-02-09 4:52 AM	Copy to clipboard
{
  "apikey": "9zG9ChaD9EWbeBPA28isEt_SBz2CketgG63O31yjfx2d",
  "host": "48bdf75f-c041-48ad-a19a-0e0171758d78-bluemix.cloudantnosqldb.appdomain.cloud",
  "iam_apikey_description": "Auto-generated for key crn:v1:bluemix:public:cloudantnosqldb:in-che:a/1a90ecb044064f22ae672e993906646b:464338be-2c89-40e1-abf0-9ccb2f65712c:resource-key:97fe136d-81ab-446a-8e26-db873c7161af",
  "iam_apikey_id": "ApiKey-6d7d6b7e-7a2d-4816-a481-b6fdebb7c636",
  "iam_apikey_name": "Service credentials-1",
  "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Manager",
  "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/1a90ecb044064f22ae672e993906646b::serviceid:ServiceId-f6ae8e87-426d-4a0d-8dd0-d3458e391850",
  "password": "13fca3b0321ee8b59cd73224d9236d8b",
  "port": 443,
  "url": "https://apikey-v2-31iklzwujizg7m9lej5ohp123xurprn8maxa4mzcx18w:13fca3b0321ee8b59cd73224d9236d8b@48bdf75f-c041-48ad-a19a-0e0171758d78-bluemix.cloudantnosqldb.appdomain.cloud",
  "username": "apikey-v2-31iklzwujizg7m9lej5ohp123xurprn8maxa4mzcx18w"
}
"""
"""

Run following command to install and verify packages

pip install ibmcloudant
pip list | find "ibmcloudant"

"""

# API Documentation source https://cloud.ibm.com/apidocs/cloudant?code=python#introduction

import json
import time


service_name = "CLOUDANT"

CLOUDANT_URL="https://apikey-v2-31iklzwujizg7m9lej5ohp123xurprn8maxa4mzcx18w:13fca3b0321ee8b59cd73224d9236d8b@48bdf75f-c041-48ad-a19a-0e0171758d78-bluemix.cloudantnosqldb.appdomain.cloud"
CLOUDANT_APIKEY="9zG9ChaD9EWbeBPA28isEt_SBz2CketgG63O31yjfx2d"
CLOUDANT_AUTH_TYPE="COUCHDB_SESSION"
CLOUDANT_USERNAME="apikey-v2-31iklzwujizg7m9lej5ohp123xurprn8maxa4mzcx18w"
CLOUDANT_PASSWORD="13fca3b0321ee8b59cd73224d9236d8b"


from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import BasicAuthenticator

authenticator = BasicAuthenticator(CLOUDANT_USERNAME, CLOUDANT_PASSWORD)

service = CloudantV1(authenticator=authenticator)

service.set_service_url(CLOUDANT_URL)
print(service)


response = service.get_server_information().get_result()
print(json.dumps(response,indent=4))

response = service.get_membership_information().get_result()
print(json.dumps(response,indent=4))

# How to check all your databases

response = service.get_all_dbs().get_result()
print(json.dumps(response,indent=4))

# Read information about a particular database
response = service.get_database_information(db='housing').get_result()
print(json.dumps(response,indent=4))

# Add many documents to a database
from ibmcloudant.cloudant_v1 import Document

for x in range(1,500):
    
    products_doc = Document(
      #id="small-appliances:1000042",
      type="product",
      productid="1000042",
      brand="Salter",
      name="Digital Kitchen Scales",
      description="Slim Colourful Design Electronic Cooking Appliance for Home / Kitchen, Weigh up to 5kg + Aquatronic for Liquids ml + fl. oz. 15Yr Guarantee - Green",
      price=14.99,
      image="assets/img/0gmsnghhew.jpg")
    
    response = service.post_document(db='housing', document=products_doc).get_result()
    
    print(json.dumps(response,indent=4))
    
    time.sleep(1)


# Query the list of all documents

response = service.post_all_docs(
  db='housing',
  include_docs=True,
  start_key='',
  limit=10
).get_result()
    
print(json.dumps(response,indent=4))

    
