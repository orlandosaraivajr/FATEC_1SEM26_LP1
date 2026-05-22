# =============================================================================
# TESTES UNITÁRIOS — 100 testes (10 por exercício)
# =============================================================================
import unittest

from prova_rick_morty import contar_especies
from prova_rick_morty import filtrar_por_status
from prova_rick_morty import nomes_maiusculo
from prova_rick_morty import agrupar_por_genero
from prova_rick_morty import media_ids
from prova_rick_morty import especies_unicas
from prova_rick_morty import tuplas_personagens
from prova_rick_morty import personagem_existe
from prova_rick_morty import indexar_por_id
from prova_rick_morty import resumo_estatistico


# =============================================================================
# EXERCÍCIO 1 — contar_especies
# =============================================================================
class TestContarEspecies(unittest.TestCase):

    def test_duas_especies_contagem_correta(self):
        entrada = {"results": [
            {"name": "Rick", "species": "Human"},
            {"name": "Morty", "species": "Human"},
            {"name": "Birdperson", "species": "Bird-Person"}
        ]}
        self.assertEqual(contar_especies(entrada), {"Human": 2, "Bird-Person": 1})

    def test_especie_repetida_tres_vezes(self):
        entrada = {"results": [
            {"name": "Mr. Meeseeks", "species": "Alien"},
            {"name": "Squanchy", "species": "Cat-Person"},
            {"name": "Alien 2", "species": "Alien"},
            {"name": "Alien 3", "species": "Alien"}
        ]}
        resultado = contar_especies(entrada)
        self.assertEqual(resultado["Alien"], 3)

    def test_unico_personagem_retorna_contagem_um(self):
        entrada = {"results": [{"name": "X", "species": "Robot"}]}
        self.assertEqual(contar_especies(entrada), {"Robot": 1})

    def test_todos_mesma_especie(self):
        entrada = {"results": [
            {"name": "A", "species": "Human"},
            {"name": "B", "species": "Human"},
            {"name": "C", "species": "Human"}
        ]}
        self.assertEqual(contar_especies(entrada), {"Human": 3})

    def test_todas_especies_diferentes(self):
        entrada = {"results": [
            {"name": "A", "species": "Human"},
            {"name": "B", "species": "Alien"},
            {"name": "C", "species": "Robot"}
        ]}
        resultado = contar_especies(entrada)
        self.assertEqual(resultado["Human"], 1)
        self.assertEqual(resultado["Alien"], 1)
        self.assertEqual(resultado["Robot"], 1)

    def test_retorno_e_dicionario(self):
        entrada = {"results": [{"name": "Rick", "species": "Human"}]}
        self.assertIsInstance(contar_especies(entrada), dict)

    def test_quantidade_de_chaves_no_resultado(self):
        entrada = {"results": [
            {"name": "A", "species": "Human"},
            {"name": "B", "species": "Alien"},
            {"name": "C", "species": "Human"}
        ]}
        resultado = contar_especies(entrada)
        self.assertEqual(len(resultado), 2)

    def test_especie_com_hifen_no_nome(self):
        entrada = {"results": [
            {"name": "Birdperson", "species": "Bird-Person"},
            {"name": "Birdperson 2", "species": "Bird-Person"}
        ]}
        self.assertEqual(contar_especies(entrada), {"Bird-Person": 2})

    def test_cinco_especies_distintas(self):
        entrada = {"results": [
            {"name": "A", "species": "Human"},
            {"name": "B", "species": "Alien"},
            {"name": "C", "species": "Robot"},
            {"name": "D", "species": "Cronenberg"},
            {"name": "E", "species": "Mytholog"}
        ]}
        resultado = contar_especies(entrada)
        self.assertEqual(len(resultado), 5)
        self.assertTrue(all(v == 1 for v in resultado.values()))

    def test_valores_sao_inteiros(self):
        entrada = {"results": [
            {"name": "Rick", "species": "Human"},
            {"name": "Morty", "species": "Human"}
        ]}
        resultado = contar_especies(entrada)
        for valor in resultado.values():
            self.assertIsInstance(valor, int)


# =============================================================================
# EXERCÍCIO 2 — filtrar_por_status
# =============================================================================
class TestFiltrarPorStatus(unittest.TestCase):

    def test_filtrar_alive(self):
        entrada = {"results": [
            {"name": "Rick", "status": "Alive"},
            {"name": "Beth", "status": "Alive"},
            {"name": "Birdperson", "status": "Dead"}
        ]}
        self.assertEqual(filtrar_por_status(entrada, "Alive"), ["Rick", "Beth"])

    def test_filtrar_dead(self):
        entrada = {"results": [
            {"name": "Rick", "status": "Alive"},
            {"name": "Birdperson", "status": "Dead"},
            {"name": "Noob Noob", "status": "unknown"}
        ]}
        self.assertEqual(filtrar_por_status(entrada, "Dead"), ["Birdperson"])

    def test_filtrar_unknown(self):
        entrada = {"results": [
            {"name": "Alien X", "status": "unknown"},
            {"name": "Rick", "status": "Alive"}
        ]}
        self.assertEqual(filtrar_por_status(entrada, "unknown"), ["Alien X"])

    def test_nenhum_resultado_retorna_lista_vazia(self):
        entrada = {"results": [{"name": "Rick", "status": "Alive"}]}
        self.assertEqual(filtrar_por_status(entrada, "Dead"), [])

    def test_todos_com_mesmo_status(self):
        entrada = {"results": [
            {"name": "A", "status": "Dead"},
            {"name": "B", "status": "Dead"},
            {"name": "C", "status": "Dead"}
        ]}
        self.assertEqual(filtrar_por_status(entrada, "Dead"), ["A", "B", "C"])

    def test_retorno_e_lista(self):
        entrada = {"results": [{"name": "Rick", "status": "Alive"}]}
        self.assertIsInstance(filtrar_por_status(entrada, "Alive"), list)

    def test_ordem_dos_nomes_preservada(self):
        entrada = {"results": [
            {"name": "Morty", "status": "Alive"},
            {"name": "Rick", "status": "Alive"}
        ]}
        self.assertEqual(filtrar_por_status(entrada, "Alive"), ["Morty", "Rick"])

    def test_um_personagem_encontrado(self):
        entrada = {"results": [
            {"name": "Birdperson", "status": "Dead"},
            {"name": "Rick", "status": "Alive"}
        ]}
        resultado = filtrar_por_status(entrada, "Dead")
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0], "Birdperson")

    def test_status_case_sensitive_nao_encontra(self):
        entrada = {"results": [{"name": "Rick", "status": "Alive"}]}
        self.assertEqual(filtrar_por_status(entrada, "alive"), [])

    def test_lista_com_cinco_personagens_alive(self):
        entrada = {"results": [
            {"name": "A", "status": "Alive"},
            {"name": "B", "status": "Dead"},
            {"name": "C", "status": "Alive"},
            {"name": "D", "status": "unknown"},
            {"name": "E", "status": "Alive"}
        ]}
        resultado = filtrar_por_status(entrada, "Alive")
        self.assertEqual(resultado, ["A", "C", "E"])


# =============================================================================
# EXERCÍCIO 3 — nomes_maiusculo
# =============================================================================
class TestNomesMaiusculo(unittest.TestCase):

    def test_dois_nomes_convertidos(self):
        entrada = {"results": [{"name": "Rick Sanchez"}, {"name": "Morty Smith"}]}
        self.assertEqual(nomes_maiusculo(entrada), ["RICK SANCHEZ", "MORTY SMITH"])

    def test_tres_nomes_convertidos(self):
        entrada = {"results": [
            {"name": "Beth Smith"},
            {"name": "Jerry Smith"},
            {"name": "Summer Smith"}
        ]}
        self.assertEqual(nomes_maiusculo(entrada),
                         ["BETH SMITH", "JERRY SMITH", "SUMMER SMITH"])

    def test_nome_ja_maiusculo_permanece(self):
        entrada = {"results": [{"name": "RICK"}]}
        self.assertEqual(nomes_maiusculo(entrada), ["RICK"])

    def test_nome_todo_minusculo(self):
        entrada = {"results": [{"name": "birdperson"}]}
        self.assertEqual(nomes_maiusculo(entrada), ["BIRDPERSON"])

    def test_retorno_e_lista(self):
        entrada = {"results": [{"name": "Rick"}]}
        self.assertIsInstance(nomes_maiusculo(entrada), list)

    def test_quantidade_de_elementos_preservada(self):
        entrada = {"results": [
            {"name": "A"}, {"name": "B"}, {"name": "C"}
        ]}
        self.assertEqual(len(nomes_maiusculo(entrada)), 3)

    def test_nome_com_espaco_mantido(self):
        entrada = {"results": [{"name": "rick sanchez"}]}
        self.assertEqual(nomes_maiusculo(entrada), ["RICK SANCHEZ"])

    def test_elementos_sao_strings(self):
        entrada = {"results": [{"name": "Rick"}, {"name": "Morty"}]}
        resultado = nomes_maiusculo(entrada)
        for item in resultado:
            self.assertIsInstance(item, str)

    def test_ordem_preservada(self):
        entrada = {"results": [{"name": "Morty"}, {"name": "Rick"}]}
        resultado = nomes_maiusculo(entrada)
        self.assertEqual(resultado[0], "MORTY")
        self.assertEqual(resultado[1], "RICK")

    def test_nome_com_hifen(self):
        entrada = {"results": [{"name": "Bird-Person"}]}
        self.assertEqual(nomes_maiusculo(entrada), ["BIRD-PERSON"])


# =============================================================================
# EXERCÍCIO 4 — agrupar_por_genero
# =============================================================================
class TestAgruparPorGenero(unittest.TestCase):

    def test_dois_generos(self):
        entrada = {"results": [
            {"name": "Rick", "gender": "Male"},
            {"name": "Summer", "gender": "Female"},
            {"name": "Morty", "gender": "Male"}
        ]}
        resultado = agrupar_por_genero(entrada)
        self.assertEqual(sorted(resultado["Male"]), ["Morty", "Rick"])
        self.assertEqual(resultado["Female"], ["Summer"])

    def test_tres_generos_distintos(self):
        entrada = {"results": [
            {"name": "Beth", "gender": "Female"},
            {"name": "Alien X", "gender": "unknown"},
            {"name": "Jerry", "gender": "Male"}
        ]}
        resultado = agrupar_por_genero(entrada)
        self.assertEqual(resultado["Female"], ["Beth"])
        self.assertEqual(resultado["unknown"], ["Alien X"])
        self.assertEqual(resultado["Male"], ["Jerry"])

    def test_unico_personagem(self):
        entrada = {"results": [{"name": "Rick", "gender": "Male"}]}
        self.assertEqual(agrupar_por_genero(entrada), {"Male": ["Rick"]})

    def test_retorno_e_dicionario(self):
        entrada = {"results": [{"name": "Rick", "gender": "Male"}]}
        self.assertIsInstance(agrupar_por_genero(entrada), dict)

    def test_valores_sao_listas(self):
        entrada = {"results": [{"name": "Rick", "gender": "Male"}]}
        resultado = agrupar_por_genero(entrada)
        for valor in resultado.values():
            self.assertIsInstance(valor, list)

    def test_todos_mesmo_genero(self):
        entrada = {"results": [
            {"name": "Rick", "gender": "Male"},
            {"name": "Morty", "gender": "Male"}
        ]}
        resultado = agrupar_por_genero(entrada)
        self.assertEqual(len(resultado), 1)
        self.assertIn("Male", resultado)

    def test_quantidade_de_chaves_corretas(self):
        entrada = {"results": [
            {"name": "A", "gender": "Male"},
            {"name": "B", "gender": "Female"},
            {"name": "C", "gender": "unknown"}
        ]}
        resultado = agrupar_por_genero(entrada)
        self.assertEqual(len(resultado), 3)

    def test_nomes_na_lista_correta(self):
        entrada = {"results": [
            {"name": "Summer", "gender": "Female"},
            {"name": "Beth", "gender": "Female"}
        ]}
        resultado = agrupar_por_genero(entrada)
        self.assertIn("Summer", resultado["Female"])
        self.assertIn("Beth", resultado["Female"])

    def test_chaves_sao_strings(self):
        entrada = {"results": [{"name": "Rick", "gender": "Male"}]}
        resultado = agrupar_por_genero(entrada)
        for chave in resultado.keys():
            self.assertIsInstance(chave, str)

    def test_quatro_personagens_dois_generos(self):
        entrada = {"results": [
            {"name": "A", "gender": "Male"},
            {"name": "B", "gender": "Female"},
            {"name": "C", "gender": "Male"},
            {"name": "D", "gender": "Female"}
        ]}
        resultado = agrupar_por_genero(entrada)
        self.assertEqual(len(resultado["Male"]), 2)
        self.assertEqual(len(resultado["Female"]), 2)


# =============================================================================
# EXERCÍCIO 5 — media_ids
# =============================================================================
class TestMediaIds(unittest.TestCase):

    def test_media_tres_personagens(self):
        entrada = {"results": [
            {"id": 1, "name": "Rick"},
            {"id": 2, "name": "Morty"},
            {"id": 3, "name": "Summer"}
        ]}
        self.assertEqual(media_ids(entrada), 2.0)

    def test_media_dois_personagens(self):
        entrada = {"results": [
            {"id": 10, "name": "Beth"},
            {"id": 20, "name": "Jerry"}
        ]}
        self.assertEqual(media_ids(entrada), 15.0)

    def test_unico_personagem_media_igual_id(self):
        entrada = {"results": [{"id": 7, "name": "X"}]}
        self.assertEqual(media_ids(entrada), 7.0)

    def test_retorno_e_float(self):
        entrada = {"results": [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}]}
        self.assertIsInstance(media_ids(entrada), float)

    def test_ids_iguais_media_igual_ao_id(self):
        entrada = {"results": [
            {"id": 5, "name": "A"},
            {"id": 5, "name": "B"},
            {"id": 5, "name": "C"}
        ]}
        self.assertEqual(media_ids(entrada), 5.0)

    def test_ids_sequenciais_de_um_a_cinco(self):
        entrada = {"results": [
            {"id": 1, "name": "A"},
            {"id": 2, "name": "B"},
            {"id": 3, "name": "C"},
            {"id": 4, "name": "D"},
            {"id": 5, "name": "E"}
        ]}
        self.assertEqual(media_ids(entrada), 3.0)

    def test_ids_grandes(self):
        entrada = {"results": [
            {"id": 100, "name": "A"},
            {"id": 200, "name": "B"}
        ]}
        self.assertEqual(media_ids(entrada), 150.0)

    def test_media_nao_inteira(self):
        entrada = {"results": [
            {"id": 1, "name": "A"},
            {"id": 2, "name": "B"}
        ]}
        self.assertEqual(media_ids(entrada), 1.5)

    def test_id_zero_incluido(self):
        entrada = {"results": [
            {"id": 0, "name": "A"},
            {"id": 10, "name": "B"}
        ]}
        self.assertEqual(media_ids(entrada), 5.0)

    def test_quatro_personagens(self):
        entrada = {"results": [
            {"id": 2, "name": "A"},
            {"id": 4, "name": "B"},
            {"id": 6, "name": "C"},
            {"id": 8, "name": "D"}
        ]}
        self.assertEqual(media_ids(entrada), 5.0)


# =============================================================================
# EXERCÍCIO 6 — especies_unicas
# =============================================================================
class TestEspeciesUnicas(unittest.TestCase):

    def test_tres_especies_com_repeticao(self):
        entrada = {"results": [
            {"species": "Human"}, {"species": "Alien"},
            {"species": "Human"}, {"species": "Robot"}
        ]}
        self.assertEqual(especies_unicas(entrada), ["Alien", "Human", "Robot"])

    def test_duas_especies_com_repeticao(self):
        entrada = {"results": [
            {"species": "Cronenberg"},
            {"species": "Human"},
            {"species": "Cronenberg"}
        ]}
        self.assertEqual(especies_unicas(entrada), ["Cronenberg", "Human"])

    def test_uma_especie_repetida(self):
        entrada = {"results": [{"species": "Human"}, {"species": "Human"}]}
        self.assertEqual(especies_unicas(entrada), ["Human"])

    def test_retorno_e_lista(self):
        entrada = {"results": [{"species": "Human"}]}
        self.assertIsInstance(especies_unicas(entrada), list)

    def test_resultado_ordenado_alfabeticamente(self):
        entrada = {"results": [
            {"species": "Zebra"},
            {"species": "Alien"},
            {"species": "Human"}
        ]}
        resultado = especies_unicas(entrada)
        self.assertEqual(resultado, sorted(resultado))

    def test_sem_repeticoes_no_resultado(self):
        entrada = {"results": [
            {"species": "Human"},
            {"species": "Human"},
            {"species": "Alien"}
        ]}
        resultado = especies_unicas(entrada)
        self.assertEqual(len(resultado), len(set(resultado)))

    def test_unica_especie(self):
        entrada = {"results": [{"species": "Robot"}]}
        self.assertEqual(especies_unicas(entrada), ["Robot"])

    def test_cinco_especies_distintas_ordenadas(self):
        entrada = {"results": [
            {"species": "Zebra"},
            {"species": "Alien"},
            {"species": "Cronenberg"},
            {"species": "Human"},
            {"species": "Bot"}
        ]}
        self.assertEqual(especies_unicas(entrada),
                         ["Alien", "Bot", "Cronenberg", "Human", "Zebra"])

    def test_elementos_sao_strings(self):
        entrada = {"results": [{"species": "Human"}, {"species": "Alien"}]}
        for item in especies_unicas(entrada):
            self.assertIsInstance(item, str)

    def test_quantidade_correta_de_especies(self):
        entrada = {"results": [
            {"species": "A"}, {"species": "B"}, {"species": "A"},
            {"species": "C"}, {"species": "B"}
        ]}
        self.assertEqual(len(especies_unicas(entrada)), 3)


# =============================================================================
# EXERCÍCIO 7 — tuplas_personagens
# =============================================================================
class TestTuplasPersonagens(unittest.TestCase):

    def test_dois_personagens(self):
        entrada = {"results": [
            {"id": 1, "name": "Rick", "status": "Alive"},
            {"id": 2, "name": "Morty", "status": "Alive"}
        ]}
        self.assertEqual(tuplas_personagens(entrada),
                         [(1, "Rick", "Alive"), (2, "Morty", "Alive")])

    def test_um_personagem_dead(self):
        entrada = {"results": [{"id": 5, "name": "Birdperson", "status": "Dead"}]}
        self.assertEqual(tuplas_personagens(entrada), [(5, "Birdperson", "Dead")])

    def test_elementos_sao_tuplas(self):
        entrada = {"results": [{"id": 1, "name": "Rick", "status": "Alive"}]}
        resultado = tuplas_personagens(entrada)
        self.assertIsInstance(resultado[0], tuple)

    def test_retorno_e_lista(self):
        entrada = {"results": [{"id": 1, "name": "Rick", "status": "Alive"}]}
        self.assertIsInstance(tuplas_personagens(entrada), list)

    def test_ordem_dos_campos_id_nome_status(self):
        entrada = {"results": [{"id": 3, "name": "Summer", "status": "Alive"}]}
        resultado = tuplas_personagens(entrada)
        self.assertEqual(resultado[0][0], 3)
        self.assertEqual(resultado[0][1], "Summer")
        self.assertEqual(resultado[0][2], "Alive")

    def test_id_e_inteiro_na_tupla(self):
        entrada = {"results": [{"id": 42, "name": "X", "status": "Alive"}]}
        resultado = tuplas_personagens(entrada)
        self.assertIsInstance(resultado[0][0], int)

    def test_nome_e_string_na_tupla(self):
        entrada = {"results": [{"id": 1, "name": "Rick", "status": "Alive"}]}
        resultado = tuplas_personagens(entrada)
        self.assertIsInstance(resultado[0][1], str)

    def test_status_e_string_na_tupla(self):
        entrada = {"results": [{"id": 1, "name": "Rick", "status": "Dead"}]}
        resultado = tuplas_personagens(entrada)
        self.assertIsInstance(resultado[0][2], str)

    def test_quantidade_de_tuplas_igual_personagens(self):
        entrada = {"results": [
            {"id": 1, "name": "A", "status": "Alive"},
            {"id": 2, "name": "B", "status": "Dead"},
            {"id": 3, "name": "C", "status": "unknown"}
        ]}
        self.assertEqual(len(tuplas_personagens(entrada)), 3)

    def test_tamanho_de_cada_tupla_e_tres(self):
        entrada = {"results": [{"id": 1, "name": "Rick", "status": "Alive"}]}
        resultado = tuplas_personagens(entrada)
        self.assertEqual(len(resultado[0]), 3)


# =============================================================================
# EXERCÍCIO 8 — personagem_existe
# =============================================================================
class TestPersonagemExiste(unittest.TestCase):

    def test_nome_em_minusculo_encontrado(self):
        entrada = {"results": [{"name": "Rick Sanchez"}, {"name": "Morty Smith"}]}
        self.assertTrue(personagem_existe(entrada, "morty smith"))

    def test_nome_inexistente_retorna_false(self):
        entrada = {"results": [{"name": "Rick Sanchez"}, {"name": "Morty Smith"}]}
        self.assertFalse(personagem_existe(entrada, "Jerry Smith"))

    def test_nome_em_maiusculo_encontrado(self):
        entrada = {"results": [{"name": "Rick Sanchez"}]}
        self.assertTrue(personagem_existe(entrada, "RICK SANCHEZ"))

    def test_nome_exato_encontrado(self):
        entrada = {"results": [{"name": "Beth Smith"}]}
        self.assertTrue(personagem_existe(entrada, "Beth Smith"))

    def test_retorno_e_booleano(self):
        entrada = {"results": [{"name": "Rick"}]}
        resultado = personagem_existe(entrada, "Rick")
        self.assertIsInstance(resultado, bool)

    def test_lista_vazia_retorna_false(self):
        entrada = {"results": []}
        self.assertFalse(personagem_existe(entrada, "Rick"))

    def test_nome_parcial_nao_encontrado(self):
        entrada = {"results": [{"name": "Rick Sanchez"}]}
        self.assertFalse(personagem_existe(entrada, "Rick"))

    def test_case_misto_encontrado(self):
        entrada = {"results": [{"name": "Summer Smith"}]}
        self.assertTrue(personagem_existe(entrada, "sUmMeR sMiTh"))

    def test_multiplos_personagens_encontra_correto(self):
        entrada = {"results": [
            {"name": "Rick Sanchez"},
            {"name": "Morty Smith"},
            {"name": "Beth Smith"}
        ]}
        self.assertTrue(personagem_existe(entrada, "beth smith"))

    def test_nome_com_hifen(self):
        entrada = {"results": [{"name": "Bird-Person"}]}
        self.assertTrue(personagem_existe(entrada, "bird-person"))


# =============================================================================
# EXERCÍCIO 9 — indexar_por_id
# =============================================================================
class TestIndexarPorId(unittest.TestCase):

    def test_dois_personagens_indexados(self):
        entrada = {"results": [
            {"id": 1, "name": "Rick", "status": "Alive", "species": "Human"},
            {"id": 2, "name": "Morty", "status": "Alive", "species": "Human"}
        ]}
        esperado = {
            1: {"nome": "Rick", "status": "Alive"},
            2: {"nome": "Morty", "status": "Alive"}
        }
        self.assertEqual(indexar_por_id(entrada), esperado)

    def test_personagem_unico(self):
        entrada = {"results": [
            {"id": 5, "name": "Birdperson", "status": "Dead", "species": "Bird-Person"}
        ]}
        self.assertEqual(indexar_por_id(entrada),
                         {5: {"nome": "Birdperson", "status": "Dead"}})

    def test_chave_e_inteiro(self):
        entrada = {"results": [{"id": 42, "name": "X", "status": "Alive"}]}
        resultado = indexar_por_id(entrada)
        self.assertIn(42, resultado)

    def test_retorno_e_dicionario(self):
        entrada = {"results": [{"id": 1, "name": "Rick", "status": "Alive"}]}
        self.assertIsInstance(indexar_por_id(entrada), dict)

    def test_valor_contem_chave_nome(self):
        entrada = {"results": [{"id": 1, "name": "Rick", "status": "Alive"}]}
        resultado = indexar_por_id(entrada)
        self.assertIn("nome", resultado[1])

    def test_valor_contem_chave_status(self):
        entrada = {"results": [{"id": 1, "name": "Rick", "status": "Alive"}]}
        resultado = indexar_por_id(entrada)
        self.assertIn("status", resultado[1])

    def test_species_nao_incluido_no_valor(self):
        entrada = {"results": [
            {"id": 1, "name": "Rick", "status": "Alive", "species": "Human"}
        ]}
        resultado = indexar_por_id(entrada)
        self.assertNotIn("species", resultado[1])

    def test_nome_correto_no_valor(self):
        entrada = {"results": [{"id": 3, "name": "Summer", "status": "Alive"}]}
        self.assertEqual(indexar_por_id(entrada)[3]["nome"], "Summer")

    def test_status_correto_no_valor(self):
        entrada = {"results": [{"id": 3, "name": "Summer", "status": "Alive"}]}
        self.assertEqual(indexar_por_id(entrada)[3]["status"], "Alive")

    def test_quantidade_de_chaves_igual_personagens(self):
        entrada = {"results": [
            {"id": 1, "name": "A", "status": "Alive"},
            {"id": 2, "name": "B", "status": "Dead"},
            {"id": 3, "name": "C", "status": "unknown"}
        ]}
        self.assertEqual(len(indexar_por_id(entrada)), 3)


# =============================================================================
# EXERCÍCIO 10 — resumo_estatistico
# =============================================================================
class TestResumoEstatistico(unittest.TestCase):

    def test_exemplo_com_dois_vivos_um_morto(self):
        entrada = {"results": [
            {"status": "Alive", "species": "Human"},
            {"status": "Dead", "species": "Human"},
            {"status": "Alive", "species": "Alien"}
        ]}
        self.assertEqual(resumo_estatistico(entrada),
                         {"total": 3, "especies": 2, "vivos": 2, "mortos": 1})

    def test_exemplo_com_dois_mortos_um_unknown(self):
        entrada = {"results": [
            {"status": "Dead", "species": "Robot"},
            {"status": "Dead", "species": "Robot"},
            {"status": "unknown", "species": "Alien"}
        ]}
        self.assertEqual(resumo_estatistico(entrada),
                         {"total": 3, "especies": 2, "vivos": 0, "mortos": 2})

    def test_todos_unknown_vivos_e_mortos_zerados(self):
        entrada = {"results": [
            {"status": "unknown", "species": "X"},
            {"status": "unknown", "species": "Y"}
        ]}
        resultado = resumo_estatistico(entrada)
        self.assertEqual(resultado["vivos"], 0)
        self.assertEqual(resultado["mortos"], 0)

    def test_total_correto(self):
        entrada = {"results": [
            {"status": "Alive", "species": "Human"},
            {"status": "Dead", "species": "Alien"},
            {"status": "unknown", "species": "Robot"}
        ]}
        self.assertEqual(resumo_estatistico(entrada)["total"], 3)

    def test_especies_unicas_correto(self):
        entrada = {"results": [
            {"status": "Alive", "species": "Human"},
            {"status": "Dead", "species": "Human"},
            {"status": "Alive", "species": "Alien"}
        ]}
        self.assertEqual(resumo_estatistico(entrada)["especies"], 2)

    def test_retorno_e_dicionario(self):
        entrada = {"results": [{"status": "Alive", "species": "Human"}]}
        self.assertIsInstance(resumo_estatistico(entrada), dict)

    def test_chaves_presentes_no_resultado(self):
        entrada = {"results": [{"status": "Alive", "species": "Human"}]}
        resultado = resumo_estatistico(entrada)
        for chave in ["total", "especies", "vivos", "mortos"]:
            self.assertIn(chave, resultado)

    def test_unico_personagem_alive(self):
        entrada = {"results": [{"status": "Alive", "species": "Human"}]}
        resultado = resumo_estatistico(entrada)
        self.assertEqual(resultado["total"], 1)
        self.assertEqual(resultado["vivos"], 1)
        self.assertEqual(resultado["mortos"], 0)
        self.assertEqual(resultado["especies"], 1)

    def test_especies_repetidas_contadas_uma_vez(self):
        entrada = {"results": [
            {"status": "Alive", "species": "Human"},
            {"status": "Dead", "species": "Human"},
            {"status": "Alive", "species": "Human"}
        ]}
        self.assertEqual(resumo_estatistico(entrada)["especies"], 1)

    def test_valores_sao_inteiros(self):
        entrada = {"results": [
            {"status": "Alive", "species": "Human"},
            {"status": "Dead", "species": "Alien"}
        ]}
        resultado = resumo_estatistico(entrada)
        for valor in resultado.values():
            self.assertIsInstance(valor, int)


if __name__ == "__main__":
    unittest.main(verbosity=2)
