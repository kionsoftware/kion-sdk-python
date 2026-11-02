from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_gcp_folders_list_response_200 import GetGCPFoldersListResponse200
from ...models.get_gcp_folders_list_response_400 import GetGCPFoldersListResponse400
from ...models.get_gcp_folders_list_response_401 import GetGCPFoldersListResponse401
from ...models.get_gcp_folders_list_response_403 import GetGCPFoldersListResponse403
from ...models.get_gcp_folders_list_response_500 import GetGCPFoldersListResponse500
from ...models.list_gcp_folders_request_body import ListGCPFoldersRequestBody
from typing import cast



def _get_kwargs(
    *,
    body: ListGCPFoldersRequestBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/gcp-resources/list-folders",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetGCPFoldersListResponse200 | GetGCPFoldersListResponse400 | GetGCPFoldersListResponse401 | GetGCPFoldersListResponse403 | GetGCPFoldersListResponse500 | None:
    if response.status_code == 200:
        response_200 = GetGCPFoldersListResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetGCPFoldersListResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetGCPFoldersListResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetGCPFoldersListResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GetGCPFoldersListResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetGCPFoldersListResponse200 | GetGCPFoldersListResponse400 | GetGCPFoldersListResponse401 | GetGCPFoldersListResponse403 | GetGCPFoldersListResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ListGCPFoldersRequestBody,

) -> Response[GetGCPFoldersListResponse200 | GetGCPFoldersListResponse400 | GetGCPFoldersListResponse401 | GetGCPFoldersListResponse403 | GetGCPFoldersListResponse500]:
    """ Returns a list of folders.

    Args:
        body (ListGCPFoldersRequestBody): ListGCPFoldersRequestBody is the body of a list folders
            call

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGCPFoldersListResponse200 | GetGCPFoldersListResponse400 | GetGCPFoldersListResponse401 | GetGCPFoldersListResponse403 | GetGCPFoldersListResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: ListGCPFoldersRequestBody,

) -> GetGCPFoldersListResponse200 | GetGCPFoldersListResponse400 | GetGCPFoldersListResponse401 | GetGCPFoldersListResponse403 | GetGCPFoldersListResponse500 | None:
    """ Returns a list of folders.

    Args:
        body (ListGCPFoldersRequestBody): ListGCPFoldersRequestBody is the body of a list folders
            call

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGCPFoldersListResponse200 | GetGCPFoldersListResponse400 | GetGCPFoldersListResponse401 | GetGCPFoldersListResponse403 | GetGCPFoldersListResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ListGCPFoldersRequestBody,

) -> Response[GetGCPFoldersListResponse200 | GetGCPFoldersListResponse400 | GetGCPFoldersListResponse401 | GetGCPFoldersListResponse403 | GetGCPFoldersListResponse500]:
    """ Returns a list of folders.

    Args:
        body (ListGCPFoldersRequestBody): ListGCPFoldersRequestBody is the body of a list folders
            call

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGCPFoldersListResponse200 | GetGCPFoldersListResponse400 | GetGCPFoldersListResponse401 | GetGCPFoldersListResponse403 | GetGCPFoldersListResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ListGCPFoldersRequestBody,

) -> GetGCPFoldersListResponse200 | GetGCPFoldersListResponse400 | GetGCPFoldersListResponse401 | GetGCPFoldersListResponse403 | GetGCPFoldersListResponse500 | None:
    """ Returns a list of folders.

    Args:
        body (ListGCPFoldersRequestBody): ListGCPFoldersRequestBody is the body of a list folders
            call

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGCPFoldersListResponse200 | GetGCPFoldersListResponse400 | GetGCPFoldersListResponse401 | GetGCPFoldersListResponse403 | GetGCPFoldersListResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
