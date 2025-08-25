from pydantic import BaseModel

from src.inner.domain.config import DomainConfigIF


class ItsYouConfig(DomainConfigIF, BaseModel):
    pass
