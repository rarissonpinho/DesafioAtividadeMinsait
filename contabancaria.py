 
class ContaBancaria:
        def __init__(self, titular, saldo): #metodo init
            self.titular = titular
            self.saldo = saldo

        def deposita(self, valor):
            self.saldo += valor

        def saca(self, valor):
            if(valor <= self.saldo):
                self.saldo = self.saldo - valor
                return True
            else:
                print("Saldo é insuficiente para esta operação!")
            return False
        
        def consultar_saldo(self):
            print(f"Saldo atual: R${self.saldo:.2f}")
        
minha_conta = ContaBancaria("Rarisson", 1000)

minha_conta.deposita(2000)

minha_conta.consultar_saldo()
        




       

        


        