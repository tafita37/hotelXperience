from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HotelRoomPersonSupport(models.Model):
    _name = 'hotel.room.person.support'
    _description = 'This table allows you to specify the rate increase based on the number of people supported in a room.'

    min_person_count = fields.Integer(string='Minimum number', required=True, unique=True)
    rate_increase  = fields.Float(string='Rate increase', required=True, unique=True)

    @api.model
    def create(self, vals):
        # Vérifier la valeur maximale actuelle de min_person_count
        max_min_person_count = self.env['hotel.room.person.support'].search([], order='min_person_count desc', limit=1).min_person_count
        # Vérifier la valeur maximale actuelle de rate_increase
        max_rate_increase = self.env['hotel.room.person.support'].search([], order='rate_increase desc', limit=1).rate_increase

        # Contrôler que les nouvelles valeurs soient supérieures
        if max_min_person_count and int(vals.get('min_person_count')) <= max_min_person_count:
            raise ValidationError(f"The 'Minimum number' must be greater than the current maximum ({max_min_person_count}).")
        if max_rate_increase and int(vals.get('rate_increase')) <= max_rate_increase:
            raise ValidationError(f"The 'Rate increase' must be greater than the current maximum ({max_rate_increase}).")

        return super(HotelRoomPersonSupport, self).create(vals)