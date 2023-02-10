from test_application.test_webservice.test_api.configtest import client


def test_should_status_code_ok(client):
	response = client.get('/test')
	assert response.status_code == 200