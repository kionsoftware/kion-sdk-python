from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_permission_scheme_by_type_response_200 import GetPermissionSchemeByTypeResponse200
from ...models.get_permission_scheme_by_type_response_401 import GetPermissionSchemeByTypeResponse401
from ...models.get_permission_scheme_by_type_response_403 import GetPermissionSchemeByTypeResponse403
from ...models.get_permission_scheme_by_type_response_404 import GetPermissionSchemeByTypeResponse404
from ...models.get_permission_scheme_by_type_response_500 import GetPermissionSchemeByTypeResponse500
from typing import cast



def _get_kwargs(
    type_: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/permission-scheme/type/{type_}".format(type_=quote(str(type_), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetPermissionSchemeByTypeResponse200 | GetPermissionSchemeByTypeResponse401 | GetPermissionSchemeByTypeResponse403 | GetPermissionSchemeByTypeResponse404 | GetPermissionSchemeByTypeResponse500 | None:
    if response.status_code == 200:
        response_200 = GetPermissionSchemeByTypeResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetPermissionSchemeByTypeResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetPermissionSchemeByTypeResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetPermissionSchemeByTypeResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetPermissionSchemeByTypeResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetPermissionSchemeByTypeResponse200 | GetPermissionSchemeByTypeResponse401 | GetPermissionSchemeByTypeResponse403 | GetPermissionSchemeByTypeResponse404 | GetPermissionSchemeByTypeResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    type_: str,
    *,
    client: AuthenticatedClient,

) -> Response[GetPermissionSchemeByTypeResponse200 | GetPermissionSchemeByTypeResponse401 | GetPermissionSchemeByTypeResponse403 | GetPermissionSchemeByTypeResponse404 | GetPermissionSchemeByTypeResponse500]:
    """ Returns a list of permission schemes by type from the application.

    Args:
        type_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPermissionSchemeByTypeResponse200 | GetPermissionSchemeByTypeResponse401 | GetPermissionSchemeByTypeResponse403 | GetPermissionSchemeByTypeResponse404 | GetPermissionSchemeByTypeResponse500]
     """


    kwargs = _get_kwargs(
        type_=type_,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    type_: str,
    *,
    client: AuthenticatedClient,

) -> GetPermissionSchemeByTypeResponse200 | GetPermissionSchemeByTypeResponse401 | GetPermissionSchemeByTypeResponse403 | GetPermissionSchemeByTypeResponse404 | GetPermissionSchemeByTypeResponse500 | None:
    """ Returns a list of permission schemes by type from the application.

    Args:
        type_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPermissionSchemeByTypeResponse200 | GetPermissionSchemeByTypeResponse401 | GetPermissionSchemeByTypeResponse403 | GetPermissionSchemeByTypeResponse404 | GetPermissionSchemeByTypeResponse500
     """


    return sync_detailed(
        type_=type_,
client=client,

    ).parsed

async def asyncio_detailed(
    type_: str,
    *,
    client: AuthenticatedClient,

) -> Response[GetPermissionSchemeByTypeResponse200 | GetPermissionSchemeByTypeResponse401 | GetPermissionSchemeByTypeResponse403 | GetPermissionSchemeByTypeResponse404 | GetPermissionSchemeByTypeResponse500]:
    """ Returns a list of permission schemes by type from the application.

    Args:
        type_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPermissionSchemeByTypeResponse200 | GetPermissionSchemeByTypeResponse401 | GetPermissionSchemeByTypeResponse403 | GetPermissionSchemeByTypeResponse404 | GetPermissionSchemeByTypeResponse500]
     """


    kwargs = _get_kwargs(
        type_=type_,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    type_: str,
    *,
    client: AuthenticatedClient,

) -> GetPermissionSchemeByTypeResponse200 | GetPermissionSchemeByTypeResponse401 | GetPermissionSchemeByTypeResponse403 | GetPermissionSchemeByTypeResponse404 | GetPermissionSchemeByTypeResponse500 | None:
    """ Returns a list of permission schemes by type from the application.

    Args:
        type_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPermissionSchemeByTypeResponse200 | GetPermissionSchemeByTypeResponse401 | GetPermissionSchemeByTypeResponse403 | GetPermissionSchemeByTypeResponse404 | GetPermissionSchemeByTypeResponse500
     """


    return (await asyncio_detailed(
        type_=type_,
client=client,

    )).parsed
