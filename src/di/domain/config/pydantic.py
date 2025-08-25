from injector import SingletonScope

from config import ItsYouConfig
from src.di.builder import ModuleBase, BindEntry
from src.domain.config.interface import DomainConfigIF


class PydanticDomainConfigModule(ModuleBase):
    __BINDINGS = (
        BindEntry(
            interface=DomainConfigIF,
            to=ItsYouConfig,
            scope=SingletonScope,
        ),
    )
