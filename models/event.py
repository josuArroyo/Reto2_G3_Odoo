# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Event(models.Model):
    _name = 'grupo3c.event'

    eventId = fields.Integer(string = "Event Id", requitred = True)
    eventType = fields.Char(string = "Event Type", requitred = True)
    description = fields.Text(string = "Description", requitred = True)
    numPart = fields.Integer(string= "Number of Participants", requitred = True)
    date = fields.Date(string = "Date", requitred = True)
    admin_id = fields.Many2one('admin',string="Organizer", requitred = True)
    customer_id = fields.Many2many('customer', string = "Customers", requitred = True)
    place = fields.Many2one('place', string = "Place", requitred = True)