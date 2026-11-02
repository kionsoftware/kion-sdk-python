from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ServiceCatalogPortfolioCreate")



@_attrs_define
class ServiceCatalogPortfolioCreate:
    """ ServiceCatalogPortfolioCreate defines a Service Catalog portfolio creation.

        Attributes:
            account_id (int | None): ID of account where the service catalog portfolio exists. Example: 1.
            name (str): Name of the service catalog portfolio in the application. Example: Create ELK Stack.
            portfolio_id (str): ID of the service catalog portfolio in AWS. Example: port-123456789.
            region (str): AWS region where the service catalog portfolio exists. Example: us-east-1.
            description (str | Unset): Description for the service catalog portfolio in the application. Example: This
                portfolio allows for the creation of an ELK stack in AWS..
            owner_user_group_ids (list[int] | None | Unset): List of groups IDs who will own the portfolio. Is required if
                no owner user IDs are listed. Example: [1, 2].
            owner_user_ids (list[int] | None | Unset): List of user IDs who will own the portfolio. Is required if no owner
                group IDs are listed. Example: [1, 2].
            tag_option (bool | None | Unset): Boolean that enables or disables tag option sharing on service catalog
                portfolios. Example: True.
     """

    account_id: int | None
    name: str
    portfolio_id: str
    region: str
    description: str | Unset = UNSET
    owner_user_group_ids: list[int] | None | Unset = UNSET
    owner_user_ids: list[int] | None | Unset = UNSET
    tag_option: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_id: int | None
        account_id = self.account_id

        name = self.name

        portfolio_id = self.portfolio_id

        region = self.region

        description = self.description

        owner_user_group_ids: list[int] | None | Unset
        if isinstance(self.owner_user_group_ids, Unset):
            owner_user_group_ids = UNSET
        elif isinstance(self.owner_user_group_ids, list):
            owner_user_group_ids = self.owner_user_group_ids


        else:
            owner_user_group_ids = self.owner_user_group_ids

        owner_user_ids: list[int] | None | Unset
        if isinstance(self.owner_user_ids, Unset):
            owner_user_ids = UNSET
        elif isinstance(self.owner_user_ids, list):
            owner_user_ids = self.owner_user_ids


        else:
            owner_user_ids = self.owner_user_ids

        tag_option: bool | None | Unset
        if isinstance(self.tag_option, Unset):
            tag_option = UNSET
        else:
            tag_option = self.tag_option


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "account_id": account_id,
            "name": name,
            "portfolio_id": portfolio_id,
            "region": region,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if owner_user_group_ids is not UNSET:
            field_dict["owner_user_group_ids"] = owner_user_group_ids
        if owner_user_ids is not UNSET:
            field_dict["owner_user_ids"] = owner_user_ids
        if tag_option is not UNSET:
            field_dict["tag_option"] = tag_option

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_account_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        account_id = _parse_account_id(d.pop("account_id"))


        name = d.pop("name")

        portfolio_id = d.pop("portfolio_id")

        region = d.pop("region")

        description = d.pop("description", UNSET)

        def _parse_owner_user_group_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_user_group_ids_type_0 = cast(list[int], data)

                return owner_user_group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        owner_user_group_ids = _parse_owner_user_group_ids(d.pop("owner_user_group_ids", UNSET))


        def _parse_owner_user_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_user_ids_type_0 = cast(list[int], data)

                return owner_user_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        owner_user_ids = _parse_owner_user_ids(d.pop("owner_user_ids", UNSET))


        def _parse_tag_option(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        tag_option = _parse_tag_option(d.pop("tag_option", UNSET))


        service_catalog_portfolio_create = cls(
            account_id=account_id,
            name=name,
            portfolio_id=portfolio_id,
            region=region,
            description=description,
            owner_user_group_ids=owner_user_group_ids,
            owner_user_ids=owner_user_ids,
            tag_option=tag_option,
        )


        service_catalog_portfolio_create.additional_properties = d
        return service_catalog_portfolio_create

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
