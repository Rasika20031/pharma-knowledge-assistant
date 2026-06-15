from fastapi import FastAPI

from app.api.upload import router as upload_router
from app.api.chat import router as chat_router
from app.api.assistant import router as assistant_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app = FastAPI(
    title="Pharma Knowledge Assistant"
)

app.include_router(upload_router)
app.include_router(chat_router)
app.include_router(assistant_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "Pharma Knowledge Assistant Running"
    }