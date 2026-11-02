from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CustomVariableOverrideInheritedData")



@_attrs_define
class CustomVariableOverrideInheritedData:
    """ CustomVariableOverrideInheritedData represents the data inherited by a custom variable override.

        Attributes:
            entity_id (int | None | Unset): EntityID is the entity id of the inherited custom variable data. Example: 1.
            entity_name (str | Unset): EntityName is the name of the entity that the custom variable is inherited from.
                Example: Example OU Name.
            entity_type (str | Unset): EntityType is the entity type of the inherited custom variable data. Example: ou.
            value (Any | Unset): Value is the value of the inherited custom variable data. Example: Example Value.
     """

    entity_id: int | None | Unset = UNSET
    entity_name: str | Unset = UNSET
    entity_type: str | Unset = UNSET
    value: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        entity_id: int | None | Unset
        if isinstance(self.entity_id, Unset):
            entity_id = UNSET
        else:
            entity_id = self.entity_id

        entity_name = self.entity_name

        entity_type = self.entity_type

        value = self.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if entity_id is not UNSET:
            field_dict["entity_id"] = entity_id
        if entity_name is not UNSET:
            field_dict["entity_name"] = entity_name
        if entity_type is not UNSET:
            field_dict["entity_type"] = entity_type
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_entity_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        entity_id = _parse_entity_id(d.pop("entity_id", UNSET))


        entity_name = d.pop("entity_name", UNSET)

        entity_type = d.pop("entity_type", UNSET)

        value = d.pop("value", UNSET)

        custom_variable_override_inherited_data = cls(
            entity_id=entity_id,
            entity_name=entity_name,
            entity_type=entity_type,
            value=value,
        )


        custom_variable_override_inherited_data.additional_properties = d
        return custom_variable_override_inherited_data

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
