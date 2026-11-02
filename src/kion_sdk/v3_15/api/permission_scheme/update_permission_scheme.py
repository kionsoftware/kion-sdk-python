from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.permission_scheme_update_request import PermissionSchemeUpdateRequest
from ...models.update_permission_scheme_response_200 import UpdatePermissionSchemeResponse200
from ...models.update_permission_scheme_response_400 import UpdatePermissionSchemeResponse400
from ...models.update_permission_scheme_response_401 import UpdatePermissionSchemeResponse401
from ...models.update_permission_scheme_response_403 import UpdatePermissionSchemeResponse403
from ...models.update_permission_scheme_response_500 import UpdatePermissionSchemeResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: PermissionSchemeUpdateRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v3/permission-scheme/{id}".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UpdatePermissionSchemeResponse200 | UpdatePermissionSchemeResponse400 | UpdatePermissionSchemeResponse401 | UpdatePermissionSchemeResponse403 | UpdatePermissionSchemeResponse500 | None:
    if response.status_code == 200:
        response_200 = UpdatePermissionSchemeResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = UpdatePermissionSchemeResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = UpdatePermissionSchemeResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = UpdatePermissionSchemeResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = UpdatePermissionSchemeResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UpdatePermissionSchemeResponse200 | UpdatePermissionSchemeResponse400 | UpdatePermissionSchemeResponse401 | UpdatePermissionSchemeResponse403 | UpdatePermissionSchemeResponse500]:
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
    body: PermissionSchemeUpdateRequest,

) -> Response[UpdatePermissionSchemeResponse200 | UpdatePermissionSchemeResponse400 | UpdatePermissionSchemeResponse401 | UpdatePermissionSchemeResponse403 | UpdatePermissionSchemeResponse500]:
    """ Updates a permission scheme in the application.

    Args:
        id (int):
        body (PermissionSchemeUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdatePermissionSchemeResponse200 | UpdatePermissionSchemeResponse400 | UpdatePermissionSchemeResponse401 | UpdatePermissionSchemeResponse403 | UpdatePermissionSchemeResponse500]
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
    body: PermissionSchemeUpdateRequest,

) -> UpdatePermissionSchemeResponse200 | UpdatePermissionSchemeResponse400 | UpdatePermissionSchemeResponse401 | UpdatePermissionSchemeResponse403 | UpdatePermissionSchemeResponse500 | None:
    """ Updates a permission scheme in the application.

    Args:
        id (int):
        body (PermissionSchemeUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdatePermissionSchemeResponse200 | UpdatePermissionSchemeResponse400 | UpdatePermissionSchemeResponse401 | UpdatePermissionSchemeResponse403 | UpdatePermissionSchemeResponse500
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
    body: PermissionSchemeUpdateRequest,

) -> Response[UpdatePermissionSchemeResponse200 | UpdatePermissionSchemeResponse400 | UpdatePermissionSchemeResponse401 | UpdatePermissionSchemeResponse403 | UpdatePermissionSchemeResponse500]:
    """ Updates a permission scheme in the application.

    Args:
        id (int):
        body (PermissionSchemeUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdatePermissionSchemeResponse200 | UpdatePermissionSchemeResponse400 | UpdatePermissionSchemeResponse401 | UpdatePermissionSchemeResponse403 | UpdatePermissionSchemeResponse500]
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
    body: PermissionSchemeUpdateRequest,

) -> UpdatePermissionSchemeResponse200 | UpdatePermissionSchemeResponse400 | UpdatePermissionSchemeResponse401 | UpdatePermissionSchemeResponse403 | UpdatePermissionSchemeResponse500 | None:
    """ Updates a permission scheme in the application.

    Args:
        id (int):
        body (PermissionSchemeUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdatePermissionSchemeResponse200 | UpdatePermissionSchemeResponse400 | UpdatePermissionSchemeResponse401 | UpdatePermissionSchemeResponse403 | UpdatePermissionSchemeResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
