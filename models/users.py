# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Users (models.Model):
    _name = 'res.users'
    _inherit = 'res.users'

    isAdmin = fields.Boolean(string = "Admin")
    isClient = fields.Boolean(string = "Client")
    
    
    place_ids = fields.One2many ("grupo3c.place", "admin_id", string= "Place id")
    training_ids = fields.One2many("grupo3c.training", 'admin_ids',string = "Trainingid")
    objective_id = fields.One2many("grupo3c.objective", 'admin', string="Objectiveid")
    admin_event_ids = fields.One2many ("grupo3c.event", 'admins', string = "Eventid")
    
    event_ids = fields.Many2many("grupo3c.event", string = "Eventid")
    objective_ids = fields.Many2many("grupo3c.objective",string = "Objective ids")