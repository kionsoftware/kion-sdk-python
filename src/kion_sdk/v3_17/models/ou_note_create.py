from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="OUNoteCreate")



@_attrs_define
class OUNoteCreate:
    """ OUNoteCreate defines the structure for creating an OU note.

        Attributes:
            create_user_id (int | None): ID of the user creating the note. Example: 1.
            name (str): Name of the OU note. Example: Important Note.
            ou_id (int | None): ID of the OU this note belongs to. Example: 1.
            text (str): Text content of the OU note. Example: This is an important note about the OU..
     """

    create_user_id: int | None
    name: str
    ou_id: int | None
    text: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        create_user_id: int | None
        create_user_id = self.create_user_id

        name = self.name

        ou_id: int | None
        ou_id = self.ou_id

        text = self.text


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "create_user_id": create_user_id,
            "name": name,
            "ou_id": ou_id,
            "text": text,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_create_user_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        create_user_id = _parse_create_user_id(d.pop("create_user_id"))


        name = d.pop("name")

        def _parse_ou_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ou_id = _parse_ou_id(d.pop("ou_id"))


        text = d.pop("text")

        ou_note_create = cls(
            create_user_id=create_user_id,
            name=name,
            ou_id=ou_id,
            text=text,
        )


        ou_note_create.additional_properties = d
        return ou_note_create

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
