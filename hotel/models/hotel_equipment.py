from odoo import models, fields

class HotelEquipment(models.Model):
    _name = 'hotel.equipment'
    _description = 'Stores equipment details for hotels, including name, description and price.'

    name = fields.Char(string='Category name', required=True, unique=True)
    description = fields.Text(string='Description', required=True, unique=True)
    price = fields.Float(string='Price', required=True)