from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UGroupViewers")



@_attrs_define
class UGroupViewers:
    """ UGroupViewers defines a user group viewer update.

        Attributes:
            viewer_user_group_ids (list[int] | None | Unset): List of groups IDs who will own the group. Is required if no
                owner user IDs are listed. Example: [1, 2].
            viewer_user_ids (list[int] | None | Unset): List of user IDs who will own the group. Is required if no owner
                group IDs are listed. Example: [1, 2].
     """

    viewer_user_group_ids: list[int] | None | Unset = UNSET
    viewer_user_ids: list[int] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
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
        })
        if viewer_user_group_ids is not UNSET:
            field_dict["viewer_user_group_ids"] = viewer_user_group_ids
        if viewer_user_ids is not UNSET:
            field_dict["viewer_user_ids"] = viewer_user_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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


        u_group_viewers = cls(
            viewer_user_group_ids=viewer_user_group_ids,
            viewer_user_ids=viewer_user_ids,
        )


        u_group_viewers.additional_properties = d
        return u_group_viewers

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
