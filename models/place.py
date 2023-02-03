# -*- coding: utf-8 -*-

from odoo import api
from odoo import exceptions
from odoo import fields
from odoo import models

class Place(models.Model):
    _name = 'grupo3c.place' 
    
    name = fields.Char(required=True, string="Name")     
    description = fields.Text(required=True, string="Description")
    placeType = fields.Char(required=True, string="Type of place")
    date = fields.Date(required=True, string="Date")
    #tenant = person who rents a place
    admin_id = fields.Many2one('res.users', string="tenant")
    event_ids = fields.One2many('grupo3c.event', "place_id", string="eventPlaceCode")
    
 
    @api.constrains('date')
    def _validate_date(self):
        for place in self:
            if fields.Date.from_string(place.date) < fields.Date.from_string(fields.Date.today()):
                raise exceptions.ValidationError("Date cannot be lower than the actual one")
            
    @api.onchange('description')
    def _onchange_description(self):
        if len(str(self.description)) > 100:
            return{
        'warning' : {
            'title':"something bad happened",
            'message':"you have reached the maximum characters allowed"
            }
        }
        
    @api.onchange('name')
    def _onchange_name(self):
        if len(str(self.name)) > 100:
            return{
        'warning' : {
            'title':"something bad happened",
            'message':"you have reached the maximum characters allowed"
            }
        }
   
    

        
