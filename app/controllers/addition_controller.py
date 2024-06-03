from datetime import datetime
from app.models.request_models import AdditionRequest
from app.models.response_models import AdditionResponse
from app.utils.multiprocessing_utils import add_lists
import logging

logger = logging.getLogger(__name__)
def handle_addition(request: AdditionRequest) -> AdditionResponse:
    logger.info("Handling addition request: %s", request)
    started_at = datetime.utcnow()
    try:
        results = add_lists(request.payload)
        status = "complete"
        logger.info("Addition request completed successfully")
    except Exception as e:
        results = []
        status = "failed"
        logger.error("Addition request failed: %s", e)
    completed_at = datetime.utcnow()
    response = AdditionResponse(
        batchid=request.batchid,
        response=results,
        status=status,
        started_at=started_at,
        completed_at=completed_at
    )
    logger.info("Response: %s", response)
    return response
    
