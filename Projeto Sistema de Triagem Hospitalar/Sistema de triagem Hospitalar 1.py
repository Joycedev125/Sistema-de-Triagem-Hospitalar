class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.head = None

    def inserirSemPrioridade(self, novo_nodo):
        if not self.head:
            self.head = novo_nodo
        else:
            current = self.head
            while current.proximo:
                current = current.proximo
            current.proximo = novo_nodo

    def inserirComPrioridade(self, novo_nodo):
        if not self.head:
            self.head = novo_nodo
        else:
            current = self.head
            previous = None
            while current and current.cor == 'A':
                previous = current
                current = current.proximo
            if not previous:
                novo_nodo.proximo = self.head
                self.head = novo_nodo
            else:
                novo_nodo.proximo = current
                previous.proximo = novo_nodo

    def inserir(self):
        cor = input("Digite a cor do cartão (A para amarelo, V para verde): ").strip().upper()
        if cor not in ['A', 'V']:
            print("Cor inválida! Use 'A' para amarelo e 'V' para verde.")
            return

        numero = int(input(f"Digite o número do cartão (iniciando em 201 para A e 1 para V): "))

        novo_nodo = Nodo(numero, cor)

        if not self.head:
            self.head = novo_nodo
        elif cor == 'V':
            self.inserirSemPrioridade(novo_nodo)
        elif cor == 'A':
            self.inserirComPrioridade(novo_nodo)

    def imprimirListaEspera(self):
        if not self.head:
            print("A lista de espera está vazia.")
        else:
            current = self.head
            while current:
                print(f"Cartão {current.cor} - Número {current.numero}")
                current = current.proximo

    def atenderPaciente(self):
        if not self.head:
            print("Não há pacientes na fila de espera.")
        else:
            paciente = self.head
            print(f"Chamando paciente com Cartão {paciente.cor} - Número {paciente.numero}")
            self.head = self.head.proximo

    def menu(self):
        while True:
            print("\nMenu do Sistema de Triagem Hospitalar:")
            print("1 - Adicionar paciente à fila")
            print("2 - Mostrar pacientes na fila")
            print("3 - Chamar paciente")
            print("4 - Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.inserir()
            elif opcao == '2':
                self.imprimirListaEspera()
            elif opcao == '3':
                self.atenderPaciente()
            elif opcao == '4':
                print("Encerrando o sistema.")
                break
            else:
                print("Opção inválida. Tente novamente.")


# Função principal para testar o sistema conforme as especificações
def main():
    sistema = ListaEncadeada()

    sistema = ListaEncadeada()

    # Chamar o método menu() para exibir o menu e interagir com o usuário
    sistema.menu()

    # Inserindo pacientes conforme especificado
    pacientes = [
        ('V', 1), ('V', 2), ('V', 3),  # Três pacientes com cartão verde
        ('A', 201), ('A', 202),  # Dois pacientes com cartão amarelo
        ('V', 4), ('V', 5),  # Dois pacientes com cartão verde
        ('A', 203), ('A', 204), ('A', 205)  # Três pacientes com cartão amarelo
    ]

    for cor, numero in pacientes:
        novo_nodo = Nodo(numero, cor)
        if cor == 'A':
            sistema.inserirComPrioridade(novo_nodo)
        else:
            sistema.inserirSemPrioridade(novo_nodo)

    # Mostrar a lista de espera após inserções
    print("\nLista de espera após inserção dos pacientes:")
    sistema.imprimirListaEspera()

    # Atendimento de dois pacientes
    print("\nAtendendo dois pacientes:")
    sistema.atenderPaciente()
    sistema.atenderPaciente()

    # Mostrar a lista de espera após atendimento
    print("\nLista de espera após atender dois pacientes:")
    sistema.imprimirListaEspera()


# Executa a função principal para testar o sistema
if __name__ == "__main__":
    main()