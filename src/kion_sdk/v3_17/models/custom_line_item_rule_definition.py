from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.billing_rule_destination import BillingRuleDestination





T = TypeVar("T", bound="CustomLineItemRuleDefinition")



@_attrs_define
class CustomLineItemRuleDefinition:
    """ 
        Attributes:
            destinations (list[BillingRuleDestination] | None): The destination list for which scopes should be added to
                this billing rule.
                It can include a list of scope IDs or a list of OU or Project IDs, from which all descendent scopes are
                included.
                Project and OU ID lists can also include scope IDs to be excluded from the descendent scope list.
            name (str): Name of the custom line item. The name can be up to 255 characters long. Example: Example Custom
                Line Item.
            rule_value (float): The value of the custom line item. Example: 100.
            description (str | Unset): Description of the custom line item. The description can be up to 1024 characters
                long. Example: This is a test billing rule of the type custom line item..
            region_id (int | None | Unset): The region ID. Optional property to include for spend report display. Example:
                1.
            service_category_id (int | None | Unset): The service category ID. Optional property to include for spend report
                display. Example: 1.
     """

    destinations: list[BillingRuleDestination] | None
    name: str
    rule_value: float
    description: str | Unset = UNSET
    region_id: int | None | Unset = UNSET
    service_category_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.billing_rule_destination import BillingRuleDestination
        destinations: list[dict[str, Any]] | None
        if isinstance(self.destinations, list):
            destinations = []
            for destinations_type_0_item_data in self.destinations:
                destinations_type_0_item = destinations_type_0_item_data.to_dict()
                destinations.append(destinations_type_0_item)


        else:
            destinations = self.destinations

        name = self.name

        rule_value = self.rule_value

        description = self.description

        region_id: int | None | Unset
        if isinstance(self.region_id, Unset):
            region_id = UNSET
        else:
            region_id = self.region_id

        service_category_id: int | None | Unset
        if isinstance(self.service_category_id, Unset):
            service_category_id = UNSET
        else:
            service_category_id = self.service_category_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "destinations": destinations,
            "name": name,
            "rule_value": rule_value,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if region_id is not UNSET:
            field_dict["region_id"] = region_id
        if service_category_id is not UNSET:
            field_dict["service_category_id"] = service_category_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.billing_rule_destination import BillingRuleDestination
        d = dict(src_dict)
        def _parse_destinations(data: object) -> list[BillingRuleDestination] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                destinations_type_0 = []
                _destinations_type_0 = data
                for destinations_type_0_item_data in (_destinations_type_0):
                    destinations_type_0_item = BillingRuleDestination.from_dict(destinations_type_0_item_data)



                    destinations_type_0.append(destinations_type_0_item)

                return destinations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BillingRuleDestination] | None, data)

        destinations = _parse_destinations(d.pop("destinations"))


        name = d.pop("name")

        rule_value = d.pop("rule_value")

        description = d.pop("description", UNSET)

        def _parse_region_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        region_id = _parse_region_id(d.pop("region_id", UNSET))


        def _parse_service_category_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        service_category_id = _parse_service_category_id(d.pop("service_category_id", UNSET))


        custom_line_item_rule_definition = cls(
            destinations=destinations,
            name=name,
            rule_value=rule_value,
            description=description,
            region_id=region_id,
            service_category_id=service_category_id,
        )


        custom_line_item_rule_definition.additional_properties = d
        return custom_line_item_rule_definition

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
