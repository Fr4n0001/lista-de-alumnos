#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 01:09:54 2022

@author: albert
"""

class lista():
    alumnos=[]
    seccion='none'
    def add_student(self,student):
        if type(student) != dict:
            print('El objeto "student" debe ser de tipo diccionario')
        else:
            self.alumnos.append(student)
            
