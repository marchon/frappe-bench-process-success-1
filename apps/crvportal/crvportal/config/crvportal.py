from __future__ import unicode_literals
from frappe import _

from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
        {
            "label": _("Materials"),
            "icon": "fa fa-star",
            "items": [
                {
                    "type": "doctype",
                    "name": "Equipment",
                    "description": _("Equipment"),
                }                
            ]
        }]
