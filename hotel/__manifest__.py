{
    'name': 'hotel',
    'version': '1.0',
    'depends': ['base', 'web', 'website'],
    'data': [
        'data/demo_data/hotel_room_category_data.xml',  
        'data/demo_data/hotel_equipment_data.xml',  
        'data/demo_data/hotel_room_person_support_data.xml',  
        'data/demo_data/hotel_room_data.xml',  

        'security/ir.model.access.csv',  

        'views/hotel_equipment_templates.xml',
        'views/hotel_equipment_form_templates.xml',
        'views/hotel_equipment_edit_templates.xml',
        'views/hotel_room_person_support_templates.xml',
        'views/hotel_room_person_support_form_templates.xml',
        'views/hotel_room_person_support_edit_templates.xml',
        'views/hotel_room_templates.xml',
        'views/hotel_room_form_templates.xml',
        'views/hotel_room_edit_templates.xml',
        'views/hotel_menu_view.xml'
    ],
    'author': 'Moi',
    'category': 'Uncategorized',
    'description': 'This module provides the core data models and basic views to manage hotel services in Odoo. It establishes a solid foundation for extending hotel-specific functionalities.',
    'installable': True,
    'application': True,
}