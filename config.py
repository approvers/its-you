from pydantic import BaseModel

from src.domain.config import DomainConfigIF


class ItsYouConfig(DomainConfigIF, BaseModel):
    pass
