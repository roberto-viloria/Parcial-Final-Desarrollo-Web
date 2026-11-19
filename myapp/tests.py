from django.test import TestCase
from django.urls import reverse

from .models import Programa


class CrearProgramaTests(TestCase):
    def test_crea_programa_y_muestra_confirmacion(self):
        self.assertEqual(reverse("programas:crear_programa"), "/programas/crear/")

        response = self.client.post(
            reverse("programas:crear_programa"),
            {
                "codigo": "ING01",
                "nombre": "Ingeniería",
                "estado": "on",
                "facultad": "Ingeniería",
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(Programa.objects.filter(codigo="ING01").exists())
        self.assertContains(response, "El programa se registró correctamente.")

    def test_codigo_duplicado_no_crea_otro_programa(self):
        Programa.objects.create(
            codigo="ING01",
            nombre="Ingeniería",
            facultad="Ingeniería",
        )

        response = self.client.post(
            reverse("programas:crear_programa"),
            {
                "codigo": "ING01",
                "nombre": "Ingeniería de sistemas",
                "estado": "on",
                "facultad": "Ingeniería",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Programa.objects.filter(codigo="ING01").count(), 1)
        self.assertTrue(response.context["form"].has_error("codigo"))