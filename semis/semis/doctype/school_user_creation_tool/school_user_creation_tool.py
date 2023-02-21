# Copyright (c) 2022, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe, os
from frappe import msgprint, _
from frappe.model.document import Document
import json
import requests
import random
from frappe.utils.pdf import get_pdf
from PyPDF2 import PdfFileWriter
from frappe.utils.background_jobs import enqueue
import ast
class SchoolUserCreationTool(Document):
	pass

@frappe.whitelist()
def get_schools(division=None, district=None, taluka=None, args_value=None):
	where = ""
	if division :
		where += " and division = '" + division + "'"
	if district:
		where += " and district = '" + district + "'"
	if taluka:
		where += " and taluka = '" + taluka + "'"
	conditions = ""
	args_va = ast.literal_eval(args_value)
	for key in args_va:
		if str(key[1]) in ['=','!=','like','not like','<','>','<=','>=','Between']:
			if key[1] == 'Between':
				conditions = conditions + " and "+ str(key[0]) + " " + str(key[1]) + " '" + str(key[2][0]) + "' and '" + str(key[2][1]) + "'"
			else:
				conditions = conditions + " and "+ str(key[0]) + " " + str(key[1]) + " '" + str(key[2]) + "'"	
	schools = frappe.db.sql(""" select distinct(name), school_name, district, school_user from `tabSchool` where enabled = 1 {0} {1}""".format(conditions,where), as_dict=1)
	return schools

@frappe.whitelist()
def user_creation_background(school_user, district):
	enqueued_method = 'frappe.semis.doctype.school_user_creation_tool.school_user_creation_tool.create_users'
	frappe.enqueue(enqueued_method, queue='default', timeout=None, event=None,is_async=True, job_name=None, now=False, enqueue_after_commit=False,school_user =school_user, district= district)
	frappe.msgprint("DONE")

@frappe.whitelist()
def create_users(school_user, district):
	school_user = json.loads(school_user)
	for x in school_user:
		if x["district"] != district:
			x["school_name"] = "District Not Matched"
			x["existed_user"] = ""
			x["user_name"] = ""
			x["password"] = ""
			x["district"] = ""
			pass
		if x["existed_user"] and x["district"] == district:
			x["user_name"] = x["semis_code"]
			if frappe.db.exists("User", x["existed_user"]):
				user = frappe.get_doc("User", x["existed_user"])
				user.save()
			else:
				user = frappe.new_doc("User")
				id_ = str(x["semis_code"]) + "@seld.com"
				x["user_name"] = x["semis_code"]
				code = random.sample(range(11111111, 99999999),1)
				password = "seld@" + str(code[0])
				x["password"] = password
				user.email= id_
				user.district= x["district"]
				user.enabled= 1
				user.school= 1
				user.semis_code= x["semis_code"]
				user.first_name= x["school_name"]
				user.username= x["semis_code"]
				user.new_password= password
				user.save()
		elif not x["existed_user"] and x["district"] == district:
			user = frappe.new_doc("User")
			id_ = str(x["semis_code"]) + "@seld.com"
			x["user_name"] = x["semis_code"]
			code = random.sample(range(11111111, 99999999),1)
			password = "seld@" + str(code[0])
			x["password"] = password
			user.email= id_
			user.district= x["district"]
			user.enabled= 1
			user.school= 1
			user.semis_code= x["semis_code"]
			user.first_name= x["school_name"]
			user.username= x["semis_code"]
			user.new_password= password
			user.save()
	return school_user