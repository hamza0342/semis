// Copyright (c) 2022, Frappe Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on('Upgradation And Status Change', {
	// refresh: function(frm) {

	// }
});
frappe.ui.form.on('School transfer', {
	property: function(frm, cdt, cdn){
		var child = frappe.get_doc(cdt, cdn);
		var parent = frm.doc; 
		if(child.property=="Level"){
			frappe.model.set_value(cdt, cdn, "current", parent.level);
		}
        if(child.property=="School Shift"){
			frappe.model.set_value(cdt, cdn, "current", parent.shift);
		}   
		if(child.property=="School Gender"){
			frappe.model.set_value(cdt, cdn, "current", parent.gender);
		}   
		if(child.property=="School Status"){
			frappe.model.set_value(cdt, cdn, "current", parent.status);
		} 
	}
});
