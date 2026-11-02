from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="GCPConnectedProject")



@_attrs_define
class GCPConnectedProject:
    """ GCPConnectedProject A GCP project connected to a Kion account.

        Attributes:
            payer_id (int | None): The Payer ID associated with the GCP Service Account ID Example: 301.
            project_id (str): The GCP Project ID / Kion Account Number. Example: my-gcp-project-id.
            project_name (str): The GCP Project Display Name. Example: My GCP Project.
     """

    payer_id: int | None
    project_id: str
    project_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        payer_id: int | None
        payer_id = self.payer_id

        project_id = self.project_id

        project_name = self.project_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "payer_id": payer_id,
            "project_id": project_id,
            "project_name": project_name,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_payer_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        payer_id = _parse_payer_id(d.pop("payer_id"))


        project_id = d.pop("project_id")

        project_name = d.pop("project_name")

        gcp_connected_project = cls(
            payer_id=payer_id,
            project_id=project_id,
            project_name=project_name,
        )


        gcp_connected_project.additional_properties = d
        return gcp_connected_project

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
