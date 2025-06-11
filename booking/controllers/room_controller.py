from odoo import http

class RoomController(http.Controller):

    @http.route('/booking', auth='public', type='http')
    def book(self, **kw):
        return "Hello, World!"