from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.app_api_key_name import AppAPIKeyName
from ...models.patch_app_api_key_response_200 import PatchAppAPIKeyResponse200
from ...models.patch_app_api_key_response_400 import PatchAppAPIKeyResponse400
from ...models.patch_app_api_key_response_401 import PatchAppAPIKeyResponse401
from ...models.patch_app_api_key_response_403 import PatchAppAPIKeyResponse403
from ...models.patch_app_api_key_response_404 import PatchAppAPIKeyResponse404
from ...models.patch_app_api_key_response_422 import PatchAppAPIKeyResponse422
from ...models.patch_app_api_key_response_500 import PatchAppAPIKeyResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: AppAPIKeyName | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v3/app-api-key/{id}".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchAppAPIKeyResponse200 | PatchAppAPIKeyResponse400 | PatchAppAPIKeyResponse401 | PatchAppAPIKeyResponse403 | PatchAppAPIKeyResponse404 | PatchAppAPIKeyResponse422 | PatchAppAPIKeyResponse500 | None:
    if response.status_code == 200:
        response_200 = PatchAppAPIKeyResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PatchAppAPIKeyResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchAppAPIKeyResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchAppAPIKeyResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PatchAppAPIKeyResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PatchAppAPIKeyResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchAppAPIKeyResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchAppAPIKeyResponse200 | PatchAppAPIKeyResponse400 | PatchAppAPIKeyResponse401 | PatchAppAPIKeyResponse403 | PatchAppAPIKeyResponse404 | PatchAppAPIKeyResponse422 | PatchAppAPIKeyResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: AppAPIKeyName | Unset = UNSET,

) -> Response[PatchAppAPIKeyResponse200 | PatchAppAPIKeyResponse400 | PatchAppAPIKeyResponse401 | PatchAppAPIKeyResponse403 | PatchAppAPIKeyResponse404 | PatchAppAPIKeyResponse422 | PatchAppAPIKeyResponse500]:
    r""" Updates the name of an App API Key in the application.

     Metadata does not contain the App API Key secret. A user with the \"Manage App
    API Keys\" permission can manage the metadata for all users. A user with the
    \"Browse App API Keys\" permission can view the metadata for all users.

    Args:
        id (int):
        body (AppAPIKeyName | Unset): AppAPIKeyName defines the name of an App API Key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchAppAPIKeyResponse200 | PatchAppAPIKeyResponse400 | PatchAppAPIKeyResponse401 | PatchAppAPIKeyResponse403 | PatchAppAPIKeyResponse404 | PatchAppAPIKeyResponse422 | PatchAppAPIKeyResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: AppAPIKeyName | Unset = UNSET,

) -> PatchAppAPIKeyResponse200 | PatchAppAPIKeyResponse400 | PatchAppAPIKeyResponse401 | PatchAppAPIKeyResponse403 | PatchAppAPIKeyResponse404 | PatchAppAPIKeyResponse422 | PatchAppAPIKeyResponse500 | None:
    r""" Updates the name of an App API Key in the application.

     Metadata does not contain the App API Key secret. A user with the \"Manage App
    API Keys\" permission can manage the metadata for all users. A user with the
    \"Browse App API Keys\" permission can view the metadata for all users.

    Args:
        id (int):
        body (AppAPIKeyName | Unset): AppAPIKeyName defines the name of an App API Key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchAppAPIKeyResponse200 | PatchAppAPIKeyResponse400 | PatchAppAPIKeyResponse401 | PatchAppAPIKeyResponse403 | PatchAppAPIKeyResponse404 | PatchAppAPIKeyResponse422 | PatchAppAPIKeyResponse500
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: AppAPIKeyName | Unset = UNSET,

) -> Response[PatchAppAPIKeyResponse200 | PatchAppAPIKeyResponse400 | PatchAppAPIKeyResponse401 | PatchAppAPIKeyResponse403 | PatchAppAPIKeyResponse404 | PatchAppAPIKeyResponse422 | PatchAppAPIKeyResponse500]:
    r""" Updates the name of an App API Key in the application.

     Metadata does not contain the App API Key secret. A user with the \"Manage App
    API Keys\" permission can manage the metadata for all users. A user with the
    \"Browse App API Keys\" permission can view the metadata for all users.

    Args:
        id (int):
        body (AppAPIKeyName | Unset): AppAPIKeyName defines the name of an App API Key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchAppAPIKeyResponse200 | PatchAppAPIKeyResponse400 | PatchAppAPIKeyResponse401 | PatchAppAPIKeyResponse403 | PatchAppAPIKeyResponse404 | PatchAppAPIKeyResponse422 | PatchAppAPIKeyResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: AppAPIKeyName | Unset = UNSET,

) -> PatchAppAPIKeyResponse200 | PatchAppAPIKeyResponse400 | PatchAppAPIKeyResponse401 | PatchAppAPIKeyResponse403 | PatchAppAPIKeyResponse404 | PatchAppAPIKeyResponse422 | PatchAppAPIKeyResponse500 | None:
    r""" Updates the name of an App API Key in the application.

     Metadata does not contain the App API Key secret. A user with the \"Manage App
    API Keys\" permission can manage the metadata for all users. A user with the
    \"Browse App API Keys\" permission can view the metadata for all users.

    Args:
        id (int):
        body (AppAPIKeyName | Unset): AppAPIKeyName defines the name of an App API Key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchAppAPIKeyResponse200 | PatchAppAPIKeyResponse400 | PatchAppAPIKeyResponse401 | PatchAppAPIKeyResponse403 | PatchAppAPIKeyResponse404 | PatchAppAPIKeyResponse422 | PatchAppAPIKeyResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
