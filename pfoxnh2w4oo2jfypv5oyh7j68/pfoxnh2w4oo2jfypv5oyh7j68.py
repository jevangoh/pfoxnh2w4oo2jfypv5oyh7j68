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

        def set_value(self, new_value: Type):
            if self._value != new_value:
                self._value = new_value
                self.value_changed.emit(self._value)
                self.valueChanged.emit(self._value)

        value: Type = Property(
            data_type,
            fget=ReadableAndWritableDependency._[Type].get_value,
            fset=set_value,
            notify=valueChanged,
        )

    return _ReadableAndWritableDependencyWithDataType
