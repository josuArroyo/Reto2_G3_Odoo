# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Event(models.Model):
    _name = 'grupo3c.event'

    eventId = fields.Integer(string = "Event Id", required = True)
    eventType = fields.Char(string = "Event Type", required = True)
    description = fields.Text(string = "Description", required = True)
    numPart = fields.Integer(string= "Number of Participants", required = True)
    date = fields.Date(string = "Date", required = True)
    admin_id = fields.Many2one('res.Users',string="Organizer", required = True)
    customer_id = fields.Many2many('res.Users', string = "Customers", required = True)
    place = fields.Many2one('grupo3c.place', string = "Place", required = True)