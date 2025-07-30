from pydantic import BaseModel

from src.common.interface import Interface


class DomainConfigInterface(BaseModel, Interface):
    pass
