# Copyright (c) 2022, Frappe Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import frappe.model.rename_doc as rd

class SEMISAllotment(Document):
	def validate(self):
		if self.allotment_date > frappe.utils.nowdate():
			frappe.throw("Future date not allowed for SEMIS Allotment Date")
	def on_submit(self):
		new_school = frappe.get_doc("School", self.school)
		new_school.semis_alloted="Yes"
		new_school.save()
		rd.rename_doc("School", self.school, self.semis_code, force=True)
		rd.rename_doc("SEMIS Allotment", self.name, self.semis_code, force=True)
		


		
