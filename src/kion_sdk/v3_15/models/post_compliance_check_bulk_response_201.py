from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PostComplianceCheckBulkResponse201")



@_attrs_define
class PostComplianceCheckBulkResponse201:
    """ 
        Attributes:
            data (list[int] | Unset): List of Compliance Checks IDs. Example: [1, 2].
            status (int | Unset): HTTP status code. Example: 200.
     """

    data: list[int] | Unset = UNSET
    status: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        data: list[int] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data



        status = self.status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data is not UNSET:
            field_dict["data"] = data
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data = cast(list[int], d.pop("data", UNSET))


        status = d.pop("status", UNSET)

        post_compliance_check_bulk_response_201 = cls(
            data=data,
            status=status,
        )


        post_compliance_check_bulk_response_201.additional_properties = d
        return post_compliance_check_bulk_response_201

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
