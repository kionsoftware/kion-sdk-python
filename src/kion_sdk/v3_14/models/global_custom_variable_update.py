from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GlobalCustomVariableUpdate")



@_attrs_define
class GlobalCustomVariableUpdate:
    """ GlobalCustomVariableUpdate represents the fields necessary to update a custom variable.

        Attributes:
            default_value (Any | Unset): DefaultValue is the global default value of the custom variable. Some examples can
                be found below.

                For the string type: "Example default value"

                For the list type: ["example", "example2"]

                For the map type: {"key": "value", "key2": "value2"} Example: {"key": "value", "key2": "value2"}.
            description (str | Unset): Description is the description of the custom variable. The description can be up to
                1024 characters. Example: Example custom variable description.
            key_validation_message (str | Unset): KeyValidationMessage is the message displayed when the custom variable
                key(s) do not match the regular expression.
                The key validation message can be up to 255 characters. Example: Example key validation message.
            key_validation_regex (str | Unset): KeyValidationRegex is the regular expression used to validate the custom
                variable key(s) within the map custom
                variable type. The key validation regex can be up to 255 characters. Example: .*.
            owner_user_group_ids (list[int] | None | Unset): OwnerUGroupIDs is the list of user group IDs who will own the
                custom variable. Example: [1, 2].
            owner_user_ids (list[int] | None | Unset): OwnerUserIDs is the list of user IDs who will own the custom
                variable. Example: [1, 2].
            value_validation_message (str | Unset): ValueValidationMessage is the message displayed when the custom variable
                value(s) do not match the regular expression.
                The validation message can be up to 255 characters. Example: Example validation message.
            value_validation_regex (str | Unset): ValueValidationRegex is the regular expression used to validate the custom
                variable value(s).
                The validation regex can be up to 255 characters. Example: .*.
     """

    default_value: Any | Unset = UNSET
    description: str | Unset = UNSET
    key_validation_message: str | Unset = UNSET
    key_validation_regex: str | Unset = UNSET
    owner_user_group_ids: list[int] | None | Unset = UNSET
    owner_user_ids: list[int] | None | Unset = UNSET
    value_validation_message: str | Unset = UNSET
    value_validation_regex: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        default_value = self.default_value

        description = self.description

        key_validation_message = self.key_validation_message

        key_validation_regex = self.key_validation_regex

        owner_user_group_ids: list[int] | None | Unset
        if isinstance(self.owner_user_group_ids, Unset):
            owner_user_group_ids = UNSET
        elif isinstance(self.owner_user_group_ids, list):
            owner_user_group_ids = self.owner_user_group_ids


        else:
            owner_user_group_ids = self.owner_user_group_ids

        owner_user_ids: list[int] | None | Unset
        if isinstance(self.owner_user_ids, Unset):
            owner_user_ids = UNSET
        elif isinstance(self.owner_user_ids, list):
            owner_user_ids = self.owner_user_ids


        else:
            owner_user_ids = self.owner_user_ids

        value_validation_message = self.value_validation_message

        value_validation_regex = self.value_validation_regex


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if default_value is not UNSET:
            field_dict["default_value"] = default_value
        if description is not UNSET:
            field_dict["description"] = description
        if key_validation_message is not UNSET:
            field_dict["key_validation_message"] = key_validation_message
        if key_validation_regex is not UNSET:
            field_dict["key_validation_regex"] = key_validation_regex
        if owner_user_group_ids is not UNSET:
            field_dict["owner_user_group_ids"] = owner_user_group_ids
        if owner_user_ids is not UNSET:
            field_dict["owner_user_ids"] = owner_user_ids
        if value_validation_message is not UNSET:
            field_dict["value_validation_message"] = value_validation_message
        if value_validation_regex is not UNSET:
            field_dict["value_validation_regex"] = value_validation_regex

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        default_value = d.pop("default_value", UNSET)

        description = d.pop("description", UNSET)

        key_validation_message = d.pop("key_validation_message", UNSET)

        key_validation_regex = d.pop("key_validation_regex", UNSET)

        def _parse_owner_user_group_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_user_group_ids_type_0 = cast(list[int], data)

                return owner_user_group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        owner_user_group_ids = _parse_owner_user_group_ids(d.pop("owner_user_group_ids", UNSET))


        def _parse_owner_user_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_user_ids_type_0 = cast(list[int], data)

                return owner_user_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        owner_user_ids = _parse_owner_user_ids(d.pop("owner_user_ids", UNSET))


        value_validation_message = d.pop("value_validation_message", UNSET)

        value_validation_regex = d.pop("value_validation_regex", UNSET)

        global_custom_variable_update = cls(
            default_value=default_value,
            description=description,
            key_validation_message=key_validation_message,
            key_validation_regex=key_validation_regex,
            owner_user_group_ids=owner_user_group_ids,
            owner_user_ids=owner_user_ids,
            value_validation_message=value_validation_message,
            value_validation_regex=value_validation_regex,
        )


        global_custom_variable_update.additional_properties = d
        return global_custom_variable_update

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
