from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="GetProjectLabel")



@_attrs_define
class GetProjectLabel:
    """ 
        Attributes:
            color (str): Hex value of the label color Example: #9fa4a6.
            key (str): Key of the label (first part of the label) Example: Department.
            value (str): Value of the label (second part of the label following the key) Example: Engineering.
            create_user_id (int | None | Unset): Numerical ID of the user that created this label Example: 1.
            create_user_name (str | Unset): Username of the the user that created this label Example: admin.
            created_at (datetime.datetime | Unset): Timestamp of when this label was created Example: 2022-09-23T19:26:08Z.
            id (int | Unset): Numerical ID of the label Example: 4.
            key_id (int | None | Unset): Numerical ID of the key for this label's key:value pair Example: 2.
            project_id (int | None | Unset): ID of the project that is being queried for labels Example: 3.
     """

    color: str
    key: str
    value: str
    create_user_id: int | None | Unset = UNSET
    create_user_name: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    id: int | Unset = UNSET
    key_id: int | None | Unset = UNSET
    project_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        color = self.color

        key = self.key

        value = self.value

        create_user_id: int | None | Unset
        if isinstance(self.create_user_id, Unset):
            create_user_id = UNSET
        else:
            create_user_id = self.create_user_id

        create_user_name = self.create_user_name

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        id = self.id

        key_id: int | None | Unset
        if isinstance(self.key_id, Unset):
            key_id = UNSET
        else:
            key_id = self.key_id

        project_id: int | None | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "color": color,
            "key": key,
            "value": value,
        })
        if create_user_id is not UNSET:
            field_dict["create_user_id"] = create_user_id
        if create_user_name is not UNSET:
            field_dict["create_user_name"] = create_user_name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if key_id is not UNSET:
            field_dict["key_id"] = key_id
        if project_id is not UNSET:
            field_dict["project_id"] = project_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        color = d.pop("color")

        key = d.pop("key")

        value = d.pop("value")

        def _parse_create_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        create_user_id = _parse_create_user_id(d.pop("create_user_id", UNSET))


        create_user_name = d.pop("create_user_name", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        id = d.pop("id", UNSET)

        def _parse_key_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        key_id = _parse_key_id(d.pop("key_id", UNSET))


        def _parse_project_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))


        get_project_label = cls(
            color=color,
            key=key,
            value=value,
            create_user_id=create_user_id,
            create_user_name=create_user_name,
            created_at=created_at,
            id=id,
            key_id=key_id,
            project_id=project_id,
        )


        get_project_label.additional_properties = d
        return get_project_label

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
