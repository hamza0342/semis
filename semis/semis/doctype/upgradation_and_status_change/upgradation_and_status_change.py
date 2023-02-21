# Copyright (c) 2022, Frappe Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class UpgradationAndStatusChange(Document):

	def validate(self):
		pass
		#if self.transfer_date > frappe.utils.nowdate():
		#	frappe.throw("Future date not allowed")
	def on_submit(self):
		new_school = frappe.get_doc("School", self.school)
		for data in self.school_transfer:
			if data.property=="Level":
				new_school.level = data.new
			if data.property=="School Shift":
				new_school.shift = data.new
			if data.property=="School Gender":
				new_school.gender = data.new
			if data.property=="School Status":	
				new_school.status = data.new
			if self.new_school_name:
				new_school.school_name = self.new_school_name
		new_school.save()
