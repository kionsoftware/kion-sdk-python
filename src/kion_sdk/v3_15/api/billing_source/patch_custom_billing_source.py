from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.custom_billing_source_update import CustomBillingSourceUpdate
from ...models.patch_custom_billing_source_response_200 import PatchCustomBillingSourceResponse200
from ...models.patch_custom_billing_source_response_400 import PatchCustomBillingSourceResponse400
from ...models.patch_custom_billing_source_response_401 import PatchCustomBillingSourceResponse401
from ...models.patch_custom_billing_source_response_403 import PatchCustomBillingSourceResponse403
from ...models.patch_custom_billing_source_response_404 import PatchCustomBillingSourceResponse404
from ...models.patch_custom_billing_source_response_422 import PatchCustomBillingSourceResponse422
from ...models.patch_custom_billing_source_response_500 import PatchCustomBillingSourceResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: CustomBillingSourceUpdate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v3/billing-source/custom/{id}".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchCustomBillingSourceResponse200 | PatchCustomBillingSourceResponse400 | PatchCustomBillingSourceResponse401 | PatchCustomBillingSourceResponse403 | PatchCustomBillingSourceResponse404 | PatchCustomBillingSourceResponse422 | PatchCustomBillingSourceResponse500 | None:
    if response.status_code == 200:
        response_200 = PatchCustomBillingSourceResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PatchCustomBillingSourceResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchCustomBillingSourceResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchCustomBillingSourceResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PatchCustomBillingSourceResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PatchCustomBillingSourceResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchCustomBillingSourceResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchCustomBillingSourceResponse200 | PatchCustomBillingSourceResponse400 | PatchCustomBillingSourceResponse401 | PatchCustomBillingSourceResponse403 | PatchCustomBillingSourceResponse404 | PatchCustomBillingSourceResponse422 | PatchCustomBillingSourceResponse500]:
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
    body: CustomBillingSourceUpdate,

) -> Response[PatchCustomBillingSourceResponse200 | PatchCustomBillingSourceResponse400 | PatchCustomBillingSourceResponse401 | PatchCustomBillingSourceResponse403 | PatchCustomBillingSourceResponse404 | PatchCustomBillingSourceResponse422 | PatchCustomBillingSourceResponse500]:
    """ Updates an existing Custom billing source.

    Args:
        id (int):
        body (CustomBillingSourceUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchCustomBillingSourceResponse200 | PatchCustomBillingSourceResponse400 | PatchCustomBillingSourceResponse401 | PatchCustomBillingSourceResponse403 | PatchCustomBillingSourceResponse404 | PatchCustomBillingSourceResponse422 | PatchCustomBillingSourceResponse500]
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
    body: CustomBillingSourceUpdate,

) -> PatchCustomBillingSourceResponse200 | PatchCustomBillingSourceResponse400 | PatchCustomBillingSourceResponse401 | PatchCustomBillingSourceResponse403 | PatchCustomBillingSourceResponse404 | PatchCustomBillingSourceResponse422 | PatchCustomBillingSourceResponse500 | None:
    """ Updates an existing Custom billing source.

    Args:
        id (int):
        body (CustomBillingSourceUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchCustomBillingSourceResponse200 | PatchCustomBillingSourceResponse400 | PatchCustomBillingSourceResponse401 | PatchCustomBillingSourceResponse403 | PatchCustomBillingSourceResponse404 | PatchCustomBillingSourceResponse422 | PatchCustomBillingSourceResponse500
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
    body: CustomBillingSourceUpdate,

) -> Response[PatchCustomBillingSourceResponse200 | PatchCustomBillingSourceResponse400 | PatchCustomBillingSourceResponse401 | PatchCustomBillingSourceResponse403 | PatchCustomBillingSourceResponse404 | PatchCustomBillingSourceResponse422 | PatchCustomBillingSourceResponse500]:
    """ Updates an existing Custom billing source.

    Args:
        id (int):
        body (CustomBillingSourceUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchCustomBillingSourceResponse200 | PatchCustomBillingSourceResponse400 | PatchCustomBillingSourceResponse401 | PatchCustomBillingSourceResponse403 | PatchCustomBillingSourceResponse404 | PatchCustomBillingSourceResponse422 | PatchCustomBillingSourceResponse500]
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
    body: CustomBillingSourceUpdate,

) -> PatchCustomBillingSourceResponse200 | PatchCustomBillingSourceResponse400 | PatchCustomBillingSourceResponse401 | PatchCustomBillingSourceResponse403 | PatchCustomBillingSourceResponse404 | PatchCustomBillingSourceResponse422 | PatchCustomBillingSourceResponse500 | None:
    """ Updates an existing Custom billing source.

    Args:
        id (int):
        body (CustomBillingSourceUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchCustomBillingSourceResponse200 | PatchCustomBillingSourceResponse400 | PatchCustomBillingSourceResponse401 | PatchCustomBillingSourceResponse403 | PatchCustomBillingSourceResponse404 | PatchCustomBillingSourceResponse422 | PatchCustomBillingSourceResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
