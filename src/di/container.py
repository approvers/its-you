from typing import TYPE_CHECKING

from injector import Injector

if TYPE_CHECKING:
    from typing import Iterable, Final

    from injector import Module

# NOTE:
#   Change here to change dependencies to load!
__MODULES: Final[Iterable[Module]] = set()

DIContainer: Final[Injector] = Injector(
    modules=__MODULES,
    auto_bind=False,
)
