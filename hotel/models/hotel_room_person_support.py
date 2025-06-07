from odoo import models, fields

class HotelRoomPersonSupport(models.Model):
    _name = 'hotel.room.person.support'
    _description = 'This table allows you to specify the rate increase based on the number of people supported in a room.'

    min_person_count = fields.Integer(string='Minimum number', required=True, unique=True)
    rate_increase  = fields.Float(string='Rate increase', required=True, unique=True)