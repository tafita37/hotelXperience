{
    'name': 'booking',
    'version': '1.0',
    'depends': ['hotel'],
    'data': [
        'security/ir.model.access.csv',  
        
        'views/hotel_menu_view.xml'
    ],
    'author': 'Moi',
    'category': 'Uncategorized',
    'description': 'A streamlined system to handle hotel room bookings: real-time availability tracking, booking confirmation, guest management',
    'installable': True,
    'application': True,
}