from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UGroupCreate")



@_attrs_define
class UGroupCreate:
    """ UGroupCreate defines a user group.

        Attributes:
            idms_id (int | None): ID of the IDMS where the user group is located. Example: 1.
            name (str): Name of the user group in the application. Example: development-team.
            add_self_as_viewer (bool | None | Unset): This option will add the user group as a viewer of itself after it is
                created. Example: True.
            description (str | Unset): Description of the user group in the application. Example: development-team.
            owner_user_group_ids (list[int] | None | Unset): List of groups IDs who will own the group. Is required if no
                owner user IDs are listed. Example: [1, 2].
            owner_user_ids (list[int] | None | Unset): List of user IDs who will own the group. Is required if no owner
                group IDs are listed. Example: [1, 2].
            user_ids (list[int] | None | Unset): IDs of the users in the user group. Example: [1, 2].
            viewer_user_group_ids (list[int] | None | Unset): List of groups IDs who will own the group. Is required if no
                owner user IDs are listed. Example: [1, 2].
            viewer_user_ids (list[int] | None | Unset): List of user IDs who will own the group. Is required if no owner
                group IDs are listed. Example: [1, 2].
     """

    idms_id: int | None
    name: str
    add_self_as_viewer: bool | None | Unset = UNSET
    description: str | Unset = UNSET
    owner_user_group_ids: list[int] | None | Unset = UNSET
    owner_user_ids: list[int] | None | Unset = UNSET
    user_ids: list[int] | None | Unset = UNSET
    viewer_user_group_ids: list[int] | None | Unset = UNSET
    viewer_user_ids: list[int] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        idms_id: int | None
        idms_id = self.idms_id

        name = self.name

        add_self_as_viewer: bool | None | Unset
        if isinstance(self.add_self_as_viewer, Unset):
            add_self_as_viewer = UNSET
        else:
            add_self_as_viewer = self.add_self_as_viewer

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

        user_ids: list[int] | None | Unset
        if isinstance(self.user_ids, Unset):
            user_ids = UNSET
        elif isinstance(self.user_ids, list):
            user_ids = self.user_ids


        else:
            user_ids = self.user_ids

        viewer_user_group_ids: list[int] | None | Unset
        if isinstance(self.viewer_user_group_ids, Unset):
            viewer_user_group_ids = UNSET
        elif isinstance(self.viewer_user_group_ids, list):
            viewer_user_group_ids = self.viewer_user_group_ids


        else:
            viewer_user_group_ids = self.viewer_user_group_ids

        viewer_user_ids: list[int] | None | Unset
        if isinstance(self.viewer_user_ids, Unset):
            viewer_user_ids = UNSET
        elif isinstance(self.viewer_user_ids, list):
            viewer_user_ids = self.viewer_user_ids


        else:
            viewer_user_ids = self.viewer_user_ids


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "idms_id": idms_id,
            "name": name,
        })
        if add_self_as_viewer is not UNSET:
            field_dict["add_self_as_viewer"] = add_self_as_viewer
        if description is not UNSET:
            field_dict["description"] = description
        if owner_user_group_ids is not UNSET:
            field_dict["owner_user_group_ids"] = owner_user_group_ids
        if owner_user_ids is not UNSET:
            field_dict["owner_user_ids"] = owner_user_ids
        if user_ids is not UNSET:
            field_dict["user_ids"] = user_ids
        if viewer_user_group_ids is not UNSET:
            field_dict["viewer_user_group_ids"] = viewer_user_group_ids
        if viewer_user_ids is not UNSET:
            field_dict["viewer_user_ids"] = viewer_user_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_idms_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        idms_id = _parse_idms_id(d.pop("idms_id"))


        name = d.pop("name")

        def _parse_add_self_as_viewer(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        add_self_as_viewer = _parse_add_self_as_viewer(d.pop("add_self_as_viewer", UNSET))


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


        def _parse_user_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                user_ids_type_0 = cast(list[int], data)

                return user_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        user_ids = _parse_user_ids(d.pop("user_ids", UNSET))


        def _parse_viewer_user_group_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                viewer_user_group_ids_type_0 = cast(list[int], data)

                return viewer_user_group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        viewer_user_group_ids = _parse_viewer_user_group_ids(d.pop("viewer_user_group_ids", UNSET))


        def _parse_viewer_user_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                viewer_user_ids_type_0 = cast(list[int], data)

                return viewer_user_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        viewer_user_ids = _parse_viewer_user_ids(d.pop("viewer_user_ids", UNSET))


        u_group_create = cls(
            idms_id=idms_id,
            name=name,
            add_self_as_viewer=add_self_as_viewer,
            description=description,
            owner_user_group_ids=owner_user_group_ids,
            owner_user_ids=owner_user_ids,
            user_ids=user_ids,
            viewer_user_group_ids=viewer_user_group_ids,
            viewer_user_ids=viewer_user_ids,
        )


        u_group_create.additional_properties = d
        return u_group_create

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
