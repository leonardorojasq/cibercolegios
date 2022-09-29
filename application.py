import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.config import settings
from routes.coordinador.coordinador_router import *
from routes.estudiante.estudiante_router import *
from routes.profesor.profesor_router import *

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
)

app.include_router(estudiante)
app.include_router(coordinador)
app.include_router(profesor)

if __name__ == "__main__":
    uvicorn.run(app=app)
