from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AzureRegionRefreshStatus")



@_attrs_define
class AzureRegionRefreshStatus:
    """ AzureRegionRefreshStatus reports whether or not an Azure Region Refresh was fully or only partially successful

        Attributes:
            message (str | Unset): Descriptive message detailing the status of the region refresh. Example: Refresh
                completed successfully..
            partial_failure (bool | None | Unset): True if only some regions successfully refreshed. This may occur if App
                Registration details on a Billing Source are invalid.
     """

    message: str | Unset = UNSET
    partial_failure: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        message = self.message

        partial_failure: bool | None | Unset
        if isinstance(self.partial_failure, Unset):
            partial_failure = UNSET
        else:
            partial_failure = self.partial_failure


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if message is not UNSET:
            field_dict["message"] = message
        if partial_failure is not UNSET:
            field_dict["partial_failure"] = partial_failure

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message", UNSET)

        def _parse_partial_failure(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        partial_failure = _parse_partial_failure(d.pop("partial_failure", UNSET))


        azure_region_refresh_status = cls(
            message=message,
            partial_failure=partial_failure,
        )


        azure_region_refresh_status.additional_properties = d
        return azure_region_refresh_status

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
