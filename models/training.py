# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.



from odoo import models, fields, api
from odoo import exceptions

class Training(models.Model):
    _name = 'grupo3c.training'
     
     #cargar sin one2many y revisar que el modelo este bien.
     #commit del codigo y partir todos del mismo codigo.
     #probamos one2many cada uno en su entidad uno a uno.
    name = fields.Text(string= "Name of training", required = True) 
    description = fields.Text(string= "Description of training", required = True)
    duration = fields.Float(string= "Duration of training", required = True)
    periodStart = fields.Date(string= "Start date of training", required = True)
    periodEnd = fields.Date(string= "End date of training", required = True)
    intensity = fields.Integer(string= "Intensity of training", required = True)
    repeats = fields.Integer(string= "Repeats of training", required = True)
    objectiveId = fields.Many2one("grupo3c.objective", string= "Objective Id")
    admin_ids = fields.Many2one ("res.users", string= "Admin ids")

    
    #La descripcion no puede superar los 100 caracteres
    @api.onchange ('description')
    def _onchange_description(self):
        if len(str(self.description)) > 100:
            return {
        'warning' : {
            'title': "Something bad happened",
            'message': "You have reached the maximum characters allowed"
        }     
    }
   
    #La descripcion no puede superar los 100 caracteres
    @api.constrains('description')
    def _check_description(self):
        for training in self:
             if len(str(self.description)) > 100:
                raise exceptions.ValidationError("La descripcion no puede superar los 100 caracters.")
    
    
    #La duracion no puede ser anterior a la actual
#    @api.constrains('periodTime')
#    def _check_periodTime(self):
#        for training in self:
#             if fields.Date.from_string(training.periodTime) < fields.Date.from_string(fields.Date.today()):
#                raise exceptions.ValidationError("El tiempo de periodo no puede ser anterior a la fecha actual.")

    #Validar que periodEnd es mayor que periodStart.
    @api.onchange('periodEnd')
    def _onchange_periodEnd(self):
        if self.periodEnd < self.periodStart:
            return {
        'warning': {
            'title': "Something bad happened",
            'message': "Period end must be greater than period start "
        }     
    }
            
    @api.constrains('periodEnd', 'periodStart')
    def _check_periodEnd_greater_periodStart(self):
        for training in self:
            if self.periodEnd < self.periodStart:
                raise exceptions.ValidationError("Period end must be greater than period start.")
  
   
    #La duracion no puede ser numero negativo
    @api.onchange ('duration')
    def _onchange_duration(self):
        if not (0 <= (self.duration)<=90 ):
            return {
        'warning': {
            'title': "Something bad happened",
            'message': "Duration cannot be negative or exceed 90 minutes "
        }     
    }
    
    #La duracion no puede superar los 100 caracteres
    @api.constrains('duration')
    def _check_duration(self):
        for training in self:
             if not (0 <= (self.duration)<=90 ):
                raise exceptions.ValidationError("La duracion no puede ser negativa ni superar los 90 minutos.")
            

    #La intensidad solo admite numero entre el 1 y el 10
    @api.onchange ('intensity')
    def _onchange_intensity(self):
        if not (0 <= (self.intensity)<=10 ):
            return {
        'warning': {
            'title': "Something bad happened",
            'message': "The intensity has to be between 1 and 10"
        }     
    }
    
    #La intensidad solo admite numero entre el 1 y el 10
    @api.constrains('intensity')
    def _check_intensity(self):
        for training in self:
             if not (0 <= (self.intensity)<=10 ):
                raise exceptions.ValidationError("La intensidad tiene que ser del 1 al 10.")
    
    
    
    #Las repeticiones solo admiten numeros entre el 1 y el 20
    @api.onchange ('repeats')
    def _onchange_repeats(self):
        if not (0 <= (self.repeats)<=20 ):
            return {
        'warning': {
            'title': "Something bad happened",
            'message': "The repeats has to be between 1 and 20"
        }     
    }
    
     #Las repeticiones solo admiten numeros entre el 1 y el 20
    @api.constrains('repeats')
    def _check_intensity(self):
        for training in self:
             if not (0 <= (self.repeats)<=20 ):
                raise exceptions.ValidationError("Las repeticiones tienen que ser del 1 al 20.")
   

    
    
    
            
    

    
