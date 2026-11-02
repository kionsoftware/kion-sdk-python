from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mcpjsonrpc_error_response import MCPJSONRPCErrorResponse
from ...models.mcpjsonrpc_request import MCPJSONRPCRequest
from ...models.mcpjsonrpc_success_response import MCPJSONRPCSuccessResponse
from ...models.post_aimcp_response_202 import PostAIMCPResponse202
from ...models.post_aimcp_response_401 import PostAIMCPResponse401
from ...models.post_aimcp_response_403 import PostAIMCPResponse403
from ...models.post_aimcp_response_404 import PostAIMCPResponse404
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: MCPJSONRPCRequest,
    accept: str,
    mcp_protocol_version: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Accept"] = accept

    if not isinstance(mcp_protocol_version, Unset):
        headers["MCP-Protocol-Version"] = mcp_protocol_version



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/ai/mcp",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MCPJSONRPCErrorResponse | MCPJSONRPCSuccessResponse | PostAIMCPResponse202 | PostAIMCPResponse401 | PostAIMCPResponse403 | PostAIMCPResponse404 | None:
    if response.status_code == 200:
        response_200 = MCPJSONRPCSuccessResponse.from_dict(response.json())



        return response_200

    if response.status_code == 202:
        response_202 = PostAIMCPResponse202.from_dict(response.json())



        return response_202

    if response.status_code == 400:
        response_400 = MCPJSONRPCErrorResponse.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostAIMCPResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostAIMCPResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PostAIMCPResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = MCPJSONRPCErrorResponse.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MCPJSONRPCErrorResponse | MCPJSONRPCSuccessResponse | PostAIMCPResponse202 | PostAIMCPResponse401 | PostAIMCPResponse403 | PostAIMCPResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: MCPJSONRPCRequest,
    accept: str,
    mcp_protocol_version: str | Unset = UNSET,

) -> Response[MCPJSONRPCErrorResponse | MCPJSONRPCSuccessResponse | PostAIMCPResponse202 | PostAIMCPResponse401 | PostAIMCPResponse403 | PostAIMCPResponse404]:
    """ Handles MCP 2025-06-18 Streamable HTTP JSON-RPC messages. The endpoint is stateless and supports
    initialize, ping, tools/list, and tools/call.

    Args:
        accept (str):
        mcp_protocol_version (str | Unset):
        body (MCPJSONRPCRequest): MCPJSONRPCRequest is a JSON-RPC 2.0 message accepted by the
            public MCP endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MCPJSONRPCErrorResponse | MCPJSONRPCSuccessResponse | PostAIMCPResponse202 | PostAIMCPResponse401 | PostAIMCPResponse403 | PostAIMCPResponse404]
     """


    kwargs = _get_kwargs(
        body=body,
accept=accept,
mcp_protocol_version=mcp_protocol_version,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: MCPJSONRPCRequest,
    accept: str,
    mcp_protocol_version: str | Unset = UNSET,

) -> MCPJSONRPCErrorResponse | MCPJSONRPCSuccessResponse | PostAIMCPResponse202 | PostAIMCPResponse401 | PostAIMCPResponse403 | PostAIMCPResponse404 | None:
    """ Handles MCP 2025-06-18 Streamable HTTP JSON-RPC messages. The endpoint is stateless and supports
    initialize, ping, tools/list, and tools/call.

    Args:
        accept (str):
        mcp_protocol_version (str | Unset):
        body (MCPJSONRPCRequest): MCPJSONRPCRequest is a JSON-RPC 2.0 message accepted by the
            public MCP endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MCPJSONRPCErrorResponse | MCPJSONRPCSuccessResponse | PostAIMCPResponse202 | PostAIMCPResponse401 | PostAIMCPResponse403 | PostAIMCPResponse404
     """


    return sync_detailed(
        client=client,
body=body,
accept=accept,
mcp_protocol_version=mcp_protocol_version,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: MCPJSONRPCRequest,
    accept: str,
    mcp_protocol_version: str | Unset = UNSET,

) -> Response[MCPJSONRPCErrorResponse | MCPJSONRPCSuccessResponse | PostAIMCPResponse202 | PostAIMCPResponse401 | PostAIMCPResponse403 | PostAIMCPResponse404]:
    """ Handles MCP 2025-06-18 Streamable HTTP JSON-RPC messages. The endpoint is stateless and supports
    initialize, ping, tools/list, and tools/call.

    Args:
        accept (str):
        mcp_protocol_version (str | Unset):
        body (MCPJSONRPCRequest): MCPJSONRPCRequest is a JSON-RPC 2.0 message accepted by the
            public MCP endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MCPJSONRPCErrorResponse | MCPJSONRPCSuccessResponse | PostAIMCPResponse202 | PostAIMCPResponse401 | PostAIMCPResponse403 | PostAIMCPResponse404]
     """


    kwargs = _get_kwargs(
        body=body,
accept=accept,
mcp_protocol_version=mcp_protocol_version,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: MCPJSONRPCRequest,
    accept: str,
    mcp_protocol_version: str | Unset = UNSET,

) -> MCPJSONRPCErrorResponse | MCPJSONRPCSuccessResponse | PostAIMCPResponse202 | PostAIMCPResponse401 | PostAIMCPResponse403 | PostAIMCPResponse404 | None:
    """ Handles MCP 2025-06-18 Streamable HTTP JSON-RPC messages. The endpoint is stateless and supports
    initialize, ping, tools/list, and tools/call.

    Args:
        accept (str):
        mcp_protocol_version (str | Unset):
        body (MCPJSONRPCRequest): MCPJSONRPCRequest is a JSON-RPC 2.0 message accepted by the
            public MCP endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MCPJSONRPCErrorResponse | MCPJSONRPCSuccessResponse | PostAIMCPResponse202 | PostAIMCPResponse401 | PostAIMCPResponse403 | PostAIMCPResponse404
     """


    return (await asyncio_detailed(
        client=client,
body=body,
accept=accept,
mcp_protocol_version=mcp_protocol_version,

    )).parsed
