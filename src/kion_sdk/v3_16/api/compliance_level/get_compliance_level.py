from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_compliance_level_response_200 import GetComplianceLevelResponse200
from ...models.get_compliance_level_response_401 import GetComplianceLevelResponse401
from ...models.get_compliance_level_response_403 import GetComplianceLevelResponse403
from ...models.get_compliance_level_response_404 import GetComplianceLevelResponse404
from ...models.get_compliance_level_response_500 import GetComplianceLevelResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v4/compliance/level/{id}".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetComplianceLevelResponse200 | GetComplianceLevelResponse401 | GetComplianceLevelResponse403 | GetComplianceLevelResponse404 | GetComplianceLevelResponse500 | None:
    if response.status_code == 200:
        response_200 = GetComplianceLevelResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetComplianceLevelResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetComplianceLevelResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetComplianceLevelResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetComplianceLevelResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetComplianceLevelResponse200 | GetComplianceLevelResponse401 | GetComplianceLevelResponse403 | GetComplianceLevelResponse404 | GetComplianceLevelResponse500]:
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

) -> Response[GetComplianceLevelResponse200 | GetComplianceLevelResponse401 | GetComplianceLevelResponse403 | GetComplianceLevelResponse404 | GetComplianceLevelResponse500]:
    """ Finds an Compliance Level by ID in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetComplianceLevelResponse200 | GetComplianceLevelResponse401 | GetComplianceLevelResponse403 | GetComplianceLevelResponse404 | GetComplianceLevelResponse500]
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

) -> GetComplianceLevelResponse200 | GetComplianceLevelResponse401 | GetComplianceLevelResponse403 | GetComplianceLevelResponse404 | GetComplianceLevelResponse500 | None:
    """ Finds an Compliance Level by ID in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetComplianceLevelResponse200 | GetComplianceLevelResponse401 | GetComplianceLevelResponse403 | GetComplianceLevelResponse404 | GetComplianceLevelResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetComplianceLevelResponse200 | GetComplianceLevelResponse401 | GetComplianceLevelResponse403 | GetComplianceLevelResponse404 | GetComplianceLevelResponse500]:
    """ Finds an Compliance Level by ID in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetComplianceLevelResponse200 | GetComplianceLevelResponse401 | GetComplianceLevelResponse403 | GetComplianceLevelResponse404 | GetComplianceLevelResponse500]
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

) -> GetComplianceLevelResponse200 | GetComplianceLevelResponse401 | GetComplianceLevelResponse403 | GetComplianceLevelResponse404 | GetComplianceLevelResponse500 | None:
    """ Finds an Compliance Level by ID in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetComplianceLevelResponse200 | GetComplianceLevelResponse401 | GetComplianceLevelResponse403 | GetComplianceLevelResponse404 | GetComplianceLevelResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
