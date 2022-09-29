from config.db import *
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

estudiante = APIRouter(
    prefix="/api/ingreso",
    tags=["Acceso Estudiante con Usuario, Contraseña y Grado"]
)


@estudiante.get('/estudiante/{user}')
async def recursos_estudiante(user:str , grado: int):
    with conection.cursor() as db:
        if user or grado:
            sql = f"""
                SELECT u.id, u.rol, u.user, g.idGrados
                FROM usuarios as u
                INNER JOIN grados as g on (u.idGrado = g.idGrados)
                WHERE u.user = '{user}' and g.idGrados = {grado};
            """
            db.execute(sql)
            datos = db.fetchone()

            if datos != None:
                try:
                    db.execute(
                        f"""
                        SELECT gale.id, gale.idGrado, gale.idArea, gale.nombre, gale.tipo_oa, gale.aplicacion_aws, gale.image_png_galeria 
                        FROM galeria as gale
                        INNER JOIN grados as grad on (gale.idGrado = grad.idGrados)
                        WHERE gale.idGrado = {grado};
                        """
                    )
                    datos = db.fetchall()
                    return JSONResponse(
                        content={
                            "status": status.HTTP_200_OK,
                            "recursos": datos
                        },
                        status_code=status.HTTP_200_OK
                    )
                except Exception:
                    print(str(Exception))
                    return {"message": "Error de conexion"}
            else:
                return JSONResponse(
                    content={
                        "message": "grado o nombre de usuario incorrectos",
                        "status": status.HTTP_401_UNAUTHORIZED
                    },
                    status_code=status.HTTP_401_UNAUTHORIZED
                )
        else:
            return {'mensaje': "No tiene autorizacion, Comuniquese con el area de Innovación!"}
