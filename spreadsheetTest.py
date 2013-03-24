#! /usr/bin/env

import gdata.spreadsheet.service

# Connecting to Google Spreadsheet service
gd_client = gdata.spreadsheet.service.SpreadsheetsService()
gd_client.email = 'Your gmail account'
gd_client.password = 'Your password'
gd_client.ProgrammaticLogin()

# Get spreadsheet's key
spreadsheet_feed = gd_client.GetSpreadsheetsFeed()
for spreadsheet in spreadsheet_feed.entry:
	spreadsheet_key = spreadsheet.id.text.rsplit('/',1)[1]
	print spreadsheet_key

# Get worksheet's key
worksheet_feed = gd_client.GetWorksheetsFeed(spreadsheet_key)
for worksheet in worksheet_feed.entry:
	worksheet_key = worksheet.id.text.rsplit('/',1)[1]
	print worksheet_key

# The order of dict doesn't matter
dict = {'firstname':'Fan', 'lastname':'Ang', 'age':'22', 'birthday': '9/12/1977'}
entry = gd_client.InsertRow(dict, spreadsheet_key, worksheet_key)
dict = {'age':'25','lastname':'zh',  'firstname':'Fan', 'birthday': '9/12/1977'}
entry2 = gd_client.InsertRow(dict, spreadsheet_key, worksheet_key)
if isinstance(entry, gdata.spreadsheet.SpreadsheetsList):
	print "Insert 1st row is success"
if isinstance(entry2, gdata.spreadsheet.SpreadsheetsList):
	print "Insert 2nd row is success"