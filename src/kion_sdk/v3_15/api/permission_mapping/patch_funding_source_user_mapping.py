from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.patch_funding_source_user_mapping_response_200 import PatchFundingSourceUserMappingResponse200
from ...models.patch_funding_source_user_mapping_response_400 import PatchFundingSourceUserMappingResponse400
from ...models.patch_funding_source_user_mapping_response_401 import PatchFundingSourceUserMappingResponse401
from ...models.patch_funding_source_user_mapping_response_403 import PatchFundingSourceUserMappingResponse403
from ...models.patch_funding_source_user_mapping_response_404 import PatchFundingSourceUserMappingResponse404
from ...models.patch_funding_source_user_mapping_response_422 import PatchFundingSourceUserMappingResponse422
from ...models.patch_funding_source_user_mapping_response_500 import PatchFundingSourceUserMappingResponse500
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
        "url": "/v3/funding-source/{id}/permission-mapping".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = []
        for body_item_data in body:
            body_item = body_item_data.to_dict()
            _kwargs["json"].append(body_item)



    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchFundingSourceUserMappingResponse200 | PatchFundingSourceUserMappingResponse400 | PatchFundingSourceUserMappingResponse401 | PatchFundingSourceUserMappingResponse403 | PatchFundingSourceUserMappingResponse404 | PatchFundingSourceUserMappingResponse422 | PatchFundingSourceUserMappingResponse500 | None:
    if response.status_code == 200:
        response_200 = PatchFundingSourceUserMappingResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PatchFundingSourceUserMappingResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchFundingSourceUserMappingResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchFundingSourceUserMappingResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PatchFundingSourceUserMappingResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PatchFundingSourceUserMappingResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchFundingSourceUserMappingResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchFundingSourceUserMappingResponse200 | PatchFundingSourceUserMappingResponse400 | PatchFundingSourceUserMappingResponse401 | PatchFundingSourceUserMappingResponse403 | PatchFundingSourceUserMappingResponse404 | PatchFundingSourceUserMappingResponse422 | PatchFundingSourceUserMappingResponse500]:
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

) -> Response[PatchFundingSourceUserMappingResponse200 | PatchFundingSourceUserMappingResponse400 | PatchFundingSourceUserMappingResponse401 | PatchFundingSourceUserMappingResponse403 | PatchFundingSourceUserMappingResponse404 | PatchFundingSourceUserMappingResponse422 | PatchFundingSourceUserMappingResponse500]:
    """ Updates a funding source's user permission mappings.

    Args:
        id (int):
        body (list[UserMapping] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchFundingSourceUserMappingResponse200 | PatchFundingSourceUserMappingResponse400 | PatchFundingSourceUserMappingResponse401 | PatchFundingSourceUserMappingResponse403 | PatchFundingSourceUserMappingResponse404 | PatchFundingSourceUserMappingResponse422 | PatchFundingSourceUserMappingResponse500]
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

) -> PatchFundingSourceUserMappingResponse200 | PatchFundingSourceUserMappingResponse400 | PatchFundingSourceUserMappingResponse401 | PatchFundingSourceUserMappingResponse403 | PatchFundingSourceUserMappingResponse404 | PatchFundingSourceUserMappingResponse422 | PatchFundingSourceUserMappingResponse500 | None:
    """ Updates a funding source's user permission mappings.

    Args:
        id (int):
        body (list[UserMapping] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchFundingSourceUserMappingResponse200 | PatchFundingSourceUserMappingResponse400 | PatchFundingSourceUserMappingResponse401 | PatchFundingSourceUserMappingResponse403 | PatchFundingSourceUserMappingResponse404 | PatchFundingSourceUserMappingResponse422 | PatchFundingSourceUserMappingResponse500
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

) -> Response[PatchFundingSourceUserMappingResponse200 | PatchFundingSourceUserMappingResponse400 | PatchFundingSourceUserMappingResponse401 | PatchFundingSourceUserMappingResponse403 | PatchFundingSourceUserMappingResponse404 | PatchFundingSourceUserMappingResponse422 | PatchFundingSourceUserMappingResponse500]:
    """ Updates a funding source's user permission mappings.

    Args:
        id (int):
        body (list[UserMapping] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchFundingSourceUserMappingResponse200 | PatchFundingSourceUserMappingResponse400 | PatchFundingSourceUserMappingResponse401 | PatchFundingSourceUserMappingResponse403 | PatchFundingSourceUserMappingResponse404 | PatchFundingSourceUserMappingResponse422 | PatchFundingSourceUserMappingResponse500]
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

) -> PatchFundingSourceUserMappingResponse200 | PatchFundingSourceUserMappingResponse400 | PatchFundingSourceUserMappingResponse401 | PatchFundingSourceUserMappingResponse403 | PatchFundingSourceUserMappingResponse404 | PatchFundingSourceUserMappingResponse422 | PatchFundingSourceUserMappingResponse500 | None:
    """ Updates a funding source's user permission mappings.

    Args:
        id (int):
        body (list[UserMapping] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchFundingSourceUserMappingResponse200 | PatchFundingSourceUserMappingResponse400 | PatchFundingSourceUserMappingResponse401 | PatchFundingSourceUserMappingResponse403 | PatchFundingSourceUserMappingResponse404 | PatchFundingSourceUserMappingResponse422 | PatchFundingSourceUserMappingResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
