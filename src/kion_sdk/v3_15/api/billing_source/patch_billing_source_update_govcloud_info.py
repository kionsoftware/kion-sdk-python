from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.billing_source_govcloud import BillingSourceGovcloud
from ...models.patch_billing_source_update_govcloud_info_response_200 import PatchBillingSourceUpdateGovcloudInfoResponse200
from ...models.patch_billing_source_update_govcloud_info_response_400 import PatchBillingSourceUpdateGovcloudInfoResponse400
from ...models.patch_billing_source_update_govcloud_info_response_401 import PatchBillingSourceUpdateGovcloudInfoResponse401
from ...models.patch_billing_source_update_govcloud_info_response_403 import PatchBillingSourceUpdateGovcloudInfoResponse403
from ...models.patch_billing_source_update_govcloud_info_response_404 import PatchBillingSourceUpdateGovcloudInfoResponse404
from ...models.patch_billing_source_update_govcloud_info_response_422 import PatchBillingSourceUpdateGovcloudInfoResponse422
from ...models.patch_billing_source_update_govcloud_info_response_500 import PatchBillingSourceUpdateGovcloudInfoResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: BillingSourceGovcloud,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v3/billing-source/{id}/govcloud".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchBillingSourceUpdateGovcloudInfoResponse200 | PatchBillingSourceUpdateGovcloudInfoResponse400 | PatchBillingSourceUpdateGovcloudInfoResponse401 | PatchBillingSourceUpdateGovcloudInfoResponse403 | PatchBillingSourceUpdateGovcloudInfoResponse404 | PatchBillingSourceUpdateGovcloudInfoResponse422 | PatchBillingSourceUpdateGovcloudInfoResponse500 | None:
    if response.status_code == 200:
        response_200 = PatchBillingSourceUpdateGovcloudInfoResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PatchBillingSourceUpdateGovcloudInfoResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchBillingSourceUpdateGovcloudInfoResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchBillingSourceUpdateGovcloudInfoResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PatchBillingSourceUpdateGovcloudInfoResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PatchBillingSourceUpdateGovcloudInfoResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchBillingSourceUpdateGovcloudInfoResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchBillingSourceUpdateGovcloudInfoResponse200 | PatchBillingSourceUpdateGovcloudInfoResponse400 | PatchBillingSourceUpdateGovcloudInfoResponse401 | PatchBillingSourceUpdateGovcloudInfoResponse403 | PatchBillingSourceUpdateGovcloudInfoResponse404 | PatchBillingSourceUpdateGovcloudInfoResponse422 | PatchBillingSourceUpdateGovcloudInfoResponse500]:
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
    body: BillingSourceGovcloud,

) -> Response[PatchBillingSourceUpdateGovcloudInfoResponse200 | PatchBillingSourceUpdateGovcloudInfoResponse400 | PatchBillingSourceUpdateGovcloudInfoResponse401 | PatchBillingSourceUpdateGovcloudInfoResponse403 | PatchBillingSourceUpdateGovcloudInfoResponse404 | PatchBillingSourceUpdateGovcloudInfoResponse422 | PatchBillingSourceUpdateGovcloudInfoResponse500]:
    """ Updates the passed in commercial payer's govcloud billing source.

    Args:
        id (int):
        body (BillingSourceGovcloud): BillingSourceGovcloud defines an account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchBillingSourceUpdateGovcloudInfoResponse200 | PatchBillingSourceUpdateGovcloudInfoResponse400 | PatchBillingSourceUpdateGovcloudInfoResponse401 | PatchBillingSourceUpdateGovcloudInfoResponse403 | PatchBillingSourceUpdateGovcloudInfoResponse404 | PatchBillingSourceUpdateGovcloudInfoResponse422 | PatchBillingSourceUpdateGovcloudInfoResponse500]
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
    body: BillingSourceGovcloud,

) -> PatchBillingSourceUpdateGovcloudInfoResponse200 | PatchBillingSourceUpdateGovcloudInfoResponse400 | PatchBillingSourceUpdateGovcloudInfoResponse401 | PatchBillingSourceUpdateGovcloudInfoResponse403 | PatchBillingSourceUpdateGovcloudInfoResponse404 | PatchBillingSourceUpdateGovcloudInfoResponse422 | PatchBillingSourceUpdateGovcloudInfoResponse500 | None:
    """ Updates the passed in commercial payer's govcloud billing source.

    Args:
        id (int):
        body (BillingSourceGovcloud): BillingSourceGovcloud defines an account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchBillingSourceUpdateGovcloudInfoResponse200 | PatchBillingSourceUpdateGovcloudInfoResponse400 | PatchBillingSourceUpdateGovcloudInfoResponse401 | PatchBillingSourceUpdateGovcloudInfoResponse403 | PatchBillingSourceUpdateGovcloudInfoResponse404 | PatchBillingSourceUpdateGovcloudInfoResponse422 | PatchBillingSourceUpdateGovcloudInfoResponse500
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
    body: BillingSourceGovcloud,

) -> Response[PatchBillingSourceUpdateGovcloudInfoResponse200 | PatchBillingSourceUpdateGovcloudInfoResponse400 | PatchBillingSourceUpdateGovcloudInfoResponse401 | PatchBillingSourceUpdateGovcloudInfoResponse403 | PatchBillingSourceUpdateGovcloudInfoResponse404 | PatchBillingSourceUpdateGovcloudInfoResponse422 | PatchBillingSourceUpdateGovcloudInfoResponse500]:
    """ Updates the passed in commercial payer's govcloud billing source.

    Args:
        id (int):
        body (BillingSourceGovcloud): BillingSourceGovcloud defines an account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchBillingSourceUpdateGovcloudInfoResponse200 | PatchBillingSourceUpdateGovcloudInfoResponse400 | PatchBillingSourceUpdateGovcloudInfoResponse401 | PatchBillingSourceUpdateGovcloudInfoResponse403 | PatchBillingSourceUpdateGovcloudInfoResponse404 | PatchBillingSourceUpdateGovcloudInfoResponse422 | PatchBillingSourceUpdateGovcloudInfoResponse500]
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
    body: BillingSourceGovcloud,

) -> PatchBillingSourceUpdateGovcloudInfoResponse200 | PatchBillingSourceUpdateGovcloudInfoResponse400 | PatchBillingSourceUpdateGovcloudInfoResponse401 | PatchBillingSourceUpdateGovcloudInfoResponse403 | PatchBillingSourceUpdateGovcloudInfoResponse404 | PatchBillingSourceUpdateGovcloudInfoResponse422 | PatchBillingSourceUpdateGovcloudInfoResponse500 | None:
    """ Updates the passed in commercial payer's govcloud billing source.

    Args:
        id (int):
        body (BillingSourceGovcloud): BillingSourceGovcloud defines an account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchBillingSourceUpdateGovcloudInfoResponse200 | PatchBillingSourceUpdateGovcloudInfoResponse400 | PatchBillingSourceUpdateGovcloudInfoResponse401 | PatchBillingSourceUpdateGovcloudInfoResponse403 | PatchBillingSourceUpdateGovcloudInfoResponse404 | PatchBillingSourceUpdateGovcloudInfoResponse422 | PatchBillingSourceUpdateGovcloudInfoResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
