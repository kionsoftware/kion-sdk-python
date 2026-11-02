from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.null_uint import NullUint





T = TypeVar("T", bound="OUNote")



@_attrs_define
class OUNote:
    """ OUNote defines an OU Note.

        Attributes:
            create_user_id (int | None | Unset): ID of the user who created the note. Example: 1.
            create_user_name (str | Unset): Name of the user who created the note. Example: John Doe.
            created_at (str | Unset): Date when the note was created. Example: 2019-02-12T22:57:10+0000.
            id (int | Unset): ID of the OU note in the application. Example: 1.
            last_update_user_id (NullUint | Unset): NullUint represents a uint that may be NULL.
            last_update_user_name (str | Unset): Name of the user who last updated the note. Example: Jane Smith.
            name (str | Unset): Name of the OU note. Example: Important Note.
            ou_id (int | None | Unset): ID of the OU this note belongs to. Example: 1.
            text (str | Unset): Text content of the OU note. Example: This is an important note about the OU..
            updated_at (None | str | Unset): Date when the note was last updated. Example: 2019-02-12T22:57:10+0000.
     """

    create_user_id: int | None | Unset = UNSET
    create_user_name: str | Unset = UNSET
    created_at: str | Unset = UNSET
    id: int | Unset = UNSET
    last_update_user_id: NullUint | Unset = UNSET
    last_update_user_name: str | Unset = UNSET
    name: str | Unset = UNSET
    ou_id: int | None | Unset = UNSET
    text: str | Unset = UNSET
    updated_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.null_uint import NullUint
        create_user_id: int | None | Unset
        if isinstance(self.create_user_id, Unset):
            create_user_id = UNSET
        else:
            create_user_id = self.create_user_id

        create_user_name = self.create_user_name

        created_at = self.created_at

        id = self.id

        last_update_user_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_update_user_id, Unset):
            last_update_user_id = self.last_update_user_id.to_dict()

        last_update_user_name = self.last_update_user_name

        name = self.name

        ou_id: int | None | Unset
        if isinstance(self.ou_id, Unset):
            ou_id = UNSET
        else:
            ou_id = self.ou_id

        text = self.text

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if create_user_id is not UNSET:
            field_dict["create_user_id"] = create_user_id
        if create_user_name is not UNSET:
            field_dict["create_user_name"] = create_user_name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if last_update_user_id is not UNSET:
            field_dict["last_update_user_id"] = last_update_user_id
        if last_update_user_name is not UNSET:
            field_dict["last_update_user_name"] = last_update_user_name
        if name is not UNSET:
            field_dict["name"] = name
        if ou_id is not UNSET:
            field_dict["ou_id"] = ou_id
        if text is not UNSET:
            field_dict["text"] = text
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.null_uint import NullUint
        d = dict(src_dict)
        def _parse_create_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        create_user_id = _parse_create_user_id(d.pop("create_user_id", UNSET))


        create_user_name = d.pop("create_user_name", UNSET)

        created_at = d.pop("created_at", UNSET)

        id = d.pop("id", UNSET)

        _last_update_user_id = d.pop("last_update_user_id", UNSET)
        last_update_user_id: NullUint | Unset
        if isinstance(_last_update_user_id,  Unset):
            last_update_user_id = UNSET
        else:
            last_update_user_id = NullUint.from_dict(_last_update_user_id)




        last_update_user_name = d.pop("last_update_user_name", UNSET)

        name = d.pop("name", UNSET)

        def _parse_ou_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ou_id = _parse_ou_id(d.pop("ou_id", UNSET))


        text = d.pop("text", UNSET)

        def _parse_updated_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))


        ou_note = cls(
            create_user_id=create_user_id,
            create_user_name=create_user_name,
            created_at=created_at,
            id=id,
            last_update_user_id=last_update_user_id,
            last_update_user_name=last_update_user_name,
            name=name,
            ou_id=ou_id,
            text=text,
            updated_at=updated_at,
        )


        ou_note.additional_properties = d
        return ou_note

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
