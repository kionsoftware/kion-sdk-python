from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.billing_rule_destination_response import BillingRuleDestinationResponse





T = TypeVar("T", bound="CustomLineItemRuleDefinitionResponse")



@_attrs_define
class CustomLineItemRuleDefinitionResponse:
    """ 
        Attributes:
            description (str | Unset):
            destinations (list[BillingRuleDestinationResponse] | None | Unset):
            name (str | Unset):
            region_id (int | None | Unset):
            rule_value (float | Unset):
            service_category_id (int | None | Unset):
     """

    description: str | Unset = UNSET
    destinations: list[BillingRuleDestinationResponse] | None | Unset = UNSET
    name: str | Unset = UNSET
    region_id: int | None | Unset = UNSET
    rule_value: float | Unset = UNSET
    service_category_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.billing_rule_destination_response import BillingRuleDestinationResponse
        description = self.description

        destinations: list[dict[str, Any]] | None | Unset
        if isinstance(self.destinations, Unset):
            destinations = UNSET
        elif isinstance(self.destinations, list):
            destinations = []
            for destinations_type_0_item_data in self.destinations:
                destinations_type_0_item = destinations_type_0_item_data.to_dict()
                destinations.append(destinations_type_0_item)


        else:
            destinations = self.destinations

        name = self.name

        region_id: int | None | Unset
        if isinstance(self.region_id, Unset):
            region_id = UNSET
        else:
            region_id = self.region_id

        rule_value = self.rule_value

        service_category_id: int | None | Unset
        if isinstance(self.service_category_id, Unset):
            service_category_id = UNSET
        else:
            service_category_id = self.service_category_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if destinations is not UNSET:
            field_dict["destinations"] = destinations
        if name is not UNSET:
            field_dict["name"] = name
        if region_id is not UNSET:
            field_dict["region_id"] = region_id
        if rule_value is not UNSET:
            field_dict["rule_value"] = rule_value
        if service_category_id is not UNSET:
            field_dict["service_category_id"] = service_category_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.billing_rule_destination_response import BillingRuleDestinationResponse
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        def _parse_destinations(data: object) -> list[BillingRuleDestinationResponse] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                destinations_type_0 = []
                _destinations_type_0 = data
                for destinations_type_0_item_data in (_destinations_type_0):
                    destinations_type_0_item = BillingRuleDestinationResponse.from_dict(destinations_type_0_item_data)



                    destinations_type_0.append(destinations_type_0_item)

                return destinations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BillingRuleDestinationResponse] | None | Unset, data)

        destinations = _parse_destinations(d.pop("destinations", UNSET))


        name = d.pop("name", UNSET)

        def _parse_region_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        region_id = _parse_region_id(d.pop("region_id", UNSET))


        rule_value = d.pop("rule_value", UNSET)

        def _parse_service_category_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        service_category_id = _parse_service_category_id(d.pop("service_category_id", UNSET))


        custom_line_item_rule_definition_response = cls(
            description=description,
            destinations=destinations,
            name=name,
            region_id=region_id,
            rule_value=rule_value,
            service_category_id=service_category_id,
        )


        custom_line_item_rule_definition_response.additional_properties = d
        return custom_line_item_rule_definition_response

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
