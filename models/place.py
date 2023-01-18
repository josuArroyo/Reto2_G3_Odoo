# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class Place(models.Model):
    _name = 'grupo3c.place' 
    
    name = fields.Char(required=True ,string="name")     
    description = fields.Text(required=True ,string="description")
    placeType = fields.Char(required=True ,string="placeType")
    date = fields.Date(required=True ,string="date")
    #tenant = person who rents a place
    admin_id = fields.Many2one('res.users',string="tenant")
    event_ids = fields.One2many('grupo3c.event', "place_id", string="eventPlaceCode")