from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PostTestGCPBillingSourceResponse200Data")



@_attrs_define
class PostTestGCPBillingSourceResponse200Data:
    """ Billing source test results.

        Attributes:
            dataset_ok (bool | Unset):
            error_message (str | Unset):
            focus_ok (bool | Unset):
            message (str | Unset): deprecated: true
            ok (bool | Unset): deprecated: true
            warning_message (str | Unset):
     """

    dataset_ok: bool | Unset = UNSET
    error_message: str | Unset = UNSET
    focus_ok: bool | Unset = UNSET
    message: str | Unset = UNSET
    ok: bool | Unset = UNSET
    warning_message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        dataset_ok = self.dataset_ok

        error_message = self.error_message

        focus_ok = self.focus_ok

        message = self.message

        ok = self.ok

        warning_message = self.warning_message


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if dataset_ok is not UNSET:
            field_dict["dataset_ok"] = dataset_ok
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if focus_ok is not UNSET:
            field_dict["focus_ok"] = focus_ok
        if message is not UNSET:
            field_dict["message"] = message
        if ok is not UNSET:
            field_dict["ok"] = ok
        if warning_message is not UNSET:
            field_dict["warning_message"] = warning_message

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dataset_ok = d.pop("dataset_ok", UNSET)

        error_message = d.pop("error_message", UNSET)

        focus_ok = d.pop("focus_ok", UNSET)

        message = d.pop("message", UNSET)

        ok = d.pop("ok", UNSET)

        warning_message = d.pop("warning_message", UNSET)

        post_test_gcp_billing_source_response_200_data = cls(
            dataset_ok=dataset_ok,
            error_message=error_message,
            focus_ok=focus_ok,
            message=message,
            ok=ok,
            warning_message=warning_message,
        )


        post_test_gcp_billing_source_response_200_data.additional_properties = d
        return post_test_gcp_billing_source_response_200_data

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
