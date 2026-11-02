from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mcpjsonrpc_error_object import MCPJSONRPCErrorObject





T = TypeVar("T", bound="MCPJSONRPCErrorResponse")



@_attrs_define
class MCPJSONRPCErrorResponse:
    """ MCPJSONRPCErrorResponse is a JSON-RPC 2.0 error response.

        Attributes:
            error (MCPJSONRPCErrorObject | Unset): MCPJSONRPCErrorObject is a JSON-RPC 2.0 error object.
            id (Any | Unset): Request id copied from the request, omitted when the error answers no
                identifiable request such as a malformed body or rejected header: MCP
                types this as a string or number and forbids null.

                omitzero, not omitempty: both drop a nil id, but omitempty would also drop
                the legal ids "" and 0, which a response must echo.
            jsonrpc (str | Unset): JSON-RPC version. Example: 2.0.
     """

    error: MCPJSONRPCErrorObject | Unset = UNSET
    id: Any | Unset = UNSET
    jsonrpc: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.mcpjsonrpc_error_object import MCPJSONRPCErrorObject
        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        id = self.id

        jsonrpc = self.jsonrpc


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if error is not UNSET:
            field_dict["error"] = error
        if id is not UNSET:
            field_dict["id"] = id
        if jsonrpc is not UNSET:
            field_dict["jsonrpc"] = jsonrpc

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mcpjsonrpc_error_object import MCPJSONRPCErrorObject
        d = dict(src_dict)
        _error = d.pop("error", UNSET)
        error: MCPJSONRPCErrorObject | Unset
        if isinstance(_error,  Unset):
            error = UNSET
        else:
            error = MCPJSONRPCErrorObject.from_dict(_error)




        id = d.pop("id", UNSET)

        jsonrpc = d.pop("jsonrpc", UNSET)

        mcpjsonrpc_error_response = cls(
            error=error,
            id=id,
            jsonrpc=jsonrpc,
        )


        mcpjsonrpc_error_response.additional_properties = d
        return mcpjsonrpc_error_response

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
