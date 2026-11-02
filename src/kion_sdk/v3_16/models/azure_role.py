from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AzureRole")



@_attrs_define
class AzureRole:
    """ AzureRole defines an Azure Role.

        Attributes:
            azure_managed_policy (bool | None | Unset): True if the policy is created and managed by Azure
            car_restricted (bool | None | Unset): True if the policy has been restricted for use by a subset of
                Users/UGroups on a Cloud Access Role.
            description (str | Unset): Description for the Role Definition in the application and Azure. Example: Gives user
                read only access to all Azure services..
            enabled (bool | None | Unset): True if the role is applied to an account by cloud rules, cloud access roles, or
                other entities. Null if the value has not been set.
            id (int | Unset): ID of the record in the application. Example: 1.
            name (str | Unset): Name of the Role Definition in the application and in Azure. Example: Read Only.
            role_permissions (str | Unset): Text of the permissions section of the Azure Role Definition.
            system_managed_policy (bool | None | Unset): True if the policy comes packaged with cloudtamer.io
     """

    azure_managed_policy: bool | None | Unset = UNSET
    car_restricted: bool | None | Unset = UNSET
    description: str | Unset = UNSET
    enabled: bool | None | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    role_permissions: str | Unset = UNSET
    system_managed_policy: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        azure_managed_policy: bool | None | Unset
        if isinstance(self.azure_managed_policy, Unset):
            azure_managed_policy = UNSET
        else:
            azure_managed_policy = self.azure_managed_policy

        car_restricted: bool | None | Unset
        if isinstance(self.car_restricted, Unset):
            car_restricted = UNSET
        else:
            car_restricted = self.car_restricted

        description = self.description

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        id = self.id

        name = self.name

        role_permissions = self.role_permissions

        system_managed_policy: bool | None | Unset
        if isinstance(self.system_managed_policy, Unset):
            system_managed_policy = UNSET
        else:
            system_managed_policy = self.system_managed_policy


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if azure_managed_policy is not UNSET:
            field_dict["azure_managed_policy"] = azure_managed_policy
        if car_restricted is not UNSET:
            field_dict["car_restricted"] = car_restricted
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if role_permissions is not UNSET:
            field_dict["role_permissions"] = role_permissions
        if system_managed_policy is not UNSET:
            field_dict["system_managed_policy"] = system_managed_policy

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_azure_managed_policy(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        azure_managed_policy = _parse_azure_managed_policy(d.pop("azure_managed_policy", UNSET))


        def _parse_car_restricted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        car_restricted = _parse_car_restricted(d.pop("car_restricted", UNSET))


        description = d.pop("description", UNSET)

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))


        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        role_permissions = d.pop("role_permissions", UNSET)

        def _parse_system_managed_policy(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        system_managed_policy = _parse_system_managed_policy(d.pop("system_managed_policy", UNSET))


        azure_role = cls(
            azure_managed_policy=azure_managed_policy,
            car_restricted=car_restricted,
            description=description,
            enabled=enabled,
            id=id,
            name=name,
            role_permissions=role_permissions,
            system_managed_policy=system_managed_policy,
        )


        azure_role.additional_properties = d
        return azure_role

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
