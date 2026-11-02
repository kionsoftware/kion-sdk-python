from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.month_range import MonthRange
  from ..models.spend_report_query_filter import SpendReportQueryFilter





T = TypeVar("T", bound="SpendReportQuery")



@_attrs_define
class SpendReportQuery:
    """ 
        Attributes:
            columns (list[str] | None): Columns Example: ['account_id', 'account_name', 'account_number', 'project_id',
                'project_name', 'parent_ou_id', 'parent_ou_name', 'billing_source_id', 'billing_source_name', 'month',
                'cloud_service_provider_id', 'cloud_service_provider_name', 'service', 'resource', 'configured_spend',
                'unadjusted_spend', 'billed_spend', 'net_billed_spend', 'list_spend', 'net_list_spend', 'unattributed_spend',
                'attributed_spend', 'net_attributed_spend', 'net_unattributed_spend', 'credit', 'refund', 'discount',
                'account_label:<LABEL_KEY>', 'account_label:<LABEL_KEY_2>', 'project_label:<LABEL_KEY>', 'tag:<TAG_KEY>',
                'tag:resourcetags/aws:createdby'].
            month_range (MonthRange): MonthRange defines a range of months
            filters (SpendReportQueryFilter | Unset): SpendReportQueryFilter defines the filters for the spend report query
     """

    columns: list[str] | None
    month_range: MonthRange
    filters: SpendReportQueryFilter | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.month_range import MonthRange
        from ..models.spend_report_query_filter import SpendReportQueryFilter
        columns: list[str] | None
        if isinstance(self.columns, list):
            columns = self.columns


        else:
            columns = self.columns

        month_range = self.month_range.to_dict()

        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "columns": columns,
            "month_range": month_range,
        })
        if filters is not UNSET:
            field_dict["filters"] = filters

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.month_range import MonthRange
        from ..models.spend_report_query_filter import SpendReportQueryFilter
        d = dict(src_dict)
        def _parse_columns(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                columns_type_0 = cast(list[str], data)

                return columns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        columns = _parse_columns(d.pop("columns"))


        month_range = MonthRange.from_dict(d.pop("month_range"))




        _filters = d.pop("filters", UNSET)
        filters: SpendReportQueryFilter | Unset
        if isinstance(_filters,  Unset):
            filters = UNSET
        else:
            filters = SpendReportQueryFilter.from_dict(_filters)




        spend_report_query = cls(
            columns=columns,
            month_range=month_range,
            filters=filters,
        )


        spend_report_query.additional_properties = d
        return spend_report_query

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
