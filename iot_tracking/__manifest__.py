{
    'name': "iot Device Tracking Application",

    'summary': """
        This module tracks the movements of device objects assigned to company resources such as employees, machines, rfid tags for inventory tracking etc. and provides reporting facilities for end users""",
    'author':'Abdulkadir Yilmaz, EMine Rumeysa Yilmaz',
    'website':'https://github.com/rumeysayilmaz/odoo-training-tr',
    'license':'LGPL-3',
    'depends':['base'],
    'data':[
        'security/ir.model.access.csv',
        'views/tracking_location_view.xml',
        'views/tracking_deviceobject_view.xml',
        'views/tracking_device_view.xml',
        'views/tracking_authorization_view.xml',
        'views/tracking_movement.xml'],
    'development_status':'Beta',
    'maintainers': ['rumeysa yilmaz abdulkadir yilmaz'],
}