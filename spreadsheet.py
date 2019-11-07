#!/usr/bin/python3
#coding: utf-8

import httplib2
import numpy as np

from apiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials

SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
APPEND_RANGE = 'Sheet1!A1:C1'

class SpreadSheet(object):
  def __init__(self, sheet_id):

    self.sheetId = sheet_id
    
    # json flie
    credentials = ServiceAccountCredentials.from_json_keyfile_name('My-Project-xxxxxx.json', scopes=SCOPES)
    
    http_auth = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?''version=v4')
    self.service = discovery.build('sheets', 'v4', http=http_auth, discoveryServiceUrl=discoveryUrl)

  def append(self, values):
    # colonm shape
    assert np.array(values).shape==(4,) , "The shape of value %s must be 4" % (np.array(values).shape)

    value_range_body = {'values':[values]}
    result = self.service.spreadsheets().values().append(spreadsheetId=self.sheetId, range=APPEND_RANGE, valueInputOption='USER_ENTERED', body=value_range_body).execute()
    #print(result)

if __name__ == '__main__':
  # sheet id
  sheet = SpreadSheet("xxx")
  sheet.append(["test 1col", "test 2col","test 3col", 3])
