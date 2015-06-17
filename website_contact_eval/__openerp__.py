{
    'name': 'Contact Evaluation',
    'category': 'Website',
    'summary': 'Contact Evaluation',
    'version': '1.1',
    'description': """
Contact Evaluation
==================
This website lead snippet module allows to 
generate tagged leads from your website. 
As a website author you can use two contact 
form snippets wherever you want on your website. 
Therefore it is possible to position many 
adopted anchors to catch the right leads from 
your website.

Contributors
============
* Jan Dasenbrock (OpenBIG.org)
* Thorsten Vocks (OpenBIG.org)
        """,
    'author': 'OpenBIG.org',
    'depends': ['crm','survey','website'],
    'data': [
        'views/website_contact_eval.xml',
        'views/snippets.xml',
        'website_contact_eval_view.xml'
    ],
    'installable': True,
    'license': 'AGPL-3',
    'auto_install': False,
}
