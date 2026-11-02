from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.custom_variable_override_data import CustomVariableOverrideData
  from ..models.custom_variable_override_inherited_data import CustomVariableOverrideInheritedData





T = TypeVar("T", bound="CustomVariableOverride")



@_attrs_define
class CustomVariableOverride:
    """ CustomVariableOverride represents a custom variable override.

        Attributes:
            custom_variable_id (int | None | Unset): CustomVariableID is the id of the custom variable. Example: 1.
            custom_variable_type (str | Unset): CustomVariableType is the type of the custom variable. Example: string.
            inherited (CustomVariableOverrideInheritedData | Unset): CustomVariableOverrideInheritedData represents the data
                inherited by a custom variable override.
            override (CustomVariableOverrideData | Unset): CustomVariableOverrideData represents the data for a custom
                variable override.
            value (Any | Unset): Value is the effective value of the custom variable override. Example: Example Value.
     """

    custom_variable_id: int | None | Unset = UNSET
    custom_variable_type: str | Unset = UNSET
    inherited: CustomVariableOverrideInheritedData | Unset = UNSET
    override: CustomVariableOverrideData | Unset = UNSET
    value: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_variable_override_data import CustomVariableOverrideData
        from ..models.custom_variable_override_inherited_data import CustomVariableOverrideInheritedData
        custom_variable_id: int | None | Unset
        if isinstance(self.custom_variable_id, Unset):
            custom_variable_id = UNSET
        else:
            custom_variable_id = self.custom_variable_id

        custom_variable_type = self.custom_variable_type

        inherited: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inherited, Unset):
            inherited = self.inherited.to_dict()

        override: dict[str, Any] | Unset = UNSET
        if not isinstance(self.override, Unset):
            override = self.override.to_dict()

        value = self.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if custom_variable_id is not UNSET:
            field_dict["custom_variable_id"] = custom_variable_id
        if custom_variable_type is not UNSET:
            field_dict["custom_variable_type"] = custom_variable_type
        if inherited is not UNSET:
            field_dict["inherited"] = inherited
        if override is not UNSET:
            field_dict["override"] = override
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_variable_override_data import CustomVariableOverrideData
        from ..models.custom_variable_override_inherited_data import CustomVariableOverrideInheritedData
        d = dict(src_dict)
        def _parse_custom_variable_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        custom_variable_id = _parse_custom_variable_id(d.pop("custom_variable_id", UNSET))


        custom_variable_type = d.pop("custom_variable_type", UNSET)

        _inherited = d.pop("inherited", UNSET)
        inherited: CustomVariableOverrideInheritedData | Unset
        if isinstance(_inherited,  Unset):
            inherited = UNSET
        else:
            inherited = CustomVariableOverrideInheritedData.from_dict(_inherited)




        _override = d.pop("override", UNSET)
        override: CustomVariableOverrideData | Unset
        if isinstance(_override,  Unset):
            override = UNSET
        else:
            override = CustomVariableOverrideData.from_dict(_override)




        value = d.pop("value", UNSET)

        custom_variable_override = cls(
            custom_variable_id=custom_variable_id,
            custom_variable_type=custom_variable_type,
            inherited=inherited,
            override=override,
            value=value,
        )


        custom_variable_override.additional_properties = d
        return custom_variable_override

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
