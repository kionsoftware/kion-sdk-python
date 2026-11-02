from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.project_funding_update import ProjectFundingUpdate





T = TypeVar("T", bound="ProjectFundingUpdates")



@_attrs_define
class ProjectFundingUpdates:
    """ ProjectFundingUpdates defines funding updates on a project.

        Attributes:
            funding (list[ProjectFundingUpdate] | None | Unset):
     """

    funding: list[ProjectFundingUpdate] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.project_funding_update import ProjectFundingUpdate
        funding: list[dict[str, Any]] | None | Unset
        if isinstance(self.funding, Unset):
            funding = UNSET
        elif isinstance(self.funding, list):
            funding = []
            for funding_type_0_item_data in self.funding:
                funding_type_0_item = funding_type_0_item_data.to_dict()
                funding.append(funding_type_0_item)


        else:
            funding = self.funding


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if funding is not UNSET:
            field_dict["funding"] = funding

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_funding_update import ProjectFundingUpdate
        d = dict(src_dict)
        def _parse_funding(data: object) -> list[ProjectFundingUpdate] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                funding_type_0 = []
                _funding_type_0 = data
                for funding_type_0_item_data in (_funding_type_0):
                    funding_type_0_item = ProjectFundingUpdate.from_dict(funding_type_0_item_data)



                    funding_type_0.append(funding_type_0_item)

                return funding_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ProjectFundingUpdate] | None | Unset, data)

        funding = _parse_funding(d.pop("funding", UNSET))


        project_funding_updates = cls(
            funding=funding,
        )


        project_funding_updates.additional_properties = d
        return project_funding_updates

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
