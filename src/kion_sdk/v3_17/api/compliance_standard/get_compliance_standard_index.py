from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_compliance_standard_index_response_200 import GetComplianceStandardIndexResponse200
from ...models.get_compliance_standard_index_response_401 import GetComplianceStandardIndexResponse401
from ...models.get_compliance_standard_index_response_500 import GetComplianceStandardIndexResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    detailed: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["detailed"] = detailed


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/compliance/standard",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetComplianceStandardIndexResponse200 | GetComplianceStandardIndexResponse401 | GetComplianceStandardIndexResponse500 | None:
    if response.status_code == 200:
        response_200 = GetComplianceStandardIndexResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetComplianceStandardIndexResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 500:
        response_500 = GetComplianceStandardIndexResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetComplianceStandardIndexResponse200 | GetComplianceStandardIndexResponse401 | GetComplianceStandardIndexResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    detailed: int | Unset = UNSET,

) -> Response[GetComplianceStandardIndexResponse200 | GetComplianceStandardIndexResponse401 | GetComplianceStandardIndexResponse500]:
    """ Finds all Compliance Standards in the application.

    Args:
        detailed (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetComplianceStandardIndexResponse200 | GetComplianceStandardIndexResponse401 | GetComplianceStandardIndexResponse500]
     """


    kwargs = _get_kwargs(
        detailed=detailed,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    detailed: int | Unset = UNSET,

) -> GetComplianceStandardIndexResponse200 | GetComplianceStandardIndexResponse401 | GetComplianceStandardIndexResponse500 | None:
    """ Finds all Compliance Standards in the application.

    Args:
        detailed (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetComplianceStandardIndexResponse200 | GetComplianceStandardIndexResponse401 | GetComplianceStandardIndexResponse500
     """


    return sync_detailed(
        client=client,
detailed=detailed,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    detailed: int | Unset = UNSET,

) -> Response[GetComplianceStandardIndexResponse200 | GetComplianceStandardIndexResponse401 | GetComplianceStandardIndexResponse500]:
    """ Finds all Compliance Standards in the application.

    Args:
        detailed (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetComplianceStandardIndexResponse200 | GetComplianceStandardIndexResponse401 | GetComplianceStandardIndexResponse500]
     """


    kwargs = _get_kwargs(
        detailed=detailed,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    detailed: int | Unset = UNSET,

) -> GetComplianceStandardIndexResponse200 | GetComplianceStandardIndexResponse401 | GetComplianceStandardIndexResponse500 | None:
    """ Finds all Compliance Standards in the application.

    Args:
        detailed (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetComplianceStandardIndexResponse200 | GetComplianceStandardIndexResponse401 | GetComplianceStandardIndexResponse500
     """


    return (await asyncio_detailed(
        client=client,
detailed=detailed,

    )).parsed
