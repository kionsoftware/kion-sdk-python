from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.compliance_control import ComplianceControl
from ...models.update_compliance_control_response_200 import UpdateComplianceControlResponse200
from ...models.update_compliance_control_response_400 import UpdateComplianceControlResponse400
from ...models.update_compliance_control_response_401 import UpdateComplianceControlResponse401
from ...models.update_compliance_control_response_403 import UpdateComplianceControlResponse403
from ...models.update_compliance_control_response_404 import UpdateComplianceControlResponse404
from ...models.update_compliance_control_response_500 import UpdateComplianceControlResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: ComplianceControl,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v4/compliance/control/{id}".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UpdateComplianceControlResponse200 | UpdateComplianceControlResponse400 | UpdateComplianceControlResponse401 | UpdateComplianceControlResponse403 | UpdateComplianceControlResponse404 | UpdateComplianceControlResponse500 | None:
    if response.status_code == 200:
        response_200 = UpdateComplianceControlResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = UpdateComplianceControlResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = UpdateComplianceControlResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = UpdateComplianceControlResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = UpdateComplianceControlResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = UpdateComplianceControlResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UpdateComplianceControlResponse200 | UpdateComplianceControlResponse400 | UpdateComplianceControlResponse401 | UpdateComplianceControlResponse403 | UpdateComplianceControlResponse404 | UpdateComplianceControlResponse500]:
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
    body: ComplianceControl,

) -> Response[UpdateComplianceControlResponse200 | UpdateComplianceControlResponse400 | UpdateComplianceControlResponse401 | UpdateComplianceControlResponse403 | UpdateComplianceControlResponse404 | UpdateComplianceControlResponse500]:
    """ Updates a Compliance Control in the application.

    Args:
        id (int):
        body (ComplianceControl): ComplianceControl defines a compliance control.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateComplianceControlResponse200 | UpdateComplianceControlResponse400 | UpdateComplianceControlResponse401 | UpdateComplianceControlResponse403 | UpdateComplianceControlResponse404 | UpdateComplianceControlResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: ComplianceControl,

) -> UpdateComplianceControlResponse200 | UpdateComplianceControlResponse400 | UpdateComplianceControlResponse401 | UpdateComplianceControlResponse403 | UpdateComplianceControlResponse404 | UpdateComplianceControlResponse500 | None:
    """ Updates a Compliance Control in the application.

    Args:
        id (int):
        body (ComplianceControl): ComplianceControl defines a compliance control.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateComplianceControlResponse200 | UpdateComplianceControlResponse400 | UpdateComplianceControlResponse401 | UpdateComplianceControlResponse403 | UpdateComplianceControlResponse404 | UpdateComplianceControlResponse500
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: ComplianceControl,

) -> Response[UpdateComplianceControlResponse200 | UpdateComplianceControlResponse400 | UpdateComplianceControlResponse401 | UpdateComplianceControlResponse403 | UpdateComplianceControlResponse404 | UpdateComplianceControlResponse500]:
    """ Updates a Compliance Control in the application.

    Args:
        id (int):
        body (ComplianceControl): ComplianceControl defines a compliance control.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateComplianceControlResponse200 | UpdateComplianceControlResponse400 | UpdateComplianceControlResponse401 | UpdateComplianceControlResponse403 | UpdateComplianceControlResponse404 | UpdateComplianceControlResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: ComplianceControl,

) -> UpdateComplianceControlResponse200 | UpdateComplianceControlResponse400 | UpdateComplianceControlResponse401 | UpdateComplianceControlResponse403 | UpdateComplianceControlResponse404 | UpdateComplianceControlResponse500 | None:
    """ Updates a Compliance Control in the application.

    Args:
        id (int):
        body (ComplianceControl): ComplianceControl defines a compliance control.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateComplianceControlResponse200 | UpdateComplianceControlResponse400 | UpdateComplianceControlResponse401 | UpdateComplianceControlResponse403 | UpdateComplianceControlResponse404 | UpdateComplianceControlResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
