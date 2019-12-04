import unittest
from projeto import *


class TestesProjeto(unittest.TestCase):
    def test_posicao(self):
        with self.assertRaises(ValueError):
            p1 = cria_posicao(-1, 2)
        p1 = cria_posicao(2, 3)
        p2 = cria_posicao(7, 0)
        self.assertFalse(posicoes_iguais(p1, p2))
        self.assertEqual(posicao_para_str(p1), '(2, 3)')
        posicoes_str = tuple(posicao_para_str(p) for p in obter_posicoes_adjacentes(p2))
        self.assertEqual(posicoes_str, ('(6, 0)', '(8, 0)', '(7, 1)'))

    def test_unidade(self):
        p = cria_posicao(2, 3)
        with self.assertRaises(ValueError):
            u1 = cria_unidade(p, 30, -5, 'elfos')
        u1 = cria_unidade(p, 30, 4, 'elfos')
        self.assertEqual(unidade_para_str(u1), 'E[30, 4]@(2, 3)')
        self.assertEqual(unidade_para_char(u1), 'E')
        u2 = cria_copia_unidade(u1)
        self.assertTrue(unidades_iguais(u1, u2))
        u1 = muda_posicao(u1, cria_posicao(3, 3))
        self.assertEqual(unidade_para_str(u1), 'E[30, 4]@(3, 3)')
        self.assertEqual(unidade_para_str(u2), 'E[30, 4]@(2, 3)')
        self.assertFalse(unidades_iguais(u1, u2))
        unidades_str = tuple(unidade_para_str(u) for u in ordenar_unidades((u1, u2)))
        self.assertEqual(unidades_str, ('E[30, 4]@(2, 3)', 'E[30, 4]@(3, 3)'))
        u2 = remove_vida(u2, 25)
        self.assertFalse(unidade_ataca(u1, u2))
        self.assertEqual(unidade_para_str(u2), 'E[1, 4]@(2, 3)')
        self.assertTrue(unidade_ataca(u1, u2))

    def test_mapa(self):
        d = (7, 5)
        w = (cria_posicao(4, 2), cria_posicao(5, 2))
        e1 = tuple(cria_unidade(cria_posicao(p[0], p[1]), 20, 4, 'humans') for p in ((3, 2), (1, 1)))
        e2 = tuple(cria_unidade(cria_posicao(p[0], p[1]), 10, 2, 'cylons') for p in ((3, 1), (1, 3), (3, 3), (5, 3)))
        m1 = cria_mapa(d, w, e1, e2)
        self.assertEqual(mapa_para_str(m1), '#######\n#H.C..#\n#..H###\n#C.C.C#\n#######')
        self.assertEqual(obter_nome_exercitos(m1), ('cylons', 'humans'))
        u1 = obter_unidade(m1, cria_posicao(1, 1))
        self.assertEqual(unidade_para_str(u1), 'H[20, 4]@(1, 1)')
        temp = tuple(unidade_para_str(u) for u in obter_unidades_exercito(m1, 'humans'))
        self.assertEqual(temp, ('H[20, 4]@(1, 1)', 'H[20, 4]@(3, 2)'))
        temp = mapa_para_str(mover_unidade(m1, u1, cria_posicao(2, 1)))
        self.assertEqual(temp, '#######\n#.HC..#\n#..H###\n#C.C.C#\n#######')
        u2 = obter_unidade(m1, cria_posicao(5, 3))
        temp = mapa_para_str(eliminar_unidade(m1, u2))
        self.assertEqual(temp, '#######\n#.HC..#\n#..H###\n#C.C..#\n#######')
        u3 = obter_unidade(m1, cria_posicao(3, 2))
        temp = tuple(unidade_para_str(u) for u in obter_inimigos_adjacentes(m1, u3))
        self.assertEqual(temp, ('C[10, 2]@(3, 1)', 'C[10, 2]@(3, 3)'))
        self.assertEqual(posicao_para_str(obter_movimento(m1, u3)), '(3, 2)')
        u4 = obter_unidade(m1, cria_posicao(1, 3))
        self.assertEqual(posicao_para_str(obter_movimento(m1, u4)), '(1, 2)')


if __name__ == '__main__':
    unittest.main()
