from pydantic import BaseModel

from src.domain.config.interface import DomainConfigIF


class ItsYouConfig(DomainConfigIF, BaseModel):
    pass
