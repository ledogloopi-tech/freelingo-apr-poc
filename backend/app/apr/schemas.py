from pydantic import BaseModel


class AprModuleMetadata(BaseModel):
    module_id: str
    title: str
    status: str
    target_language: str
    bridge_language: str
    authorized_for_pilot: bool
    authorized_for_public_release: bool
