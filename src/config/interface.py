from pydantic import BaseModel

from src.domain.interface.common.interface import Interface


class ConfigIF(BaseModel, Interface):
    pass
