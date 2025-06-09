from odoo import http
from odoo.http import request
from odoo.exceptions import AccessDenied

class RoomController(http.Controller):

    @http.route(['/room', '/'], auth='user', website=True)
    def list_room(self, **kw):
        if not request.env.user.has_group('base.group_system'):
            raise AccessDenied("Access denied: you must be an administrator to access this page.")

        rooms = request.env['hotel.room'].sudo().search([])
        return request.render('hotel.room_list_template', {
            'rooms': rooms
        })
    
    @http.route('/room/create', auth='user', website=True, methods=['GET', 'POST'])
    def create_room(self, **post):
        if not request.env.user.has_group('base.group_system'):
            raise AccessDenied("Access denied: you must be an administrator to access this page.")
        if http.request.httprequest.method == 'POST':
            request.env['hotel.room'].sudo().create({
                'number': post.get('number'),
                'price': post.get('price'),
                'supported_person_count': post.get('supported_person_count'),
                'room_category_id': post.get('room_category_id'),
            })
            return request.redirect('/room')
        categories = request.env['hotel.room.category'].sudo().search([])
        return request.render('hotel.room_create_template', {
            'categories': categories
        })
    
    @http.route(
        '/room/<model("hotel.room"):room>/edit', 
        auth='user', 
        website=True, 
        methods=['GET', 'POST']
    )
    def edit_room(self, room, **post):
        print(post.get('room_category_id'), "ypuuuuu")
        if not request.env.user.has_group('base.group_system'):
            raise AccessDenied("Access denied: you must be an administrator to access this page.")
        if http.request.httprequest.method == 'POST':
            room.sudo().write({
                'price': post.get('price'),
                'room_category_id': int(post.get('room_category_id')) if post.get('room_category_id') else False,
                'supported_person_count': post.get('supported_person_count'),
            })
            return request.redirect('/room')
        categories = request.env['hotel.room.category'].sudo().search([])
        return request.render('hotel.room_edit_template', {
            'room': room,
            'categories': categories
        })
    
    @http.route('/room/person_support', auth='user', website=True)
    def list_person_support(self, **kw):
        if not request.env.user.has_group('base.group_system'):
            raise AccessDenied("Access denied: you must be an administrator to access this page.")

        person_supports = request.env['hotel.room.person.support'].sudo().search([])
        return request.render('hotel.person_support_list_template', {
            'person_supports': person_supports
        })
    
    @http.route('/room/person_support/create', auth='user', website=True, methods=['GET', 'POST'])
    def create_person_support(self, **post):
        if not request.env.user.has_group('base.group_system'):
            raise AccessDenied("Access denied: you must be an administrator to access this page.")
        if http.request.httprequest.method == 'POST':
            request.env['hotel.room.person.support'].sudo().create({
                'min_person_count': post.get('min_person_count'),
                'rate_increase': post.get('rate_increase'),
            })
            return request.redirect('/room/person_support')
        return request.render('hotel.person_support_create_template', {})
    
    @http.route(
        '/room/person_support/<model("hotel.room.person.support"):person_support>/edit', 
        auth='user', 
        website=True, 
        methods=['GET', 'POST']
    )
    def edit_person_support(self, person_support, **post):
        if not request.env.user.has_group('base.group_system'):
            raise AccessDenied("Access denied: you must be an administrator to access this page.")
        if http.request.httprequest.method == 'POST':
            person_support.sudo().write({
                'min_person_count': post.get('min_person_count'),
                'rate_increase': post.get('rate_increase'),
            })
            return request.redirect('/room/person_support')
        return request.render('hotel.person_support_edit_template', {
            'person_support': person_support
        })
    
    @http.route(
        '/room/person_support/<model("hotel.room.person.support"):person_support>/delete', auth='user', website=True, methods=['GET']
    )
    def delete_person_support(self, person_support, **kw):
        if not request.env.user.has_group('base.group_system'):
            raise AccessDenied("Access denied: you must be an administrator to access this page.")
        person_support.sudo().unlink()
        return request.redirect('/room/person_support')
