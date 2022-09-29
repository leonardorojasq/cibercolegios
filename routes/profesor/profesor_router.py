#***************************************************
from config.db import *
from fastapi import APIRouter
from fastapi.responses import JSONResponse

#*************************************************

profesor = APIRouter(
    prefix="/api/ingreso",
    tags=["Acceso Profesor con Usuario , Contraseña y Nombre de Area"]
)


@profesor.get('/profesor/{user}/{idArea}')
async def profesorado(user:str,idArea:str):

    with conection.cursor() as db:
        if user and idArea:
            sql = f"""select u.id, u.rol, u.user, a.idArea from usuarios as u
                    inner join areas as a on (u.idArea = a.id) where u.user = '{user}' """
            db.execute(sql)
            datos = db.fetchone()

            if datos != None:
                try:
                    db.execute(f"""select g.* from galeria as g
                                inner join areas as a on (g.idArea = a.idArea)
                                where g.idArea = '{idArea}' """)
                    
                    datos = db.fetchall()

                    return {'recursos': datos, 'mensaje': "Recursos listados."}
                except Exception as e:
                    return "Algo paso leo"
            else:
                return {'message':"usuario no tiene los permisos de profesor"}
        else:
            return {'mensaje': "No tiene autorizacion, Comuniquese con el area de Innovación!"}
