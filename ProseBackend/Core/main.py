from fastapi import FastAPI

from Routers import project_router, module_router

app = FastAPI(title="Prose Backend API")

app.include_router(project_router.router)
app.include_router(module_router.router)
