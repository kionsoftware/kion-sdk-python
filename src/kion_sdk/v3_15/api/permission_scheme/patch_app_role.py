from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.app_role_update import AppRoleUpdate
from ...models.patch_app_role_response_201 import PatchAppRoleResponse201
from ...models.patch_app_role_response_400 import PatchAppRoleResponse400
from ...models.patch_app_role_response_401 import PatchAppRoleResponse401
from ...models.patch_app_role_response_403 import PatchAppRoleResponse403
from ...models.patch_app_role_response_422 import PatchAppRoleResponse422
from ...models.patch_app_role_response_500 import PatchAppRoleResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: AppRoleUpdate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v3/app-role/{id}".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchAppRoleResponse201 | PatchAppRoleResponse400 | PatchAppRoleResponse401 | PatchAppRoleResponse403 | PatchAppRoleResponse422 | PatchAppRoleResponse500 | None:
    if response.status_code == 201:
        response_201 = PatchAppRoleResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PatchAppRoleResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchAppRoleResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchAppRoleResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PatchAppRoleResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchAppRoleResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchAppRoleResponse201 | PatchAppRoleResponse400 | PatchAppRoleResponse401 | PatchAppRoleResponse403 | PatchAppRoleResponse422 | PatchAppRoleResponse500]:
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
    body: AppRoleUpdate,

) -> Response[PatchAppRoleResponse201 | PatchAppRoleResponse400 | PatchAppRoleResponse401 | PatchAppRoleResponse403 | PatchAppRoleResponse422 | PatchAppRoleResponse500]:
    """ Updates an App Role in the application.

    Args:
        id (int):
        body (AppRoleUpdate): AppRoleUpdate defines an App role update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchAppRoleResponse201 | PatchAppRoleResponse400 | PatchAppRoleResponse401 | PatchAppRoleResponse403 | PatchAppRoleResponse422 | PatchAppRoleResponse500]
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
    body: AppRoleUpdate,

) -> PatchAppRoleResponse201 | PatchAppRoleResponse400 | PatchAppRoleResponse401 | PatchAppRoleResponse403 | PatchAppRoleResponse422 | PatchAppRoleResponse500 | None:
    """ Updates an App Role in the application.

    Args:
        id (int):
        body (AppRoleUpdate): AppRoleUpdate defines an App role update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchAppRoleResponse201 | PatchAppRoleResponse400 | PatchAppRoleResponse401 | PatchAppRoleResponse403 | PatchAppRoleResponse422 | PatchAppRoleResponse500
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
    body: AppRoleUpdate,

) -> Response[PatchAppRoleResponse201 | PatchAppRoleResponse400 | PatchAppRoleResponse401 | PatchAppRoleResponse403 | PatchAppRoleResponse422 | PatchAppRoleResponse500]:
    """ Updates an App Role in the application.

    Args:
        id (int):
        body (AppRoleUpdate): AppRoleUpdate defines an App role update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchAppRoleResponse201 | PatchAppRoleResponse400 | PatchAppRoleResponse401 | PatchAppRoleResponse403 | PatchAppRoleResponse422 | PatchAppRoleResponse500]
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
    body: AppRoleUpdate,

) -> PatchAppRoleResponse201 | PatchAppRoleResponse400 | PatchAppRoleResponse401 | PatchAppRoleResponse403 | PatchAppRoleResponse422 | PatchAppRoleResponse500 | None:
    """ Updates an App Role in the application.

    Args:
        id (int):
        body (AppRoleUpdate): AppRoleUpdate defines an App role update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchAppRoleResponse201 | PatchAppRoleResponse400 | PatchAppRoleResponse401 | PatchAppRoleResponse403 | PatchAppRoleResponse422 | PatchAppRoleResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
