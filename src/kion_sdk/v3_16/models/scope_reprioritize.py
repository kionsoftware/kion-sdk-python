from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="ScopeReprioritize")



@_attrs_define
class ScopeReprioritize:
    """ ScopeReprioritize defines a Scope reprioritization.

        Attributes:
            scope_ids (list[int] | None): ScopeIDs is the list of scope IDs in the desired order
     """

    scope_ids: list[int] | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        scope_ids: list[int] | None
        if isinstance(self.scope_ids, list):
            scope_ids = self.scope_ids


        else:
            scope_ids = self.scope_ids


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "scope_ids": scope_ids,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_scope_ids(data: object) -> list[int] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scope_ids_type_0 = cast(list[int], data)

                return scope_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None, data)

        scope_ids = _parse_scope_ids(d.pop("scope_ids"))


        scope_reprioritize = cls(
            scope_ids=scope_ids,
        )


        scope_reprioritize.additional_properties = d
        return scope_reprioritize

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
