from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_compliance_standard_response_200 import GetComplianceStandardResponse200
from ...models.get_compliance_standard_response_401 import GetComplianceStandardResponse401
from ...models.get_compliance_standard_response_403 import GetComplianceStandardResponse403
from ...models.get_compliance_standard_response_404 import GetComplianceStandardResponse404
from ...models.get_compliance_standard_response_500 import GetComplianceStandardResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/compliance/standard/{id}".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetComplianceStandardResponse200 | GetComplianceStandardResponse401 | GetComplianceStandardResponse403 | GetComplianceStandardResponse404 | GetComplianceStandardResponse500 | None:
    if response.status_code == 200:
        response_200 = GetComplianceStandardResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetComplianceStandardResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetComplianceStandardResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetComplianceStandardResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetComplianceStandardResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetComplianceStandardResponse200 | GetComplianceStandardResponse401 | GetComplianceStandardResponse403 | GetComplianceStandardResponse404 | GetComplianceStandardResponse500]:
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

) -> Response[GetComplianceStandardResponse200 | GetComplianceStandardResponse401 | GetComplianceStandardResponse403 | GetComplianceStandardResponse404 | GetComplianceStandardResponse500]:
    """ Finds an Compliance Standard by ID in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetComplianceStandardResponse200 | GetComplianceStandardResponse401 | GetComplianceStandardResponse403 | GetComplianceStandardResponse404 | GetComplianceStandardResponse500]
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

) -> GetComplianceStandardResponse200 | GetComplianceStandardResponse401 | GetComplianceStandardResponse403 | GetComplianceStandardResponse404 | GetComplianceStandardResponse500 | None:
    """ Finds an Compliance Standard by ID in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetComplianceStandardResponse200 | GetComplianceStandardResponse401 | GetComplianceStandardResponse403 | GetComplianceStandardResponse404 | GetComplianceStandardResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetComplianceStandardResponse200 | GetComplianceStandardResponse401 | GetComplianceStandardResponse403 | GetComplianceStandardResponse404 | GetComplianceStandardResponse500]:
    """ Finds an Compliance Standard by ID in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetComplianceStandardResponse200 | GetComplianceStandardResponse401 | GetComplianceStandardResponse403 | GetComplianceStandardResponse404 | GetComplianceStandardResponse500]
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

) -> GetComplianceStandardResponse200 | GetComplianceStandardResponse401 | GetComplianceStandardResponse403 | GetComplianceStandardResponse404 | GetComplianceStandardResponse500 | None:
    """ Finds an Compliance Standard by ID in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetComplianceStandardResponse200 | GetComplianceStandardResponse401 | GetComplianceStandardResponse403 | GetComplianceStandardResponse404 | GetComplianceStandardResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
