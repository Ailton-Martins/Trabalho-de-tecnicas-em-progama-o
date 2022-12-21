from json_storage import JsonStorage
from Alunos import Alunos


class Persistencia():
    __storage = JsonStorage()

    def criar(self, dado: Alunos) -> Alunos:
        dados = self.selecionar_todos()
        dado.setId(self.__gerarId())
        dados.append(dado)
        self.__storage.gravarJson(list(map(lambda x: x.toDict(), dados)))

    def editar(self, dado: Alunos) -> None:
        dados = self.selecionar_todos()
        for i, data in enumerate(dados):
            if data.getId() == dado.getId():
                dados[i] = dado
        self.__storage.gravarJson(list(map(lambda x: x.toDict(), dados)))

    def excluir(self, id: int) -> None:
        dados = self.selecionar_todos()
        for dado in dados:
            if dado.getId() == id:
                dados.remove(dado)
        self.__storage.gravarJson(dados)

    def selecionar(self, id: int) -> Alunos | None:
        dados = self.selecionar_todos()
        for dado in dados:
            if dado.getId() == id:
                return dado
        return None

    def selecionar_todos(self) -> list[Alunos]:
        alunos = []
        for i in self.__storage.lerJson():
            alunos = Alunos()
            alunos.setNome(i['id'])
            alunos.setCPF(i['nome'])
            alunos.setMatricula(i['preco'])
            alunos.setEndereço(i['quantidade'])
            alunos.setTelefone(i['quantidade'])
            alunos.append(alunos)
        return alunos

    def __gerarId(self) -> int:
        dados = self.selecionar_todos()
        if len(dados) == 0:
            return 1
        return dados[-1].getId() + 1
