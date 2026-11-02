from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="BillingSourceGovcloud")



@_attrs_define
class BillingSourceGovcloud:
    """ BillingSourceGovcloud defines an account.

        Attributes:
            account_creation_enabled (bool | None | Unset): Setting for whether account creation in govcloud is enabled or
                not in this billing source.
            aws_account_number (str | Unset): AWS account number. Example: 121212121212.
            car_external_id (str | Unset): The external ID used when assuming the cloud access role for this billing source.
                Example: CAR-9849055.
            id (int | Unset): ID of the record in the application. Example: 1.
            name (str | Unset): Name of the payer in the application. Example: GC Billing Account.
            payer_id (int | None | Unset): The ID of the Payer that this govcloud info is attached to. Example: 1.
            service_external_id (str | Unset): The external ID used for automated internal actions using the service role
                for this billing source. Example: Service-3764894.
     """

    account_creation_enabled: bool | None | Unset = UNSET
    aws_account_number: str | Unset = UNSET
    car_external_id: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    payer_id: int | None | Unset = UNSET
    service_external_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_creation_enabled: bool | None | Unset
        if isinstance(self.account_creation_enabled, Unset):
            account_creation_enabled = UNSET
        else:
            account_creation_enabled = self.account_creation_enabled

        aws_account_number = self.aws_account_number

        car_external_id = self.car_external_id

        id = self.id

        name = self.name

        payer_id: int | None | Unset
        if isinstance(self.payer_id, Unset):
            payer_id = UNSET
        else:
            payer_id = self.payer_id

        service_external_id = self.service_external_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_creation_enabled is not UNSET:
            field_dict["account_creation_enabled"] = account_creation_enabled
        if aws_account_number is not UNSET:
            field_dict["aws_account_number"] = aws_account_number
        if car_external_id is not UNSET:
            field_dict["car_external_id"] = car_external_id
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if payer_id is not UNSET:
            field_dict["payer_id"] = payer_id
        if service_external_id is not UNSET:
            field_dict["service_external_id"] = service_external_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_account_creation_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        account_creation_enabled = _parse_account_creation_enabled(d.pop("account_creation_enabled", UNSET))


        aws_account_number = d.pop("aws_account_number", UNSET)

        car_external_id = d.pop("car_external_id", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        def _parse_payer_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        payer_id = _parse_payer_id(d.pop("payer_id", UNSET))


        service_external_id = d.pop("service_external_id", UNSET)

        billing_source_govcloud = cls(
            account_creation_enabled=account_creation_enabled,
            aws_account_number=aws_account_number,
            car_external_id=car_external_id,
            id=id,
            name=name,
            payer_id=payer_id,
            service_external_id=service_external_id,
        )


        billing_source_govcloud.additional_properties = d
        return billing_source_govcloud

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
