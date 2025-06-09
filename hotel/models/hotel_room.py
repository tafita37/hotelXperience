from odoo import models, fields, api

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

    total_price = fields.Float(
        string='Total Price',
        compute='_compute_total_price',
        store=True
    )

    @api.depends('price', 'room_category_id.rate_increase', 'supported_person_count')
    def _compute_total_price(self):
        for rec in self:
            base = rec.price or 0.0
            cat_increase = rec.room_category_id.rate_increase if rec.room_category_id else 0.0

            # Chercher le premier hotel.room.person.support où min_person_count <= supported_person_count, trié par min_person_count desc
            person_support = self.env['hotel.room.person.support'].search(
                [('min_person_count', '<=', rec.supported_person_count)],
                order='min_person_count desc',
                limit=1
            )
            person_increase = person_support.rate_increase if person_support else 0.0

            rec.total_price = base + (cat_increase * base / 100) + (person_increase * base / 100)