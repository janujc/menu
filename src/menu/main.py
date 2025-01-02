"""This module is the entrypoint for menu"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Hello World"}
