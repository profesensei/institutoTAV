from django.test import TestCase

# Create your tests here.
import unittest
from personas.models import Alumno

# assertTrue
# assertFalse
# assertEquals


class testAlumno(unittest.TestCase):
    '''
    def test_crear_objeto(self):
        alumno = Alumno.objects.create(fecha_nacimiento='2020-10-23',
                                       rut='10-4',
                                       nombre='Susana',
                                       apellido_paterno='Correa',
                                       apellido_materno='Lopez',
                                       genero='femenino',
                                       activo=1,
                                       foto='' )
        alumno.save()

        self.assertTrue(alumno,True)
    '''

    def test_val_rut(self):
        alumno = Alumno.objects.get( rut = '10-4')
        #programar, validad, if,
        self.assertEquals(alumno.rut, '10-4')


    def test_crear_demo(self):
        a=1
        self.assertEqual(a,1)