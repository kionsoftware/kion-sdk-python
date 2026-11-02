from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Project")



@_attrs_define
class Project:
    """ Project defines a project.

        Attributes:
            archived (bool | None | Unset): True is the project is archived, false if the project is active.
            auto_pay (bool | None | Unset): True if the application can use the spend plan to process payments from the
                account. Example: True.
            default_aws_region (str | Unset): Default AWS region that the project will use for assuming into accounts.
                Example: us-east-1.
            description (str | Unset): Description for the project in the application. Example: Project being used to test
                cloud migration..
            id (int | Unset): ID of the record in the application. Example: 1.
            name (str | Unset): Name of the Project in the application. Example: Tech Project 1.
            ou_id (int | None | Unset): ID of the OU containing the project. Example: 1.
     """

    archived: bool | None | Unset = UNSET
    auto_pay: bool | None | Unset = UNSET
    default_aws_region: str | Unset = UNSET
    description: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    ou_id: int | None | Unset = UNSET
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

        id = self.id

        name = self.name

        ou_id: int | None | Unset
        if isinstance(self.ou_id, Unset):
            ou_id = UNSET
        else:
            ou_id = self.ou_id


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
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if ou_id is not UNSET:
            field_dict["ou_id"] = ou_id

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

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        def _parse_ou_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ou_id = _parse_ou_id(d.pop("ou_id", UNSET))


        project = cls(
            archived=archived,
            auto_pay=auto_pay,
            default_aws_region=default_aws_region,
            description=description,
            id=id,
            name=name,
            ou_id=ou_id,
        )


        project.additional_properties = d
        return project

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
