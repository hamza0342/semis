# Copyright (c) 2022, Frappe Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Teacher(Document):
	def validate(self):
		pass
		'''get_files = frappe.db.sql("""select img.name, ff.file_url from `tabASC Images` as img, `tabFile` as ff 
				where ff.attached_to_doctype='ASC Images' and ff.attached_to_name=img.name and ff.attached_to_field='image_8' and img.image_8 is null """)
		frappe.msgprint(frappe.as_json(get_files))
		for x in get_files:
			frappe.db.set_value("ASC Images", x[0], 'image_8', x[1])
		frappe.msgprint("Done")'''
		
		'''get_images = frappe.db.sql("""select name, image_1, image_2, image_3, image_4, image_5, image_6, image_7, image_8 
						from `tabASC Images` where name!='420040434-2021-22' """)
		for x in get_images:
			count_ = 0
			if x[1]:
				count_ += 1
			if x[2]:
				count_ += 1
			if x[3]:
				count_ += 1
			if x[4]:
				count_ += 1
			if x[5]:
				count_ += 1
			if x[6]:
				count_ += 1
			if x[7]:
				count_ += 1
			if x[8]:
				count_ += 1
			frappe.db.sql(""" update `tabASC Images` set total_images=%s where name=%s """,(count_, x[0]))
		frappe.msgprint(frappe.as_json("Done"))'''
