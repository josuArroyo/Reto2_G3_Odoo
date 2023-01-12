# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class Place(models.Model):
    _name = 'grupo3c.place' 
    
    place_id = fields.Char(required=True ,string="place_id")
    name = fields.Char(required=True ,string="name")     
    description = fields.Text(required=True ,string="description")
    placeType = fields.Char(required=True ,string="placeType")
    date = fields.Date(required=True ,string="date")
    #tenant = person who rents a place
    Admin_id = fields.Many2one('res.users',string="tenant" , required = True)
    Events_ids = fields.One2many('grupo3c.event', "place", string="eventPlaceCode")
   

