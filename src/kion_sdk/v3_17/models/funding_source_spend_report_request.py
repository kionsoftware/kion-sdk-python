from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="FundingSourceSpendReportRequest")



@_attrs_define
class FundingSourceSpendReportRequest:
    """ FundingSourceSpendReportRequest represents request parameters for a spend report.

        Attributes:
            end_datecode (int | Unset): EndDatecode is the end date for when to pull the funding source report (exclusive)
                Example: 201901.
            ids (list[int] | None | Unset): IDs are the funding source ids to pull for the funding source report Example:
                [1, 2].
            start_datecode (int | Unset): StartMonth is the start date for when to pull the funding source report
                (inclusive) Example: 201901.
     """

    end_datecode: int | Unset = UNSET
    ids: list[int] | None | Unset = UNSET
    start_datecode: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        end_datecode = self.end_datecode

        ids: list[int] | None | Unset
        if isinstance(self.ids, Unset):
            ids = UNSET
        elif isinstance(self.ids, list):
            ids = self.ids


        else:
            ids = self.ids

        start_datecode = self.start_datecode


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if end_datecode is not UNSET:
            field_dict["end_datecode"] = end_datecode
        if ids is not UNSET:
            field_dict["ids"] = ids
        if start_datecode is not UNSET:
            field_dict["start_datecode"] = start_datecode

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        end_datecode = d.pop("end_datecode", UNSET)

        def _parse_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ids_type_0 = cast(list[int], data)

                return ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        ids = _parse_ids(d.pop("ids", UNSET))


        start_datecode = d.pop("start_datecode", UNSET)

        funding_source_spend_report_request = cls(
            end_datecode=end_datecode,
            ids=ids,
            start_datecode=start_datecode,
        )


        funding_source_spend_report_request.additional_properties = d
        return funding_source_spend_report_request

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
