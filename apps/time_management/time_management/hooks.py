# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "time_management"
app_title = "Time Management"
app_publisher = "Frappe"
app_description = "App for managing employee timesheets, work flow, and locations"
app_icon = "octicon octicon-calendar"
app_color = "#f99625"
app_email = "sbonser@agilebusiness.com"
app_license = "GNU General Public License"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/time_management/css/time_management.css"
# app_include_js = "/assets/time_management/js/time_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/time_management/css/time_management.css"
# web_include_js = "/assets/time_management/js/time_management.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "time_management.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "time_management.install.before_install"
# after_install = "time_management.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "time_management.notifications.get_notification_config"

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
# 		"time_management.tasks.all"
# 	],
# 	"daily": [
# 		"time_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"time_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"time_management.tasks.weekly"
# 	]
# 	"monthly": [
# 		"time_management.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "time_management.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "time_management.event.get_events"
# }

