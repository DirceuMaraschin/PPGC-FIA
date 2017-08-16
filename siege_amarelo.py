#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from estados import Estados
from regras import *
import sys
from serv import Conexao

print '\n===========\n|| SIEGE ||\n===========\n'

class Siege():
    #vermelho = ['d1', 'd3', 'd5', 'd7', 'd9', 'd11', 'd13', 'd15']
    #['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'a11', 'a12', 'a13', 'a14', 'a15', 'a16']
    vermelho = ['g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8']
    #amarelo = ['g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8']
    #['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8']
    amarelo =  ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'd1', 'd3', 'd5', 'd7', 'd9', 'd11', 'd13', 'd15', 'h1']

    captures = []
    player = 0

    #verifica possibilidade de capturas
    def verifyCapture(self, piece, neighbor):
        captures = []

        for tuples in capturas[piece]:
            if(neighbor in tuples):
                if((tuples[2] not in self.amarelo) and (tuples not in self.vermelho)):
                    captures = [[piece, tuples[2], tuples[1]]]
                #break

            return captures

    def verifica_todas_capturas(self, turno): #verifica massacres
        todas_capt = []

        if (turno == 'amarelo'):
            for peca in self.amarelo:
                for vizinho in vizinhos[peca]:
                    if (vizinho in self.vermelho):
                        todas_capt += self.verifyCapture(peca, vizinho)

        elif (turno == 'vermelho'):
            for peca in self.vermelho:
                for vizinho in vizinhos[peca]:
                    if (vizinho in self.amarelo):
                        todas_capt += self.verifyCapture(peca, vizinho)

        self.captures = todas_capt[:]

    #verifica se ocorreu uma captura e, se for, remove a peça capturada
    def checkCapture(self, turno, movement):
        answer = False

        #teste para identificar se for uma captura
        #continuar no turno caso hajam outras
        if(movement[1] in vizinhos[movement[0]]):
            answer = False
        else:
            answer = True

            if (turno == 'vermelho'): #remove do amarelo
                index = self.amarelo.index(movement[2])
                self.amarelo.remove(movement[2]) #remove o terceiro elemento da tripla
            elif(turno == 'amarelo'): #remove do vermelho
                index = self.vermelho.index(movement[2])
                self.vermelho.remove(movement[2])

        return answer

    #realizar movimentos
    def makeMovement(self, movement):
        if(movement[0] in self.vermelho): #movimento possível para vermelho
            index = self.vermelho.index(movement[0]) #pega indice
            self.vermelho[index] = movement[1] #atualiza posição
        elif(movement[0] in self.amarelo):
            index = self.amarelo.index(movement[0])
            self.amarelo[index] = movement[1]


    def cond_vitoria(self):
        #testa se alguma peça vermelha chegou à posição 'h1', vitória vermelha
        if ('h1' in self.vermelho):
            print "VITORIA VERMELHA!"
            return True
        #caso todas as peças vermelhas tiverem sido consumidas, vitória amarela
        elif (len(self.vermelho) == 0):
            print "VITORIA AMARELA!"
            return True
        elif (len(self.amarelo) == 0):
            print "VITORIA VERMELHA!"
            return True
        else:
            return False


    def min_max(self, turno):
        plays = 1
        states = []
        newStates = []

        states.append(Estados([self.amarelo[:],self.vermelho[:]],None))

        for i in range(plays):

            for state in states:
                newStates+= state.gera_filhos(turno)

            if(turno == 'amarelo'):
                turno = 'vermelho'
            else:
                turno = 'amarelo'

            print "Minimax_estados: " + str(len(newStates))
            states = []

            for state in newStates:
                states+=state.gera_filhos(turno)
            newStates = []

            if(turno=='amarelo'):
                turno = 'vermelho'
            else:
                turno = 'amarelo'

        choiceState = states[0]
        for i in range(plays + (plays - 1)):
            choiceState = choiceState.pai_estados

            print choiceState.movimento
        return choiceState.movimento


    def GameSiege(self):
        turno = 'amarelo'
        #instancia da conexao
        conexao = Conexao(turno,'127.0.0.1')

        while (not self.cond_vitoria()):

            if(turno == 'vermelho'):
                print turno
                self.captures = []
                move = self.min_max(turno)

                #envia a mensagem
                conexao.enviaMensagem(conexao.montaMensagem(move))
                #print move
                self.makeMovement(move)
                #print self.vermelho
                #print self.amarelo
                if(self.checkCapture(turno, move) == True):
                    self.verifica_todas_capturas(turno)
                    #print len(self.captures)
                    #print self.captures
                    print "MASSACRE EM AMARELOS"

                    move = None
                    while((len(self.captures))>0):
                        move = self.captures.pop()
                        conexao.enviaMensagem(conexao.montaMensagem(move))
                        #print move
                        self.makeMovement(move)
                        self.checkCapture(turno, move)
                        self.verifica_todas_capturas(turno)
                        move = None

                move = conexao.recebeMensagem()
                self.makeMovement(move)
                self.checkCapture(turno, move)
                #sys.exit() #para finalizar forçado
                #turno = 'amarelo' #passa o turno

            elif(turno == 'amarelo'):
                print turno

                move = conexao.recebeMensagem()
                self.makeMovement(move)
                self.checkCapture(turno, move)

                self.captures = []
                move = self.min_max(turno)
                conexao.enviaMensagem(conexao.montaMensagem(move))
                #print move
                self.makeMovement(move)
                if(self.checkCapture(turno, move) == True):
                    self.verifica_todas_capturas(turno)
                    #print self.vermelho
                    #print self.amarelo
                    #print len(self.captures)
                    #print self.captures
                    print "MASSACRE EM VERMELHOS"

                    move = None
                    while((len(self.captures))>0):
                        move = self.captures.pop()
                        conexao.enviaMensagem(conexao.montaMensagem(move))

                        self.makeMovement(move)
                        self.checkCapture(turno, move)
                        self.verifica_todas_capturas(turno)
                        move = None
                    #sys.exit() #para finalizar forçado
                #turno = 'vermelho'


###########
#INICIALIZAÇÃO#
###########
siege = Siege()
siege.GameSiege()







