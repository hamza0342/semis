# Copyright (c) 2021, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.permissions import add_user_permission

class School(Document):
	def validate(self):
		if self.closing_date or self.notification_no:
			frappe.db.sql("update `tabSchool` set enabled = 0, asc_criteria = 'No', smc_criteria = 'No', gsp_criteria = 'No' where name = %s ", self.name)

	def on_update(self):
		school_user= self.school_user
		if school_user:
			if frappe.db.exists("User", school_user):	
				user = frappe.get_doc('User', school_user)
				if user:
					user.save()
	'''def validate(self):
		if self.hm_user_id and self.head_master:
			school_per = frappe.db.exists('User Permission', {
				'allow': 'School',
				'for_value': self.name,
				'user': self.hm_user_id
			})

			if school_per: 
				return
			else:
				add_user_permission("School", self.name, self.hm_user_id)
				get_users = frappe.db.sql("""select user_id from `tabEmployee` where designation='H.M' and user_id != %s """,(self.hm_user_id))
				if get_users:
					list_ = []
					for users in get_users:
						list_.append(users[0])
					if len(list_) > 0:
						frappe.db.sql("""delete from `tabUser Permission` where allow='School' and for_value=%s and user in %s """,(self.name, tuple(list_)))'''	
							
				
