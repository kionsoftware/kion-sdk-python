from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OCIBillingSource")



@_attrs_define
class OCIBillingSource:
    """ OCIBillingSource defines a billing source used for testing and creation.

        Attributes:
            account_type_id (int | None | Unset): The Account Type ID is the corresponding billing source account's type.
                26 - OCI Commercial
                27 - OCI Government
                28 - OCI Federal Example: 26.
            billing_start_date (str | Unset): Start date of billing source (YYYY-MM). Example: 2019-01.
            fingerprint (str | Unset): The api access fingerprint Example: ocid1.fingerprint.oc1..example.
            id (int | Unset): ID of the billing source. Example: 254.
            is_parent_tenancy (bool | None | Unset): Indicates whether the billing source is a parent OCI tenancy. Example:
                True.
            name (str | Unset): Name of the billing source. Example: My Master Payer.
            private_key (str | Unset): The private key used for API Access Example: ocid1.privatekey.oc1..example.
            region (str | Unset): The OCI default api region Example: ocid1.region.oc1..example.
            tenancy_ocid (str | Unset): The OCID of the tenancy Example: ocid1.tenancy.oc1..example.
            user_ocid (str | Unset): The OCID of the api user Example: ocid1.user.oc1..example.
     """

    account_type_id: int | None | Unset = UNSET
    billing_start_date: str | Unset = UNSET
    fingerprint: str | Unset = UNSET
    id: int | Unset = UNSET
    is_parent_tenancy: bool | None | Unset = UNSET
    name: str | Unset = UNSET
    private_key: str | Unset = UNSET
    region: str | Unset = UNSET
    tenancy_ocid: str | Unset = UNSET
    user_ocid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_type_id: int | None | Unset
        if isinstance(self.account_type_id, Unset):
            account_type_id = UNSET
        else:
            account_type_id = self.account_type_id

        billing_start_date = self.billing_start_date

        fingerprint = self.fingerprint

        id = self.id

        is_parent_tenancy: bool | None | Unset
        if isinstance(self.is_parent_tenancy, Unset):
            is_parent_tenancy = UNSET
        else:
            is_parent_tenancy = self.is_parent_tenancy

        name = self.name

        private_key = self.private_key

        region = self.region

        tenancy_ocid = self.tenancy_ocid

        user_ocid = self.user_ocid


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_type_id is not UNSET:
            field_dict["account_type_id"] = account_type_id
        if billing_start_date is not UNSET:
            field_dict["billing_start_date"] = billing_start_date
        if fingerprint is not UNSET:
            field_dict["fingerprint"] = fingerprint
        if id is not UNSET:
            field_dict["id"] = id
        if is_parent_tenancy is not UNSET:
            field_dict["is_parent_tenancy"] = is_parent_tenancy
        if name is not UNSET:
            field_dict["name"] = name
        if private_key is not UNSET:
            field_dict["private_key"] = private_key
        if region is not UNSET:
            field_dict["region"] = region
        if tenancy_ocid is not UNSET:
            field_dict["tenancy_ocid"] = tenancy_ocid
        if user_ocid is not UNSET:
            field_dict["user_ocid"] = user_ocid

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_account_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        account_type_id = _parse_account_type_id(d.pop("account_type_id", UNSET))


        billing_start_date = d.pop("billing_start_date", UNSET)

        fingerprint = d.pop("fingerprint", UNSET)

        id = d.pop("id", UNSET)

        def _parse_is_parent_tenancy(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_parent_tenancy = _parse_is_parent_tenancy(d.pop("is_parent_tenancy", UNSET))


        name = d.pop("name", UNSET)

        private_key = d.pop("private_key", UNSET)

        region = d.pop("region", UNSET)

        tenancy_ocid = d.pop("tenancy_ocid", UNSET)

        user_ocid = d.pop("user_ocid", UNSET)

        oci_billing_source = cls(
            account_type_id=account_type_id,
            billing_start_date=billing_start_date,
            fingerprint=fingerprint,
            id=id,
            is_parent_tenancy=is_parent_tenancy,
            name=name,
            private_key=private_key,
            region=region,
            tenancy_ocid=tenancy_ocid,
            user_ocid=user_ocid,
        )


        oci_billing_source.additional_properties = d
        return oci_billing_source

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
