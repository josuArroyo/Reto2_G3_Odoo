# -*- coding: utf-8 -*-

from odoo import models, fields, api

class pepito (models.Model):
    _name = 'res.Users'
    _inherit = 'res.Users'

    eventId = fields.One2Many ("grupo3c.event", string = "Event id")
    isAdmin = fields.Boolean(string = "Admin", required = True)
    isClient = fields.Boolean(string = "Clien", required = True)
    placeId = fields.One2Many("grupo3c.Place",string= "Place id", required = True)
    trainingId = fields.One2many("grupo3c.training", string = "Training id", required = True)
    objective_id = fields.One2Many("grupo3c.objective", string="Objective id", required = True)
    event_ids = fields.Many2many("grupo3c.event", string = "Event id", required = True)
    objective_ids = fields.Many2many("grupo3c.objective",string = "Objective ids", required = True)