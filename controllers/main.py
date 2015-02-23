# -*- encoding: utf-8 -*-
##############################################################################
#
#    contractmanagement_licencetypes
#    (C) 2014 big-consulting GmbH
#    Author: Jan Dasenbrock (openBIG.org)
#
#    All Rights reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import SUPERUSER_ID
from openerp.addons.web import http
from openerp.addons.web.http import request


class ContactEval(http.Controller):

	@http.route(['/contact_eval/confirm'], type='json', auth="public", website=True)
	def contact_eval_confirm(self,lead_email = None, lead_name= None, group_id= None, **post):
		cr, uid, context = request.cr, SUPERUSER_ID, request.context
		categ_obj = request.registry.get("crm.case.categ")

		categ_name = categ_obj.browse(cr, uid,[int(group_id)], context=context).display_name

		print "''''''''''''''''''''WORKS''''''''''''''''''''''''"
		print group_id
		print categ_name
		#prepares fields of new lead
		post = {
			'description' : "",
			'email_from' : lead_email,
			'name' : categ_name + " for " + lead_name,
			'contact_name' : lead_name,
			'categ_ids' : [(6, 0, [group_id])],
			'is_eval': True,
		}

		#prepares description of new lead
		environ = request.httprequest.headers.environ
		post['description'] = "%s\n-----------------------------\nIP: %s\nUSER_AGENT: %s\nACCEPT_LANGUAGE: %s\nREFERER: %s" % (
			post['description'],
			environ.get("REMOTE_ADDR"),
			environ.get("HTTP_USER_AGENT"),
			environ.get("HTTP_ACCEPT_LANGUAGE"),
			environ.get("HTTP_REFERER"))

		lead_new = request.registry['crm.lead'].create(request.cr, SUPERUSER_ID, post, request.context)
		#returns lead id
		return lead_new
		