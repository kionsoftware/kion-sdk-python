from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.funding_source import FundingSource





T = TypeVar("T", bound="FSProjectFunding")



@_attrs_define
class FSProjectFunding:
    """ FSProjectFunding defines the funding for a project.

        Attributes:
            available_to_project (float | Unset): The amount of money available to the project from this funding source.
            end_datecode (str | Unset): The month this funding source stops being usable (YYYY-MM). Example: 2019-12.
            funding_source (FundingSource | Unset): FundingSource defines a funding source.
            planned_for_project (float | Unset): The amount of money already planned for the project from this funding
                source.
            remaining_on_project (float | Unset): The amount of money remaining for the project to use from this funding
                source.
            spent_on_project (float | Unset): The amount of money spent on the project from this funding source.
            start_datecode (str | Unset): The month this funding source starts being usable (YYYY-MM). Example: 2019-01.
     """

    available_to_project: float | Unset = UNSET
    end_datecode: str | Unset = UNSET
    funding_source: FundingSource | Unset = UNSET
    planned_for_project: float | Unset = UNSET
    remaining_on_project: float | Unset = UNSET
    spent_on_project: float | Unset = UNSET
    start_datecode: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.funding_source import FundingSource
        available_to_project = self.available_to_project

        end_datecode = self.end_datecode

        funding_source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.funding_source, Unset):
            funding_source = self.funding_source.to_dict()

        planned_for_project = self.planned_for_project

        remaining_on_project = self.remaining_on_project

        spent_on_project = self.spent_on_project

        start_datecode = self.start_datecode


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if available_to_project is not UNSET:
            field_dict["available_to_project"] = available_to_project
        if end_datecode is not UNSET:
            field_dict["end_datecode"] = end_datecode
        if funding_source is not UNSET:
            field_dict["funding_source"] = funding_source
        if planned_for_project is not UNSET:
            field_dict["planned_for_project"] = planned_for_project
        if remaining_on_project is not UNSET:
            field_dict["remaining_on_project"] = remaining_on_project
        if spent_on_project is not UNSET:
            field_dict["spent_on_project"] = spent_on_project
        if start_datecode is not UNSET:
            field_dict["start_datecode"] = start_datecode

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.funding_source import FundingSource
        d = dict(src_dict)
        available_to_project = d.pop("available_to_project", UNSET)

        end_datecode = d.pop("end_datecode", UNSET)

        _funding_source = d.pop("funding_source", UNSET)
        funding_source: FundingSource | Unset
        if isinstance(_funding_source,  Unset):
            funding_source = UNSET
        else:
            funding_source = FundingSource.from_dict(_funding_source)




        planned_for_project = d.pop("planned_for_project", UNSET)

        remaining_on_project = d.pop("remaining_on_project", UNSET)

        spent_on_project = d.pop("spent_on_project", UNSET)

        start_datecode = d.pop("start_datecode", UNSET)

        fs_project_funding = cls(
            available_to_project=available_to_project,
            end_datecode=end_datecode,
            funding_source=funding_source,
            planned_for_project=planned_for_project,
            remaining_on_project=remaining_on_project,
            spent_on_project=spent_on_project,
            start_datecode=start_datecode,
        )


        fs_project_funding.additional_properties = d
        return fs_project_funding

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
