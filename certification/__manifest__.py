{
    'name':'Certification',
    'summary':'Defines certificatiob for different purposes',
    'author':'Odoo training class',
    'website':'https://github.com/rumeysayilmaz/odoo-training-tr',
    'category':'Certification Management',
    'version': '12.0.1.0.0',
    'license':'AGPL-3',
    'depends':['base'],
    'data':[
        'security/ir.model.access.csv',
        'views/certification_standard.xml',
        'views/certification_bodies.xml',
        'views/certification_view.xml',
        'views/res_partner.xml'],
    'development_status':'Beta',
    'maintainers': ['eficient'],
}