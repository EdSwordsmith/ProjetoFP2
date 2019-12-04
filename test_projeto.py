import unittest
import projeto
import StringIO
import sys

# NOTAS:
# Em eh_posicao apenas sao testados casos que devem retornar True.
# Em eh_unidade apenas sao testados casos que devem retornar True.



class TestPosicao(unittest.TestCase):

    def setUp(self):
        self.pos_1 = projeto.cria_posicao(0, 0)
        self.pos_2 = projeto.cria_posicao(0, 10)
        self.pos_3 = projeto.cria_posicao(10, 0)
        self.pos_4 = projeto.cria_posicao(10, 10)

    def test_cria_posicao(self):
        self.assertIsNotNone(projeto.cria_posicao(0, 0))
        self.assertIsNotNone(projeto.cria_posicao(0, 10))
        self.assertIsNotNone(projeto.cria_posicao(10, 0))
        self.assertIsNotNone(projeto.cria_posicao(10, 10))

        with self.assertRaises(ValueError): projeto.cria_posicao(-1, 0)
        with self.assertRaises(ValueError): projeto.cria_posicao(0, -1)
        with self.assertRaises(ValueError): projeto.cria_posicao(-1, -1)
        with self.assertRaises(ValueError): projeto.cria_posicao(-1, 0)
        with self.assertRaises(ValueError): projeto.cria_posicao(0, -1)
        with self.assertRaises(ValueError): projeto.cria_posicao(-10, -10)
        with self.assertRaises(ValueError): projeto.cria_posicao(0.0, 0)
        with self.assertRaises(ValueError): projeto.cria_posicao(0, 0.0)
        with self.assertRaises(ValueError): projeto.cria_posicao(0.0, 0.0)
        with self.assertRaises(ValueError): projeto.cria_posicao("0", 0)
        with self.assertRaises(ValueError): projeto.cria_posicao(0, "0")
        with self.assertRaises(ValueError): projeto.cria_posicao("0", "0")

    def test_cria_copia_posicao(self):
        self.assertTrue(projeto.posicoes_iguais(
            projeto.cria_copia_posicao(self.pos_1), self.pos_1))
        self.assertTrue(projeto.posicoes_iguais(
            projeto.cria_copia_posicao(self.pos_2), self.pos_2))
        self.assertTrue(projeto.posicoes_iguais(
            projeto.cria_copia_posicao(self.pos_3), self.pos_3))
        self.assertTrue(projeto.posicoes_iguais(
            projeto.cria_copia_posicao(self.pos_4), self.pos_4))

    def test_obter_pos_x(self):
        self.assertEqual(projeto.obter_pos_x(self.pos_1), 0)
        self.assertEqual(projeto.obter_pos_x(self.pos_2), 0)
        self.assertEqual(projeto.obter_pos_x(self.pos_3), 10)
        self.assertEqual(projeto.obter_pos_x(self.pos_4), 10)

    def test_obter_pos_y(self):
        self.assertEqual(projeto.obter_pos_y(self.pos_1), 0)
        self.assertEqual(projeto.obter_pos_y(self.pos_2), 10)
        self.assertEqual(projeto.obter_pos_y(self.pos_3), 0)
        self.assertEqual(projeto.obter_pos_y(self.pos_4), 10)

    def test_eh_posicao(self):
        self.assertTrue(projeto.eh_posicao(self.pos_1))
        self.assertTrue(projeto.eh_posicao(self.pos_2))
        self.assertTrue(projeto.eh_posicao(self.pos_3))
        self.assertTrue(projeto.eh_posicao(self.pos_4))

        self.assertFalse(projeto.eh_posicao([]))
        self.assertFalse(projeto.eh_posicao(()))
        self.assertFalse(projeto.eh_posicao([0]))
        self.assertFalse(projeto.eh_posicao((0,)))
        self.assertFalse(projeto.eh_posicao([0, -1]))
        self.assertFalse(projeto.eh_posicao((0, -1)))
        self.assertFalse(projeto.eh_posicao([-1, 0]))
        self.assertFalse(projeto.eh_posicao((-1, 0)))
        self.assertFalse(projeto.eh_posicao([-1, -1]))
        self.assertFalse(projeto.eh_posicao((-1, -1)))


    def test_posicoes_iguais(self):
        self.assertTrue(projeto.posicoes_iguais(self.pos_1, self.pos_1))
        self.assertTrue(projeto.posicoes_iguais(self.pos_2, self.pos_2))
        self.assertTrue(projeto.posicoes_iguais(self.pos_3, self.pos_3))
        self.assertTrue(projeto.posicoes_iguais(self.pos_4, self.pos_4))

        self.assertFalse(projeto.posicoes_iguais(self.pos_1, self.pos_2))
        self.assertFalse(projeto.posicoes_iguais(self.pos_1, self.pos_3))
        self.assertFalse(projeto.posicoes_iguais(self.pos_1, self.pos_4))
        self.assertFalse(projeto.posicoes_iguais(self.pos_2, self.pos_3))
        self.assertFalse(projeto.posicoes_iguais(self.pos_2, self.pos_4))
        self.assertFalse(projeto.posicoes_iguais(self.pos_3, self.pos_4))

    def test_posicao_para_str(self):
        self.assertEqual(projeto.posicao_para_str(self.pos_1), "(0, 0)")
        self.assertEqual(projeto.posicao_para_str(self.pos_2), "(0, 10)")
        self.assertEqual(projeto.posicao_para_str(self.pos_3), "(10, 0)")
        self.assertEqual(projeto.posicao_para_str(self.pos_4), "(10, 10)")

    def test_obter_posicoes_adjacentes(self):
        self.assertEqual(
            projeto.obter_posicoes_adjacentes(projeto.cria_posicao(0, 0)),
            (projeto.cria_posicao(1, 0),
            projeto.cria_posicao(0, 1))
        )
        self.assertEqual(
            projeto.obter_posicoes_adjacentes(projeto.cria_posicao(0, 10)),
            (projeto.cria_posicao(0, 9),
            projeto.cria_posicao(1, 10),
            projeto.cria_posicao(0, 11))
        )
        self.assertEqual(
            projeto.obter_posicoes_adjacentes(projeto.cria_posicao(10, 0)),
            (projeto.cria_posicao(9, 0),
            projeto.cria_posicao(11, 0),
            projeto.cria_posicao(10, 1))
        )
        self.assertEqual(
            projeto.obter_posicoes_adjacentes(projeto.cria_posicao(10, 10)),
            (projeto.cria_posicao(10, 9),
            projeto.cria_posicao(9, 10),
            projeto.cria_posicao(11, 10),
            projeto.cria_posicao(10, 11))
        )


# =============================================================================


class TestUnidade(unittest.TestCase):

    def setUp(self):
        self.pos_1 = projeto.cria_posicao(0, 0)
        self.pos_2 = projeto.cria_posicao(0, 10)
        self.pos_3 = projeto.cria_posicao(10, 0)
        self.pos_4 = projeto.cria_posicao(10, 10)

        self.unit_1 = projeto.cria_unidade(self.pos_1, 30, 4, "elfos")
        self.unit_2 = projeto.cria_unidade(self.pos_2, 25, 7, "elfos")
        self.unit_3 = projeto.cria_unidade(self.pos_3, 50, 2, "ogres")
        self.unit_4 = projeto.cria_unidade(self.pos_4, 40, 3, "ogres")


    def test_cria_unidade(self):
        self.assertIsNotNone(self.unit_1)
        self.assertIsNotNone(self.unit_2)
        self.assertIsNotNone(self.unit_3)
        self.assertIsNotNone(self.unit_4)

        with self.assertRaises(ValueError):
            projeto.cria_unidade("(1, 1)", 30, 4, "elfos")
        with self.assertRaises(ValueError):
            projeto.cria_unidade(self.pos_1, 0, 4, "elfos")
        with self.assertRaises(ValueError):
            projeto.cria_unidade(self.pos_1, 1.0, 4, "elfos")
        with self.assertRaises(ValueError):
            projeto.cria_unidade(self.pos_1, 1, 0, "elfos")
        with self.assertRaises(ValueError):
            projeto.cria_unidade(self.pos_1, 1, 4.0, "elfos")
        with self.assertRaises(ValueError):
            projeto.cria_unidade(self.pos_1, 1, 4, "")
        with self.assertRaises(ValueError):
            projeto.cria_unidade(self.pos_1, 1, 4, 100)

    def test_cria_copia_unidade(self):
        self.assertTrue(projeto.unidades_iguais(
            projeto.cria_copia_unidade(self.unit_1), self.unit_1))
        self.assertTrue(projeto.unidades_iguais(
            projeto.cria_copia_unidade(self.unit_2), self.unit_2))
        self.assertTrue(projeto.unidades_iguais(
            projeto.cria_copia_unidade(self.unit_3), self.unit_3))
        self.assertTrue(projeto.unidades_iguais(
            projeto.cria_copia_unidade(self.unit_4), self.unit_4))

    def test_obter_posicao(self):
        self.assertTrue(projeto.posicoes_iguais(projeto.obter_posicao(
            self.unit_1), self.pos_1))
        self.assertTrue(projeto.posicoes_iguais(projeto.obter_posicao(
            self.unit_2), self.pos_2))
        self.assertTrue(projeto.posicoes_iguais(projeto.obter_posicao(
            self.unit_3), self.pos_3))
        self.assertTrue(projeto.posicoes_iguais(projeto.obter_posicao(
            self.unit_4), self.pos_4))

    def test_obter_exercito(self):
        self.assertEqual(projeto.obter_exercito(self.unit_1), "elfos")
        self.assertEqual(projeto.obter_exercito(self.unit_2), "elfos")
        self.assertEqual(projeto.obter_exercito(self.unit_3), "ogres")
        self.assertEqual(projeto.obter_exercito(self.unit_4), "ogres")

    def test_obter_forca(self):
        self.assertEqual(projeto.obter_forca(self.unit_1), 4)
        self.assertEqual(projeto.obter_forca(self.unit_2), 7)
        self.assertEqual(projeto.obter_forca(self.unit_3), 2)
        self.assertEqual(projeto.obter_forca(self.unit_4), 3)

    def test_obter_vida(self):
        self.assertEqual(projeto.obter_vida(self.unit_1), 30)
        self.assertEqual(projeto.obter_vida(self.unit_2), 25)
        self.assertEqual(projeto.obter_vida(self.unit_3), 50)
        self.assertEqual(projeto.obter_vida(self.unit_4), 40)

    def test_muda_posicao(self):
        muda_1 = projeto.muda_posicao(self.unit_1, self.pos_2)
        muda_2 = projeto.muda_posicao(self.unit_2, self.pos_3)
        muda_3 = projeto.muda_posicao(self.unit_3, self.pos_4)
        muda_4 = projeto.muda_posicao(self.unit_4, self.pos_1)

        self.assertTrue(
            projeto.unidades_iguais(muda_1, projeto.cria_unidade(
                self.pos_2, projeto.obter_vida(self.unit_1),
                projeto.obter_forca(self.unit_1),
                projeto.obter_exercito(self.unit_1)
            ))
        )
        self.assertTrue(
            projeto.unidades_iguais(muda_2, projeto.cria_unidade(
                self.pos_3, projeto.obter_vida(self.unit_2),
                projeto.obter_forca(self.unit_2),
                projeto.obter_exercito(self.unit_2)
            ))
        )
        self.assertTrue(
            projeto.unidades_iguais(muda_3, projeto.cria_unidade(
                self.pos_4, projeto.obter_vida(self.unit_3),
                projeto.obter_forca(self.unit_3),
                projeto.obter_exercito(self.unit_3)
            ))
        )
        self.assertTrue(
            projeto.unidades_iguais(muda_4, projeto.cria_unidade(
                self.pos_1, projeto.obter_vida(self.unit_4),
                projeto.obter_forca(self.unit_4),
                projeto.obter_exercito(self.unit_4)
            ))
        )

    def test_eh_unidade(self):
        self.assertTrue(projeto.eh_unidade(self.unit_1))
        self.assertTrue(projeto.eh_unidade(self.unit_2))
        self.assertTrue(projeto.eh_unidade(self.unit_3))
        self.assertTrue(projeto.eh_unidade(self.unit_4))

    def test_unidades_iguais(self):
        self.assertTrue(projeto.unidades_iguais(self.unit_1, self.unit_1))
        self.assertTrue(projeto.unidades_iguais(self.unit_2, self.unit_2))
        self.assertTrue(projeto.unidades_iguais(self.unit_3, self.unit_3))
        self.assertTrue(projeto.unidades_iguais(self.unit_4, self.unit_4))

        self.assertFalse(projeto.unidades_iguais(self.unit_1, self.unit_2))
        self.assertFalse(projeto.unidades_iguais(self.unit_1, self.unit_3))
        self.assertFalse(projeto.unidades_iguais(self.unit_1, self.unit_4))
        self.assertFalse(projeto.unidades_iguais(self.unit_2, self.unit_3))
        self.assertFalse(projeto.unidades_iguais(self.unit_2, self.unit_4))
        self.assertFalse(projeto.unidades_iguais(self.unit_3, self.unit_4))

    def test_unidade_para_char(self):
        self.assertEqual(projeto.unidade_para_char(self.unit_1), "E")
        self.assertEqual(projeto.unidade_para_char(self.unit_2), "E")
        self.assertEqual(projeto.unidade_para_char(self.unit_3), "O")
        self.assertEqual(projeto.unidade_para_char(self.unit_4), "O")

    def test_unidade_para_str(self):
        self.assertEqual(
            projeto.unidade_para_str(self.unit_1), "E[30, 4]@(0, 0)")
        self.assertEqual(
            projeto.unidade_para_str(self.unit_2), "E[25, 7]@(0, 10)")
        self.assertEqual(
            projeto.unidade_para_str(self.unit_3), "O[50, 2]@(10, 0)")
        self.assertEqual(
            projeto.unidade_para_str(self.unit_4), "O[40, 3]@(10, 10)")

    def test_unidade_ataca(self):
        unit_1 = projeto.cria_unidade(
            projeto.cria_posicao(0, 0), 5, 4, "elfos")
        unit_2 = projeto.cria_unidade(
            projeto.cria_posicao(0, 0), 7, 3, "ogres")

        self.assertEqual(projeto.unidade_ataca(unit_1, unit_2), False)
        self.assertEqual(projeto.obter_vida(unit_1), 5)
        self.assertEqual(projeto.obter_vida(unit_2), 3)
        self.assertEqual(projeto.unidade_ataca(unit_2, unit_1), False)
        self.assertEqual(projeto.obter_vida(unit_1), 2)
        self.assertEqual(projeto.obter_vida(unit_2), 3)
        self.assertEqual(projeto.unidade_ataca(unit_1, unit_2), True)

    def test_ordenar_unidades(self):
        res = (self.unit_1, self.unit_3, self.unit_2, self.unit_4)
        res = tuple(projeto.unidade_para_str(x) for x in res)

        self.assertEqual(
            tuple(
                projeto.unidade_para_str(x) for x in projeto.ordenar_unidades(
                (self.unit_1, self.unit_2, self.unit_3, self.unit_4))), res)
        self.assertEqual(
            tuple(
                projeto.unidade_para_str(x) for x in projeto.ordenar_unidades(
                (self.unit_2, self.unit_3, self.unit_4, self.unit_1))), res)
        self.assertEqual(
            tuple(
                projeto.unidade_para_str(x) for x in projeto.ordenar_unidades(
                (self.unit_2, self.unit_4, self.unit_1, self.unit_3))), res)




# =============================================================================


class TestMapa(unittest.TestCase):

    def setUp(self):
        self.pos_1 = projeto.cria_posicao(1, 1)
        self.pos_2 = projeto.cria_posicao(1, 10)
        self.pos_3 = projeto.cria_posicao(10, 1)
        self.pos_4 = projeto.cria_posicao(10, 10)

        self.unit_1 = projeto.cria_unidade(self.pos_1, 30, 4, "elfos")
        self.unit_2 = projeto.cria_unidade(self.pos_2, 25, 7, "elfos")
        self.unit_3 = projeto.cria_unidade(self.pos_3, 50, 2, "ogres")
        self.unit_4 = projeto.cria_unidade(self.pos_4, 40, 3, "ogres")

        self.e1 = (self.unit_2, self.unit_1)
        self.e2 = (self.unit_4, self.unit_3)

        self.map_1 = projeto.cria_mapa(
            (5, 7), (projeto.cria_posicao(3, 5),), self.e1, self.e2)
        self.map_2 = projeto.cria_mapa(
            (7, 5), (projeto.cria_posicao(1, 3),), self.e2, self.e1)
        self.map_3 = projeto.cria_mapa(
            (5, 7), (projeto.cria_posicao(3, 5),), self.e2, self.e1)
        self.map_4 = projeto.cria_mapa(
            (7, 5), (projeto.cria_posicao(1, 3),), self.e1, self.e2)
        self.map_5 = projeto.cria_mapa(
            (7, 5), (projeto.cria_posicao(1, 3),), (self.unit_2,), self.e2)
        self.map_6 = projeto.cria_mapa(
            (7, 5), (projeto.cria_posicao(1, 3),), (self.unit_2,), (self.unit_3,))

        self.map_7 = projeto.cria_mapa(
            (5, 7), (projeto.cria_posicao(3, 5), projeto.cria_posicao(3, 4)), self.e1, self.e2)
        self.map_8 = projeto.cria_mapa(
            (5, 7), (projeto.cria_posicao(3, 4), projeto.cria_posicao(3, 5)), self.e1, self.e2)

    def test_cria_mapa(self):
        self.assertIsNotNone(self.map_1)
        self.assertIsNotNone(self.map_2)

        with self.assertRaises(ValueError):
            projeto.cria_mapa((3, 3.0), (), self.e1, self.e2)
        with self.assertRaises(ValueError):
            projeto.cria_mapa((3, 2), (), self.e1, self.e2)
        with self.assertRaises(ValueError):
            projeto.cria_mapa((2, 3), (), self.e1, self.e2)
        with self.assertRaises(ValueError):
            projeto.cria_mapa((3,), (), self.e1, self.e2)
        with self.assertRaises(ValueError):
            projeto.cria_mapa((3.0, 3), (), self.e1, self.e2)
        with self.assertRaises(ValueError):
            projeto.cria_mapa((3.0, 3.0), (), self.e1, self.e2)
        with self.assertRaises(ValueError):
            projeto.cria_mapa((3, "3"), (), self.e1, self.e2)
        with self.assertRaises(ValueError):
            projeto.cria_mapa(("3", 3), (), self.e1, self.e2)
        with self.assertRaises(ValueError):
            projeto.cria_mapa(("3", "3"), (), self.e1, self.e2)
        with self.assertRaises(ValueError):
            projeto.cria_mapa((3, 3), (), self.e1 + (35,), self.e2)


        with self.assertRaises(ValueError):
            projeto.cria_mapa(
                (5, 5), (projeto.cria_posicao(0, 0),), self.e1, self.e2)
        with self.assertRaises(ValueError):
            projeto.cria_mapa(
                (5, 5), (projeto.cria_posicao(1, 4),), self.e1, self.e2)
        with self.assertRaises(ValueError):
            projeto.cria_mapa(
                (5, 5), (projeto.cria_posicao(4, 1),), self.e1, self.e2)
        with self.assertRaises(ValueError):
            projeto.cria_mapa(
                (5, 5), (projeto.cria_posicao(4, 4),), self.e1, self.e2)
        with self.assertRaises(ValueError):
            projeto.cria_mapa(
                (5, 5), (projeto.cria_posicao(1, 6),), self.e1, self.e2)
        with self.assertRaises(ValueError):
            projeto.cria_mapa(
                (5, 5), (projeto.cria_posicao(6, 1),), self.e1, self.e2)
        with self.assertRaises(ValueError):
            projeto.cria_mapa(
                (5, 5), (projeto.cria_posicao(6, 6),), self.e1, self.e2)

        with self.assertRaises(ValueError):
            projeto.cria_mapa((5, 5), (
                projeto.cria_posicao(3, 3),projeto.cria_posicao(3, 2),
                projeto.cria_posicao(3, 2)), self.e1, self.e2)

    def test_cria_copia_mapa(self):
        self.assertTrue(projeto.mapas_iguais(
            projeto.cria_copia_mapa(self.map_1), self.map_1))
        self.assertTrue(projeto.mapas_iguais(
            projeto.cria_copia_mapa(self.map_2), self.map_2))

    def test_obter_tamanho(self):
        self.assertEqual(projeto.obter_tamanho(self.map_1), (5, 7))
        self.assertEqual(projeto.obter_tamanho(self.map_2), (7, 5))

    def test_obter_nome_exercitos(self):
        self.assertEqual(
            projeto.obter_nome_exercitos(self.map_1), ("elfos", "ogres"))
        self.assertEqual(
            projeto.obter_nome_exercitos(self.map_2), ("elfos", "ogres"))

    def test_obter_unidades_exercito(self):
        res1 = tuple(projeto.unidade_para_str(x) for x
            in projeto.ordenar_unidades(self.e1))
        res2 = tuple(projeto.unidade_para_str(x) for x
            in projeto.ordenar_unidades(self.e2))


        self.assertEqual(tuple(projeto.unidade_para_str(x) for x in
            projeto.obter_unidades_exercito(self.map_1, "elfos")), res1)
        self.assertEqual(tuple(projeto.unidade_para_str(x) for x in
            projeto.obter_unidades_exercito(self.map_1, "ogres")), res2)
        self.assertEqual(tuple(projeto.unidade_para_str(x) for x in
            projeto.obter_unidades_exercito(self.map_2, "elfos")), res1)
        self.assertEqual(tuple(projeto.unidade_para_str(x) for x in
            projeto.obter_unidades_exercito(self.map_2, "ogres")), res2)

    def test_obter_todas_unidades(self):
        res = tuple(projeto.unidade_para_str(x) for x
            in projeto.ordenar_unidades(self.e1 + self.e2))

        self.assertEqual(tuple(projeto.unidade_para_str(x) for x
            in projeto.obter_todas_unidades(self.map_1)), res)
        self.assertEqual(tuple(projeto.unidade_para_str(x) for x
            in projeto.obter_todas_unidades(self.map_2)), res)

    def test_obter_unidade(self):
        self.assertTrue(projeto.unidades_iguais(projeto.obter_unidade(
            self.map_1, projeto.cria_posicao(1, 10)), self.unit_2))
        self.assertTrue(projeto.unidades_iguais(projeto.obter_unidade(
            self.map_2, projeto.cria_posicao(1, 10)), self.unit_2))
        self.assertTrue(projeto.unidades_iguais(projeto.obter_unidade(
            self.map_1, projeto.cria_posicao(10, 1)), self.unit_3))
        self.assertTrue(projeto.unidades_iguais(projeto.obter_unidade(
            self.map_2, projeto.cria_posicao(10, 1)), self.unit_3))

    def test_eliminar_unidade(self):
        self.assertTrue(projeto.mapas_iguais(
            projeto.eliminar_unidade(self.map_4, self.unit_1), self.map_5
        ))
        self.assertTrue(projeto.mapas_iguais(
            projeto.eliminar_unidade(self.map_4, self.unit_4), self.map_6
        ))

    def test_mover_unidade(self):
        pos = projeto.cria_posicao(1, 2)
        self.assertEqual(projeto.unidade_para_str(projeto.obter_unidade(
            projeto.mover_unidade(self.map_1, self.unit_1, pos), pos)),
            "E[30, 4]@(1, 2)")

        pos = projeto.cria_posicao(3, 2)
        self.assertEqual(projeto.unidade_para_str(projeto.obter_unidade(
            projeto.mover_unidade(self.map_2, self.unit_3, pos), pos)),
            "O[50, 2]@(3, 2)")

    def test_eh_posicao_unidade(self):
        self.assertTrue(projeto.eh_posicao_unidade(self.map_1, self.pos_1))
        self.assertTrue(projeto.eh_posicao_unidade(self.map_1, self.pos_2))
        self.assertTrue(projeto.eh_posicao_unidade(self.map_1, self.pos_3))
        self.assertTrue(projeto.eh_posicao_unidade(self.map_1, self.pos_4))
        self.assertTrue(projeto.eh_posicao_unidade(self.map_2, self.pos_1))
        self.assertTrue(projeto.eh_posicao_unidade(self.map_2, self.pos_2))
        self.assertTrue(projeto.eh_posicao_unidade(self.map_2, self.pos_3))
        self.assertTrue(projeto.eh_posicao_unidade(self.map_2, self.pos_4))

        self.assertFalse(projeto.eh_posicao_unidade(self.map_5, self.pos_1))
        self.assertFalse(projeto.eh_posicao_unidade(self.map_6, self.pos_1))
        self.assertFalse(projeto.eh_posicao_unidade(self.map_6, self.pos_4))

    def test_eh_posicao_corredor(self):
        self.assertTrue(projeto.eh_posicao_corredor(self.map_1, projeto.cria_posicao(3, 4)))
        self.assertTrue(projeto.eh_posicao_corredor(self.map_1, projeto.cria_posicao(1, 1)))
        self.assertTrue(projeto.eh_posicao_corredor(self.map_2, projeto.cria_posicao(1, 1)))
        self.assertTrue(projeto.eh_posicao_corredor(self.map_2, projeto.cria_posicao(3, 3)))

        self.assertFalse(projeto.eh_posicao_corredor(self.map_1, projeto.cria_posicao(3, 5)))
        self.assertFalse(projeto.eh_posicao_corredor(self.map_1, projeto.cria_posicao(3, 6)))
        self.assertFalse(projeto.eh_posicao_corredor(self.map_1, projeto.cria_posicao(3, 7)))
        self.assertFalse(projeto.eh_posicao_corredor(self.map_1, projeto.cria_posicao(4, 3)))
        self.assertFalse(projeto.eh_posicao_corredor(self.map_1, projeto.cria_posicao(5, 3)))
        self.assertFalse(projeto.eh_posicao_corredor(self.map_1, projeto.cria_posicao(6, 3)))
        self.assertFalse(projeto.eh_posicao_corredor(self.map_1, projeto.cria_posicao(0, 3)))
        self.assertFalse(projeto.eh_posicao_corredor(self.map_1, projeto.cria_posicao(3, 0)))

    def test_eh_posicao_parede(self):
        self.assertFalse(projeto.eh_posicao_parede(self.map_1, projeto.cria_posicao(3, 4)))
        self.assertFalse(projeto.eh_posicao_parede(self.map_1, projeto.cria_posicao(1, 1)))
        self.assertFalse(projeto.eh_posicao_parede(self.map_2, projeto.cria_posicao(1, 1)))
        self.assertFalse(projeto.eh_posicao_parede(self.map_2, projeto.cria_posicao(3, 3)))

        self.assertTrue(projeto.eh_posicao_parede(self.map_1, projeto.cria_posicao(3, 5)))
        self.assertTrue(projeto.eh_posicao_parede(self.map_1, projeto.cria_posicao(3, 6)))
        self.assertTrue(projeto.eh_posicao_parede(self.map_1, projeto.cria_posicao(3, 7)))
        self.assertTrue(projeto.eh_posicao_parede(self.map_1, projeto.cria_posicao(4, 3)))
        self.assertTrue(projeto.eh_posicao_parede(self.map_1, projeto.cria_posicao(5, 3)))
        self.assertTrue(projeto.eh_posicao_parede(self.map_1, projeto.cria_posicao(6, 3)))
        self.assertTrue(projeto.eh_posicao_parede(self.map_1, projeto.cria_posicao(0, 3)))
        self.assertTrue(projeto.eh_posicao_parede(self.map_1, projeto.cria_posicao(3, 0)))

    def test_mapas_iguais(self):
        self.assertTrue(projeto.mapas_iguais(self.map_1, self.map_3))
        self.assertTrue(projeto.mapas_iguais(projeto.cria_copia_mapa(self.map_2), self.map_2))
        self.assertTrue(projeto.mapas_iguais(self.map_7, self.map_8))

        self.assertFalse(projeto.mapas_iguais(self.map_1, self.map_4))
        self.assertFalse(projeto.mapas_iguais(self.map_2, self.map_1))
        self.assertFalse(projeto.mapas_iguais(self.map_1, self.map_7))
        self.assertFalse(projeto.mapas_iguais(self.map_1, self.map_8))

    def test_mapa_para_str(self):
        d = (7, 5)
        w = (projeto.cria_posicao(4,2), projeto.cria_posicao(5,2))
        e1 = tuple(projeto.cria_unidade(projeto.cria_posicao(p[0], p[1]), 20, 4, "humans")
            for p in ((3, 2),(1, 1)))
        e2 = tuple(projeto.cria_unidade(projeto.cria_posicao(p[0], p[1]), 10, 2, "cylons")
            for p in ((3, 1), (1, 3), (3, 3), (5, 3)))
        m1 = projeto.cria_mapa(d, w, e1, e2)

        self.assertTrue(projeto.mapa_para_str(m1), "#######\n#H.C..#\n#..H###\n#C.C.C#\n#######")

    def test_obter_inimigos_adjacentes(self):
        unit_1 = projeto.cria_unidade(projeto.cria_posicao(3, 3), 10, 5, "elfos")
        unit_2 = projeto.cria_unidade(projeto.cria_posicao(3, 4), 10, 5, "elfos")
        unit_3 = projeto.cria_unidade(projeto.cria_posicao(3, 2), 10, 5, "ogres")
        unit_4 = projeto.cria_unidade(projeto.cria_posicao(2, 3), 10, 5, "ogres")

        map_1 = projeto.cria_mapa((7, 7), (projeto.cria_posicao(4, 3),), (unit_1, unit_2), (unit_3, unit_4))
        self.assertEqual(
            tuple(projeto.unidade_para_str(x) for x in
            projeto.obter_inimigos_adjacentes(map_1, unit_1)),
            tuple(projeto.unidade_para_str(x) for x in
            (unit_3, unit_4)))

        self.assertEqual(
            projeto.obter_inimigos_adjacentes(map_1, unit_2), ())

        self.assertEqual(
            tuple(projeto.unidade_para_str(x) for x in
            projeto.obter_inimigos_adjacentes(map_1, unit_3)),
            tuple(projeto.unidade_para_str(x) for x in
            (unit_1,)))

        self.assertEqual(
            tuple(projeto.unidade_para_str(x) for x in
            projeto.obter_inimigos_adjacentes(map_1, unit_4)),
            tuple(projeto.unidade_para_str(x) for x in
            (unit_1,)))

    def test_calcula_pontos(self):
        self.assertEqual(projeto.calcula_pontos(self.map_1, "elfos"), 55)
        self.assertEqual(projeto.calcula_pontos(self.map_1, "ogres"), 90)
        self.assertEqual(projeto.calcula_pontos(self.map_2, "elfos"), 55)
        self.assertEqual(projeto.calcula_pontos(self.map_2, "ogres"), 90)
        self.assertEqual(projeto.calcula_pontos(self.map_3, "elfos"), 55)
        self.assertEqual(projeto.calcula_pontos(self.map_3, "ogres"), 90)
        self.assertEqual(projeto.calcula_pontos(self.map_4, "elfos"), 55)
        self.assertEqual(projeto.calcula_pontos(self.map_4, "ogres"), 90)

    def test_simula_turno(self):
        d = (7, 6)
        w = (projeto.cria_posicao(2,3), projeto.cria_posicao(4,4))
        e1 = tuple(projeto.cria_unidade(projeto.cria_posicao(p[0], p[1]),
            30, 5, "elfos")
        for p in ((4, 2), (5, 4)))
        e2 = tuple(projeto.cria_unidade(projeto.cria_posicao(p[0], p[1]),
            20, 5, "orcos")
        for p in ((2, 1), (3, 4), (5, 2), (5, 3)))
        m1 = projeto.cria_mapa(d, w, e1, e2)

        self.assertEqual((projeto.calcula_pontos(m1, "elfos"),
            projeto.calcula_pontos(m1, "orcos")), (60, 80))
        self.assertEqual(projeto.mapa_para_str(projeto.simula_turno(m1)),
            "#######\n#..O..#\n#...EO#\n#.#O.O#\n#...#E#\n#######")
        self.assertEqual((projeto.calcula_pontos(m1, "elfos"),
            projeto.calcula_pontos(m1, "orcos")), (50, 70))
        self.assertEqual(projeto.mapa_para_str(projeto.simula_turno(m1)),
            "#######\n#...O.#\n#..OEO#\n#.#..O#\n#...#E#\n#######")
        self.assertEqual((projeto.calcula_pontos(m1, "elfos"),
            projeto.calcula_pontos(m1, "orcos")), (30, 60))
        self.assertEqual(projeto.mapa_para_str(projeto.simula_turno(m1)),
            "#######\n#...O.#\n#..O.O#\n#.#..O#\n#...#E#\n#######")
        self.assertEqual((projeto.calcula_pontos(m1, "elfos"),
            projeto.calcula_pontos(m1, "orcos")), (15, 55))
        self.assertEqual(projeto.mapa_para_str(projeto.simula_turno(m1)),
            "#######\n#...O.#\n#..O.O#\n#.#...#\n#...#E#\n#######")
        self.assertEqual((projeto.calcula_pontos(m1, "elfos"),
            projeto.calcula_pontos(m1, "orcos")), (10, 50))

    def test_simula_batalha(self):
        capturedOutput = StringIO.StringIO()          # Create StringIO object
        sys.stdout = capturedOutput
        self.assertEqual(projeto.simula_batalha("./testes/config1.txt", False), "rebellion")
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "#######\n#E..R.#\n#...#.#\n#RR.#R#\n#######\n[ empire:30 rebellion:40 ]\n#######\n#....R#\n#.R.#.#\n#R..#.#\n#######\n[ empire:0 rebellion:18 ]\n")
        capturedOutput = StringIO.StringIO()          # Create StringIO object
        sys.stdout = capturedOutput
        self.assertEqual(projeto.simula_batalha("./testes/config2.txt", False), "EMPATE")
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "######\n#..G.#\n#E...#\n###G.#\n#GE#.#\n######\n[ elfos:40 goblins:60 ]\n######\n#....#\n#G...#\n###..#\n#.E#.#\n######\n[ elfos:10 goblins:4 ]\n")
        capturedOutput = StringIO.StringIO()          # Create StringIO object
        sys.stdout = capturedOutput
        self.assertEqual(projeto.simula_batalha("./testes/config3.txt", False), "globins")
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "############################\n#########E#####.......GE.###\n#########............E...G##\n######.###....#####..G....##\n#.G#....##...#######......##\n##.#....##GG#########.....##\n#....G#....E#########....###\n#...........#########.....##\n#####..G....#########...####\n#####....G..#########.#...##\n#######...G..#######G.....##\n######....E...#####.......##\n######...GG.......E......###\n#######.G...#....#..#...####\n############################\n[ elfos:120 globins:210 ]\n############################\n#########.#####..........###\n#########...G.............##\n######.###...G#####.......##\n#..#....##...#######......##\n##.#....##G.#########.....##\n#.....#.....#########....###\n#...........#########.....##\n#####.......#########...####\n#####......G#########.#...##\n#######......#######G.....##\n######........#####.......##\n######.......G...........###\n#######.....#....#..#...####\n############################\n[ elfos:0 globins:62 ]\n")
        capturedOutput = StringIO.StringIO()          # Create StringIO object
        sys.stdout = capturedOutput
        self.assertEqual(projeto.simula_batalha("./testes/config1b.txt", False), "rebellion")
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "#######\n#E..R.#\n#...#.#\n#RR.#R#\n#######\n[ empire:30 rebellion:40 ]\n#######\n#....R#\n#.R.#.#\n#R..#.#\n#######\n[ empire:0 rebellion:18 ]\n")
        capturedOutput = StringIO.StringIO()          # Create StringIO object
        sys.stdout = capturedOutput
        self.assertEqual(projeto.simula_batalha("./testes/config2b.txt", False), "EMPATE")
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "######\n#..G.#\n#E...#\n###G.#\n#GE#.#\n######\n[ elfos:40 goblins:60 ]\n######\n#....#\n#G...#\n###..#\n#.E#.#\n######\n[ elfos:10 goblins:4 ]\n")
        capturedOutput = StringIO.StringIO()          # Create StringIO object
        sys.stdout = capturedOutput
        self.assertEqual(projeto.simula_batalha("./testes/config3b.txt", False), "globins")
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "############################\n#########E#####.......GE.###\n#########............E...G##\n######.###....#####..G....##\n#.G#....##...#######......##\n##.#....##GG#########.....##\n#....G#....E#########....###\n#...........#########.....##\n#####..G....#########...####\n#####....G..#########.#...##\n#######...G..#######G.....##\n######....E...#####.......##\n######...GG.......E......###\n#######.G...#....#..#...####\n############################\n[ elfos:120 globins:210 ]\n############################\n#########.#####..........###\n#########...G.............##\n######.###...G#####.......##\n#..#....##...#######......##\n##.#....##G.#########.....##\n#.....#.....#########....###\n#...........#########.....##\n#####.......#########...####\n#####......G#########.#...##\n#######......#######G.....##\n######........#####.......##\n######.......G...........###\n#######.....#....#..#...####\n############################\n[ elfos:0 globins:62 ]\n")

        capturedOutput = StringIO.StringIO()          # Create StringIO object
        sys.stdout = capturedOutput
        self.assertEqual(projeto.simula_batalha("./testes/config1.txt", True), "rebellion")
        sys.stdout = sys.__stdout__
        with open("./testes/result1.txt") as f:
            self.assertEqual(capturedOutput.getvalue(), f.read())
        capturedOutput = StringIO.StringIO()          # Create StringIO object
        sys.stdout = capturedOutput
        self.assertEqual(projeto.simula_batalha("./testes/config1b.txt", True), "rebellion")
        sys.stdout = sys.__stdout__
        with open("./testes/result1.txt") as f:
            self.assertEqual(capturedOutput.getvalue(), f.read())

        capturedOutput = StringIO.StringIO()          # Create StringIO object
        sys.stdout = capturedOutput
        self.assertEqual(projeto.simula_batalha("./testes/config2.txt", True), "EMPATE")
        sys.stdout = sys.__stdout__
        with open("./testes/result2.txt") as f:
            self.assertEqual(capturedOutput.getvalue(), f.read())
        capturedOutput = StringIO.StringIO()          # Create StringIO object
        sys.stdout = capturedOutput
        self.assertEqual(projeto.simula_batalha("./testes/config2b.txt", True), "EMPATE")
        sys.stdout = sys.__stdout__
        with open("./testes/result2.txt") as f:
            self.assertEqual(capturedOutput.getvalue(), f.read())

        capturedOutput = StringIO.StringIO()          # Create StringIO object
        sys.stdout = capturedOutput
        self.assertEqual(projeto.simula_batalha("./testes/config3.txt", True), "globins")
        sys.stdout = sys.__stdout__
        with open("./testes/result3.txt") as f:
            self.assertEqual(capturedOutput.getvalue(), f.read())
        capturedOutput = StringIO.StringIO()          # Create StringIO object
        sys.stdout = capturedOutput
        self.assertEqual(projeto.simula_batalha("./testes/config3b.txt", True), "globins")
        sys.stdout = sys.__stdout__
        with open("./testes/result3.txt") as f:
            self.assertEqual(capturedOutput.getvalue(), f.read())





if __name__ == "__main__":
    unittest.main()

