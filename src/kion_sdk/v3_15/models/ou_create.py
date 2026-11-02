from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OUCreate")



@_attrs_define
class OUCreate:
    """ OUCreate defines an OU creation.

        Attributes:
            name (str): Name of the OU in the application. Example: Research and Development.
            parent_ou_id (int | None): ID of the OU containing this OU. A parent OU ID of 0 will create a top-level OU.
                Example: 1.
            permission_scheme_id (int | None): ID of the permission scheme applied to the ou. Example: 2.
            description (str | Unset): Description for the OU in the application. Example: Internal research and development
                of cloud applications..
            owner_user_group_ids (list[int] | None | Unset): List of groups IDs who will own the ou. Is required if no owner
                user IDs are listed. Example: [1, 2].
            owner_user_ids (list[int] | None | Unset): List of user IDs who will own the ou. Is required if no owner group
                IDs are listed. Example: [1, 2].
     """

    name: str
    parent_ou_id: int | None
    permission_scheme_id: int | None
    description: str | Unset = UNSET
    owner_user_group_ids: list[int] | None | Unset = UNSET
    owner_user_ids: list[int] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        parent_ou_id: int | None
        parent_ou_id = self.parent_ou_id

        permission_scheme_id: int | None
        permission_scheme_id = self.permission_scheme_id

        description = self.description

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


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "parent_ou_id": parent_ou_id,
            "permission_scheme_id": permission_scheme_id,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if owner_user_group_ids is not UNSET:
            field_dict["owner_user_group_ids"] = owner_user_group_ids
        if owner_user_ids is not UNSET:
            field_dict["owner_user_ids"] = owner_user_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_parent_ou_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        parent_ou_id = _parse_parent_ou_id(d.pop("parent_ou_id"))


        def _parse_permission_scheme_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        permission_scheme_id = _parse_permission_scheme_id(d.pop("permission_scheme_id"))


        description = d.pop("description", UNSET)

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


        ou_create = cls(
            name=name,
            parent_ou_id=parent_ou_id,
            permission_scheme_id=permission_scheme_id,
            description=description,
            owner_user_group_ids=owner_user_group_ids,
            owner_user_ids=owner_user_ids,
        )


        ou_create.additional_properties = d
        return ou_create

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
