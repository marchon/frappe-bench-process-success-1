# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "crvportal"
app_title = "Crvportal"
app_publisher = "agilebusiness.net"
app_description = "Workflow demo app"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "vasistabhargava@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/crvportal/css/crvportal.css"
# app_include_js = "/assets/crvportal/js/crvportal.js"

# include js, css files in header of web template
# web_include_css = "/assets/crvportal/css/crvportal.css"
# web_include_js = "/assets/crvportal/js/crvportal.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "crvportal.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "crvportal.install.before_install"
# after_install = "crvportal.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "crvportal.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"crvportal.tasks.all"
# 	],
# 	"daily": [
# 		"crvportal.tasks.daily"
# 	],
# 	"hourly": [
# 		"crvportal.tasks.hourly"
# 	],
# 	"weekly": [
# 		"crvportal.tasks.weekly"
# 	]
# 	"monthly": [
# 		"crvportal.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "crvportal.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "crvportal.event.get_events"
# }

