from odoo import models, fields

class HotelRoomCategory(models.Model):
    _name = 'hotel.room.category'
    _description = 'Defines room categories with a unique ID, name, level, and rate increase for pricing.'

    name = fields.Char(string='Category name', required=True, unique=True)
    level = fields.Integer(string='Level', required=True, unique=True)
    rate_increase = fields.Float(string='Rate Increase', required=True, unique=True)