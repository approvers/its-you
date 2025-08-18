from pydantic import BaseModel

from src.common.interface import Interface


class ConfigIF(BaseModel, Interface):
    pass
