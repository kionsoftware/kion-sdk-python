from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ServiceCatalogPortfolioUpdate")



@_attrs_define
class ServiceCatalogPortfolioUpdate:
    """ ServiceCatalogPortfolioUpdate defines a Service Catalog portfolio update.

        Attributes:
            account_id (int | None | Unset): ID of account where the service catalog portfolio exists. Example: 1.
            description (str | Unset): Description for the service catalog portfolio in the application. Example: This
                portfolio allows for the creation of an ELK stack in AWS..
            name (str | Unset): Name of the service catalog portfolio in the application. Example: Create ELK Stack.
            portfolio_id (str | Unset): ID of the service catalog portfolio in AWS. Example: port-123456789.
            region (str | Unset): AWS region where the service catalog portfolio exists. Example: us-east-1.
            tag_option (bool | None | Unset): Boolean that enables or disables tag option sharing on service catalog
                portfolios. Example: True.
     """

    account_id: int | None | Unset = UNSET
    description: str | Unset = UNSET
    name: str | Unset = UNSET
    portfolio_id: str | Unset = UNSET
    region: str | Unset = UNSET
    tag_option: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_id: int | None | Unset
        if isinstance(self.account_id, Unset):
            account_id = UNSET
        else:
            account_id = self.account_id

        description = self.description

        name = self.name

        portfolio_id = self.portfolio_id

        region = self.region

        tag_option: bool | None | Unset
        if isinstance(self.tag_option, Unset):
            tag_option = UNSET
        else:
            tag_option = self.tag_option


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if portfolio_id is not UNSET:
            field_dict["portfolio_id"] = portfolio_id
        if region is not UNSET:
            field_dict["region"] = region
        if tag_option is not UNSET:
            field_dict["tag_option"] = tag_option

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_account_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        account_id = _parse_account_id(d.pop("account_id", UNSET))


        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        portfolio_id = d.pop("portfolio_id", UNSET)

        region = d.pop("region", UNSET)

        def _parse_tag_option(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        tag_option = _parse_tag_option(d.pop("tag_option", UNSET))


        service_catalog_portfolio_update = cls(
            account_id=account_id,
            description=description,
            name=name,
            portfolio_id=portfolio_id,
            region=region,
            tag_option=tag_option,
        )


        service_catalog_portfolio_update.additional_properties = d
        return service_catalog_portfolio_update

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
