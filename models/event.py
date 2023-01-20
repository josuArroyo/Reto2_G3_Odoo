# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Event(models.Model):
    _name = 'grupo3c.event'

    eventType = fields.Char(string = "Event Type", required = True)
    description = fields.Text(string = "Description", required = True)
    numPart = fields.Integer(string= "Number of Participants", required = True)
    date = fields.Date(string = "Date", required = True)
    
    
    admins = fields.Many2one('res.users',string="Organizer", required = True)
    customer_id = fields.Many2many('res.users', string = "Customers", required = True)
    place_id = fields.Many2one('grupo3c.place', string= "Place", required = True)
    
