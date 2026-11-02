from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_compliance_check_state_response_200 import GetComplianceCheckStateResponse200
from ...models.get_compliance_check_state_response_401 import GetComplianceCheckStateResponse401
from ...models.get_compliance_check_state_response_403 import GetComplianceCheckStateResponse403
from ...models.get_compliance_check_state_response_404 import GetComplianceCheckStateResponse404
from ...models.get_compliance_check_state_response_500 import GetComplianceCheckStateResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/compliance/check/{id}/state".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetComplianceCheckStateResponse200 | GetComplianceCheckStateResponse401 | GetComplianceCheckStateResponse403 | GetComplianceCheckStateResponse404 | GetComplianceCheckStateResponse500 | None:
    if response.status_code == 200:
        response_200 = GetComplianceCheckStateResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetComplianceCheckStateResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetComplianceCheckStateResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetComplianceCheckStateResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetComplianceCheckStateResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetComplianceCheckStateResponse200 | GetComplianceCheckStateResponse401 | GetComplianceCheckStateResponse403 | GetComplianceCheckStateResponse404 | GetComplianceCheckStateResponse500]:
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

) -> Response[GetComplianceCheckStateResponse200 | GetComplianceCheckStateResponse401 | GetComplianceCheckStateResponse403 | GetComplianceCheckStateResponse404 | GetComplianceCheckStateResponse500]:
    """ Finds a Compliance Check State by ID in the application.

     <strong>This endpoint will soon be deprecated in favor of a new compliance check state tracking
    model in a future release.</strong>

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetComplianceCheckStateResponse200 | GetComplianceCheckStateResponse401 | GetComplianceCheckStateResponse403 | GetComplianceCheckStateResponse404 | GetComplianceCheckStateResponse500]
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

) -> GetComplianceCheckStateResponse200 | GetComplianceCheckStateResponse401 | GetComplianceCheckStateResponse403 | GetComplianceCheckStateResponse404 | GetComplianceCheckStateResponse500 | None:
    """ Finds a Compliance Check State by ID in the application.

     <strong>This endpoint will soon be deprecated in favor of a new compliance check state tracking
    model in a future release.</strong>

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetComplianceCheckStateResponse200 | GetComplianceCheckStateResponse401 | GetComplianceCheckStateResponse403 | GetComplianceCheckStateResponse404 | GetComplianceCheckStateResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetComplianceCheckStateResponse200 | GetComplianceCheckStateResponse401 | GetComplianceCheckStateResponse403 | GetComplianceCheckStateResponse404 | GetComplianceCheckStateResponse500]:
    """ Finds a Compliance Check State by ID in the application.

     <strong>This endpoint will soon be deprecated in favor of a new compliance check state tracking
    model in a future release.</strong>

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetComplianceCheckStateResponse200 | GetComplianceCheckStateResponse401 | GetComplianceCheckStateResponse403 | GetComplianceCheckStateResponse404 | GetComplianceCheckStateResponse500]
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

) -> GetComplianceCheckStateResponse200 | GetComplianceCheckStateResponse401 | GetComplianceCheckStateResponse403 | GetComplianceCheckStateResponse404 | GetComplianceCheckStateResponse500 | None:
    """ Finds a Compliance Check State by ID in the application.

     <strong>This endpoint will soon be deprecated in favor of a new compliance check state tracking
    model in a future release.</strong>

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetComplianceCheckStateResponse200 | GetComplianceCheckStateResponse401 | GetComplianceCheckStateResponse403 | GetComplianceCheckStateResponse404 | GetComplianceCheckStateResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
