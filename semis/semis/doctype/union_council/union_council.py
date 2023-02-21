# Copyright (c) 2021, Frappe Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class UnionCouncil(Document):
	def validate(self):
		pass
		# tehsielname = frappe.db.sql(""" select taluka_name
		# from `tabTaluka` where taluka_code=%s """%self.taluka_id)
		# self.taluka_name = tehsielname
		# hello