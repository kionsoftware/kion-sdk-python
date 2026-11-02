from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.compliance_control import ComplianceControl
from ...models.create_compliance_control_response_201 import CreateComplianceControlResponse201
from ...models.create_compliance_control_response_400 import CreateComplianceControlResponse400
from ...models.create_compliance_control_response_401 import CreateComplianceControlResponse401
from ...models.create_compliance_control_response_403 import CreateComplianceControlResponse403
from ...models.create_compliance_control_response_500 import CreateComplianceControlResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: ComplianceControl | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v4/compliance/control",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreateComplianceControlResponse201 | CreateComplianceControlResponse400 | CreateComplianceControlResponse401 | CreateComplianceControlResponse403 | CreateComplianceControlResponse500 | None:
    if response.status_code == 201:
        response_201 = CreateComplianceControlResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = CreateComplianceControlResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = CreateComplianceControlResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = CreateComplianceControlResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = CreateComplianceControlResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CreateComplianceControlResponse201 | CreateComplianceControlResponse400 | CreateComplianceControlResponse401 | CreateComplianceControlResponse403 | CreateComplianceControlResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ComplianceControl | Unset = UNSET,

) -> Response[CreateComplianceControlResponse201 | CreateComplianceControlResponse400 | CreateComplianceControlResponse401 | CreateComplianceControlResponse403 | CreateComplianceControlResponse500]:
    """ Creates a new Compliance Control in the application.

    Args:
        body (ComplianceControl | Unset): ComplianceControl defines a compliance control.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateComplianceControlResponse201 | CreateComplianceControlResponse400 | CreateComplianceControlResponse401 | CreateComplianceControlResponse403 | CreateComplianceControlResponse500]
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
    body: ComplianceControl | Unset = UNSET,

) -> CreateComplianceControlResponse201 | CreateComplianceControlResponse400 | CreateComplianceControlResponse401 | CreateComplianceControlResponse403 | CreateComplianceControlResponse500 | None:
    """ Creates a new Compliance Control in the application.

    Args:
        body (ComplianceControl | Unset): ComplianceControl defines a compliance control.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateComplianceControlResponse201 | CreateComplianceControlResponse400 | CreateComplianceControlResponse401 | CreateComplianceControlResponse403 | CreateComplianceControlResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ComplianceControl | Unset = UNSET,

) -> Response[CreateComplianceControlResponse201 | CreateComplianceControlResponse400 | CreateComplianceControlResponse401 | CreateComplianceControlResponse403 | CreateComplianceControlResponse500]:
    """ Creates a new Compliance Control in the application.

    Args:
        body (ComplianceControl | Unset): ComplianceControl defines a compliance control.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateComplianceControlResponse201 | CreateComplianceControlResponse400 | CreateComplianceControlResponse401 | CreateComplianceControlResponse403 | CreateComplianceControlResponse500]
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
    body: ComplianceControl | Unset = UNSET,

) -> CreateComplianceControlResponse201 | CreateComplianceControlResponse400 | CreateComplianceControlResponse401 | CreateComplianceControlResponse403 | CreateComplianceControlResponse500 | None:
    """ Creates a new Compliance Control in the application.

    Args:
        body (ComplianceControl | Unset): ComplianceControl defines a compliance control.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateComplianceControlResponse201 | CreateComplianceControlResponse400 | CreateComplianceControlResponse401 | CreateComplianceControlResponse403 | CreateComplianceControlResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
