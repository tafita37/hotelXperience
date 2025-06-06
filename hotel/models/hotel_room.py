from odoo import models, fields

class HotelRoom(models.Model):
    _name = 'hotel.room'
    _description = 'Defines the essential information for each room in a hotel, including pricing, status, and category, as well as the capacity and associated hotel.'

    number = fields.Integer(string='Room number', required=True, unique=True)
    price = fields.Float(string='Room price', required=True)
    state = fields.Selection(
        selection=[
            ('available', 'Available'),
            ('occupied', 'Occupied'),
        ],
        string="Status",
        default='available',
        readonly=True   
    )
    room_category_id  = fields.Many2one('hotel.room.category', string='Category room', required=True)
    supported_person_count = fields.Integer(string='Number of people supported', required=True)