# -*- encoding: utf-8 -*-
##############################################################################
#
#    website_blog_press
#    (C) 2014 big-consulting GmbH 
#    (C) 2014 OpenGlobe 
#    Author: Thorsten Vocks (openBIG.org) 
#    Author: Mikołaj Dziurzyński, Grzegorz Grzelak (OpenGlobe)
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
#
{
    'name' : 'Press release management',
    'version': '1.0',
    'summary': 'Write, publish and link press releases',
    'sequence': '19',
    'category': 'Marketing',
    'complexity': 'easy',
    'description':
        """
Write, publish and link press releases
=======================================

As a user of this module it is possible to write press releases in 
a blog with activated setting "Link to Foreign URL". The author 
may write a short introduction before linking to an external website. 
Furthermore it is possible to change author and publish date of an 
blogpost. The module adds two fields to blog.post and modifies 
the view of blog.post. 

It also adds an description field, which will be displayed in the list 
view of the blog.

Contributors
============
* Jan Dasenbrock (OpenBIG.org)
* Thorsten Vocks (OpenBIG.org)
* Mikołaj Dziurzyński (OpenGlobe)
        """,
    'data': [
     "website_blog_press_backend.xml",
     "website_blog_press_website.xml",
        
    ],
    'depends' : ['website_blog'],
    'installable': True,
    'auto_install': False,
    'license': 'AGPL-3',
    'application': True,
}
