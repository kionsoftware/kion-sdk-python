from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.service_catalog_portfolio import ServiceCatalogPortfolio
  from ..models.u_group import UGroup
  from ..models.user import User





T = TypeVar("T", bound="ServiceCatalogPortfolioWithOwners")



@_attrs_define
class ServiceCatalogPortfolioWithOwners:
    """ ServiceCatalogPortfolioWithOwners defines a service catalog portfolio with owners.

        Attributes:
            owner_user_groups (list[UGroup] | None | Unset):
            owner_users (list[User] | None | Unset):
            service_catalog_portfolio (ServiceCatalogPortfolio | Unset): ServiceCatalogPortfolio defines a Service Catalog
                portfolio.
     """

    owner_user_groups: list[UGroup] | None | Unset = UNSET
    owner_users: list[User] | None | Unset = UNSET
    service_catalog_portfolio: ServiceCatalogPortfolio | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.service_catalog_portfolio import ServiceCatalogPortfolio
        from ..models.u_group import UGroup
        from ..models.user import User
        owner_user_groups: list[dict[str, Any]] | None | Unset
        if isinstance(self.owner_user_groups, Unset):
            owner_user_groups = UNSET
        elif isinstance(self.owner_user_groups, list):
            owner_user_groups = []
            for owner_user_groups_type_0_item_data in self.owner_user_groups:
                owner_user_groups_type_0_item = owner_user_groups_type_0_item_data.to_dict()
                owner_user_groups.append(owner_user_groups_type_0_item)


        else:
            owner_user_groups = self.owner_user_groups

        owner_users: list[dict[str, Any]] | None | Unset
        if isinstance(self.owner_users, Unset):
            owner_users = UNSET
        elif isinstance(self.owner_users, list):
            owner_users = []
            for owner_users_type_0_item_data in self.owner_users:
                owner_users_type_0_item = owner_users_type_0_item_data.to_dict()
                owner_users.append(owner_users_type_0_item)


        else:
            owner_users = self.owner_users

        service_catalog_portfolio: dict[str, Any] | Unset = UNSET
        if not isinstance(self.service_catalog_portfolio, Unset):
            service_catalog_portfolio = self.service_catalog_portfolio.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if owner_user_groups is not UNSET:
            field_dict["owner_user_groups"] = owner_user_groups
        if owner_users is not UNSET:
            field_dict["owner_users"] = owner_users
        if service_catalog_portfolio is not UNSET:
            field_dict["service_catalog_portfolio"] = service_catalog_portfolio

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_catalog_portfolio import ServiceCatalogPortfolio
        from ..models.u_group import UGroup
        from ..models.user import User
        d = dict(src_dict)
        def _parse_owner_user_groups(data: object) -> list[UGroup] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_user_groups_type_0 = []
                _owner_user_groups_type_0 = data
                for owner_user_groups_type_0_item_data in (_owner_user_groups_type_0):
                    owner_user_groups_type_0_item = UGroup.from_dict(owner_user_groups_type_0_item_data)



                    owner_user_groups_type_0.append(owner_user_groups_type_0_item)

                return owner_user_groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UGroup] | None | Unset, data)

        owner_user_groups = _parse_owner_user_groups(d.pop("owner_user_groups", UNSET))


        def _parse_owner_users(data: object) -> list[User] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_users_type_0 = []
                _owner_users_type_0 = data
                for owner_users_type_0_item_data in (_owner_users_type_0):
                    owner_users_type_0_item = User.from_dict(owner_users_type_0_item_data)



                    owner_users_type_0.append(owner_users_type_0_item)

                return owner_users_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[User] | None | Unset, data)

        owner_users = _parse_owner_users(d.pop("owner_users", UNSET))


        _service_catalog_portfolio = d.pop("service_catalog_portfolio", UNSET)
        service_catalog_portfolio: ServiceCatalogPortfolio | Unset
        if isinstance(_service_catalog_portfolio,  Unset):
            service_catalog_portfolio = UNSET
        else:
            service_catalog_portfolio = ServiceCatalogPortfolio.from_dict(_service_catalog_portfolio)




        service_catalog_portfolio_with_owners = cls(
            owner_user_groups=owner_user_groups,
            owner_users=owner_users,
            service_catalog_portfolio=service_catalog_portfolio,
        )


        service_catalog_portfolio_with_owners.additional_properties = d
        return service_catalog_portfolio_with_owners

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
