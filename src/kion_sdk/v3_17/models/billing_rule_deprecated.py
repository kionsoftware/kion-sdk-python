from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.billing_rule_criteria import BillingRuleCriteria
  from ..models.null_int import NullInt
  from ..models.null_time import NullTime





T = TypeVar("T", bound="BillingRuleDeprecated")



@_attrs_define
class BillingRuleDeprecated:
    """ 
        Attributes:
            billing_criteria (BillingRuleCriteria | Unset):
            created_at (datetime.datetime | Unset):
            created_by (int | Unset):
            deleted_at (None | NullTime | Unset):
            description (str | Unset):
            end_month (NullInt | Unset): NullInt represents an int that may be NULL.
            id (int | Unset):
            name (str | Unset):
            start_month (int | Unset):
            type_ (int | Unset):
            updated_at (None | NullTime | Unset):
            value (float | Unset):
     """

    billing_criteria: BillingRuleCriteria | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    created_by: int | Unset = UNSET
    deleted_at: None | NullTime | Unset = UNSET
    description: str | Unset = UNSET
    end_month: NullInt | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    start_month: int | Unset = UNSET
    type_: int | Unset = UNSET
    updated_at: None | NullTime | Unset = UNSET
    value: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.billing_rule_criteria import BillingRuleCriteria
        from ..models.null_int import NullInt
        from ..models.null_time import NullTime
        billing_criteria: dict[str, Any] | Unset = UNSET
        if not isinstance(self.billing_criteria, Unset):
            billing_criteria = self.billing_criteria.to_dict()

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by = self.created_by

        deleted_at: dict[str, Any] | None | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        elif isinstance(self.deleted_at, NullTime):
            deleted_at = self.deleted_at.to_dict()
        else:
            deleted_at = self.deleted_at

        description = self.description

        end_month: dict[str, Any] | Unset = UNSET
        if not isinstance(self.end_month, Unset):
            end_month = self.end_month.to_dict()

        id = self.id

        name = self.name

        start_month = self.start_month

        type_ = self.type_

        updated_at: dict[str, Any] | None | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, NullTime):
            updated_at = self.updated_at.to_dict()
        else:
            updated_at = self.updated_at

        value = self.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if billing_criteria is not UNSET:
            field_dict["billing_criteria"] = billing_criteria
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if description is not UNSET:
            field_dict["description"] = description
        if end_month is not UNSET:
            field_dict["end_month"] = end_month
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if start_month is not UNSET:
            field_dict["start_month"] = start_month
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.billing_rule_criteria import BillingRuleCriteria
        from ..models.null_int import NullInt
        from ..models.null_time import NullTime
        d = dict(src_dict)
        _billing_criteria = d.pop("billing_criteria", UNSET)
        billing_criteria: BillingRuleCriteria | Unset
        if isinstance(_billing_criteria,  Unset):
            billing_criteria = UNSET
        else:
            billing_criteria = BillingRuleCriteria.from_dict(_billing_criteria)




        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        created_by = d.pop("created_by", UNSET)

        def _parse_deleted_at(data: object) -> None | NullTime | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                deleted_at_type_1 = NullTime.from_dict(data)



                return deleted_at_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | NullTime | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at", UNSET))


        description = d.pop("description", UNSET)

        _end_month = d.pop("end_month", UNSET)
        end_month: NullInt | Unset
        if isinstance(_end_month,  Unset):
            end_month = UNSET
        else:
            end_month = NullInt.from_dict(_end_month)




        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        start_month = d.pop("start_month", UNSET)

        type_ = d.pop("type", UNSET)

        def _parse_updated_at(data: object) -> None | NullTime | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                updated_at_type_1 = NullTime.from_dict(data)



                return updated_at_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | NullTime | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))


        value = d.pop("value", UNSET)

        billing_rule_deprecated = cls(
            billing_criteria=billing_criteria,
            created_at=created_at,
            created_by=created_by,
            deleted_at=deleted_at,
            description=description,
            end_month=end_month,
            id=id,
            name=name,
            start_month=start_month,
            type_=type_,
            updated_at=updated_at,
            value=value,
        )


        billing_rule_deprecated.additional_properties = d
        return billing_rule_deprecated

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
