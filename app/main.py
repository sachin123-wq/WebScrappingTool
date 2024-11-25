from fastapi import FastAPI
from app.router.routes import router


app = FastAPI()

# Include API routes
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Scraping Tool using python FastAPI!"}


