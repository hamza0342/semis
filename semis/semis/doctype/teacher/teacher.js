// Copyright (c) 2022, Frappe Technologies and contributors
// For license information, please see license.txt
frappe.require([
	'/assets/semis_theme/js/personal_detail_validation.js',
]);

frappe.ui.form.on('Teacher', {
	// refresh: function(frm) {

	// }
	cnic: function (frm) {
		if (frm.doc.cnic) {
			$("input[data-fieldname='cnic']").focusout(function () {
				var cnic = frm.doc.cnic
				if (!(cnic_validate(cnic))) {
					$(".msgprint").empty()
					frappe.msgprint("Please Enter valid CNIC")
					frm.set_value("cnic", '')
				}
			});
		}

	},
	contact_no: function (frm) {
		if (frm.doc.contact_no) {
			$("input[data-fieldname='contact_no']").focusout(function () {
				var num = frm.doc.contact_no
				if (!(phone_validate(num))) {
					$(".msgprint").empty()
					frappe.msgprint("Please Enter valid Phone Number")
					frm.set_value("contact_no", '')
				}
			});
		}

	},

	full_name: function (frm) {
		$("input[data-fieldname='full_name']").focusout(function () {
			var name = frm.doc.full_name
			if (!(name_validate(name))) {
				$(".msgprint").empty()
				frappe.msgprint("Please Enter valid Name")
				frm.set_value("full_name", '')
			}
		});

	},


	onload: function (frm) {
		$("input[data-fieldname='cnic']").mask('00000-0000000-0');
		$("input[data-fieldname='contact_no']").mask('0000-0000000');

	},



});
