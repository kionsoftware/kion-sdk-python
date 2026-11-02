from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="ListGCPFoldersRequestBody")



@_attrs_define
class ListGCPFoldersRequestBody:
    """ ListGCPFoldersRequestBody is the body of a list folders call

        Attributes:
            parent_name (str): ParentName is the fully qualified gcp resource identifier to list folders for.
                This must be in the format organizations/<org #> or folders/<folder #> Example: organizations/1026377682360.
            payer_id (int | None): PayerID is the ID of the GCP billing source to list folders on Example: 32.
     """

    parent_name: str
    payer_id: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        parent_name = self.parent_name

        payer_id: int | None
        payer_id = self.payer_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "parent_name": parent_name,
            "payer_id": payer_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        parent_name = d.pop("parent_name")

        def _parse_payer_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        payer_id = _parse_payer_id(d.pop("payer_id"))


        list_gcp_folders_request_body = cls(
            parent_name=parent_name,
            payer_id=payer_id,
        )


        list_gcp_folders_request_body.additional_properties = d
        return list_gcp_folders_request_body

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
