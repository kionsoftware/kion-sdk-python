from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.compliance_standard_update import ComplianceStandardUpdate
from ...models.patch_compliance_standard_response_200 import PatchComplianceStandardResponse200
from ...models.patch_compliance_standard_response_400 import PatchComplianceStandardResponse400
from ...models.patch_compliance_standard_response_401 import PatchComplianceStandardResponse401
from ...models.patch_compliance_standard_response_403 import PatchComplianceStandardResponse403
from ...models.patch_compliance_standard_response_404 import PatchComplianceStandardResponse404
from ...models.patch_compliance_standard_response_422 import PatchComplianceStandardResponse422
from ...models.patch_compliance_standard_response_500 import PatchComplianceStandardResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: ComplianceStandardUpdate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v3/compliance/standard/{id}".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchComplianceStandardResponse200 | PatchComplianceStandardResponse400 | PatchComplianceStandardResponse401 | PatchComplianceStandardResponse403 | PatchComplianceStandardResponse404 | PatchComplianceStandardResponse422 | PatchComplianceStandardResponse500 | None:
    if response.status_code == 200:
        response_200 = PatchComplianceStandardResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PatchComplianceStandardResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchComplianceStandardResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchComplianceStandardResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PatchComplianceStandardResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PatchComplianceStandardResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchComplianceStandardResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchComplianceStandardResponse200 | PatchComplianceStandardResponse400 | PatchComplianceStandardResponse401 | PatchComplianceStandardResponse403 | PatchComplianceStandardResponse404 | PatchComplianceStandardResponse422 | PatchComplianceStandardResponse500]:
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
    body: ComplianceStandardUpdate,

) -> Response[PatchComplianceStandardResponse200 | PatchComplianceStandardResponse400 | PatchComplianceStandardResponse401 | PatchComplianceStandardResponse403 | PatchComplianceStandardResponse404 | PatchComplianceStandardResponse422 | PatchComplianceStandardResponse500]:
    """ Updates a compliance standard in the application.

    Args:
        id (int):
        body (ComplianceStandardUpdate): ComplianceStandardUpdate defines a Compliance Standard
            update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchComplianceStandardResponse200 | PatchComplianceStandardResponse400 | PatchComplianceStandardResponse401 | PatchComplianceStandardResponse403 | PatchComplianceStandardResponse404 | PatchComplianceStandardResponse422 | PatchComplianceStandardResponse500]
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
    body: ComplianceStandardUpdate,

) -> PatchComplianceStandardResponse200 | PatchComplianceStandardResponse400 | PatchComplianceStandardResponse401 | PatchComplianceStandardResponse403 | PatchComplianceStandardResponse404 | PatchComplianceStandardResponse422 | PatchComplianceStandardResponse500 | None:
    """ Updates a compliance standard in the application.

    Args:
        id (int):
        body (ComplianceStandardUpdate): ComplianceStandardUpdate defines a Compliance Standard
            update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchComplianceStandardResponse200 | PatchComplianceStandardResponse400 | PatchComplianceStandardResponse401 | PatchComplianceStandardResponse403 | PatchComplianceStandardResponse404 | PatchComplianceStandardResponse422 | PatchComplianceStandardResponse500
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
    body: ComplianceStandardUpdate,

) -> Response[PatchComplianceStandardResponse200 | PatchComplianceStandardResponse400 | PatchComplianceStandardResponse401 | PatchComplianceStandardResponse403 | PatchComplianceStandardResponse404 | PatchComplianceStandardResponse422 | PatchComplianceStandardResponse500]:
    """ Updates a compliance standard in the application.

    Args:
        id (int):
        body (ComplianceStandardUpdate): ComplianceStandardUpdate defines a Compliance Standard
            update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchComplianceStandardResponse200 | PatchComplianceStandardResponse400 | PatchComplianceStandardResponse401 | PatchComplianceStandardResponse403 | PatchComplianceStandardResponse404 | PatchComplianceStandardResponse422 | PatchComplianceStandardResponse500]
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
    body: ComplianceStandardUpdate,

) -> PatchComplianceStandardResponse200 | PatchComplianceStandardResponse400 | PatchComplianceStandardResponse401 | PatchComplianceStandardResponse403 | PatchComplianceStandardResponse404 | PatchComplianceStandardResponse422 | PatchComplianceStandardResponse500 | None:
    """ Updates a compliance standard in the application.

    Args:
        id (int):
        body (ComplianceStandardUpdate): ComplianceStandardUpdate defines a Compliance Standard
            update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchComplianceStandardResponse200 | PatchComplianceStandardResponse400 | PatchComplianceStandardResponse401 | PatchComplianceStandardResponse403 | PatchComplianceStandardResponse404 | PatchComplianceStandardResponse422 | PatchComplianceStandardResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
