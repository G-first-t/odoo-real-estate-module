from odoo import fields,models,api

class MyEstate(models.Model):
    _name="my_estate"
    _description="this is for real estate management"


    name=fields.Char(string="Name", required=True)
    description=fields.Text(string="Description")
    postcode=fields.Char(string="Postcode")
    date_availability=fields.Date(string="Available Date",required=True)
    expected_price=fields.Float(string="Expected Price")
    selling_price=fields.Float(string="Selling Price")
    bedrooms=fields.Integer(string="Bedrooms")
    living_area=fields.Integer(string="Living Area")
    facades=fields.Integer(string="Facades")
    garage=fields.Boolean(string="Garage")
    garden=fields.Boolean(string="Garden")
    garden_area=fields.Integer(string="Garden Area")
    garden_orientation=fields.Selection(string="Garden Orientation",
                                        selection=[("north","north"),
                                                   ("south","south"),
                                                   ("east","east"),
                                                   ("west","west")])







    