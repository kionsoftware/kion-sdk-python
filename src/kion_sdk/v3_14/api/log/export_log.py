from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.export_log_response_201 import ExportLogResponse201
from ...models.export_log_response_400 import ExportLogResponse400
from ...models.export_log_response_401 import ExportLogResponse401
from ...models.export_log_response_403 import ExportLogResponse403
from ...models.export_log_response_422 import ExportLogResponse422
from ...models.export_log_response_500 import ExportLogResponse500
from ...models.log_export import LogExport
from typing import cast



def _get_kwargs(
    *,
    body: LogExport,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/log/export",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ExportLogResponse201 | ExportLogResponse400 | ExportLogResponse401 | ExportLogResponse403 | ExportLogResponse422 | ExportLogResponse500 | None:
    if response.status_code == 201:
        response_201 = ExportLogResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = ExportLogResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ExportLogResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = ExportLogResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = ExportLogResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = ExportLogResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ExportLogResponse201 | ExportLogResponse400 | ExportLogResponse401 | ExportLogResponse403 | ExportLogResponse422 | ExportLogResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: LogExport,

) -> Response[ExportLogResponse201 | ExportLogResponse400 | ExportLogResponse401 | ExportLogResponse403 | ExportLogResponse422 | ExportLogResponse500]:
    """ Exports logs.

    Args:
        body (LogExport): LogExport defines a Log Export.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExportLogResponse201 | ExportLogResponse400 | ExportLogResponse401 | ExportLogResponse403 | ExportLogResponse422 | ExportLogResponse500]
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
    body: LogExport,

) -> ExportLogResponse201 | ExportLogResponse400 | ExportLogResponse401 | ExportLogResponse403 | ExportLogResponse422 | ExportLogResponse500 | None:
    """ Exports logs.

    Args:
        body (LogExport): LogExport defines a Log Export.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExportLogResponse201 | ExportLogResponse400 | ExportLogResponse401 | ExportLogResponse403 | ExportLogResponse422 | ExportLogResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: LogExport,

) -> Response[ExportLogResponse201 | ExportLogResponse400 | ExportLogResponse401 | ExportLogResponse403 | ExportLogResponse422 | ExportLogResponse500]:
    """ Exports logs.

    Args:
        body (LogExport): LogExport defines a Log Export.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExportLogResponse201 | ExportLogResponse400 | ExportLogResponse401 | ExportLogResponse403 | ExportLogResponse422 | ExportLogResponse500]
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
    body: LogExport,

) -> ExportLogResponse201 | ExportLogResponse400 | ExportLogResponse401 | ExportLogResponse403 | ExportLogResponse422 | ExportLogResponse500 | None:
    """ Exports logs.

    Args:
        body (LogExport): LogExport defines a Log Export.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExportLogResponse201 | ExportLogResponse400 | ExportLogResponse401 | ExportLogResponse403 | ExportLogResponse422 | ExportLogResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
