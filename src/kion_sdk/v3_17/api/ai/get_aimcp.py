from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_aimcp_response_400 import GetAIMCPResponse400
from ...models.get_aimcp_response_401 import GetAIMCPResponse401
from ...models.get_aimcp_response_403 import GetAIMCPResponse403
from ...models.get_aimcp_response_404 import GetAIMCPResponse404
from ...models.get_aimcp_response_405 import GetAIMCPResponse405
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    accept: str,
    mcp_protocol_version: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Accept"] = accept

    if not isinstance(mcp_protocol_version, Unset):
        headers["MCP-Protocol-Version"] = mcp_protocol_version



    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/ai/mcp",
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetAIMCPResponse400 | GetAIMCPResponse401 | GetAIMCPResponse403 | GetAIMCPResponse404 | GetAIMCPResponse405 | None:
    if response.status_code == 400:
        response_400 = GetAIMCPResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetAIMCPResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetAIMCPResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetAIMCPResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 405:
        response_405 = GetAIMCPResponse405.from_dict(response.json())



        return response_405

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetAIMCPResponse400 | GetAIMCPResponse401 | GetAIMCPResponse403 | GetAIMCPResponse404 | GetAIMCPResponse405]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    accept: str,
    mcp_protocol_version: str | Unset = UNSET,

) -> Response[GetAIMCPResponse400 | GetAIMCPResponse401 | GetAIMCPResponse403 | GetAIMCPResponse404 | GetAIMCPResponse405]:
    """ Returns 405 because server-initiated SSE streams are not supported.

    Args:
        accept (str):
        mcp_protocol_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAIMCPResponse400 | GetAIMCPResponse401 | GetAIMCPResponse403 | GetAIMCPResponse404 | GetAIMCPResponse405]
     """


    kwargs = _get_kwargs(
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
    accept: str,
    mcp_protocol_version: str | Unset = UNSET,

) -> GetAIMCPResponse400 | GetAIMCPResponse401 | GetAIMCPResponse403 | GetAIMCPResponse404 | GetAIMCPResponse405 | None:
    """ Returns 405 because server-initiated SSE streams are not supported.

    Args:
        accept (str):
        mcp_protocol_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAIMCPResponse400 | GetAIMCPResponse401 | GetAIMCPResponse403 | GetAIMCPResponse404 | GetAIMCPResponse405
     """


    return sync_detailed(
        client=client,
accept=accept,
mcp_protocol_version=mcp_protocol_version,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    accept: str,
    mcp_protocol_version: str | Unset = UNSET,

) -> Response[GetAIMCPResponse400 | GetAIMCPResponse401 | GetAIMCPResponse403 | GetAIMCPResponse404 | GetAIMCPResponse405]:
    """ Returns 405 because server-initiated SSE streams are not supported.

    Args:
        accept (str):
        mcp_protocol_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAIMCPResponse400 | GetAIMCPResponse401 | GetAIMCPResponse403 | GetAIMCPResponse404 | GetAIMCPResponse405]
     """


    kwargs = _get_kwargs(
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
    accept: str,
    mcp_protocol_version: str | Unset = UNSET,

) -> GetAIMCPResponse400 | GetAIMCPResponse401 | GetAIMCPResponse403 | GetAIMCPResponse404 | GetAIMCPResponse405 | None:
    """ Returns 405 because server-initiated SSE streams are not supported.

    Args:
        accept (str):
        mcp_protocol_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAIMCPResponse400 | GetAIMCPResponse401 | GetAIMCPResponse403 | GetAIMCPResponse404 | GetAIMCPResponse405
     """


    return (await asyncio_detailed(
        client=client,
accept=accept,
mcp_protocol_version=mcp_protocol_version,

    )).parsed
