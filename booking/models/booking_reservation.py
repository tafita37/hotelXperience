from odoo import models, fields

class BookingReservation(models.Model):
    _name = 'booking.reservation'
    _description = 'Booking Reservation'

    client_id = fields.Many2one(
        'res.users',
        string='Client',
        required=True,
        help='The client making the reservation'
    )
    room_id = fields.Many2one(
        'hotel.chambre',
        string='Room',
        required=True,
        help='The room being reserved'
    )
    creation_date = fields.Datetime(
        string='Creation Date',
        default=lambda self: fields.Datetime.now(),
        help='The date and time when the reservation was created'
    )
    start_datetime = fields.Datetime(
        string='Start Date',
        required=True,
        help='The start date and time of the reservation'
    )
    reservation_duration = fields.Integer(
        string='Reservation Duration (days)',
        required=True,
        help='The duration of the reservation in days'
    )
    end_date_time= fields.Datetime(
        string='End Date',
        compute='_compute_date_heure_sortie',
        store=True,
        help='The end date and time of the reservation, computed from start date and duration'
    )
    number_of_people = fields.Integer(
        string='Number of People',
        required=True,
        help='The number of people for the reservation'
    )