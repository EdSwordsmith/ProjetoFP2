###########################################
# FP2019/2020 @ IST                       #
# Projeto 2 - Tecnico Battle Simulator    #
#                                         #
###########################################
# TAD mapa - Funcao de alto nivel         #
#            obter_movimento              #
###########################################


def cria_posicao(x, y):
    '''
    A funcao cria_posicao devolve uma posicao com as coordenadas dadas.

    cria_posicao: N x N -> posicao
    '''
    if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
        raise ValueError('cria_posicao: argumentos invalidos')
    return {'x': x, 'y': y}


def cria_copia_posicao(pos):
    '''
    Devolve uma copia da posicao pos

    posicao -> posicao
    '''
    return cria_posicao(obter_pos_x(pos), obter_pos_y(pos))


def obter_pos_x(pos):
    '''
    A funcao obter_pos_x devolve o valor da componente x de pos

    obter_pos_x: posicao -> N
    '''
    return pos['x']


def obter_pos_y(pos):
    '''
    A funcao obter_pos_y devolve o valor da componente y de pos

    obter_pos_y: posicao -> N
    '''
    return pos['y']


def eh_posicao(arg):
    '''
    eh_posicao: universal -> booleano
    '''
    return isinstance(arg, dict) and 'x' in arg and 'y' in arg \
        and isinstance(obter_pos_x(arg), int) and obter_pos_x(arg) >= 0 \
        and isinstance(obter_pos_y(arg), int) and obter_pos_y(arg) >= 0


def posicoes_iguais(p1, p2):
    '''
    posicoes_iguais: posicao x posicao -> booleano
    '''
    return p1 == p2


def posicao_para_str(pos):
    '''
    posicao_para_str: posicao -> str
    '''
    return '(' + str(obter_pos_x(pos)) + ', ' + str(obter_pos_y(pos)) + ')'


def obter_posicoes_adjacentes(pos):
    '''
    obter_posicoes_adjacentes: posicao -> tuplo de posicoes
    '''
    x, y = obter_pos_x(pos), obter_pos_y(pos)
    res = ()
    if y > 0:
        res += (cria_posicao(x, y - 1),)
    if x > 0:
        res += (cria_posicao(x - 1, y),)
    return res + (cria_posicao(x + 1, y), cria_posicao(x, y + 1))


def cria_unidade(pos, v, f, e):
    '''
    posicao x N x N x str -> unidade
    '''
    if not eh_posicao(pos) or not isinstance(v, int) or v <= 0 \
            or not isinstance(f, int) or f <= 0 or not isinstance(e, str) or len(e) == 0:
        raise ValueError('cria_unidade: argumentos invalidos')
    return {'pos': pos, 'vida': v, 'forca': f, 'exercito': e}


def cria_copia_unidade(unit):
    '''
    unidade -> unidade
    '''
    return cria_unidade(obter_posicao(unit), obter_vida(unit), obter_forca(unit), obter_exercito(unit))


def obter_posicao(unit):
    '''
    unidade -> posicao
    '''
    return unit['pos']


def obter_exercito(unit):
    '''
    unidade -> str
    '''
    return unit['exercito']


def obter_forca(unit):
    '''
    unidade -> N
    '''
    return unit['forca']


def obter_vida(unit):
    '''
    unidade -> N
    '''
    return unit['vida']


def muda_posicao(unit, pos):
    '''
    unidade x posicao -> unidade
    '''
    unit['pos'] = pos
    return unit


def remove_vida(unit, v):
    '''
    unidade x N -> unidade
    '''
    unit['vida'] -= v
    return unit


def eh_unidade(arg):
    '''
    universal -> booleano
    '''
    return isinstance(arg, dict) and len(arg) == 4 \
        and 'pos' in arg and eh_posicao(obter_posicao(arg)) \
        and 'vida' in arg and isinstance(obter_vida(arg), int) and obter_vida(arg) > 0 \
        and 'forca' in arg and isinstance(obter_forca(arg), int) and obter_forca(arg) > 0 \
        and 'exercito' in arg and isinstance(obter_exercito(arg), str) and len(obter_exercito(arg)) != 0


def unidades_iguais(unit1, unit2):
    '''
    unidade x unidade -> booleano
    '''
    return unit1 == unit2


def unidade_para_char(unit):
    '''
    unidade -> str
    '''
    return obter_exercito(unit)[0].upper()


def unidade_para_str(unit):
    '''
    unidade_para_str: unidade -> str
    '''
    return '{}:[{}, {}]@{}'.format(unidade_para_char(unit), obter_vida(unit),
                                   obter_forca(unit), posicao_para_str(obter_posicao(unit)))


def unidade_ataca(unit1, unit2):
    forca = obter_forca(unit1)
    remove_vida(unit2, forca)
    return obter_vida(unit2) <= 0


def obter_movimento(mapa, unit):
    '''
    A funcao obter_movimento devolve a posicao seguinte da unidade argumento
    de acordo com as regras de movimento das unidades no labirinto.

    obter_movimento: mapa x unidade -> posicao
    '''

    ######################
    # Funcoes auxiliares #
    ######################
    def pos_to_tuple(pos):
        return obter_pos_x(pos), obter_pos_y(pos)

    def tuple_to_pos(tup):
        return cria_posicao(tup[0], tup[1])

    def tira_repetidos(tup_posicoes):
        conj_tuplos = set(tuple(map(pos_to_tuple, tup_posicoes)))
        return tuple(map(tuple_to_pos, conj_tuplos))

    def obter_objetivos(source):
        enemy_side = tuple(filter(lambda u: u != obter_exercito(source), obter_nome_exercitos(mapa)))[0]
        target_units = obter_unidades_exercito(mapa, enemy_side)
        tup_com_repetidos = \
            tuple(adj
                  for other_unit in target_units
                  for adj in obter_posicoes_adjacentes(obter_posicao(other_unit))
                  if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj))
        return tira_repetidos(tup_com_repetidos)

    def backtrack(target):
        result = ()
        while target is not None:
            result = (target,) + result
            target, _ = visited[target]
        return result

    ####################
    # Funcao principal #
    ####################
    # Nao mexer se ja esta' adjacente a inimigo
    if obter_inimigos_adjacentes(mapa, unit):
        return obter_posicao(unit)

    visited = {}
    # posicao a explorar, posicao anterior e distancia
    to_explore = [(pos_to_tuple(obter_posicao(unit)), None, 0)]
    # registro do numero de passos minimo ate primeira posicao objetivo
    min_dist = None
    # estrutura que guarda todas as posicoes objetivo a igual minima distancia
    min_dist_targets = []

    targets = tuple(pos_to_tuple(obj) for obj in obter_objetivos(unit))

    while to_explore:  # enquanto nao esteja vazio
        pos, previous, dist = to_explore.pop(0)

        if pos not in visited:  # posicao foi ja explorada?
            visited[pos] = (previous, dist)  # registro no conjunto de exploracao
            if pos in targets:  # se a posicao atual eh uma dos objetivos
                # se eh primeiro objetivo  ou se esta a  distancia minima
                if min_dist is None or dist == min_dist:
                    # acrescentor 'a lista de posicoes minimas
                    min_dist = dist
                    min_dist_targets.append(pos)
            else:  # nao 'e objetivo, acrescento adjacentes
                for adj in obter_posicoes_adjacentes(tuple_to_pos(pos)):
                    if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj):
                        to_explore.append((pos_to_tuple(adj), pos, dist + 1))

        # Parar se estou a visitar posicoes mais distantes que o minimo,
        # ou se ja encontrei todos os objetivos
        if (min_dist is not None and dist > min_dist) or len(min_dist_targets) == len(targets):
            break

    # se encontrei pelo menos uma posicao objetivo, 
    # escolhe a de ordem de leitura menor e devolve o primeiro movimento
    if len(min_dist_targets) > 0:
        # primeiro dos objetivos em ordem de leitura
        tar = sorted(min_dist_targets, key=lambda x: (x[1], x[0]))[0]
        path = backtrack(tar)
        return tuple_to_pos(path[1])

    # Caso nenhuma posicao seja alcancavel
    return obter_posicao(unit)
