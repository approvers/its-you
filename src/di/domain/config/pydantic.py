from injector import SingletonScope

from config import ItsYouConfig
from src.di.builder import ModuleBase, BindEntry
from src.domain.config import DomainConfigIF


class PydanticDomainConfigModule(ModuleBase):
    _BINDINGS = (
        BindEntry(
            interface=DomainConfigIF,
            to=ItsYouConfig,
            scope=SingletonScope,
        ),
    )
