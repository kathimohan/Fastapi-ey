from fastapi import FastAPI
from app.views.addition import router as addition_router
import logging
from app.logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)
logger.info("Logging is configured.")

app = FastAPI()

app.include_router(addition_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
