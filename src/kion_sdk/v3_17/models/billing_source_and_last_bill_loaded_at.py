from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.billing_source import BillingSource





T = TypeVar("T", bound="BillingSourceAndLastBillLoadedAt")



@_attrs_define
class BillingSourceAndLastBillLoadedAt:
    """ BillingSourceAndLastBillLoadedAt defines a billing source and the timestamp of its most recently loaded bill.

        Attributes:
            billing_source (BillingSource | Unset): BillingSource defines the contents of a billing source.
            last_bill_loaded_at (str | Unset): Time when we processed the most recently loaded bill for the billing source.
                Example: 2019-08-28T00:00:00.000Z.
     """

    billing_source: BillingSource | Unset = UNSET
    last_bill_loaded_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.billing_source import BillingSource
        billing_source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.billing_source, Unset):
            billing_source = self.billing_source.to_dict()

        last_bill_loaded_at = self.last_bill_loaded_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if billing_source is not UNSET:
            field_dict["billing_source"] = billing_source
        if last_bill_loaded_at is not UNSET:
            field_dict["last_bill_loaded_at"] = last_bill_loaded_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.billing_source import BillingSource
        d = dict(src_dict)
        _billing_source = d.pop("billing_source", UNSET)
        billing_source: BillingSource | Unset
        if isinstance(_billing_source,  Unset):
            billing_source = UNSET
        else:
            billing_source = BillingSource.from_dict(_billing_source)




        last_bill_loaded_at = d.pop("last_bill_loaded_at", UNSET)

        billing_source_and_last_bill_loaded_at = cls(
            billing_source=billing_source,
            last_bill_loaded_at=last_bill_loaded_at,
        )


        billing_source_and_last_bill_loaded_at.additional_properties = d
        return billing_source_and_last_bill_loaded_at

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
