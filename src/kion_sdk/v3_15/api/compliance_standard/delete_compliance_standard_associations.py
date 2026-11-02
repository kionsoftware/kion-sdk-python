from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.compliance_standard_associations import ComplianceStandardAssociations
from ...models.delete_compliance_standard_associations_response_200 import DeleteComplianceStandardAssociationsResponse200
from ...models.delete_compliance_standard_associations_response_400 import DeleteComplianceStandardAssociationsResponse400
from ...models.delete_compliance_standard_associations_response_401 import DeleteComplianceStandardAssociationsResponse401
from ...models.delete_compliance_standard_associations_response_403 import DeleteComplianceStandardAssociationsResponse403
from ...models.delete_compliance_standard_associations_response_404 import DeleteComplianceStandardAssociationsResponse404
from ...models.delete_compliance_standard_associations_response_422 import DeleteComplianceStandardAssociationsResponse422
from ...models.delete_compliance_standard_associations_response_500 import DeleteComplianceStandardAssociationsResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: ComplianceStandardAssociations,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/compliance/standard/{id}/association".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteComplianceStandardAssociationsResponse200 | DeleteComplianceStandardAssociationsResponse400 | DeleteComplianceStandardAssociationsResponse401 | DeleteComplianceStandardAssociationsResponse403 | DeleteComplianceStandardAssociationsResponse404 | DeleteComplianceStandardAssociationsResponse422 | DeleteComplianceStandardAssociationsResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteComplianceStandardAssociationsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = DeleteComplianceStandardAssociationsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteComplianceStandardAssociationsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DeleteComplianceStandardAssociationsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DeleteComplianceStandardAssociationsResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = DeleteComplianceStandardAssociationsResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = DeleteComplianceStandardAssociationsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteComplianceStandardAssociationsResponse200 | DeleteComplianceStandardAssociationsResponse400 | DeleteComplianceStandardAssociationsResponse401 | DeleteComplianceStandardAssociationsResponse403 | DeleteComplianceStandardAssociationsResponse404 | DeleteComplianceStandardAssociationsResponse422 | DeleteComplianceStandardAssociationsResponse500]:
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
    body: ComplianceStandardAssociations,

) -> Response[DeleteComplianceStandardAssociationsResponse200 | DeleteComplianceStandardAssociationsResponse400 | DeleteComplianceStandardAssociationsResponse401 | DeleteComplianceStandardAssociationsResponse403 | DeleteComplianceStandardAssociationsResponse404 | DeleteComplianceStandardAssociationsResponse422 | DeleteComplianceStandardAssociationsResponse500]:
    """ Removes associations to a Compliance Standard.

    Args:
        id (int):
        body (ComplianceStandardAssociations): ComplianceStandardAssociations defines a Compliance
            Standard association update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteComplianceStandardAssociationsResponse200 | DeleteComplianceStandardAssociationsResponse400 | DeleteComplianceStandardAssociationsResponse401 | DeleteComplianceStandardAssociationsResponse403 | DeleteComplianceStandardAssociationsResponse404 | DeleteComplianceStandardAssociationsResponse422 | DeleteComplianceStandardAssociationsResponse500]
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
    body: ComplianceStandardAssociations,

) -> DeleteComplianceStandardAssociationsResponse200 | DeleteComplianceStandardAssociationsResponse400 | DeleteComplianceStandardAssociationsResponse401 | DeleteComplianceStandardAssociationsResponse403 | DeleteComplianceStandardAssociationsResponse404 | DeleteComplianceStandardAssociationsResponse422 | DeleteComplianceStandardAssociationsResponse500 | None:
    """ Removes associations to a Compliance Standard.

    Args:
        id (int):
        body (ComplianceStandardAssociations): ComplianceStandardAssociations defines a Compliance
            Standard association update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteComplianceStandardAssociationsResponse200 | DeleteComplianceStandardAssociationsResponse400 | DeleteComplianceStandardAssociationsResponse401 | DeleteComplianceStandardAssociationsResponse403 | DeleteComplianceStandardAssociationsResponse404 | DeleteComplianceStandardAssociationsResponse422 | DeleteComplianceStandardAssociationsResponse500
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
    body: ComplianceStandardAssociations,

) -> Response[DeleteComplianceStandardAssociationsResponse200 | DeleteComplianceStandardAssociationsResponse400 | DeleteComplianceStandardAssociationsResponse401 | DeleteComplianceStandardAssociationsResponse403 | DeleteComplianceStandardAssociationsResponse404 | DeleteComplianceStandardAssociationsResponse422 | DeleteComplianceStandardAssociationsResponse500]:
    """ Removes associations to a Compliance Standard.

    Args:
        id (int):
        body (ComplianceStandardAssociations): ComplianceStandardAssociations defines a Compliance
            Standard association update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteComplianceStandardAssociationsResponse200 | DeleteComplianceStandardAssociationsResponse400 | DeleteComplianceStandardAssociationsResponse401 | DeleteComplianceStandardAssociationsResponse403 | DeleteComplianceStandardAssociationsResponse404 | DeleteComplianceStandardAssociationsResponse422 | DeleteComplianceStandardAssociationsResponse500]
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
    body: ComplianceStandardAssociations,

) -> DeleteComplianceStandardAssociationsResponse200 | DeleteComplianceStandardAssociationsResponse400 | DeleteComplianceStandardAssociationsResponse401 | DeleteComplianceStandardAssociationsResponse403 | DeleteComplianceStandardAssociationsResponse404 | DeleteComplianceStandardAssociationsResponse422 | DeleteComplianceStandardAssociationsResponse500 | None:
    """ Removes associations to a Compliance Standard.

    Args:
        id (int):
        body (ComplianceStandardAssociations): ComplianceStandardAssociations defines a Compliance
            Standard association update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteComplianceStandardAssociationsResponse200 | DeleteComplianceStandardAssociationsResponse400 | DeleteComplianceStandardAssociationsResponse401 | DeleteComplianceStandardAssociationsResponse403 | DeleteComplianceStandardAssociationsResponse404 | DeleteComplianceStandardAssociationsResponse422 | DeleteComplianceStandardAssociationsResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
