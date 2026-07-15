from fastapi import APIRouter, Depends, HTTPException

from app.apr.schemas import AprModuleMetadata
from app.core.config import settings
from app.core.deps import get_current_user
from app.models.user import User

router = APIRouter(prefix="/api/apr", tags=["apr"])


@router.get("/modules/primeira-conexao", response_model=AprModuleMetadata)
async def get_primeira_conexao_metadata(
    _current_user: User = Depends(get_current_user),
) -> AprModuleMetadata:
    if not settings.APR_POC_ENABLED:
        raise HTTPException(status_code=404, detail="APR proof of concept is disabled")

    return AprModuleMetadata(
        module_id="APR-R1-RM-01",
        title="Primeira Conexão",
        status="technical-boundary-only",
        target_language="pt-BR",
        bridge_language="es",
        authorized_for_pilot=False,
        authorized_for_public_release=False,
    )
