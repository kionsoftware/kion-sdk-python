from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.reset_all_compliance_checks_response_200 import ResetAllComplianceChecksResponse200
from ...models.reset_all_compliance_checks_response_400 import ResetAllComplianceChecksResponse400
from ...models.reset_all_compliance_checks_response_401 import ResetAllComplianceChecksResponse401
from ...models.reset_all_compliance_checks_response_403 import ResetAllComplianceChecksResponse403
from ...models.reset_all_compliance_checks_response_500 import ResetAllComplianceChecksResponse500
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/compliance/check/state/reset",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ResetAllComplianceChecksResponse200 | ResetAllComplianceChecksResponse400 | ResetAllComplianceChecksResponse401 | ResetAllComplianceChecksResponse403 | ResetAllComplianceChecksResponse500 | None:
    if response.status_code == 200:
        response_200 = ResetAllComplianceChecksResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ResetAllComplianceChecksResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ResetAllComplianceChecksResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = ResetAllComplianceChecksResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = ResetAllComplianceChecksResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ResetAllComplianceChecksResponse200 | ResetAllComplianceChecksResponse400 | ResetAllComplianceChecksResponse401 | ResetAllComplianceChecksResponse403 | ResetAllComplianceChecksResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[ResetAllComplianceChecksResponse200 | ResetAllComplianceChecksResponse400 | ResetAllComplianceChecksResponse401 | ResetAllComplianceChecksResponse403 | ResetAllComplianceChecksResponse500]:
    """ Resets the state of all compliance checks.

     <strong>This endpoint will soon be deprecated in favor of a new compliance check state tracking
    model in a future release.</strong>

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResetAllComplianceChecksResponse200 | ResetAllComplianceChecksResponse400 | ResetAllComplianceChecksResponse401 | ResetAllComplianceChecksResponse403 | ResetAllComplianceChecksResponse500]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,

) -> ResetAllComplianceChecksResponse200 | ResetAllComplianceChecksResponse400 | ResetAllComplianceChecksResponse401 | ResetAllComplianceChecksResponse403 | ResetAllComplianceChecksResponse500 | None:
    """ Resets the state of all compliance checks.

     <strong>This endpoint will soon be deprecated in favor of a new compliance check state tracking
    model in a future release.</strong>

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResetAllComplianceChecksResponse200 | ResetAllComplianceChecksResponse400 | ResetAllComplianceChecksResponse401 | ResetAllComplianceChecksResponse403 | ResetAllComplianceChecksResponse500
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[ResetAllComplianceChecksResponse200 | ResetAllComplianceChecksResponse400 | ResetAllComplianceChecksResponse401 | ResetAllComplianceChecksResponse403 | ResetAllComplianceChecksResponse500]:
    """ Resets the state of all compliance checks.

     <strong>This endpoint will soon be deprecated in favor of a new compliance check state tracking
    model in a future release.</strong>

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResetAllComplianceChecksResponse200 | ResetAllComplianceChecksResponse400 | ResetAllComplianceChecksResponse401 | ResetAllComplianceChecksResponse403 | ResetAllComplianceChecksResponse500]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,

) -> ResetAllComplianceChecksResponse200 | ResetAllComplianceChecksResponse400 | ResetAllComplianceChecksResponse401 | ResetAllComplianceChecksResponse403 | ResetAllComplianceChecksResponse500 | None:
    """ Resets the state of all compliance checks.

     <strong>This endpoint will soon be deprecated in favor of a new compliance check state tracking
    model in a future release.</strong>

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResetAllComplianceChecksResponse200 | ResetAllComplianceChecksResponse400 | ResetAllComplianceChecksResponse401 | ResetAllComplianceChecksResponse403 | ResetAllComplianceChecksResponse500
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
