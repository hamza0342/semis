// Copyright (c) 2021, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('School', {
	onload: function (frm) {

		// if (frm.is_new()) {
		// 	frm.set_df_property("closure_details_section", "hidden", 1);
		// }
		// frm.set_query("district", function () {
		// 	return {
		// 		"filters": {
		// 			"division": frm.doc.division
		// 		}
		// 	};
		// });
		// frm.set_query("taluka", function () {
		// 	return {
		// 		"filters": {
		// 			"district": frm.doc.district
		// 		}
		// 	}
		// });
		// frm.set_query("uc", function () {
		// 	return {
		// 		"filters": {
		// 			"taluka_name": frm.doc.taluka
		// 		}
		// 	}
		// });
	}
	// refresh: function(frm) {
	// 	frm.set_query("taluka", function() {
	// 		return {
	// 			"filters": {
	// 			"district": ['=', frm.doc.district]
	// 			}
	// 		};
	// 	});
	// 	frm.set_query("union_council", function() {
	// 		return {
	// 			"filters": {
	// 			"taluka_name": ['=', frm.doc.taluka]
	// 			}
	// 		};
	// 	});
	// 	frm.set_query("head_master", function() {
	// 		return {
	// 			"filters": {
	// 			"designation": ['=', 'H.M']
	// 			}
	// 		};
	// 	});
	// }
});
