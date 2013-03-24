#!/usr/bin/python

import gdata.docs.service
import re

class UploadFile:
	username = 'Your gmail account'
	key = 'Your password'

	def __init__(self, filename):
		self.filename = filename
		self.client = gdata.docs.service.DocsService()
		self.client.ClientLogin(self.username,self.key, source="Upload resume to google docs") 

	def upload(self):
		ext = self._GetFileExtension(self.filename)
		if not ext or ext not in gdata.docs.service.SUPPORTED_FILETYPES:
			print 'File type not supported. Check the file extension.'
			return
		else:
			content_type = gdata.docs.service.SUPPORTED_FILETYPES[ext]

		ms = gdata.MediaSource(file_path=self.filename, content_type=content_type)

		# Upload all the file into 'Royalty Application Resume' folder, You can change the folder's ID or just remove it
		entry = self.client.Upload(ms, self.filename, '/feeds/folders/private/full/folder%3A0Bwtm7gcPHXA8a1hnVUFSU2hYNWM')

		if entry:
			print 'Upload successful!'
			print 'Document now accessible at:', entry.GetAlternateLink().href
		else:
			print 'Upload error.'

	def _GetFileExtension(self, file_name):
		"""Returns the uppercase file extension for a file.

		Args:
		  file_name: [string] The basename of a filename.

		Returns:
		  A string containing the file extension of the file.
		"""
		match = re.search('.*\.([a-zA-Z]{3,}$)', file_name)
		if match:
			return match.group(1).upper()
		return False