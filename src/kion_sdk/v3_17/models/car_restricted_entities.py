from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CARRestrictedEntities")



@_attrs_define
class CARRestrictedEntities:
    """ CARRestrictedEntities defines user and group ID lists.

        Attributes:
            car_restricted_ugroup_ids (list[int] | None | Unset): List of user group IDs who will be able to use the iam
                policy on Cloud Access Roles Example: [1, 2].
            car_restricted_user_ids (list[int] | None | Unset): List of user IDs who will be able to use the iam policy on
                Cloud Access Roles. Example: [1, 2].
     """

    car_restricted_ugroup_ids: list[int] | None | Unset = UNSET
    car_restricted_user_ids: list[int] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        car_restricted_ugroup_ids: list[int] | None | Unset
        if isinstance(self.car_restricted_ugroup_ids, Unset):
            car_restricted_ugroup_ids = UNSET
        elif isinstance(self.car_restricted_ugroup_ids, list):
            car_restricted_ugroup_ids = self.car_restricted_ugroup_ids


        else:
            car_restricted_ugroup_ids = self.car_restricted_ugroup_ids

        car_restricted_user_ids: list[int] | None | Unset
        if isinstance(self.car_restricted_user_ids, Unset):
            car_restricted_user_ids = UNSET
        elif isinstance(self.car_restricted_user_ids, list):
            car_restricted_user_ids = self.car_restricted_user_ids


        else:
            car_restricted_user_ids = self.car_restricted_user_ids


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if car_restricted_ugroup_ids is not UNSET:
            field_dict["car_restricted_ugroup_ids"] = car_restricted_ugroup_ids
        if car_restricted_user_ids is not UNSET:
            field_dict["car_restricted_user_ids"] = car_restricted_user_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_car_restricted_ugroup_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                car_restricted_ugroup_ids_type_0 = cast(list[int], data)

                return car_restricted_ugroup_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        car_restricted_ugroup_ids = _parse_car_restricted_ugroup_ids(d.pop("car_restricted_ugroup_ids", UNSET))


        def _parse_car_restricted_user_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                car_restricted_user_ids_type_0 = cast(list[int], data)

                return car_restricted_user_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        car_restricted_user_ids = _parse_car_restricted_user_ids(d.pop("car_restricted_user_ids", UNSET))


        car_restricted_entities = cls(
            car_restricted_ugroup_ids=car_restricted_ugroup_ids,
            car_restricted_user_ids=car_restricted_user_ids,
        )


        car_restricted_entities.additional_properties = d
        return car_restricted_entities

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
