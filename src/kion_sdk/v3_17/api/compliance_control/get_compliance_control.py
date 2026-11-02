from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_compliance_control_response_200 import GetComplianceControlResponse200
from ...models.get_compliance_control_response_401 import GetComplianceControlResponse401
from ...models.get_compliance_control_response_403 import GetComplianceControlResponse403
from ...models.get_compliance_control_response_404 import GetComplianceControlResponse404
from ...models.get_compliance_control_response_500 import GetComplianceControlResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v4/compliance/control/{id}".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetComplianceControlResponse200 | GetComplianceControlResponse401 | GetComplianceControlResponse403 | GetComplianceControlResponse404 | GetComplianceControlResponse500 | None:
    if response.status_code == 200:
        response_200 = GetComplianceControlResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetComplianceControlResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetComplianceControlResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetComplianceControlResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetComplianceControlResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetComplianceControlResponse200 | GetComplianceControlResponse401 | GetComplianceControlResponse403 | GetComplianceControlResponse404 | GetComplianceControlResponse500]:
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

) -> Response[GetComplianceControlResponse200 | GetComplianceControlResponse401 | GetComplianceControlResponse403 | GetComplianceControlResponse404 | GetComplianceControlResponse500]:
    """ Finds a Compliance Control by ID in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetComplianceControlResponse200 | GetComplianceControlResponse401 | GetComplianceControlResponse403 | GetComplianceControlResponse404 | GetComplianceControlResponse500]
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

) -> GetComplianceControlResponse200 | GetComplianceControlResponse401 | GetComplianceControlResponse403 | GetComplianceControlResponse404 | GetComplianceControlResponse500 | None:
    """ Finds a Compliance Control by ID in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetComplianceControlResponse200 | GetComplianceControlResponse401 | GetComplianceControlResponse403 | GetComplianceControlResponse404 | GetComplianceControlResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetComplianceControlResponse200 | GetComplianceControlResponse401 | GetComplianceControlResponse403 | GetComplianceControlResponse404 | GetComplianceControlResponse500]:
    """ Finds a Compliance Control by ID in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetComplianceControlResponse200 | GetComplianceControlResponse401 | GetComplianceControlResponse403 | GetComplianceControlResponse404 | GetComplianceControlResponse500]
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

) -> GetComplianceControlResponse200 | GetComplianceControlResponse401 | GetComplianceControlResponse403 | GetComplianceControlResponse404 | GetComplianceControlResponse500 | None:
    """ Finds a Compliance Control by ID in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetComplianceControlResponse200 | GetComplianceControlResponse401 | GetComplianceControlResponse403 | GetComplianceControlResponse404 | GetComplianceControlResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
