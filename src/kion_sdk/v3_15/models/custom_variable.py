from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.null_time import NullTime





T = TypeVar("T", bound="CustomVariable")



@_attrs_define
class CustomVariable:
    """ CustomVariable represents a custom variable.

        Attributes:
            created_at (datetime.datetime | Unset): CreatedAt is the timestamp when the custom variable was created.
                Example: 2021-01-01T00:00:00Z.
            created_by (int | Unset): CreatedBy is the ID of the user who created the custom variable Example: 1.
            default_value (Any | Unset): DefaultValue is the global default value of the custom variable. Some examples can
                be found below.

                For the string type: "Example default value"

                For the list type: ["example", "example2"]

                For the map type: {"key": "value", "key2": "value2"} Example: {"key": "value", "key2": "value2"}.
            deleted_at (None | NullTime | Unset):
            description (str | Unset): Description is the description of the custom variable. Example: Example custom
                variable description.
            id (int | Unset): ID is the unique identifier for the custom variable. Example: 1.
            key_validation_message (str | Unset): KeyValidationMessage is the message displayed when the custom variable
                key(s) do not match the regular expression. Example: Example key validation message.
            key_validation_regex (str | Unset): KeyValidationRegex is the regular expression used to validate the custom
                variable key(s) within the map custom
                variable type. Example: .*.
            name (str | Unset): Name is the name of the custom variable. Example: Example custom variable.
            owner_user_group_ids (list[int] | None | Unset): OwnerUGroupIDs is the list of user group IDs who will own the
                custom variable. Example: [1, 2].
            owner_user_ids (list[int] | None | Unset): OwnerUserIDs is the list of user IDs who will own the custom
                variable. Example: [1, 2].
            type_ (str | Unset): Type is the type of the custom variable.  The supported types are string, list, and map.
                Example: map.
            updated_at (None | NullTime | Unset):
            value_validation_message (str | Unset): ValueValidationMessage is the message displayed when the custom variable
                value(s) do not match the regular expression. Example: Example validation message.
            value_validation_regex (str | Unset): ValueValidationRegex is the regular expression used to validate the custom
                variable value(s). Example: .*.
     """

    created_at: datetime.datetime | Unset = UNSET
    created_by: int | Unset = UNSET
    default_value: Any | Unset = UNSET
    deleted_at: None | NullTime | Unset = UNSET
    description: str | Unset = UNSET
    id: int | Unset = UNSET
    key_validation_message: str | Unset = UNSET
    key_validation_regex: str | Unset = UNSET
    name: str | Unset = UNSET
    owner_user_group_ids: list[int] | None | Unset = UNSET
    owner_user_ids: list[int] | None | Unset = UNSET
    type_: str | Unset = UNSET
    updated_at: None | NullTime | Unset = UNSET
    value_validation_message: str | Unset = UNSET
    value_validation_regex: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.null_time import NullTime
        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by = self.created_by

        default_value = self.default_value

        deleted_at: dict[str, Any] | None | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        elif isinstance(self.deleted_at, NullTime):
            deleted_at = self.deleted_at.to_dict()
        else:
            deleted_at = self.deleted_at

        description = self.description

        id = self.id

        key_validation_message = self.key_validation_message

        key_validation_regex = self.key_validation_regex

        name = self.name

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

        type_ = self.type_

        updated_at: dict[str, Any] | None | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, NullTime):
            updated_at = self.updated_at.to_dict()
        else:
            updated_at = self.updated_at

        value_validation_message = self.value_validation_message

        value_validation_regex = self.value_validation_regex


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if default_value is not UNSET:
            field_dict["default_value"] = default_value
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if key_validation_message is not UNSET:
            field_dict["key_validation_message"] = key_validation_message
        if key_validation_regex is not UNSET:
            field_dict["key_validation_regex"] = key_validation_regex
        if name is not UNSET:
            field_dict["name"] = name
        if owner_user_group_ids is not UNSET:
            field_dict["owner_user_group_ids"] = owner_user_group_ids
        if owner_user_ids is not UNSET:
            field_dict["owner_user_ids"] = owner_user_ids
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if value_validation_message is not UNSET:
            field_dict["value_validation_message"] = value_validation_message
        if value_validation_regex is not UNSET:
            field_dict["value_validation_regex"] = value_validation_regex

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.null_time import NullTime
        d = dict(src_dict)
        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        created_by = d.pop("created_by", UNSET)

        default_value = d.pop("default_value", UNSET)

        def _parse_deleted_at(data: object) -> None | NullTime | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                deleted_at_type_1 = NullTime.from_dict(data)



                return deleted_at_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | NullTime | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at", UNSET))


        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        key_validation_message = d.pop("key_validation_message", UNSET)

        key_validation_regex = d.pop("key_validation_regex", UNSET)

        name = d.pop("name", UNSET)

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


        type_ = d.pop("type", UNSET)

        def _parse_updated_at(data: object) -> None | NullTime | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                updated_at_type_1 = NullTime.from_dict(data)



                return updated_at_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | NullTime | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))


        value_validation_message = d.pop("value_validation_message", UNSET)

        value_validation_regex = d.pop("value_validation_regex", UNSET)

        custom_variable = cls(
            created_at=created_at,
            created_by=created_by,
            default_value=default_value,
            deleted_at=deleted_at,
            description=description,
            id=id,
            key_validation_message=key_validation_message,
            key_validation_regex=key_validation_regex,
            name=name,
            owner_user_group_ids=owner_user_group_ids,
            owner_user_ids=owner_user_ids,
            type_=type_,
            updated_at=updated_at,
            value_validation_message=value_validation_message,
            value_validation_regex=value_validation_regex,
        )


        custom_variable.additional_properties = d
        return custom_variable

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
