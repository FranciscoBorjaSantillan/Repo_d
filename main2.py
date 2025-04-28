import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
import uvicorn
 
#Modelo / Schema
@strawberry.type
class Saludo:
    id: int
    nombre: str
    mensaje: str
 
BD = []

#Resolver / Funcion
@strawberry.type
class Query:
 
    @strawberry.field
    def prueba_saludo(self) -> Saludo:
        return Saludo(id=1001,nombre="TEst",mensaje="Hola Mundo")
   
    @strawberry.field
    def lista_saludos(self) -> list[Saludo]:
        return BD
    
    @strawberry.field
    def filtrado_saludo(self, id: int) -> Saludo:
        for row in BD:
            if row.id  == id:
                return row
        return None
   
   
#Mutaciones
@strawberry.type
class Mutation:
 
    @strawberry.field
    def agregar_saludo(self,idAPI: int, nombreAPI:str, mensajeAPI:str) -> Saludo:
        nuevo_registro = Saludo(id=idAPI,nombre=nombreAPI,mensaje=mensajeAPI)
        BD.append(nuevo_registro)
        return nuevo_registro
   

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)
 
#Init FastApi
app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
 
#Ejecutar servidor
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)