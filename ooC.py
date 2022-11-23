class Lampada:

    def __init__(self, cor, preco, potencia, estado):
        self.cor = cor
        self.preco = preco
        self.potencia = potencia
        self.estado = estado


    def get_preco(self):
        return self.preco

    def set_preco(self, preco):
        self.preco = preco
        return self.preco

    def interruptor(self,estado): #estado pode ser true e false
        if estado == "acender" or "acende":
            self.estado = True
            print("a luz esta acesa")
        elif estado == "apaga" or "apagar":
            self.estado = False
            print("a luz esta apagada")
        else:
            print("houve algum erro!!!")

#############################################################################################################################
#acesso aos dados da lampada

lampada = Lampada("verde", 10, 50, None )



cliente = lampada.interruptor(input())

print(lampada.estado)

