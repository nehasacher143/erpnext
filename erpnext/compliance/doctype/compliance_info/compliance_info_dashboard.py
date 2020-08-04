from frappe import _


def get_data():
	return {
		'fieldname': 'license',
		'transactions': [
			{
				'label': _('Licensees'),
				'items': ['Customer', 'Supplier']
			}
		]
	}
