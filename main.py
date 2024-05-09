from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, drop_tables
from router import router as task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_tables()
    print("База очищена")
    await create_tables()
    print("База создана")
    yield
    print("Выключение приложения")


app = FastAPI(lifespan=lifespan)
app.include_router(task_router)
