from json_storage import jsoStorange
from aluno import Aluno

class Persistencia():
    __storange = jsoStorange() 

    def criar(self, dado: Aluno) -> Aluno:
        dados = self.__storange.lerJson()
        dado.setId(self.__gerarId())
        dados.append(dado.toDict)
        self.__storange.gravarJson(dados)


    def editar(self, dado: Aluno) -> None:
        dados = self.__storange.lerJson()
        for i, data in enumerate(dados):
            if data.getId() == dado.getId():
                dados[i] = dado.toDict
        self.__storange.gravarJson(dados)


    def excluir(self, id: int) -> None:
        dados = self.__storange.lerJson()
        for dado in dados:
            if dado.getId()== id:
                dados.remove(dado)
        self.__storange.gravarJson(dados)


    def selecionar(self, id: int) -> Aluno | None:
        dados = self.selecionar_todos()
        for dado in dados:
            if dado.getId()== id:
                return dado
        return None


    def selecionar_todos(self) -> list:
        alunos = []
        for i in self.__storange.lerJson():
            aluno = Aluno()
            aluno.setId(i['id'])
            aluno.setNome(i['nome'])
            aluno.setCpf(i['cpf'])
            aluno.setMatricula(i['matricula'])
            alunos.append(Aluno)
        return aluno


    def __gerarId(self) -> int:
        dados = self.__storange.lerJson()
        if len(dados) == 0:
            return 1
        return dados[-1].getId()+ 1
