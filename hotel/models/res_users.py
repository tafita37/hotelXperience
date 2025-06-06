from odoo import models, fields, api

class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def create(self, vals):
        if not vals.get('groups_id'):
            # base.group_user is the default internal user group
            group_user = self.env.ref('base.group_user')
            vals['groups_id'] = [(6, 0, [group_user.id])]
        return super(ResUsers, self).create(vals)
