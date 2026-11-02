from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.open_id_update import OpenIDUpdate
from ...models.patch_open_id_response_200 import PatchOpenIDResponse200
from ...models.patch_open_id_response_400 import PatchOpenIDResponse400
from ...models.patch_open_id_response_401 import PatchOpenIDResponse401
from ...models.patch_open_id_response_403 import PatchOpenIDResponse403
from ...models.patch_open_id_response_404 import PatchOpenIDResponse404
from ...models.patch_open_id_response_422 import PatchOpenIDResponse422
from ...models.patch_open_id_response_500 import PatchOpenIDResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: OpenIDUpdate | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v4/idms/open-id/{id}".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchOpenIDResponse200 | PatchOpenIDResponse400 | PatchOpenIDResponse401 | PatchOpenIDResponse403 | PatchOpenIDResponse404 | PatchOpenIDResponse422 | PatchOpenIDResponse500 | None:
    if response.status_code == 200:
        response_200 = PatchOpenIDResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PatchOpenIDResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchOpenIDResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchOpenIDResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PatchOpenIDResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PatchOpenIDResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchOpenIDResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchOpenIDResponse200 | PatchOpenIDResponse400 | PatchOpenIDResponse401 | PatchOpenIDResponse403 | PatchOpenIDResponse404 | PatchOpenIDResponse422 | PatchOpenIDResponse500]:
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
    body: OpenIDUpdate | Unset = UNSET,

) -> Response[PatchOpenIDResponse200 | PatchOpenIDResponse400 | PatchOpenIDResponse401 | PatchOpenIDResponse403 | PatchOpenIDResponse404 | PatchOpenIDResponse422 | PatchOpenIDResponse500]:
    """ Updates an existing OpenID in the application.

    Args:
        id (int):
        body (OpenIDUpdate | Unset): OpenIDUpdate defines the expected payload for updating an
            OpenID IDMS entity in the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchOpenIDResponse200 | PatchOpenIDResponse400 | PatchOpenIDResponse401 | PatchOpenIDResponse403 | PatchOpenIDResponse404 | PatchOpenIDResponse422 | PatchOpenIDResponse500]
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
    body: OpenIDUpdate | Unset = UNSET,

) -> PatchOpenIDResponse200 | PatchOpenIDResponse400 | PatchOpenIDResponse401 | PatchOpenIDResponse403 | PatchOpenIDResponse404 | PatchOpenIDResponse422 | PatchOpenIDResponse500 | None:
    """ Updates an existing OpenID in the application.

    Args:
        id (int):
        body (OpenIDUpdate | Unset): OpenIDUpdate defines the expected payload for updating an
            OpenID IDMS entity in the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchOpenIDResponse200 | PatchOpenIDResponse400 | PatchOpenIDResponse401 | PatchOpenIDResponse403 | PatchOpenIDResponse404 | PatchOpenIDResponse422 | PatchOpenIDResponse500
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
    body: OpenIDUpdate | Unset = UNSET,

) -> Response[PatchOpenIDResponse200 | PatchOpenIDResponse400 | PatchOpenIDResponse401 | PatchOpenIDResponse403 | PatchOpenIDResponse404 | PatchOpenIDResponse422 | PatchOpenIDResponse500]:
    """ Updates an existing OpenID in the application.

    Args:
        id (int):
        body (OpenIDUpdate | Unset): OpenIDUpdate defines the expected payload for updating an
            OpenID IDMS entity in the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchOpenIDResponse200 | PatchOpenIDResponse400 | PatchOpenIDResponse401 | PatchOpenIDResponse403 | PatchOpenIDResponse404 | PatchOpenIDResponse422 | PatchOpenIDResponse500]
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
    body: OpenIDUpdate | Unset = UNSET,

) -> PatchOpenIDResponse200 | PatchOpenIDResponse400 | PatchOpenIDResponse401 | PatchOpenIDResponse403 | PatchOpenIDResponse404 | PatchOpenIDResponse422 | PatchOpenIDResponse500 | None:
    """ Updates an existing OpenID in the application.

    Args:
        id (int):
        body (OpenIDUpdate | Unset): OpenIDUpdate defines the expected payload for updating an
            OpenID IDMS entity in the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchOpenIDResponse200 | PatchOpenIDResponse400 | PatchOpenIDResponse401 | PatchOpenIDResponse403 | PatchOpenIDResponse404 | PatchOpenIDResponse422 | PatchOpenIDResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
