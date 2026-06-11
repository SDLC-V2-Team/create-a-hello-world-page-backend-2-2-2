import pytest
from unittest.mock import Mock, patch
import os
import http.server
import socketserver
import server


def test_port_constant():
    assert server.PORT == 8000


def test_directory_constant_is_valid():
    assert isinstance(server.DIRECTORY, str)
    assert os.path.isdir(server.DIRECTORY)


def test_handler_is_subclass_of_simple_handler():
    assert issubclass(server.Handler, http.server.SimpleHTTPRequestHandler)


@patch('socketserver.BaseRequestHandler.__init__', return_value=None)
@patch('http.server.SimpleHTTPRequestHandler.__init__')
def test_handler_init_passes_directory(mock_super_init, mock_base_init):
    request = Mock()
    client_address = ('127.0.0.1', 12345)
    srv = Mock()
    handler = server.Handler(request, client_address, srv)
    mock_super_init.assert_called_once_with(
        request, client_address, srv,
        directory=server.DIRECTORY
    )


def test_run_server_creates_tcpserver_and_serves_forever():
    with patch('server.socketserver.TCPServer') as MockTCPServer:
        mock_server = MockTCPServer.return_value.__enter__.return_value
        server.run_server()
        MockTCPServer.assert_called_once_with(("", server.PORT), server.Handler)
        mock_server.serve_forever.assert_called_once_with()