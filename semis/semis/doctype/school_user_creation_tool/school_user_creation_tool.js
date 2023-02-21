// Copyright (c) 2022, Frappe Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on('School User Creation Tool', {
	onload: function(frm) {
		$(".primary-action").hide();
		const doctype = frm.doc.reference_doctype;
		console.log("doctype", doctype);
		if (doctype) {
			alert("ok")
			frappe.model.with_doctype(doctype, () => set_field_options(frm));
		} else {
			reset_filter_and_field(frm);
		}
		cur_frm.set_value('reference_doctype', 'School');
		refresh_field('reference_doctype');

		frm.set_query("semis_code", "school_users", function (doc, cdt, cdn) {
			return {
				filters: {
					"enabled": 1
				}
			};
		});
	},
	reference_doctype: frm => {
		const doctype = frm.doc.reference_doctype;
		if (doctype) {
			frappe.model.with_doctype(doctype, () => set_field_options(frm));
		} else {
			reset_filter_and_field(frm);
		}
	},
	division: function (frm) {
		frm.set_value("district", '');
		frm.set_value("taluka", '');
		if (frm.doc.division) {
			frm.set_query("district", function () {
				return {
					"filters": {
						"division": frm.doc.division,
					}
				};
			});
		}
	},
	district: function (frm) {
		frm.set_value("taluka", '');
		if (frm.doc.district) {
			frm.set_query("taluka", function () {
				return {
					"filters": {
						"district": frm.doc.district
					}
				};
			});
		}
	},
	get_schools: function (frm) {
		if (frm.doc.district || frm.doc.division || frm.doc.taluka) {
			var filter_list_arr = frm.filter_list.get_filters().map(filter => filter.slice(1, 4))
			frm.clear_table("school_users", "");
			frappe.call({
				method: "frappe.semis.doctype.school_user_creation_tool.school_user_creation_tool.get_schools",
				args: {
					divison: frm.doc.divison,
					district: frm.doc.district,
					taluka: frm.doc.taluka,
					"args_value": filter_list_arr
				},
				callback: function (r) {
					$.each(r.message, function (index, data) {
						var row = frappe.model.add_child(frm.doc, "School Users", "school_users");
						row.semis_code = data.name
						row.school_name = data.school_name
						row.existed_user = data.school_user
						row.district = data.district
					});
					refresh_field("school_users");
				}
			})
		}
	},
	create_users: function (frm) {
		const school_user = frm.doc.school_users
		if (school_user.length != 0) {
			frappe.call({
				method: "frappe.semis.doctype.school_user_creation_tool.school_user_creation_tool.user_creation_background",
				args: {
					school_user: school_user,
					district: frm.doc.district
				},
				freeze: true,
				callback: function (r) {
					console.log("Res", r.message);
					frm.clear_table("school_users");
					for (let i = 0; i < r.message.length; i++) {
						const data = r.message[i];
						var row = frappe.model.add_child(frm.doc, "School Users", "school_users");
						row.semis_code = data.semis_code
						row.user_name = data.user_name
						row.password = data.password
						row.school_name = data.school_name
						row.existed_user = data.existed_user
						row.district = data.district
					}
					refresh_field("school_users");
				}
			})

		}
	},
});

const reset_filter_and_field = (frm) => {
	const filter_wrapper = frm.fields_dict.filter_list.$wrapper;
	filter_wrapper.empty();
	frm.filter_list = [];
};

const set_field_options = (frm) => {
	const filter_wrapper = frm.fields_dict.filter_list.$wrapper;
	const doctype = frm.doc.reference_doctype;
	const related_doctypes = get_doctypes(doctype);

	filter_wrapper.empty();

	frm.filter_list = new frappe.ui.FilterGroup({
		parent: filter_wrapper,
		doctype: doctype,
		on_change: () => { },
	});
	frm.refresh();
};
const get_doctypes = parentdt => {
	return [parentdt].concat(
		frappe.meta.get_table_fields(parentdt).map(df => df.options)
	);
};