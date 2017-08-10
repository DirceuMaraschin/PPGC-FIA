#!/usr/bin/env python
# -*- coding: utf-8 -*-

from regras import *

class Estados:
    estados = []
    pai_estados = None
    movimento = []

    def __init__(self, estados, referencia):
        self.estados = estados[:]
        self.pai_estados = referencia #referencia ao pai

    def gera_filhos(self, turno):
        filhos = []
        novas_posicoes = []
        turno_tab = 0

        #simplificar
        if(turno == 'amarelo'):
            turno_tab = 0               #estados[0] == amarelo
        elif (turno == 'vermelho'):
            turno_tab = 1               #estados[1] == vermelho

        for peca in self.estados[turno_tab]:
            novas_posicoes += self.verifica_vizinhos(turno, peca)
        novas_posicoes += self.verifica_capturas_possiveis(turno)
        #cria novos filhos
        for posicao in novas_posicoes:
            filho = Estados(self.estados, self)
            filho.aplica_movimento(posicao)

            #filho.calcula_heuristica()

            filhos.append(filho)
            filho = None

        return filhos

    #verifica possibilidade de capturas
    def valida_capturas(self, peca, vizinho):
        captura_possivel = []

        for captura in capturas[peca]:
            if(vizinho in captura):
                if((captura[2] not in self.estados[0]) and (captura[2] not in self.estados[1])):
                    captura_possivel = [[peca, captura[2], captura[1]]] # [peça, captura, destino]

            return captura_possivel

    def verifica_capturas_possiveis(self, turno):
        ver_capt = []

        if(turno == 'amarelo'):
            for peca in self.estados[0]:
                for vizinho in vizinhos[peca]:
                    if(vizinho in self.estados[1]):
                        ver_capt += (self.valida_capturas(peca,vizinho))

        elif(turno == 'vermelho'):
            for peca in self.estados[1]:
                for vizinho in vizinhos[peca]:
                    if(vizinho in self.estados[0]):
                        ver_capt += (self.valida_capturas(peca,vizinho))

        return ver_capt

    def verifica_vizinhos(self, turno, peca):
            espaco_vazio = []

            if(turno == 'amarelo'):
                for vizinho in vizinhos[peca]:
                    if((vizinho not in self.estados[0]) and (vizinho not in self.estados[1])):
                        #print [peca,vizinho,'']
                        espaco_vazio.append([peca, vizinho,''])
                    elif(vizinho in self.estados[0]):
                        pass

            elif(turno == 'vermelho'):
                for vizinho in vizinhos[peca]:
                    if((vizinho not in self.estados[0]) and (vizinho not in self.estados[1])):
                        espaco_vazio.append([peca,vizinho,''])
                    elif(vizinho in self.estados[1]):
                        pass

            return espaco_vazio

    def aplica_movimento(self, movimento):
        self.movimento = list(movimento)

        #print movimento
        #print self.movimento

        #estado em amarelos
        if(movimento[0] in self.estados[0]): #movimento possível para vermelho
            posicao_peca = self.estados[0].index(movimento[0]) #pega indice
            self.estados[0][posicao_peca] = movimento[1] #atualiza posição

            #print movimento

            if (movimento[2] != ''):
                self.estados[1].remove(movimento[2]) #remove peca

        #estado em vermelhos
        elif(movimento[0] in self.estados[1]):
            posicao_peca = self.estados[1].index(movimento[0])
            self.estados[1][posicao_peca] = movimento[1]

            if (movimento[2] != ''):
                self.estados[0].remove(movimento[2]) #remove peca
