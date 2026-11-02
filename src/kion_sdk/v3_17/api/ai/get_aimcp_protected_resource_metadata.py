from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_aimcp_protected_resource_metadata_response_404 import GetAIMCPProtectedResourceMetadataResponse404
from ...models.mcp_protected_resource_metadata import MCPProtectedResourceMetadata
from typing import cast



def _get_kwargs(
    base: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/.well-known/oauth-protected-resource/{base}/v3/ai/mcp".format(base=quote(str(base), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetAIMCPProtectedResourceMetadataResponse404 | MCPProtectedResourceMetadata | None:
    if response.status_code == 200:
        response_200 = MCPProtectedResourceMetadata.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = GetAIMCPProtectedResourceMetadataResponse404.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetAIMCPProtectedResourceMetadataResponse404 | MCPProtectedResourceMetadata]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    base: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[GetAIMCPProtectedResourceMetadataResponse404 | MCPProtectedResourceMetadata]:
    """ Returns OAuth protected resource metadata for the public MCP endpoint.

    Args:
        base (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAIMCPProtectedResourceMetadataResponse404 | MCPProtectedResourceMetadata]
     """


    kwargs = _get_kwargs(
        base=base,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    base: str,
    *,
    client: AuthenticatedClient | Client,

) -> GetAIMCPProtectedResourceMetadataResponse404 | MCPProtectedResourceMetadata | None:
    """ Returns OAuth protected resource metadata for the public MCP endpoint.

    Args:
        base (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAIMCPProtectedResourceMetadataResponse404 | MCPProtectedResourceMetadata
     """


    return sync_detailed(
        base=base,
client=client,

    ).parsed

async def asyncio_detailed(
    base: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[GetAIMCPProtectedResourceMetadataResponse404 | MCPProtectedResourceMetadata]:
    """ Returns OAuth protected resource metadata for the public MCP endpoint.

    Args:
        base (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAIMCPProtectedResourceMetadataResponse404 | MCPProtectedResourceMetadata]
     """


    kwargs = _get_kwargs(
        base=base,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    base: str,
    *,
    client: AuthenticatedClient | Client,

) -> GetAIMCPProtectedResourceMetadataResponse404 | MCPProtectedResourceMetadata | None:
    """ Returns OAuth protected resource metadata for the public MCP endpoint.

    Args:
        base (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAIMCPProtectedResourceMetadataResponse404 | MCPProtectedResourceMetadata
     """


    return (await asyncio_detailed(
        base=base,
client=client,

    )).parsed
