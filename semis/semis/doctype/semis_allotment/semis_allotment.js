// Copyright (c) 2022, Frappe Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on('SEMIS Allotment', {
	// refresh: function(frm) {

	// }
	onload :function(frm){
		frm.set_query("school", function() {
   
			return { 
				"filters": {	
				 "semis_alloted":'No',	
				 "status":'Functional',
				}
			};
		});
	}
});
