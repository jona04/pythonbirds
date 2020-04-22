from unittest import TestCase

from oo.motor import Motor


class CarroTestCase(TestCase):
    def test_velocidade_inicial(self):
        motor=Motor()
        self.assertEqual(0,motor.velocidade)

    def test_acelerar(self):
        motor=Motor()
        motor.acelerar()
        self.assertEqual(1,motor.velocidade)

    def test_frear(self):
        motor=Motor()
        motor.acelerar()
        motor.acelerar()
        motor.frear()
        self.assertEqual(0,motor.velocidade)