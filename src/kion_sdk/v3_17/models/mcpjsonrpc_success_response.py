from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="MCPJSONRPCSuccessResponse")



@_attrs_define
class MCPJSONRPCSuccessResponse:
    """ MCPJSONRPCSuccessResponse is a JSON-RPC 2.0 success response.

        Attributes:
            id (Any | Unset): Request id copied from the request. Example: 1.
            jsonrpc (str | Unset): JSON-RPC version. Example: 2.0.
            result (Any | Unset): Method result.
     """

    id: Any | Unset = UNSET
    jsonrpc: str | Unset = UNSET
    result: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        jsonrpc = self.jsonrpc

        result = self.result


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if jsonrpc is not UNSET:
            field_dict["jsonrpc"] = jsonrpc
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        jsonrpc = d.pop("jsonrpc", UNSET)

        result = d.pop("result", UNSET)

        mcpjsonrpc_success_response = cls(
            id=id,
            jsonrpc=jsonrpc,
            result=result,
        )


        mcpjsonrpc_success_response.additional_properties = d
        return mcpjsonrpc_success_response

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
