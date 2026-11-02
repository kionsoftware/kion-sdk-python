from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.ou import OU





T = TypeVar("T", bound="ProjectWithOU")



@_attrs_define
class ProjectWithOU:
    """ ProjectWithOU defines a project with OU.

        Attributes:
            archived (bool | None | Unset): True is the project is archived, false if the project is active.
            auto_pay (bool | None | Unset): True if the application can use the spend plan to process payments from the
                account. Example: True.
            description (str | Unset): Description for the project in the application. Example: Project being used to test
                cloud migration..
            id (int | Unset): ID of the record in the application. Example: 1.
            name (str | Unset): Name of the Project in the application. Example: Tech Project 1.
            ou (OU | Unset): OU defines an OU.
     """

    archived: bool | None | Unset = UNSET
    auto_pay: bool | None | Unset = UNSET
    description: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    ou: OU | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ou import OU
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

        description = self.description

        id = self.id

        name = self.name

        ou: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ou, Unset):
            ou = self.ou.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if archived is not UNSET:
            field_dict["archived"] = archived
        if auto_pay is not UNSET:
            field_dict["auto_pay"] = auto_pay
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if ou is not UNSET:
            field_dict["ou"] = ou

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ou import OU
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


        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _ou = d.pop("ou", UNSET)
        ou: OU | Unset
        if isinstance(_ou,  Unset):
            ou = UNSET
        else:
            ou = OU.from_dict(_ou)




        project_with_ou = cls(
            archived=archived,
            auto_pay=auto_pay,
            description=description,
            id=id,
            name=name,
            ou=ou,
        )


        project_with_ou.additional_properties = d
        return project_with_ou

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
