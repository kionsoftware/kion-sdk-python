from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.patch_project_user_mapping_response_200 import PatchProjectUserMappingResponse200
from ...models.patch_project_user_mapping_response_400 import PatchProjectUserMappingResponse400
from ...models.patch_project_user_mapping_response_401 import PatchProjectUserMappingResponse401
from ...models.patch_project_user_mapping_response_403 import PatchProjectUserMappingResponse403
from ...models.patch_project_user_mapping_response_404 import PatchProjectUserMappingResponse404
from ...models.patch_project_user_mapping_response_422 import PatchProjectUserMappingResponse422
from ...models.patch_project_user_mapping_response_500 import PatchProjectUserMappingResponse500
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
        "url": "/v3/project/{id}/permission-mapping".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = []
        for body_item_data in body:
            body_item = body_item_data.to_dict()
            _kwargs["json"].append(body_item)



    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchProjectUserMappingResponse200 | PatchProjectUserMappingResponse400 | PatchProjectUserMappingResponse401 | PatchProjectUserMappingResponse403 | PatchProjectUserMappingResponse404 | PatchProjectUserMappingResponse422 | PatchProjectUserMappingResponse500 | None:
    if response.status_code == 200:
        response_200 = PatchProjectUserMappingResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PatchProjectUserMappingResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchProjectUserMappingResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchProjectUserMappingResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PatchProjectUserMappingResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PatchProjectUserMappingResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchProjectUserMappingResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchProjectUserMappingResponse200 | PatchProjectUserMappingResponse400 | PatchProjectUserMappingResponse401 | PatchProjectUserMappingResponse403 | PatchProjectUserMappingResponse404 | PatchProjectUserMappingResponse422 | PatchProjectUserMappingResponse500]:
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

) -> Response[PatchProjectUserMappingResponse200 | PatchProjectUserMappingResponse400 | PatchProjectUserMappingResponse401 | PatchProjectUserMappingResponse403 | PatchProjectUserMappingResponse404 | PatchProjectUserMappingResponse422 | PatchProjectUserMappingResponse500]:
    """ Updates a project's user permission mappings.

    Args:
        id (int):
        body (list[UserMapping] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchProjectUserMappingResponse200 | PatchProjectUserMappingResponse400 | PatchProjectUserMappingResponse401 | PatchProjectUserMappingResponse403 | PatchProjectUserMappingResponse404 | PatchProjectUserMappingResponse422 | PatchProjectUserMappingResponse500]
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

) -> PatchProjectUserMappingResponse200 | PatchProjectUserMappingResponse400 | PatchProjectUserMappingResponse401 | PatchProjectUserMappingResponse403 | PatchProjectUserMappingResponse404 | PatchProjectUserMappingResponse422 | PatchProjectUserMappingResponse500 | None:
    """ Updates a project's user permission mappings.

    Args:
        id (int):
        body (list[UserMapping] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchProjectUserMappingResponse200 | PatchProjectUserMappingResponse400 | PatchProjectUserMappingResponse401 | PatchProjectUserMappingResponse403 | PatchProjectUserMappingResponse404 | PatchProjectUserMappingResponse422 | PatchProjectUserMappingResponse500
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

) -> Response[PatchProjectUserMappingResponse200 | PatchProjectUserMappingResponse400 | PatchProjectUserMappingResponse401 | PatchProjectUserMappingResponse403 | PatchProjectUserMappingResponse404 | PatchProjectUserMappingResponse422 | PatchProjectUserMappingResponse500]:
    """ Updates a project's user permission mappings.

    Args:
        id (int):
        body (list[UserMapping] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchProjectUserMappingResponse200 | PatchProjectUserMappingResponse400 | PatchProjectUserMappingResponse401 | PatchProjectUserMappingResponse403 | PatchProjectUserMappingResponse404 | PatchProjectUserMappingResponse422 | PatchProjectUserMappingResponse500]
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

) -> PatchProjectUserMappingResponse200 | PatchProjectUserMappingResponse400 | PatchProjectUserMappingResponse401 | PatchProjectUserMappingResponse403 | PatchProjectUserMappingResponse404 | PatchProjectUserMappingResponse422 | PatchProjectUserMappingResponse500 | None:
    """ Updates a project's user permission mappings.

    Args:
        id (int):
        body (list[UserMapping] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchProjectUserMappingResponse200 | PatchProjectUserMappingResponse400 | PatchProjectUserMappingResponse401 | PatchProjectUserMappingResponse403 | PatchProjectUserMappingResponse404 | PatchProjectUserMappingResponse422 | PatchProjectUserMappingResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
