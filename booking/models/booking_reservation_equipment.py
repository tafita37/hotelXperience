from odoo import models, fields

class BookingReservationEquipment(models.Model):
    _name = 'booking.reservation.equipment'
    _description = 'Booking Reservation Equipment'

    reservation_id = fields.Many2one('booking.reservation', string='Reservation', required=True)
    equipment_id = fields.Many2one('hotel.equipment', string='Equipment', required=True)