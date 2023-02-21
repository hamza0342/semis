# Copyright (c) 2022, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe, os
from frappe import msgprint, _
from frappe.model.document import Document
import json
import requests
from frappe.utils.pdf import get_pdf
from PyPDF2 import PdfFileWriter
from frappe.utils.background_jobs import enqueue
import ast

class LiveDBUpdateTool(Document):
	pass

@frappe.whitelist()
def get_schools(year=None, division=None, district=None, taluka=None, args_value=None):
	where = ""
	if year:
		where = " and year = '" + year + "'"
	if division :
		where += " and region = '" + division + "'"
	if district:
		where += " and district = '" + district + "'"
	if taluka:
		where += " and taluka = '" + taluka + "'"
	conditions = ""
	args_va = ast.literal_eval(args_value)
	for key in args_va:
		if str(key[1]) in ['=','!=','in','like','not like','<','>','<=','>=','Between']:
			if key[1] == 'Between':
				conditions = conditions + " and "+ str(key[0]) + " " + str(key[1]) + " '" + str(key[2][0]) + "' and '" + str(key[2][1]) + "'"
			if key[1] == 'in':
				in_tuple = tuple(key[2])
				conditions = conditions + " and "+ str(key[0]) + " " + str(key[1]) + " " + str(in_tuple) + " "	
			else:
				conditions = conditions + " and "+ str(key[0]) + " " + str(key[1]) + " '" + str(key[2]) + "'"
	query_e = """select semis_code, lat_n, lon_e, school_name, school_gender, region, district, taluka, uc, shift, level, location, status_detail, is_campus_school from `tabASC` where docstatus!='2' {0} {1}""".format(conditions,where)
	data = frappe.db.sql(query_e,as_dict=1)
	if data:
		frappe.enqueue(update_data, timeout=48000, data=data)
		# update_data(data)
		return len(data)
	else:
		return 0


def update_data(data):
	for row in data:
			school = None
			school_exist = frappe.db.sql("Select name from tabSchool where name = '%s' "%(row['semis_code']))
			if not school_exist:
				school = frappe.new_doc("School")
				school.semis_code = row['semis_code']
			else:
				school = frappe.get_doc("School", row['semis_code'])
			school.school_name = row['school_name']
			school.gender = row['school_gender']
			school.status = row['status_detail']
			school.level = row['level']
			# school.gps_coordinateslongitude = row['gps_coordinateslongitude']
			# school.gps_coordinateslatitude = row['gps_coordinateslatitude']
			school.division = row['region']
			school.district = row['district']
			school.taluka = row['taluka']
			school.union_council = row['uc']
			school.location = row['location']
			school.shift = row['shift']					
			school.campus_school = row['is_campus_school']
			school.save()



@frappe.whitelist()
def update_status(data=None,year=None, division=None, district=None, taluka=None):
	data = json.loads(data)
	default_year = frappe.db.get_single_value("ASC Panel", "default_year")
	if data:
		for row in data:
			school = frappe.get_doc("School", row['semis_code'])
			# school.semis_code = row['semis_code']
			school.school_name = row['school_name']
			school.gender = row['school_gender']
			school.status = row['status']
			school.level = row['level']
			# school.gps_coordinateslongitude = row['gps_coordinateslongitude']
			# school.gps_coordinateslatitude = row['gps_coordinateslatitude']
			school.division = row['division']
			school.district = row['district']
			school.taluka = row['taluka']
			school.union_council = row['union_council']
			school.location = row['location']
			school.shift = row['shift']					
			school.campus_school = row['campus_school']
			school.save()
		return 1
	else:
		return 0