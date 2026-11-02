from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.generate_external_i_ds_response_200 import GenerateExternalIDsResponse200
from ...models.generate_external_i_ds_response_400 import GenerateExternalIDsResponse400
from ...models.generate_external_i_ds_response_401 import GenerateExternalIDsResponse401
from ...models.generate_external_i_ds_response_403 import GenerateExternalIDsResponse403
from ...models.generate_external_i_ds_response_500 import GenerateExternalIDsResponse500
from typing import cast



def _get_kwargs(
    account_number: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/external-id/{account_number}".format(account_number=quote(str(account_number), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GenerateExternalIDsResponse200 | GenerateExternalIDsResponse400 | GenerateExternalIDsResponse401 | GenerateExternalIDsResponse403 | GenerateExternalIDsResponse500 | None:
    if response.status_code == 200:
        response_200 = GenerateExternalIDsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GenerateExternalIDsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GenerateExternalIDsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GenerateExternalIDsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GenerateExternalIDsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GenerateExternalIDsResponse200 | GenerateExternalIDsResponse400 | GenerateExternalIDsResponse401 | GenerateExternalIDsResponse403 | GenerateExternalIDsResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_number: str,
    *,
    client: AuthenticatedClient,

) -> Response[GenerateExternalIDsResponse200 | GenerateExternalIDsResponse400 | GenerateExternalIDsResponse401 | GenerateExternalIDsResponse403 | GenerateExternalIDsResponse500]:
    """ Gets the service and CAR external ids for a given aws account number. If external ids do not already
    exist they will be generated.

    Args:
        account_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenerateExternalIDsResponse200 | GenerateExternalIDsResponse400 | GenerateExternalIDsResponse401 | GenerateExternalIDsResponse403 | GenerateExternalIDsResponse500]
     """


    kwargs = _get_kwargs(
        account_number=account_number,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    account_number: str,
    *,
    client: AuthenticatedClient,

) -> GenerateExternalIDsResponse200 | GenerateExternalIDsResponse400 | GenerateExternalIDsResponse401 | GenerateExternalIDsResponse403 | GenerateExternalIDsResponse500 | None:
    """ Gets the service and CAR external ids for a given aws account number. If external ids do not already
    exist they will be generated.

    Args:
        account_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenerateExternalIDsResponse200 | GenerateExternalIDsResponse400 | GenerateExternalIDsResponse401 | GenerateExternalIDsResponse403 | GenerateExternalIDsResponse500
     """


    return sync_detailed(
        account_number=account_number,
client=client,

    ).parsed

async def asyncio_detailed(
    account_number: str,
    *,
    client: AuthenticatedClient,

) -> Response[GenerateExternalIDsResponse200 | GenerateExternalIDsResponse400 | GenerateExternalIDsResponse401 | GenerateExternalIDsResponse403 | GenerateExternalIDsResponse500]:
    """ Gets the service and CAR external ids for a given aws account number. If external ids do not already
    exist they will be generated.

    Args:
        account_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenerateExternalIDsResponse200 | GenerateExternalIDsResponse400 | GenerateExternalIDsResponse401 | GenerateExternalIDsResponse403 | GenerateExternalIDsResponse500]
     """


    kwargs = _get_kwargs(
        account_number=account_number,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    account_number: str,
    *,
    client: AuthenticatedClient,

) -> GenerateExternalIDsResponse200 | GenerateExternalIDsResponse400 | GenerateExternalIDsResponse401 | GenerateExternalIDsResponse403 | GenerateExternalIDsResponse500 | None:
    """ Gets the service and CAR external ids for a given aws account number. If external ids do not already
    exist they will be generated.

    Args:
        account_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenerateExternalIDsResponse200 | GenerateExternalIDsResponse400 | GenerateExternalIDsResponse401 | GenerateExternalIDsResponse403 | GenerateExternalIDsResponse500
     """


    return (await asyncio_detailed(
        account_number=account_number,
client=client,

    )).parsed
