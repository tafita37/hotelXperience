from odoo import http
from odoo.http import request
from odoo.exceptions import AccessDenied

class EquipmentController(http.Controller):

    @http.route('/equipment', auth='user', website=True)
    def list_equipment(self, **kw):
        # Vérifier que l'utilisateur appartient au groupe base.group_system
        if not request.env.user.has_group('base.group_system'):
            raise AccessDenied("Access denied: you must be an administrator to access this page.")
        
        equipments = request.env['hotel.equipment'].sudo().search([])
        return request.render('hotel.equipment_list_template', {
            'equipments': equipments
        })

    @http.route('/equipment/<model("hotel.equipment"):equipment>', auth='public', website=True)
    def equipment_detail(self, equipment, **kw):
        return request.render('hotel.equipment_detail_template', {
            'equipment': equipment
        })

    @http.route('/equipment/create', auth='user', website=True, methods=['GET', 'POST'])
    def create_equipment(self, **post):
        if not request.env.user.has_group('base.group_system'):
            raise AccessDenied("Access denied: you must be an administrator to access this page.")
        if http.request.httprequest.method == 'POST':
            request.env['hotel.equipment'].sudo().create({
                'name': post.get('name'),
                'description': post.get('description'),
                'price': post.get('price'),
            })
            return request.redirect('/equipment')
        return request.render('hotel.equipment_create_template', {})

    @http.route('/equipment/<model("hotel.equipment"):equipment>/edit', auth='user', website=True, methods=['GET', 'POST'])
    def edit_equipment(self, equipment, **post):
        if not request.env.user.has_group('base.group_system'):
            raise AccessDenied("Access denied: you must be an administrator to access this page.")
        if http.request.httprequest.method == 'POST':
            equipment.sudo().write({
                'name': post.get('name'),
                'description': post.get('description'),
            })
            return request.redirect('/equipment')
        return request.render('hotel.equipment_edit_template', {
            'equipment': equipment
        })

    @http.route('/equipment/<model("hotel.equipment"):equipment>/delete', auth='user', website=True, methods=['GET'])
    def delete_equipment(self, equipment, **kw):
        if not request.env.user.has_group('base.group_system'):
            raise AccessDenied("Access denied: you must be an administrator to access this page.")
        equipment.sudo().unlink()
        return request.redirect('/equipment')