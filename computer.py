#! -*- coding:utf-8 -*-

import platform

def os():
    #Retorna o SO
    return platform.uname().system

def osVersion():
    #Retorna a versão do SO
    return platform.uname().version

def name():
    #
    return platform.uname().node

def arch():
    #Retorna a arquitetura
    return platform.uname().machine

def cpu():
    #Retorna o processador
    return platform.uname().processor

def distro():
    if os() == "linux":
        return platform.linux_distribution()

    else:
        return os()