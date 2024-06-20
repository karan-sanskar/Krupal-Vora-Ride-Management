# Copyright (c) 2024, krupal vora and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe
class RideBooking(Document):
	def after_insert(self):
		amt=0
		try:
			l=frappe.get_all("Ride Add On", filters = dict(parent=self.name),fields = ['amount'])
			for i in l:
				amt=amt+int(i['amount'])
		except:
			frappe.log_error("No records in child table")
		try:
			self.total_amount=(self.price_per_km*self.estimated_km)+amt
		except:
			frappe.log_error("Estimated KM not entered")
		
		
