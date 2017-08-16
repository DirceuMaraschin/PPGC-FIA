#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

class Conexao:
    sock = None
    UDP_PORT = 0
    UDP_IP = ""

    def __init__(self,turno,ip):
        self.UDP_IP = ip

        if(turno == 'vermelho'):
            self.UDP_PORT = 5001
        elif(turno == 'amarelo'):
            self.UDP_PORT = 5002

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.enviaMensagem("conecta")

    def montaMensagem(self,mensagem):

        if(mensagem[1][1]==''):
            msg = "de "+str(mensagem[0])+" para "+str(mensagem[1])
        else:
            msg = "de "+str(mensagem[0])+" para "+str(mensagem[1])+" captura "+str(mensagem[2])

        return msg

    def enviaMensagem(self,mensagem):
        self.sock.sendto(mensagem.encode('utf-8'), (self.UDP_IP, self.UDP_PORT))

    def recebeMensagem(self):
        while True:
           data, addr = self.sock.recvfrom(1024) # buffer size is 1024 bytes

           if(data != "ok" and data != '' and data != 'conectado'):
               return (self.decodeMensagem(data))

    def decodeMensagem(self,mensagem):
        msg = mensagem.split()

        if("captura" in msg):
            return [msg[1], msg[3], msg[5]]
        else:
            return [msg[1], msg[3],'']
