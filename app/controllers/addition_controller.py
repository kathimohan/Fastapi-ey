from datetime import datetime
from app.models.request_models import AdditionRequest
from app.models.response_models import AdditionResponse
from app.utils.multiprocessing_utils import add_lists

def handle_addition(request: AdditionRequest) -> AdditionResponse:
    started_at = datetime.utcnow()
    try:
        results = add_lists(request.payload)
        status = "complete"
    except Exception as e:
        results = []
        status = "failed"
    completed_at = datetime.utcnow()
    return AdditionResponse(
        batchid=request.batchid,
        response=results,
        status=status,
        started_at=started_at,
        completed_at=completed_at
    )
