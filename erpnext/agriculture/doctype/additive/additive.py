# -*- coding: utf-8 -*-
# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Additive(Document):
	def load_contents(self):
		docs = frappe.get_all("Agriculture Analysis Criteria",
			filters={'linked_doctype':'Additive', 'additive_type': self.additive_type})
		self.additive_contents =None
		for doc in docs:
			self.append('additive_contents', {'title': str(doc.name)})