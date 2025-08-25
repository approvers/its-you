from typing import TYPE_CHECKING

from injector import Injector

from src.di.domain.config.pydantic import PydanticDomainConfigModule

if TYPE_CHECKING:
    from typing import Iterable, Final

    from injector import Module

# NOTE:
#   Change here to change dependencies to load!
__MODULES: "Final[Iterable[Module]]" = (PydanticDomainConfigModule(),)

DIContainer: "Final[Injector]" = Injector(
    modules=__MODULES,
    auto_bind=False,
)
