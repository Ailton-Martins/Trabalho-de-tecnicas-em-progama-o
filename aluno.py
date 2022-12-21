class Aluno():
    __Id : int
    __nome:str
    __cpf:str
    __matricula:str

    def getId(self):
        return self.__Id

    def setId(self, id):
        self.__Id = id     

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getCpf(self):
        return self.__cpf

    def setCpf(self, cpf):
        self.__cpf = cpf

    def getMatricula(self):
        return self.__matricula

    def setMatricula(self, matricula):
        self.__matricula = matricula
                       
    def toDict(self):
        return {
            'id': self.__id,
            'nome': self.__nome,
            'cpf' : self.__cpf,
            'matricula': self.__matricula

        }                            