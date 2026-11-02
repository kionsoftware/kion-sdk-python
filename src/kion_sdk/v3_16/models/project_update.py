from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ProjectUpdate")



@_attrs_define
class ProjectUpdate:
    """ ProjectUpdate defines a project update.

        Attributes:
            archived (bool | None | Unset): True is the project is archived, false if the project is active.
            auto_pay (bool | None | Unset): True if the application can use the spend plan to process payments from the
                account. Example: True.
            default_aws_region (str | Unset): Default AWS region that the project will use for assuming into accounts.
                Example: us-east-1.
            description (str | Unset): Description for the project in the application. Example: Project being used to test
                cloud migration..
            name (str | Unset): Name of the Project in the application. Example: Tech Project 1.
            permission_scheme_id (int | None | Unset): ID of the permission scheme applied to the project. Example: 1.
     """

    archived: bool | None | Unset = UNSET
    auto_pay: bool | None | Unset = UNSET
    default_aws_region: str | Unset = UNSET
    description: str | Unset = UNSET
    name: str | Unset = UNSET
    permission_scheme_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        archived: bool | None | Unset
        if isinstance(self.archived, Unset):
            archived = UNSET
        else:
            archived = self.archived

        auto_pay: bool | None | Unset
        if isinstance(self.auto_pay, Unset):
            auto_pay = UNSET
        else:
            auto_pay = self.auto_pay

        default_aws_region = self.default_aws_region

        description = self.description

        name = self.name

        permission_scheme_id: int | None | Unset
        if isinstance(self.permission_scheme_id, Unset):
            permission_scheme_id = UNSET
        else:
            permission_scheme_id = self.permission_scheme_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if archived is not UNSET:
            field_dict["archived"] = archived
        if auto_pay is not UNSET:
            field_dict["auto_pay"] = auto_pay
        if default_aws_region is not UNSET:
            field_dict["default_aws_region"] = default_aws_region
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if permission_scheme_id is not UNSET:
            field_dict["permission_scheme_id"] = permission_scheme_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_archived(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        archived = _parse_archived(d.pop("archived", UNSET))


        def _parse_auto_pay(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        auto_pay = _parse_auto_pay(d.pop("auto_pay", UNSET))


        default_aws_region = d.pop("default_aws_region", UNSET)

        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        def _parse_permission_scheme_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        permission_scheme_id = _parse_permission_scheme_id(d.pop("permission_scheme_id", UNSET))


        project_update = cls(
            archived=archived,
            auto_pay=auto_pay,
            default_aws_region=default_aws_region,
            description=description,
            name=name,
            permission_scheme_id=permission_scheme_id,
        )


        project_update.additional_properties = d
        return project_update

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
