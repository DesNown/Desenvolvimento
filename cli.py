import computer
import sys
import cpu

params = sys.argv

if len(params) > 1:
    if params[1] == 'os' or params[1] == 'system':
        print('Sistema Operacional:',computer.os())
        print("Versão:",computer.osVersion())

    elif params[1] == 'name':
        print("Node de rede:", computer.name())

    elif params[1] == 'distro':
        print(computer.distro())

    elif params[1] == 'processor' or params[1] == '-p':
        if len(params) == 4 and params[2] == 'percentage' and int(params[3]) >=1:
            for i in range(int(params[3])):
                print("Consumindo:",cpu.percentage().user + cpu.percentage().system, "%")
                print("Livre:", cpu.percentage().idle, "%")
                print("------------------------")
        else:
            print("Processador:",computer.cpu())
            print("Velocidade:", cpu.freq(),"Gz")
            print("Nucleos:", cpu.cores())
            print("Nucleos Fisicos", cpu.pyCores())

    elif params[1] == 'arc':
        print("Arquitetura da maquina:", compuer.arc())

    else:
    
        print("Parametro Desconhecido!")
else:
    print("Sistema Operacional:", computer.os(), end="\n\n")
