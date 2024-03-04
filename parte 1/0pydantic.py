from pydantic import BaseModel
class User(BaseModel):
    name: str
    email: str
    age: int
#O Pydantic irá automaticamente aplicar as regras de validação e garantir que os dados estejam corretos.
input("Aperte enter para ver o tipo de User")
print(type(User))
user_data = {
      "name": "John Doe",
      "email": "johndoe@example.com",
      "age": 25
  }
input("Aperte enter para ver o tipo de user-data")
print(type(user_data))
user_data = {
      "name": "John Doe",
      "email": "johndoe",
      "age": 25
  }
user = User(**user_data)
input("Aperte enter para ver o tipo de User")
print(type(user))


#######################################################################################

class Aviao(BaseModel):
    nome: str
    modelo: str
    ano: int

input('Aperte enter para ver o tipo de user-data')

aeronave = {

    'nome': 'TAM',
    'modelo': 'Avião',
    'ano': 2024

}

aviao = Aviao(**aeronave)
print(dict(aviao))


    

    

