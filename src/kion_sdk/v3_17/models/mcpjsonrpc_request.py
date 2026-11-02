from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="MCPJSONRPCRequest")



@_attrs_define
class MCPJSONRPCRequest:
    """ MCPJSONRPCRequest is a JSON-RPC 2.0 message accepted by the public MCP endpoint.

        Attributes:
            id (Any | Unset): Request id. Omit this field for notifications. Example: 1.
            jsonrpc (str | Unset): JSON-RPC version. Must be "2.0". Example: 2.0.
            method (str | Unset): MCP method name. Example: tools/list.
            params (Any | Unset): MCP method params.
     """

    id: Any | Unset = UNSET
    jsonrpc: str | Unset = UNSET
    method: str | Unset = UNSET
    params: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        jsonrpc = self.jsonrpc

        method = self.method

        params = self.params


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if jsonrpc is not UNSET:
            field_dict["jsonrpc"] = jsonrpc
        if method is not UNSET:
            field_dict["method"] = method
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        jsonrpc = d.pop("jsonrpc", UNSET)

        method = d.pop("method", UNSET)

        params = d.pop("params", UNSET)

        mcpjsonrpc_request = cls(
            id=id,
            jsonrpc=jsonrpc,
            method=method,
            params=params,
        )


        mcpjsonrpc_request.additional_properties = d
        return mcpjsonrpc_request

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
