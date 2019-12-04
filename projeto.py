###########################################
# FP2019/2020 @ IST                       #
# Projeto 2 - Tecnico Battle Simulator    #
#                                         #
###########################################


def cria_posicao(x, y):
    '''
    A funcao cria_posicao recebe os valores correspondentes as coordenadas
    de uma posicao e devolve a posicao correspondente.

    cria_posicao: N x N -> posicao
    '''
    if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
        raise ValueError('cria_posicao: argumentos invalidos')
    return {'x': x, 'y': y}


def cria_copia_posicao(pos):
    '''
    A funcao cria_copia_posicao recebe uma posicao e devolve
    uma copia nova da posicao.

    cria_copia_posicao: posicao -> posicao
    '''
    return cria_posicao(obter_pos_x(pos), obter_pos_y(pos))


def obter_pos_x(pos):
    '''
    A funcao obter_pos_x devolve o valor da
    componente x da posicao dada.

    obter_pos_x: posicao -> N
    '''
    return pos['x']


def obter_pos_y(pos):
    '''
    A funcao obter_pos_y devolve o valor da
    componente y da posicao dada.

    obter_pos_y: posicao -> N
    '''
    return pos['y']


def eh_posicao(arg):
    '''
    A funcao eh_posicao devolve True caso o seu argumento
    seja um TAD posicao e False caso contrario.

    eh_posicao: universal -> booleano
    '''
    return isinstance(arg, dict) and 'x' in arg and 'y' in arg \
           and isinstance(obter_pos_x(arg), int) and obter_pos_x(arg) >= 0 \
           and isinstance(obter_pos_y(arg), int) and obter_pos_y(arg) >= 0


def posicoes_iguais(p1, p2):
    '''
    A funcao posicoes_iguais devolve True apenas se ambas
    as posicoes dadas forem iguais.

    posicoes_iguais: posicao x posicao -> booleano
    '''
    return p1 == p2


def posicao_para_str(pos):
    '''
    A funcao posicao_para_str devolve a cadeia de caracteres '(x, y)' que
    representa o seu argumento, sendo os valores x e y as coordenadas da
    posicao dada.
    
    posicao_para_str: posicao -> str
    '''
    return '({}, {})'.format(obter_pos_x(pos), obter_pos_y(pos))


def obter_posicoes_adjacentes(pos):
    '''
    A funcao obter_posicoes_adjacentes devolve um tuplo com as
    posicoes adjacentes a posicao dada de acordo com a ordem
    de leitura de um labirinto.

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
    A funcao cria unidade recebe uma posicao,
    dois valores inteiros maiores que 0 correspondentes a vida e
    forca da unidade, e uma cadeia de caracteres nao vazia
    correspondente ao exercito da unidade e devolve a unidade correspondente.

    cria_unidade: posicao x N x N x str -> unidade
    '''
    if not eh_posicao(pos) or not isinstance(v, int) or v <= 0 \
            or not isinstance(f, int) or f <= 0 or not isinstance(e, str) or len(e) == 0:
        raise ValueError('cria_unidade: argumentos invalidos')
    return {'pos': pos, 'vida': v, 'forca': f, 'exercito': e}


def cria_copia_unidade(unit):
    '''
    A funcao cria_copia_unidade recebe uma unidade
    unit e devolve uma nova copia da unidade.

    cria_copia_unidade: unidade -> unidade
    '''
    return cria_unidade(obter_posicao(unit), obter_vida(unit), obter_forca(unit), obter_exercito(unit))


def obter_posicao(unit):
    '''
    A funcao obter_posicao devolve a posicao da unidade dada.

    obter_posicao: unidade -> posicao
    '''
    return unit['pos']


def obter_exercito(unit):
    '''
    A funcao obter_exercito devolve a cadeia
    de caracteres correspondente ao exercito da unidade dada.

    obter_exercito: unidade -> str
    '''
    return unit['exercito']


def obter_forca(unit):
    '''
    A funcao obter_forca devolve o valor que
    corresponde a forca de ataque da unidade dada.

    obter_forca: unidade -> N
    '''
    return unit['forca']


def obter_vida(unit):
    '''
    A funcao obter_vida devolve o valor que
    corresponde a vida da unidade dada.

    obter_vida: unidade -> N
    '''
    return unit['vida']


def muda_posicao(unit, pos):
    '''
    A funcao muda_posicao muda destrutivamente a unidade dada
    alterando a posicao para ser igual a posicao dada.

    muda_posicao: unidade x posicao -> unidade
    '''
    unit['pos'] = pos
    return unit


def remove_vida(unit, v):
    '''
    A funcao remove_vida muda destrutivamente a unidade dada
    alterando os pontos de vida subtraindo o valor dado.

    remove_vida: unidade x N -> unidade
    '''
    unit['vida'] -= v
    return unit


def eh_unidade(arg):
    '''
    A funcao eh_unidade devolve True caso o seu argumento
    seja um TAD unidade e False caso contrario.

    eh_unidade: universal -> booleano
    '''
    return isinstance(arg, dict) and len(arg) == 4 \
           and 'pos' in arg and eh_posicao(obter_posicao(arg)) \
           and 'vida' in arg and isinstance(obter_vida(arg), int) and obter_vida(arg) > 0 \
           and 'forca' in arg and isinstance(obter_forca(arg), int) and obter_forca(arg) > 0 \
           and 'exercito' in arg and isinstance(obter_exercito(arg), str) and len(obter_exercito(arg)) != 0


def unidades_iguais(unit1, unit2):
    '''
    A funcao unidades_iguais devolve True apenas se ambas
    as unidades dadas forem iguais.

    unidades_iguais: unidade x unidade -> booleano
    '''
    return unit1 == unit2


def unidade_para_char(unit):
    '''
    A funcao unidade_para_char devolve a cadeia de
    caracteres dum unico elemento, correspondente
    ao primeiro caracter em maiuscula do exercito da unidade dada.

    unidade_para_char: unidade -> str
    '''
    return obter_exercito(unit)[0].upper()


def unidade_para_str(unit):
    '''
    A funcao unidade_para_char devolve a cadeia de caracteres, correspondente
    ao primeiro caracter em maiuscula do exercito da unidade dada.

    unidade_para_str: unidade -> str
    '''
    return '{}[{}, {}]@{}'.format(unidade_para_char(unit), obter_vida(unit),
                                  obter_forca(unit), posicao_para_str(obter_posicao(unit)))


def unidade_ataca(unit1, unit2):
    '''
    A funcao unidade_ataca modifica destrutivamente a segunda unidade
    retirando o valor de pontos de vida correspondente a forca de
    ataque da primeira unidade.

    unidade_ataca: unidade x unidade -> booleano
    '''
    forca = obter_forca(unit1)
    remove_vida(unit2, forca)
    return obter_vida(unit2) <= 0


def ordenar_unidades(conj_units):
    '''
    A funcao ordenar_unidades devolve um tuplo contendo as
    mesmas unidades do tuplo fornecido, ordenadas de acordo
    com a ordem de leitura do labirinto.

    ordenar_unidades: tuplo unidades -> tuplo unidades
    '''

    def sort_key(unit):
        pos = obter_posicao(unit)
        return obter_pos_y(pos), obter_pos_x(pos)

    return tuple(sorted(conj_units, key=sort_key))


def cria_mapa(d, w, e1, e2):
    '''
    A funcao cria_mapa recebe um tuplo de 2 valores inteiros correspondentes
    as dimensoes do mapa, um tuplo de 0 ou mais posicoes correspondentes
    as posicoes das paredes que nao se encontram nos limites exteriores do
    labirinto e dois tuplos que contem uma ou mais unidades correspondentes
    aos dois exercitos e devolve o mapa.

    cria_mapa: int x tuplo posicoes x tuplo unidades x tuplo unidades -> mapa
    '''

    def tuplo_unidades(arg):
        '''
        A funcao tuplo_unidades devolve True, se o argumento fornecido
        for um tuplo que contem apenas unidades.

        tuplo_unidades: universal -> booleano
        '''
        if not isinstance(arg, tuple) or len(arg) == 0:
            return False
        for unit in arg:
            if not eh_unidade(unit):
                return False
        return True

    if not isinstance(d, tuple) or not isinstance(w, tuple) \
            or not tuplo_unidades(e1) or not tuplo_unidades(e2) \
            or d[0] < 3 or d[1] < 3 or len(d) != 2:
        raise ValueError('cria_mapa: argumentos invalidos')

    for pos in w:
        if not eh_posicao(pos) or obter_pos_x(pos) <= 0 or obter_pos_y(pos) <= 0 \
                or obter_pos_x(pos) >= d[0] - 1 or obter_pos_y(pos) >= d[1] - 1:
            raise ValueError('cria_mapa: argumentos invalidos')

    e1_nome = obter_exercito(e1[0])
    e2_nome = obter_exercito(e2[0])
    return {'tamanho': d, 'exercitos': {e1_nome: e1, e2_nome: e2}, 'paredes': w}


def cria_copia_mapa(mapa):
    '''
    A funcao cria_copia_mapa recebe um mapa e devolve uma copia
    nova do mapa.

    cria_copia_mapa: mapa -> mapa
    '''
    nomes = obter_nome_exercitos(mapa)
    e1 = tuple(cria_copia_unidade(u) for u in obter_unidades_exercito(mapa, nomes[0]))
    e2 = tuple(cria_copia_unidade(u) for u in obter_unidades_exercito(mapa, nomes[1]))
    return cria_mapa(obter_tamanho(mapa), mapa['paredes'], e1, e2)


def obter_tamanho(mapa):
    '''
    A funcao obter_tamanho recebe um mapa e devolve um tuplo correspondente
    a dimensao do mapa.

    obter_tamanho: mapa -> tuplo inteiros
    '''
    return mapa['tamanho']


def obter_nome_exercitos(mapa):
    '''
    A funcao obter_nome_exercitos recebe um mapa e devolve um tuplo ordenado com
    duas cadeias de caracteres correspondem aos nomes dos exercitos.

    obter_nome_exercitos: mapa -> tuplo str
    '''
    return tuple(sorted(mapa['exercitos'].keys()))


def obter_unidades_exercito(mapa, exercito):
    '''
    A funcao obter_unidades_exercito recebe um mapa e uma cadeia de caracteres
    correspondente a um exercito e devolve um tuplo ordenado de acordo com a
    ordem de leitura do labirinto que contem as unidades pertencentes a esse exercito.

    obter_unidades_exercito: mapa x str -> tuplo unidades
    '''
    return ordenar_unidades(mapa['exercitos'][exercito])


def obter_todas_unidades(mapa):
    '''
    A funcao obter_todas_unidades recebe um mapa e devolve um
    tuplo ordenado de todas as unidades do mapa, ordenadas de acordo com
    a ordem de leitura do labirinto.

    obter_todas_unidades: mapa -> tuplo unidades
    '''
    unidades = ()
    for exercito in obter_nome_exercitos(mapa):
        unidades += obter_unidades_exercito(mapa, exercito)
    return ordenar_unidades(unidades)


def obter_unidade(mapa, posicao):
    '''
    A funcao obter_unidade recebe um mapa e uma posicao e devolve a unidade
    do mapa que se encontra nessa posicao.

    obter_unidade: mapa x posicao -> unidade
    '''
    for unidade in obter_todas_unidades(mapa):
        if posicoes_iguais(obter_posicao(unidade), posicao):
            return unidade
    return None


def eh_posicao_unidade(mapa, posicao):
    '''
    A funcao eh_posicao_unidade devolve True se ha uma unidade na
    posicao que e dada.

    eh_posicao_unidade: mapa x posicao -> booleano
    '''
    return obter_unidade(mapa, posicao) is not None


def eh_posicao_corredor(mapa, posicao):
    '''
    A funcao eh_posicao_corredor devolve True se na posicao dada nao
    existe nenhuma parede.

    eh_posicao_corredor: mapa x posicao -> booleano
    '''
    return not eh_posicao_parede(mapa, posicao)


def eh_posicao_parede(mapa, posicao):
    '''
    A funcao eh_posicao_parede devolve True se na posicao dada existir uma parede.

    eh_posicao_parede: mapa x posicao -> booleano
    '''
    tamanho = obter_tamanho(mapa)
    # Verificar se a posicao se encontra num limite exterior do labirinto
    if obter_pos_x(posicao) == 0 or obter_pos_y(posicao) == 0 \
            or obter_pos_x(posicao) == tamanho[0] - 1 or obter_pos_y(posicao) == tamanho[1] - 1:
        return True
    # Caso nao seja de um limite exterior, verificar se e uma parede interior
    return posicao in mapa['paredes']


def eliminar_unidade(mapa, unit):
    '''
    A funcao eliminar_unidade modifica destrutivamente o mapa, eliminando a
    unidade dada, deixando a posicao que essa ocupava livre e devolve o proprio mapa.

    eliminar_unidade: mapa x unidade -> mapa
    '''
    exercito = obter_exercito(unit)
    unidades = obter_unidades_exercito(mapa, exercito)
    for i in range(len(unidades)):
        if unidades_iguais(unit, unidades[i]):
            mapa['exercitos'][exercito] = unidades[:i] + unidades[i + 1:]
            break
    return mapa


def mover_unidade(mapa, unit, posicao):
    '''
    A funcao mover_unidade modifica destrutivamente o mapa e a
    unidade fornecidos, mudando a posicao onde a unidade se encontra e
    devolve o proprio mapa.

    mover_unidade: mapa x unidade -> mapa
    '''
    muda_posicao(unit, posicao)
    return mapa


def mapas_iguais(mapa1, mapa2):
    '''
    A funcao mapas_iguais devolve True se os dois mapas forem iguais.

    mapas_iguais: mapa x mapa -> booleano
    '''
    return obter_todas_unidades(mapa1) == obter_todas_unidades(mapa2) and \
           obter_tamanho(mapa1) == obter_tamanho(mapa2) and \
           mapa1['paredes'] == mapa2['paredes']


def mapa_para_str(mapa):
    '''
    A funcao mapa_para_str devolve uma cadeia de caracteres que representa o mapa como
    descrito no primeiro projeto, neste caso, com as unidades representadas pela sua representacao externa.

    mapa_para_str: mapa -> str
    '''
    tamanho = obter_tamanho(mapa)
    res = ''
    for y in range(tamanho[1]):
        for x in range(tamanho[0]):
            pos = cria_posicao(x, y)
            if eh_posicao_parede(mapa, pos):
                res += '#'
            elif eh_posicao_unidade(mapa, pos):
                unit = obter_unidade(mapa, pos)
                res += unidade_para_char(unit)
            else:
                res += '.'
        res += '\n'
    return res[:-1]


def obter_inimigos_adjacentes(mapa, unit):
    '''
    A funcao obter_inimigos_adjacentes devolve um tuplo contendo as unidades inimigas
    adjacentes a unidade dada de acordo com a ordem de leitura do labirinto.

    obter_inimigos_adjacentes: mapa x unidade -> tuplo unidades
    '''
    exercito = obter_exercito(unit)
    res = ()
    for pos in obter_posicoes_adjacentes(obter_posicao(unit)):
        unidade = obter_unidade(mapa, pos)
        if unidade is not None and obter_exercito(unidade) != exercito:
            res += (unidade,)
    return ordenar_unidades(res)


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


def calcula_pontos(mapa, exercito):
    '''
    A funcao calcula_pontos recebe um mapa e uma cadeia de caracteres correspondente ao nome
    de um dos exercitos do mapa e devolve a sua pontuacao. A pontuacao dum exercito
    e o total dos pontos de vida de todas as unidades do exercito.

    calcula_pontos: mapa x str -> int
    '''
    pontos = 0
    for unit in obter_unidades_exercito(mapa, exercito):
        pontos += obter_vida(unit)
    return pontos


def simula_turno(mapa):
    '''
    A funcao simula_turno modifica destrutivamente o mapa fornecido como argumento de acordo
    com a simulacao de um turno de batalha completo, e devolve o proprio mapa. Isto e,
    seguindo a ordem de leitura do labirinto, cada unidade viva realiza um
    unico movimento e pode realizar um ataque se possivel de acordo com as regras descritas.

    simula_turno: mapa -> mapa
    '''
    for unit in obter_todas_unidades(mapa):
        if obter_vida(unit) > 0:
            pos = obter_movimento(mapa, unit)
            mapa = mover_unidade(mapa, unit, pos)
            inimigos = obter_inimigos_adjacentes(mapa, unit)
            if inimigos and unidade_ataca(unit, inimigos[0]):
                eliminar_unidade(mapa, inimigos[0])
    return mapa


def simula_batalha(config, verboso):
    '''
    A funcao simula_batalha simula uma batalha completa. A batalha termina quando
    um dos exercitos vence ou se nao ocorrer nenhuma alteracao ao mapa ou as
    unidades apos um turno. Recebe uma cadeia de caracteres e um valor booleano
    e devolve o nome do exercito ganhador. A cadeia de caracteres passada por
    argumento corresponde ao ficheiro de configuracao do simulador e o booleano
    corresponde a se o simulador se encontra no modo verboso.

    simula_batalha: str x booleano -> str
    '''
    def print_info(mapa):
        print(mapa_para_str(mapa))
        e1, e2 = obter_nome_exercitos(mapa)
        pontuacao = '[ {}:{} {}:{} ]'.format(e1, calcula_pontos(mapa, e1), e2, calcula_pontos(mapa, e2))
        print(pontuacao)

    def empate(mapa):
        copia = cria_copia_mapa(mapa)
        copia = simula_turno(copia)
        return mapas_iguais(mapa, copia)

    def acabou(mapa, e1, e2):
        if calcula_pontos(mapa, e1) == 0 or calcula_pontos(mapa, e2) == 0:
            return True
        return empate(mapa)

    file = open(config, 'r')
    tamanho = eval(file.readline())
    config_e1 = eval(file.readline())
    config_e2 = eval(file.readline())
    paredes_pos = eval(file.readline())
    pos_e1 = eval(file.readline())
    pos_e2 = eval(file.readline())
    file.close()

    paredes = tuple(cria_posicao(p[0], p[1]) for p in paredes_pos)
    e1 = tuple(cria_unidade(cria_posicao(p[0], p[1]), config_e1[1], config_e1[2], config_e1[0])
               for p in pos_e1)
    e2 = tuple(cria_unidade(cria_posicao(p[0], p[1]), config_e2[1], config_e2[2], config_e2[0])
               for p in pos_e2)
    mapa = cria_mapa(tamanho, paredes, e1, e2)

    print_info()

    while not acabou(mapa, config_e1[0], config_e2[0]):
        mapa = simula_turno(mapa)
        if verboso:
            print_info()
    if not verboso:
        print_info()

    if not calcula_pontos(m1, config_e1[0]) == 0 and not calcula_pontos(m1, config_e2[0]) == 0:
        return 'EMPATE'
    return next(filter(lambda x: calcula_pontos(mapa, x) != 0, list(obter_nome_exercitos(mapa))))
