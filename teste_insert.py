from views import Produto, Cliente, Funcionario, Venda
import pymongo
import jsons

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dadosRelacionamento"]
mycol = mydb["dados"]

produto = Produto(1, "Danone")

x = mycol.insert_one(jsons.dump(produto))
print(x)

cliente = Cliente(1, "Joao")

x = mycol.insert_one(jsons.dump(cliente))
print(x)

funcionario = Funcionario(1, "Jose")

x = mycol.insert_one(jsons.dump(funcionario))
print(x)

venda = Venda(1,"venda legal", produto, funcionario, cliente)

x = mycol.insert_one(jsons.dump(venda))
print(x)
