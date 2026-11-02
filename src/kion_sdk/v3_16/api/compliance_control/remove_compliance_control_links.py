from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.compliance_control_links import ComplianceControlLinks
from ...models.remove_compliance_control_links_response_200 import RemoveComplianceControlLinksResponse200
from ...models.remove_compliance_control_links_response_400 import RemoveComplianceControlLinksResponse400
from ...models.remove_compliance_control_links_response_401 import RemoveComplianceControlLinksResponse401
from ...models.remove_compliance_control_links_response_403 import RemoveComplianceControlLinksResponse403
from ...models.remove_compliance_control_links_response_404 import RemoveComplianceControlLinksResponse404
from ...models.remove_compliance_control_links_response_422 import RemoveComplianceControlLinksResponse422
from ...models.remove_compliance_control_links_response_500 import RemoveComplianceControlLinksResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: ComplianceControlLinks,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v4/compliance/control/{id}/links".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RemoveComplianceControlLinksResponse200 | RemoveComplianceControlLinksResponse400 | RemoveComplianceControlLinksResponse401 | RemoveComplianceControlLinksResponse403 | RemoveComplianceControlLinksResponse404 | RemoveComplianceControlLinksResponse422 | RemoveComplianceControlLinksResponse500 | None:
    if response.status_code == 200:
        response_200 = RemoveComplianceControlLinksResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = RemoveComplianceControlLinksResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = RemoveComplianceControlLinksResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = RemoveComplianceControlLinksResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = RemoveComplianceControlLinksResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = RemoveComplianceControlLinksResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = RemoveComplianceControlLinksResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RemoveComplianceControlLinksResponse200 | RemoveComplianceControlLinksResponse400 | RemoveComplianceControlLinksResponse401 | RemoveComplianceControlLinksResponse403 | RemoveComplianceControlLinksResponse404 | RemoveComplianceControlLinksResponse422 | RemoveComplianceControlLinksResponse500]:
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
    body: ComplianceControlLinks,

) -> Response[RemoveComplianceControlLinksResponse200 | RemoveComplianceControlLinksResponse400 | RemoveComplianceControlLinksResponse401 | RemoveComplianceControlLinksResponse403 | RemoveComplianceControlLinksResponse404 | RemoveComplianceControlLinksResponse422 | RemoveComplianceControlLinksResponse500]:
    """ Removes compliance control links in the system

    Args:
        id (int):
        body (ComplianceControlLinks): ComplianceControlLinks defines a set of compliance-control
            to asset links in the system.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoveComplianceControlLinksResponse200 | RemoveComplianceControlLinksResponse400 | RemoveComplianceControlLinksResponse401 | RemoveComplianceControlLinksResponse403 | RemoveComplianceControlLinksResponse404 | RemoveComplianceControlLinksResponse422 | RemoveComplianceControlLinksResponse500]
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
    body: ComplianceControlLinks,

) -> RemoveComplianceControlLinksResponse200 | RemoveComplianceControlLinksResponse400 | RemoveComplianceControlLinksResponse401 | RemoveComplianceControlLinksResponse403 | RemoveComplianceControlLinksResponse404 | RemoveComplianceControlLinksResponse422 | RemoveComplianceControlLinksResponse500 | None:
    """ Removes compliance control links in the system

    Args:
        id (int):
        body (ComplianceControlLinks): ComplianceControlLinks defines a set of compliance-control
            to asset links in the system.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoveComplianceControlLinksResponse200 | RemoveComplianceControlLinksResponse400 | RemoveComplianceControlLinksResponse401 | RemoveComplianceControlLinksResponse403 | RemoveComplianceControlLinksResponse404 | RemoveComplianceControlLinksResponse422 | RemoveComplianceControlLinksResponse500
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
    body: ComplianceControlLinks,

) -> Response[RemoveComplianceControlLinksResponse200 | RemoveComplianceControlLinksResponse400 | RemoveComplianceControlLinksResponse401 | RemoveComplianceControlLinksResponse403 | RemoveComplianceControlLinksResponse404 | RemoveComplianceControlLinksResponse422 | RemoveComplianceControlLinksResponse500]:
    """ Removes compliance control links in the system

    Args:
        id (int):
        body (ComplianceControlLinks): ComplianceControlLinks defines a set of compliance-control
            to asset links in the system.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoveComplianceControlLinksResponse200 | RemoveComplianceControlLinksResponse400 | RemoveComplianceControlLinksResponse401 | RemoveComplianceControlLinksResponse403 | RemoveComplianceControlLinksResponse404 | RemoveComplianceControlLinksResponse422 | RemoveComplianceControlLinksResponse500]
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
    body: ComplianceControlLinks,

) -> RemoveComplianceControlLinksResponse200 | RemoveComplianceControlLinksResponse400 | RemoveComplianceControlLinksResponse401 | RemoveComplianceControlLinksResponse403 | RemoveComplianceControlLinksResponse404 | RemoveComplianceControlLinksResponse422 | RemoveComplianceControlLinksResponse500 | None:
    """ Removes compliance control links in the system

    Args:
        id (int):
        body (ComplianceControlLinks): ComplianceControlLinks defines a set of compliance-control
            to asset links in the system.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoveComplianceControlLinksResponse200 | RemoveComplianceControlLinksResponse400 | RemoveComplianceControlLinksResponse401 | RemoveComplianceControlLinksResponse403 | RemoveComplianceControlLinksResponse404 | RemoveComplianceControlLinksResponse422 | RemoveComplianceControlLinksResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
