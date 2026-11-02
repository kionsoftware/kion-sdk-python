from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.custom_billing_source_test_results import CustomBillingSourceTestResults





T = TypeVar("T", bound="PostTestCustomBillingSourceResponse200")



@_attrs_define
class PostTestCustomBillingSourceResponse200:
    """ 
        Attributes:
            data (CustomBillingSourceTestResults | Unset): CustomBillingSourceTestResults defines the results of a custom
                billing source test.
            status (int | Unset): HTTP status code. Example: 200.
     """

    data: CustomBillingSourceTestResults | Unset = UNSET
    status: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_billing_source_test_results import CustomBillingSourceTestResults
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

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
        from ..models.custom_billing_source_test_results import CustomBillingSourceTestResults
        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: CustomBillingSourceTestResults | Unset
        if isinstance(_data,  Unset):
            data = UNSET
        else:
            data = CustomBillingSourceTestResults.from_dict(_data)




        status = d.pop("status", UNSET)

        post_test_custom_billing_source_response_200 = cls(
            data=data,
            status=status,
        )


        post_test_custom_billing_source_response_200.additional_properties = d
        return post_test_custom_billing_source_response_200

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
