#!/usr/bin/env python
# -*- coding: utf-8 -*-

#vizinhos, configuração do tabuleiro
vizinhos = ({
                    'd8': ['d7', 'd9', 'c8'], \
                    'd9': ['d8', 'd10', 'c9', 'e5'], \
                    'd6': ['d5', 'd7', 'c6'], \
                    'd7': ['d6', 'd8', 'c7', 'e4'], \
                    'd4': ['d3', 'd5', 'c4'], \
                    'd5': ['d4', 'd6', 'c5', 'e3'], \
                    'd2': ['d1', 'd3', 'c2'], \
                    'd3': ['d2', 'd4', 'c3', 'e2'], \
                    'd1': ['d2', 'd16', 'c1', 'e1'], \
                    'c13': ['c12', 'b13', 'd13'], \
                    'c12': ['c13', 'b12', 'd12'], \
                    'c11': ['c10', 'b11', 'd11'], \
                    'c10': ['c11', 'b10', 'd10'], \
                    'c16': ['c1', 'b16', 'd16'], \
                    'c15': ['c14', 'b15', 'd15'], \
                    'c14': ['c15', 'b14', 'd14'], \
                    'g7': ['g6', 'g8', 'f7', 'h1'], \
                    'g6': ['g5', 'g7', 'f6', 'h1'], \
                    'g5': ['g4', 'g6', 'f5', 'h1'], \
                    'g4': ['g3', 'g5', 'f4', 'h1'], \
                    'g3': ['g2', 'g4', 'f3', 'h1'], \
                    'g2': ['g1', 'g3', 'f2', 'h1'], \
                    'g1': ['g2', 'g8', 'f1', 'h1'], \
                    'g8': ['g7', 'g1', 'f8', 'h1'], \
                    'b4': ['b3', 'a4', 'c4'], \
                    'b5': ['b6', 'a5', 'c5'], \
                    'b6': ['b5', 'a6', 'c6'], \
                    'b7': ['b8', 'a7', 'c7'], \
                    'b1': ['b2', 'a1', 'c1'], \
                    'b2': ['b1', 'a2', 'c2'], \
                    'b3': ['b4', 'a3', 'c3'], \
                    'b8': ['b7', 'a8', 'c8'], \
                    'b9': ['b10', 'a9', 'c9'], \
                    'e8': ['e7', 'f8', 'd15'], \
                    'e5': ['e6', 'f5', 'd9'], \
                    'e4': ['e3', 'f4', 'd7'], \
                    'e7': ['e8', 'f7', 'd13'], \
                    'e6': ['e5', 'f6', 'd11'], \
                    'e1': ['e2', 'f1', 'd1'], \
                    'e3': ['e4', 'f3', 'd5'], \
                    'e2': ['e1', 'f2', 'd3'], \
                    'h1': ['g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8'], \
                    'c9': ['c8', 'b9', 'd9'], \
                    'c8': ['c9', 'b8', 'd8'], \
                    'c3': ['c2', 'b3', 'd3'], \
                    'c2': ['c3', 'b2', 'd2'], \
                    'c1': ['c16', 'b1', 'd1'], \
                    'c7': ['c6', 'b7', 'd7'], \
                    'c6': ['c7', 'b6', 'd6'], \
                    'c5': ['c4', 'b5', 'd5'], \
                    'c4': ['c5', 'b4', 'd4'], \
                    'f1': ['f8', 'e1', 'g1'], \
                    'f2': ['f3', 'e2', 'g2'], \
                    'f3': ['f2', 'e3', 'g3'], \
                    'f4': ['f5', 'e4', 'g4'], \
                    'f5': ['f4', 'e5', 'g5'], \
                    'f6': ['f7', 'e6', 'g6'], \
                    'f7': ['f6', 'e7', 'g7'], \
                    'f8': ['f1', 'e8', 'g8'], \
                    'd14': ['d13', 'd15', 'c14'], \
                    'd15': ['d14', 'd16', 'c15', 'e8'], \
                    'd16': ['d15', 'd1', 'c16'], \
                    'd10': ['d9', 'd11', 'c10'], \
                    'd11': ['d10', 'd12', 'c11', 'e6'], \
                    'd12': ['d11', 'd13', 'c12'], \
                    'd13': ['d12', 'd14', 'c13', 'e7'], \
                    'b16': ['b15', 'a16', 'c16'], \
                    'b14': ['b13', 'a14', 'c14'], \
                    'b15': ['b16', 'a15', 'c15'], \
                    'b12': ['b11', 'a12', 'c12'], \
                    'b13': ['b14', 'a13', 'c13'], \
                    'b10': ['b9', 'a10', 'c10'], \
                    'b11': ['b12', 'a11', 'c11'], \
                    'a15': ['a14', 'a16', 'b15'], \
                    'a14': ['a13', 'a15', 'b14'], \
                    'a16': ['a15', 'a1', 'b16'], \
                    'a11': ['a10', 'a12', 'b11'], \
                    'a10': ['a9', 'a11', 'b10'], \
                    'a13': ['a12', 'a14', 'b13'], \
                    'a12': ['a11', 'a13', 'b12'], \
                    'a1': ['a2', 'a16', 'b1'], \
                    'a3': ['a2', 'a4', 'b3'], \
                    'a2': ['a1', 'a3', 'b2'], \
                    'a5': ['a4', 'a6', 'b5'], \
                    'a4': ['a3', 'a5', 'b4'], \
                    'a7': ['a6', 'a8', 'b7'], \
                    'a6': ['a5', 'a7', 'b6'], \
                    'a9': ['a8', 'a10', 'b9'], \
                    'a8': ['a7', 'a9', 'b8'] \
                    })

#capturas possíveis
#conf: (posição atual, peça a ser cap, nova posição)
capturas = ({
                    'd8': [('d8', 'c8', 'b8'), ('d8', 'd7', 'd6'), ('d8', 'd9', 'd10')], \
                    'd9': [('d9', 'c9', 'b9'), ('d9', 'd8', 'd7'), ('d9', 'd10', 'd11'), ('d9', 'e5', 'f5')], \
                    'd6': [('d6', 'c6', 'b6'), ('d6', 'd5', 'd4'), ('d6', 'd7', 'd8')], \
                    'd7': [('d7', 'c7', 'b7'), ('d7', 'd6', 'd5'), ('d7', 'd8', 'd9'), ('d7', 'e4', 'f4')], \
                    'd4': [('d4', 'c4', 'b4'), ('d4', 'd3', 'd2'), ('d4', 'd5', 'd6')], \
                    'd5': [('d5', 'c5', 'b5'), ('d5', 'd4', 'd3'), ('d5', 'd6', 'd7'), ('d5', 'e3', 'f3')], \
                    'd2': [('d2', 'c2', 'b2'), ('d2', 'd3', 'd4'), ('d2', 'd1', 'd16')], \
                    'd3': [('d3', 'c3', 'b3'), ('d3', 'd2', 'd1'), ('d3', 'd4', 'd5'), ('d3', 'e2', 'f2')], \
                    'd1': [('d1', 'c1', 'b1'), ('d1', 'd2', 'd3'), ('d1', 'e1', 'f1'), ('d1', 'd16', 'd15')], \
                    'c13': [('c13', 'b13', 'a13'), ('c13', 'd13', 'e7')], \
                    'c12': [('c12', 'b12', 'a12')], \
                    'c11': [('c11', 'b11', 'a11'), ('c11', 'd11', 'e6')], \
                    'c10': [('c10', 'b10', 'a10')], \
                    'c16': [('c16', 'b16', 'a16')], \
                    'c15': [('c15', 'b15', 'a15'), ('c15', 'd15', 'e8')], \
                    'c14': [('c14', 'b14', 'a14')], \
                    'g7': [('g7', 'f7', 'e7'), ('g7', 'h1', 'g3'), ('g7', 'g6', 'g5'), ('g7', 'g8', 'g1'), ('g7', 'h1', 'g3')], \
                    'g6': [('g6', 'f6', 'e6'), ('g6', 'h1', 'g2'), ('g6', 'g5', 'g4'), ('g6', 'g7', 'g8'), ('g6', 'h1', 'g2')], \
                    'g5': [('g5', 'f5', 'e5'), ('g5', 'h1', 'g1'), ('g5', 'g4', 'g3'), ('g5', 'g6', 'g7'), ('g5', 'h1', 'g1')], \
                    'g4': [('g4', 'f4', 'e4'), ('g4', 'g3', 'g2'), ('g4', 'g5', 'g6'), ('g4', 'h1', 'g8'), ('g4', 'h1', 'g8')], \
                    'g3': [('g3', 'f3', 'e3'), ('g3', 'g2', 'g1'), ('g3', 'g4', 'g5'), ('g3', 'h1', 'g7'), ('g3', 'h1', 'g7')], \
                    'g2': [('g2', 'f2', 'e2'), ('g2', 'g3', 'g4'), ('g2', 'h1', 'g6'), ('g2', 'h1', 'g6'), ('g2', 'g1', 'g8')], \
                    'g1': [('g1', 'f1', 'e1'), ('g1', 'g2', 'g3'), ('g1', 'h1', 'g5'), ('g1', 'h1', 'g5'), ('g1', 'g8', 'g7')], \
                    'g8': [('g8', 'f8', 'e8'), ('g8', 'h1', 'g4'), ('g8', 'g7', 'g6'), ('g8', 'g1', 'g2'), ('g8', 'h1', 'g4')], \
                    'b4': [('b4', 'c4', 'd4')], \
                    'b5': [('b5', 'c5', 'd5')], \
                    'b6': [('b6', 'c6', 'd6')], \
                    'b7': [('b7', 'c7', 'd7')], \
                    'b1': [('b1', 'c1', 'd1')], \
                    'b2': [('b2', 'c2', 'd2')], \
                    'b3': [('b3', 'c3', 'd3')], \
                    'b8': [('b8', 'c8', 'd8')], \
                    'b9': [('b9', 'c9', 'd9')], \
                    'e8': [('e8', 'd15', 'c15'), ('e8', 'f8', 'g8')], \
                    'e5': [('e5', 'd9', 'c9'), ('e5', 'f5', 'g5')], \
                    'e4': [('e4', 'd7', 'c7'), ('e4', 'f4', 'g4')], \
                    'e7': [('e7', 'd13', 'c13'), ('e7', 'f7', 'g7')], \
                    'e6': [('e6', 'd11', 'c11'), ('e6', 'f6', 'g6')], \
                    'e1': [('e1', 'd1', 'c1'), ('e1', 'f1', 'g1')], \
                    'e3': [('e3', 'd5', 'c5'), ('e3', 'f3', 'g3')], \
                    'e2': [('e2', 'd3', 'c3'), ('e2', 'f2', 'g2')], \
                    'h1': [('h1', 'g1', 'f1'), ('h1', 'g2', 'f2'), ('h1', 'g3', 'f3'), ('h1', 'g4', 'f4'), ('h1', 'g5', 'f5'), ('h1', 'g6', 'f6'), ('h1', 'g7', 'f7'), ('h1', 'g8', 'f8')], \
                    'c9': [('c9', 'b9', 'a9'), ('c9', 'd9', 'e5')], 'c8': [('c8', 'b8', 'a8')], \
                    'c3': [('c3', 'b3', 'a3'), ('c3', 'd3', 'e2')], \
                    'c2': [('c2', 'b2', 'a2')], \
                    'c1': [('c1', 'b1', 'a1'), ('c1', 'd1', 'e1')], \
                    'c7': [('c7', 'b7', 'a7'), ('c7', 'd7', 'e4')], \
                    'c6': [('c6', 'b6', 'a6')], \
                    'c5': [('c5', 'b5', 'a5'), ('c5', 'd5', 'e3')], \
                    'c4': [('c4', 'b4', 'a4')], \
                    'f1': [('f1', 'e1', 'd1'), ('f1', 'g1', 'h1')], \
                    'f2': [('f2', 'e2', 'd3'), ('f2', 'g2', 'h1')], \
                    'f3': [('f3', 'e3', 'd5'), ('f3', 'g3', 'h1')], \
                    'f4': [('f4', 'e4', 'd7'), ('f4', 'g4', 'h1')], \
                    'f5': [('f5', 'e5', 'd9'), ('f5', 'g5', 'h1')], \
                    'f6': [('f6', 'e6', 'd11'), ('f6', 'g6', 'h1')], \
                    'f7': [('f7', 'e7', 'd13'), ('f7', 'g7', 'h1')], \
                    'f8': [('f8', 'e8', 'd15'), ('f8', 'g8', 'h1')], \
                    'd14': [('d14', 'c14', 'b14'), ('d14', 'd13', 'd12'), ('d14', 'd15', 'd16')], \
                    'd15': [('d15', 'c15', 'b15'), ('d15', 'd14', 'd13'), ('d15', 'd16', 'd1'), ('d15', 'e8', 'f8')], \
                    'd16': [('d16', 'c16', 'b16'), ('d16', 'd15', 'd14'), ('d16', 'd1', 'd2')], \
                    'd10': [('d10', 'c10', 'b10'), ('d10', 'd9', 'd8'), ('d10', 'd11', 'd12')], \
                    'd11': [('d11', 'c11', 'b11'), ('d11', 'd10', 'd9'), ('d11', 'd12', 'd13'), ('d11', 'e6', 'f6')], \
                    'd12': [('d12', 'c12', 'b12'), ('d12', 'd11', 'd10'), ('d12', 'd13', 'd14')], \
                    'd13': [('d13', 'c13', 'b13'), ('d13', 'd12', 'd11'), ('d13', 'd14', 'd15'), ('d13', 'e7', 'f7')], \
                    'b16': [('b16', 'c16', 'd16')], \
                    'b14': [('b14', 'c14', 'd14')], \
                    'b15': [('b15', 'c15', 'd15')], \
                    'b12': [('b12', 'c12', 'd12')], \
                    'b13': [('b13', 'c13', 'd13')], \
                    'b10': [('b10', 'c10', 'd10')], \
                    'b11': [('b11', 'c11', 'd11')], \
                    'a15': [('a15', 'a14', 'a13'), ('a15', 'a16', 'a1'), ('a15', 'b15', 'c15')], \
                    'a14': [('a14', 'a13', 'a12'), ('a14', 'a15', 'a16'), ('a14', 'b14', 'c14')], \
                    'a16': [('a16', 'a15', 'a14'), ('a16', 'a1', 'a2'), ('a16', 'b16', 'c16')], \
                    'a11': [('a11', 'a10', 'a9'), ('a11', 'a12', 'a13'), ('a11', 'b11', 'c11')], \
                    'a10': [('a10', 'a9', 'a8'), ('a10', 'a11', 'a12'), ('a10', 'b10', 'c10')], \
                    'a13': [('a13', 'a12', 'a11'), ('a13', 'a14', 'a15'), ('a13', 'b13', 'c13')], \
                    'a12': [('a12', 'a11', 'a10'), ('a12', 'a13', 'a14'), ('a12', 'b12', 'c12')], \
                    'a1': [('a1', 'a2', 'a3'), ('a1', 'b1', 'c1'), ('a1', 'a16', 'a15')], \
                    'a3': [('a3', 'a2', 'a1'), ('a3', 'a4', 'a5'), ('a3', 'b3', 'c3')], \
                    'a2': [('a2', 'a3', 'a4'), ('a2', 'b2', 'c2'), ('a2', 'a1', 'a16')], \
                    'a5': [('a5', 'a4', 'a3'), ('a5', 'a6', 'a7'), ('a5', 'b5', 'c5')], \
                    'a4': [('a4', 'a3', 'a2'), ('a4', 'a5', 'a6'), ('a4', 'b4', 'c4')], \
                    'a7': [('a7', 'a6', 'a5'), ('a7', 'a8', 'a9'), ('a7', 'b7', 'c7')], \
                    'a6': [('a6', 'a5', 'a4'), ('a6', 'a7', 'a8'), ('a6', 'b6', 'c6')], \
                    'a9': [('a9', 'a8', 'a7'), ('a9', 'a10', 'a11'), ('a9', 'b9', 'c9')], \
                    'a8': [('a8', 'a7', 'a6'), ('a8', 'a9', 'a10'), ('a8', 'b8', 'c8')] \
                    })