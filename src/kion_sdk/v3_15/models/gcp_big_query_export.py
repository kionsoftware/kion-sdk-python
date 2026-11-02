from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GCPBigQueryExport")



@_attrs_define
class GCPBigQueryExport:
    """ GCPBigQueryExport describes information about where billing data is exported in BigQuery

        Attributes:
            dataset_name (str | Unset): The name of the BigQuery dataset where the export lives Example:
                BigQueryBillingExportDataset.
            focus_view_name (str | Unset): The name of the FOCUS view in BigQuery. Example: focus_view_v1.
            gcp_project_id (str | Unset): The ID of the GCP project where the BigQuery dataset lives Example:
                myproject-5468419.
            table_format (str | Unset): The format of the BigQuery table where the export lives.  One of 'auto', 'standard'
                or 'detailed'. Example: auto.
            table_name (str | Unset): The name of the BigQuery table where the export lives Example: my_table.
     """

    dataset_name: str | Unset = UNSET
    focus_view_name: str | Unset = UNSET
    gcp_project_id: str | Unset = UNSET
    table_format: str | Unset = UNSET
    table_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        dataset_name = self.dataset_name

        focus_view_name = self.focus_view_name

        gcp_project_id = self.gcp_project_id

        table_format = self.table_format

        table_name = self.table_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if dataset_name is not UNSET:
            field_dict["dataset_name"] = dataset_name
        if focus_view_name is not UNSET:
            field_dict["focus_view_name"] = focus_view_name
        if gcp_project_id is not UNSET:
            field_dict["gcp_project_id"] = gcp_project_id
        if table_format is not UNSET:
            field_dict["table_format"] = table_format
        if table_name is not UNSET:
            field_dict["table_name"] = table_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dataset_name = d.pop("dataset_name", UNSET)

        focus_view_name = d.pop("focus_view_name", UNSET)

        gcp_project_id = d.pop("gcp_project_id", UNSET)

        table_format = d.pop("table_format", UNSET)

        table_name = d.pop("table_name", UNSET)

        gcp_big_query_export = cls(
            dataset_name=dataset_name,
            focus_view_name=focus_view_name,
            gcp_project_id=gcp_project_id,
            table_format=table_format,
            table_name=table_name,
        )


        gcp_big_query_export.additional_properties = d
        return gcp_big_query_export

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
