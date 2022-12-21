import json
import os.path
class jsoStorange:
    __nome_arquivo = 'dados.json'


    def lerJson(self):
        if not os.path.isfile(self.__nome_arquivo):
            self.criarArquivo()

        arq = open(self.__nome_arquivo, 'r', encoding='utf-8')
        data = arq.read()

        if len(data) == 0:
            return []

        data = json.loads(data)
        arq.close()

        return data


    def gravarJson(self,dados):
        arq = open(self.__nome_arquivo, 'w+', encoding='utf-8')
        data = json.dumps(dados, indent=4)
        arq.write(data)
        arq.close()


    def criarArquivo(self):
        arq = open(self.__nome_arquivo, 'w+', encoding='utf-8')
        arq.close()
