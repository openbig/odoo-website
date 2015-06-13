from datetime import datetime
import difflib
import lxml
import random

from openerp import tools
from openerp import SUPERUSER_ID
from openerp.osv import osv, fields
from openerp.tools.translate import _

class BlogPost(osv.Model):
    _name = "blog.post"
    _inherit = ["blog.post"]
    _columns = {
    #adds new fields to blog_post
        'post_description': fields.html("Description", translate=True),
        'read_on_text': fields.char("Read On Text", translate=True),
        'foreign_url': fields.char("Foreign URL"),
        }
    _defaults = {
        'read_on_text': _('Read on'),
    }
    
class Blog(osv.Model):
    _name = 'blog.blog'
    _inherit = 'blog.blog'
    _columns = {
        'link_foreign': fields.boolean('Link to foreign URL'),

        }
