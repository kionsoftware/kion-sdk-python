from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GCPRoleTestResult")



@_attrs_define
class GCPRoleTestResult:
    """ GCPRoleTestResult Erroneous data returned from Google testApiPermissions endpoint

        Attributes:
            test_passed (bool | None): Whether or not the permissions can be applied to the resource Example: True.
            invalid_permissions (list[str] | None | Unset): List of invalid permissions upon test results Example:
                ['resourcemanager.projects.get', 'resourcemanager.projects.list'].
            valid_permissions (list[str] | None | Unset): List of valid permissions, with invalid permissions removed
                Example: for ["iam.role.get", "resourcemanager.projects.list"] where resource manager permissions are invalid,
                ["iam.role.get"].
     """

    test_passed: bool | None
    invalid_permissions: list[str] | None | Unset = UNSET
    valid_permissions: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        test_passed: bool | None
        test_passed = self.test_passed

        invalid_permissions: list[str] | None | Unset
        if isinstance(self.invalid_permissions, Unset):
            invalid_permissions = UNSET
        elif isinstance(self.invalid_permissions, list):
            invalid_permissions = self.invalid_permissions


        else:
            invalid_permissions = self.invalid_permissions

        valid_permissions: list[str] | None | Unset
        if isinstance(self.valid_permissions, Unset):
            valid_permissions = UNSET
        elif isinstance(self.valid_permissions, list):
            valid_permissions = self.valid_permissions


        else:
            valid_permissions = self.valid_permissions


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "test_passed": test_passed,
        })
        if invalid_permissions is not UNSET:
            field_dict["invalid_permissions"] = invalid_permissions
        if valid_permissions is not UNSET:
            field_dict["valid_permissions"] = valid_permissions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_test_passed(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        test_passed = _parse_test_passed(d.pop("test_passed"))


        def _parse_invalid_permissions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                invalid_permissions_type_0 = cast(list[str], data)

                return invalid_permissions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        invalid_permissions = _parse_invalid_permissions(d.pop("invalid_permissions", UNSET))


        def _parse_valid_permissions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                valid_permissions_type_0 = cast(list[str], data)

                return valid_permissions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        valid_permissions = _parse_valid_permissions(d.pop("valid_permissions", UNSET))


        gcp_role_test_result = cls(
            test_passed=test_passed,
            invalid_permissions=invalid_permissions,
            valid_permissions=valid_permissions,
        )


        gcp_role_test_result.additional_properties = d
        return gcp_role_test_result

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
