from typing import Optional, Callable

from PySide6.QtCore import Property, Signal

import eibzpkxvd6ejecypxs4pqrez3 as ReadableAndWritableDependency


def pfoxnh2w4oo2jfypv5oyh7j68[Type](
    datatype: type[Type], default: Type | Callable[[], Type]
) -> type[ReadableAndWritableDependency._[Type]]:
    class _ReadableAndWritableDependencyWithDataType(ReadableAndWritableDependency._[Type]):
        value_changed = Signal(datatype)
        valueChanged = Signal(datatype)
        data_type = datatype

        def __init__(self, value: Optional[Type] = None):
            if value is None:
                value = default if isinstance(default, datatype) else default()
            super().__init__(value)

        value = Property(
            data_type,
            fget=ReadableAndWritableDependency._[Type].value.fget,
            fset=ReadableAndWritableDependency._[Type].value.fset,
            notify=valueChanged,
        )

    return _ReadableAndWritableDependencyWithDataType
