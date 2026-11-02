from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.reset_compliance_check_response_200 import ResetComplianceCheckResponse200
from ...models.reset_compliance_check_response_400 import ResetComplianceCheckResponse400
from ...models.reset_compliance_check_response_401 import ResetComplianceCheckResponse401
from ...models.reset_compliance_check_response_403 import ResetComplianceCheckResponse403
from ...models.reset_compliance_check_response_500 import ResetComplianceCheckResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/compliance/check/{id}/state/reset".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ResetComplianceCheckResponse200 | ResetComplianceCheckResponse400 | ResetComplianceCheckResponse401 | ResetComplianceCheckResponse403 | ResetComplianceCheckResponse500 | None:
    if response.status_code == 200:
        response_200 = ResetComplianceCheckResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ResetComplianceCheckResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ResetComplianceCheckResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = ResetComplianceCheckResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = ResetComplianceCheckResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ResetComplianceCheckResponse200 | ResetComplianceCheckResponse400 | ResetComplianceCheckResponse401 | ResetComplianceCheckResponse403 | ResetComplianceCheckResponse500]:
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

) -> Response[ResetComplianceCheckResponse200 | ResetComplianceCheckResponse400 | ResetComplianceCheckResponse401 | ResetComplianceCheckResponse403 | ResetComplianceCheckResponse500]:
    """ Resets the state of a compliance check.

     <strong>This endpoint will soon be deprecated in favor of a new compliance check state tracking
    model in a future release.</strong>

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResetComplianceCheckResponse200 | ResetComplianceCheckResponse400 | ResetComplianceCheckResponse401 | ResetComplianceCheckResponse403 | ResetComplianceCheckResponse500]
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

) -> ResetComplianceCheckResponse200 | ResetComplianceCheckResponse400 | ResetComplianceCheckResponse401 | ResetComplianceCheckResponse403 | ResetComplianceCheckResponse500 | None:
    """ Resets the state of a compliance check.

     <strong>This endpoint will soon be deprecated in favor of a new compliance check state tracking
    model in a future release.</strong>

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResetComplianceCheckResponse200 | ResetComplianceCheckResponse400 | ResetComplianceCheckResponse401 | ResetComplianceCheckResponse403 | ResetComplianceCheckResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[ResetComplianceCheckResponse200 | ResetComplianceCheckResponse400 | ResetComplianceCheckResponse401 | ResetComplianceCheckResponse403 | ResetComplianceCheckResponse500]:
    """ Resets the state of a compliance check.

     <strong>This endpoint will soon be deprecated in favor of a new compliance check state tracking
    model in a future release.</strong>

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResetComplianceCheckResponse200 | ResetComplianceCheckResponse400 | ResetComplianceCheckResponse401 | ResetComplianceCheckResponse403 | ResetComplianceCheckResponse500]
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

) -> ResetComplianceCheckResponse200 | ResetComplianceCheckResponse400 | ResetComplianceCheckResponse401 | ResetComplianceCheckResponse403 | ResetComplianceCheckResponse500 | None:
    """ Resets the state of a compliance check.

     <strong>This endpoint will soon be deprecated in favor of a new compliance check state tracking
    model in a future release.</strong>

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResetComplianceCheckResponse200 | ResetComplianceCheckResponse400 | ResetComplianceCheckResponse401 | ResetComplianceCheckResponse403 | ResetComplianceCheckResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
