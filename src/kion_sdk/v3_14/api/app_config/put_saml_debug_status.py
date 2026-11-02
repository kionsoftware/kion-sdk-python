from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.put_saml_debug_status_response_200 import PutSAMLDebugStatusResponse200
from ...models.put_saml_debug_status_response_401 import PutSAMLDebugStatusResponse401
from ...models.put_saml_debug_status_response_403 import PutSAMLDebugStatusResponse403
from ...models.put_saml_debug_status_response_500 import PutSAMLDebugStatusResponse500
from ...models.saml_debug_status import SAMLDebugStatus
from typing import cast



def _get_kwargs(
    *,
    body: SAMLDebugStatus,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v3/app-config/saml-debugging",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PutSAMLDebugStatusResponse200 | PutSAMLDebugStatusResponse401 | PutSAMLDebugStatusResponse403 | PutSAMLDebugStatusResponse500 | None:
    if response.status_code == 200:
        response_200 = PutSAMLDebugStatusResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = PutSAMLDebugStatusResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PutSAMLDebugStatusResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = PutSAMLDebugStatusResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PutSAMLDebugStatusResponse200 | PutSAMLDebugStatusResponse401 | PutSAMLDebugStatusResponse403 | PutSAMLDebugStatusResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SAMLDebugStatus,

) -> Response[PutSAMLDebugStatusResponse200 | PutSAMLDebugStatusResponse401 | PutSAMLDebugStatusResponse403 | PutSAMLDebugStatusResponse500]:
    """ Sets the SAML debugging enabled status

    Args:
        body (SAMLDebugStatus): SAMLDebugStatus represents the enabled status of SAML debugging

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutSAMLDebugStatusResponse200 | PutSAMLDebugStatusResponse401 | PutSAMLDebugStatusResponse403 | PutSAMLDebugStatusResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: SAMLDebugStatus,

) -> PutSAMLDebugStatusResponse200 | PutSAMLDebugStatusResponse401 | PutSAMLDebugStatusResponse403 | PutSAMLDebugStatusResponse500 | None:
    """ Sets the SAML debugging enabled status

    Args:
        body (SAMLDebugStatus): SAMLDebugStatus represents the enabled status of SAML debugging

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutSAMLDebugStatusResponse200 | PutSAMLDebugStatusResponse401 | PutSAMLDebugStatusResponse403 | PutSAMLDebugStatusResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SAMLDebugStatus,

) -> Response[PutSAMLDebugStatusResponse200 | PutSAMLDebugStatusResponse401 | PutSAMLDebugStatusResponse403 | PutSAMLDebugStatusResponse500]:
    """ Sets the SAML debugging enabled status

    Args:
        body (SAMLDebugStatus): SAMLDebugStatus represents the enabled status of SAML debugging

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutSAMLDebugStatusResponse200 | PutSAMLDebugStatusResponse401 | PutSAMLDebugStatusResponse403 | PutSAMLDebugStatusResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SAMLDebugStatus,

) -> PutSAMLDebugStatusResponse200 | PutSAMLDebugStatusResponse401 | PutSAMLDebugStatusResponse403 | PutSAMLDebugStatusResponse500 | None:
    """ Sets the SAML debugging enabled status

    Args:
        body (SAMLDebugStatus): SAMLDebugStatus represents the enabled status of SAML debugging

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutSAMLDebugStatusResponse200 | PutSAMLDebugStatusResponse401 | PutSAMLDebugStatusResponse403 | PutSAMLDebugStatusResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
