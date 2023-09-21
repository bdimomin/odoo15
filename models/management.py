from odoo import api, fields, models, _


class ManagementManagement(models.Model):
    _name = "management.management"
    _order = "name"
    _description = "Management"

    name = fields.Char(string="Name", required=True)
    id_number = fields.Char(string="ID", required=True)
    gender = fields.Selection ([ 
        ('male', 'Male'),
        ('female', 'Female'),

    ])
    phone = fields.Char(string="Contact", required=True)
    about = fields.Text()
    teacher_id= fields.One2many('teacher.teacher','management_id',string="Teacher")
    student_id= fields.One2many('student.student','management_id', string="Student")
 


        
