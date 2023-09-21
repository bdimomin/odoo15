from odoo import api, fields, models, _


class TeacherTeacher(models.Model):
    _name = "teacher.teacher"
    _order = "name"
    _description = "Teacher"

    id_number = fields.Char(string="ID Number", required=True)
    name = fields.Char(string="Name", required=True)
    group = fields.Selection ([ 
        ('business studies', 'Business Studies'),
        ('humanities', 'Humanities'),
        ('science', 'Science'),


    ])
    gender = fields.Selection ([ 
        ('male', 'Male'),
        ('female', 'Female'),

    ])
    phone = fields.Char(string="Contact", required=True)
    about = fields.Text()
    student_id= fields.One2many('student.student','teacher_id', string="Student")
    management_id = fields.Many2one('management.management', string="Management")

 


        
