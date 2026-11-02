from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ExternalIDs")



@_attrs_define
class ExternalIDs:
    """ ExternalIDs defines external id type structure.

        Attributes:
            car_external_id (str | Unset): The external id used with trust policies for the account's cloud access roles
                Example: CAR-1234567.
            service_external_id (str | Unset): The external id used with trust policies for the account's service roles
                Example: Service-1234567.
     """

    car_external_id: str | Unset = UNSET
    service_external_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        car_external_id = self.car_external_id

        service_external_id = self.service_external_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if car_external_id is not UNSET:
            field_dict["car_external_id"] = car_external_id
        if service_external_id is not UNSET:
            field_dict["service_external_id"] = service_external_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        car_external_id = d.pop("car_external_id", UNSET)

        service_external_id = d.pop("service_external_id", UNSET)

        external_i_ds = cls(
            car_external_id=car_external_id,
            service_external_id=service_external_id,
        )


        external_i_ds.additional_properties = d
        return external_i_ds

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
