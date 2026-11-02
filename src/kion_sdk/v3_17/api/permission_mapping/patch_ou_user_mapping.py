from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.patch_ou_user_mapping_response_200 import PatchOUUserMappingResponse200
from ...models.patch_ou_user_mapping_response_400 import PatchOUUserMappingResponse400
from ...models.patch_ou_user_mapping_response_401 import PatchOUUserMappingResponse401
from ...models.patch_ou_user_mapping_response_403 import PatchOUUserMappingResponse403
from ...models.patch_ou_user_mapping_response_404 import PatchOUUserMappingResponse404
from ...models.patch_ou_user_mapping_response_422 import PatchOUUserMappingResponse422
from ...models.patch_ou_user_mapping_response_500 import PatchOUUserMappingResponse500
from ...models.user_mapping import UserMapping
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: list[UserMapping] | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v3/ou/{id}/permission-mapping".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = []
        for body_item_data in body:
            body_item = body_item_data.to_dict()
            _kwargs["json"].append(body_item)



    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchOUUserMappingResponse200 | PatchOUUserMappingResponse400 | PatchOUUserMappingResponse401 | PatchOUUserMappingResponse403 | PatchOUUserMappingResponse404 | PatchOUUserMappingResponse422 | PatchOUUserMappingResponse500 | None:
    if response.status_code == 200:
        response_200 = PatchOUUserMappingResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PatchOUUserMappingResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchOUUserMappingResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchOUUserMappingResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PatchOUUserMappingResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PatchOUUserMappingResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchOUUserMappingResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchOUUserMappingResponse200 | PatchOUUserMappingResponse400 | PatchOUUserMappingResponse401 | PatchOUUserMappingResponse403 | PatchOUUserMappingResponse404 | PatchOUUserMappingResponse422 | PatchOUUserMappingResponse500]:
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
    body: list[UserMapping] | Unset = UNSET,

) -> Response[PatchOUUserMappingResponse200 | PatchOUUserMappingResponse400 | PatchOUUserMappingResponse401 | PatchOUUserMappingResponse403 | PatchOUUserMappingResponse404 | PatchOUUserMappingResponse422 | PatchOUUserMappingResponse500]:
    """ Updates an ou's user permission mappings.

    Args:
        id (int):
        body (list[UserMapping] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchOUUserMappingResponse200 | PatchOUUserMappingResponse400 | PatchOUUserMappingResponse401 | PatchOUUserMappingResponse403 | PatchOUUserMappingResponse404 | PatchOUUserMappingResponse422 | PatchOUUserMappingResponse500]
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
    body: list[UserMapping] | Unset = UNSET,

) -> PatchOUUserMappingResponse200 | PatchOUUserMappingResponse400 | PatchOUUserMappingResponse401 | PatchOUUserMappingResponse403 | PatchOUUserMappingResponse404 | PatchOUUserMappingResponse422 | PatchOUUserMappingResponse500 | None:
    """ Updates an ou's user permission mappings.

    Args:
        id (int):
        body (list[UserMapping] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchOUUserMappingResponse200 | PatchOUUserMappingResponse400 | PatchOUUserMappingResponse401 | PatchOUUserMappingResponse403 | PatchOUUserMappingResponse404 | PatchOUUserMappingResponse422 | PatchOUUserMappingResponse500
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
    body: list[UserMapping] | Unset = UNSET,

) -> Response[PatchOUUserMappingResponse200 | PatchOUUserMappingResponse400 | PatchOUUserMappingResponse401 | PatchOUUserMappingResponse403 | PatchOUUserMappingResponse404 | PatchOUUserMappingResponse422 | PatchOUUserMappingResponse500]:
    """ Updates an ou's user permission mappings.

    Args:
        id (int):
        body (list[UserMapping] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchOUUserMappingResponse200 | PatchOUUserMappingResponse400 | PatchOUUserMappingResponse401 | PatchOUUserMappingResponse403 | PatchOUUserMappingResponse404 | PatchOUUserMappingResponse422 | PatchOUUserMappingResponse500]
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
    body: list[UserMapping] | Unset = UNSET,

) -> PatchOUUserMappingResponse200 | PatchOUUserMappingResponse400 | PatchOUUserMappingResponse401 | PatchOUUserMappingResponse403 | PatchOUUserMappingResponse404 | PatchOUUserMappingResponse422 | PatchOUUserMappingResponse500 | None:
    """ Updates an ou's user permission mappings.

    Args:
        id (int):
        body (list[UserMapping] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchOUUserMappingResponse200 | PatchOUUserMappingResponse400 | PatchOUUserMappingResponse401 | PatchOUUserMappingResponse403 | PatchOUUserMappingResponse404 | PatchOUUserMappingResponse422 | PatchOUUserMappingResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
