class Alunos():
    __nome: str
    __cpf: str
    __matricula: str
    __endereco: str
    __telefone: str

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getCPF(self):
        return self.__cpf

    def setCPF(self, cpf):
        self.__cpf = cpf

    def getMatricula(self):
        return self.__matricula

    def setMatricula(self, matricula):
        self.__matricula = matricula

    def getEndereço(self):
        return self.__endereco

    def setEndereço(self, endereço):
        self.__endereco = endereço

    def getTelefone(self, telefone):
        return self.__telefone

    def setTelefone(self, telefone):
        self.__telefone = telefone

    def toDict(self):
        return {
            'Nome': self.__nome,
            'CPF': self.__cpf,
            'Matricula': self.__matricula,
            'Endereço': self.__endereco,
            'Telefone': self.__telefone
        }
