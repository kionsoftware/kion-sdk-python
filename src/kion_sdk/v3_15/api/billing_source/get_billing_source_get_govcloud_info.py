from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_billing_source_get_govcloud_info_response_200 import GetBillingSourceGetGovcloudInfoResponse200
from ...models.get_billing_source_get_govcloud_info_response_401 import GetBillingSourceGetGovcloudInfoResponse401
from ...models.get_billing_source_get_govcloud_info_response_403 import GetBillingSourceGetGovcloudInfoResponse403
from ...models.get_billing_source_get_govcloud_info_response_500 import GetBillingSourceGetGovcloudInfoResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/billing-source/{id}/govcloud".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetBillingSourceGetGovcloudInfoResponse200 | GetBillingSourceGetGovcloudInfoResponse401 | GetBillingSourceGetGovcloudInfoResponse403 | GetBillingSourceGetGovcloudInfoResponse500 | None:
    if response.status_code == 200:
        response_200 = GetBillingSourceGetGovcloudInfoResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetBillingSourceGetGovcloudInfoResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetBillingSourceGetGovcloudInfoResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GetBillingSourceGetGovcloudInfoResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetBillingSourceGetGovcloudInfoResponse200 | GetBillingSourceGetGovcloudInfoResponse401 | GetBillingSourceGetGovcloudInfoResponse403 | GetBillingSourceGetGovcloudInfoResponse500]:
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

) -> Response[GetBillingSourceGetGovcloudInfoResponse200 | GetBillingSourceGetGovcloudInfoResponse401 | GetBillingSourceGetGovcloudInfoResponse403 | GetBillingSourceGetGovcloudInfoResponse500]:
    """ Gets the GovCloud account info if enabled on a Billing Source or not.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBillingSourceGetGovcloudInfoResponse200 | GetBillingSourceGetGovcloudInfoResponse401 | GetBillingSourceGetGovcloudInfoResponse403 | GetBillingSourceGetGovcloudInfoResponse500]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,

) -> GetBillingSourceGetGovcloudInfoResponse200 | GetBillingSourceGetGovcloudInfoResponse401 | GetBillingSourceGetGovcloudInfoResponse403 | GetBillingSourceGetGovcloudInfoResponse500 | None:
    """ Gets the GovCloud account info if enabled on a Billing Source or not.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBillingSourceGetGovcloudInfoResponse200 | GetBillingSourceGetGovcloudInfoResponse401 | GetBillingSourceGetGovcloudInfoResponse403 | GetBillingSourceGetGovcloudInfoResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetBillingSourceGetGovcloudInfoResponse200 | GetBillingSourceGetGovcloudInfoResponse401 | GetBillingSourceGetGovcloudInfoResponse403 | GetBillingSourceGetGovcloudInfoResponse500]:
    """ Gets the GovCloud account info if enabled on a Billing Source or not.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBillingSourceGetGovcloudInfoResponse200 | GetBillingSourceGetGovcloudInfoResponse401 | GetBillingSourceGetGovcloudInfoResponse403 | GetBillingSourceGetGovcloudInfoResponse500]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,

) -> GetBillingSourceGetGovcloudInfoResponse200 | GetBillingSourceGetGovcloudInfoResponse401 | GetBillingSourceGetGovcloudInfoResponse403 | GetBillingSourceGetGovcloudInfoResponse500 | None:
    """ Gets the GovCloud account info if enabled on a Billing Source or not.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBillingSourceGetGovcloudInfoResponse200 | GetBillingSourceGetGovcloudInfoResponse401 | GetBillingSourceGetGovcloudInfoResponse403 | GetBillingSourceGetGovcloudInfoResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
