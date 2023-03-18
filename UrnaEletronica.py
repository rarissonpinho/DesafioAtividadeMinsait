class UrnaEletronica:
    def __init__(self):
        self.candidatos = [{"nome_candidato": "Julio", "partido": "A"},
                           {"nome_candidato": "Maria", "partido": "B"},
                           {"nome_candidato": "José", "partido": "C"},
                           {"nome_candidato": "Ana", "partido": "D"}]
    
    def exibe_candidatos(self):
        for candidato in self.candidatos:            
            print(candidato.get("nome_candidato"))
            print(candidato.get("partido"))
            
    def adicionar_novo_candidato(self, nome_candidato, partido):
        self.candidatos.append({"nome_candidato": nome_candidato, "partido": partido})

    def remover_ultimo_candidato(self):
        self.candidatos.pop()

    def atualizar_candidato(self, indice_candidato, chave, valor):
        try: 
            self.candidatos[indice_candidato][chave] = valor
        except IndexError:
            print(f"Índice de candidato inválido: {indice_candidato}")

            
urna = UrnaEletronica()

urna.exibe_candidatos()

urna.adicionar_novo_candidato("João Hernesto", "Honesto")

urna.exibe_candidatos()

print("##############")

urna.remover_ultimo_candidato()

urna.exibe_candidatos()

print("##############")

urna.atualizar_candidato(0, "nome_candidato", "Silva")
urna.atualizar_candidato(0, "partido", "Bom pra você")


urna.exibe_candidatos()




            