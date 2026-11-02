from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ProjectNoteCreate")



@_attrs_define
class ProjectNoteCreate:
    """ ProjectNoteCreate represents the creation of a ProjectNote.

        Attributes:
            create_user_id (int | None | Unset): CreateUserID is the id of the user creating the project note. Example: 1.
            name (str | Unset): Name is the name of the project note. Example: "Project Note 1".
            project_id (int | None | Unset): ProjectID of the project id associated to the project note. Example: 1.
            text (str | Unset): Text is the notes written for the project note. Example: "This is the note".
     """

    create_user_id: int | None | Unset = UNSET
    name: str | Unset = UNSET
    project_id: int | None | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        create_user_id: int | None | Unset
        if isinstance(self.create_user_id, Unset):
            create_user_id = UNSET
        else:
            create_user_id = self.create_user_id

        name = self.name

        project_id: int | None | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        text = self.text


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if create_user_id is not UNSET:
            field_dict["create_user_id"] = create_user_id
        if name is not UNSET:
            field_dict["name"] = name
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_create_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        create_user_id = _parse_create_user_id(d.pop("create_user_id", UNSET))


        name = d.pop("name", UNSET)

        def _parse_project_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))


        text = d.pop("text", UNSET)

        project_note_create = cls(
            create_user_id=create_user_id,
            name=name,
            project_id=project_id,
            text=text,
        )


        project_note_create.additional_properties = d
        return project_note_create

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
