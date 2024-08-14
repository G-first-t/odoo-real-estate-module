from odoo import fields,models,api


class PropertyOffer(models.Model):
    _name="property.offer"

    price=fields.Float('Price')
    status=fields.Selection(string="status",
                            selection=[
                                ('Accepted','Accepted'),
                                ('Refused','Refused')])
    partner_id=fields.Many2one('res.partner')
    property_id=fields.Many2one('my_estate')