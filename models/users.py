# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Users (models.Model):
    _name = 'res.users'
    _inherit = 'res.users'

    isAdmin = fields.Boolean(string = "Admin")
    isClient = fields.Boolean(string = "Client")
    
    admin_event_ids = fields.One2many ("grupo3c.event", 'admins', string = "Event id")
    place_ids = fields.One2many("grupo3c.place", 'admin_id', string= "Place id")
    training_ids = fields.One2many("grupo3c.training", 'admin_ids', string = "Training id")
    objective_id = fields.One2many("grupo3c.objective", 'admin', string="Objective id")
    event_ids = fields.Many2many("grupo3c.event", string = "Event id")
    objective_ids = fields.Many2many("grupo3c.objective",string = "Objective ids")
