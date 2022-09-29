#**********************************************
from config.db import *
from fastapi import APIRouter
from fastapi.responses import JSONResponse

#***********************************************

coordinador =APIRouter(
prefix="/api/ingreso",
    tags=["Acceso Coordinador con Usuario y Contraseña"]
)


@coordinador.get('/coordinador/{user}')
def rector(user):
    with conection.cursor() as db:
        if user:
            sql = "SELECT * FROM usuarios WHERE rol=3 AND user = '{0}'".format(user) 
            db.execute(sql)
            datos = db.fetchone()

            if datos != None:
                try:
                    db.execute("SELECT id, idArea, nombre, tipo_oa, aplicacion_aws, image_png_galeria FROM galeria")
                    datos = db.fetchall()

                    return {'recursos': datos, 'mensaje': "Recursos listados."}
                except Exception:
                    return "Algo paso leo"
            else:
                return {'message':"usuario no tiene los permisos de coordinador"}
        else:
            return {'mensaje': "No tiene autorizacion, Comuniquese con el area de Innovación!"}
