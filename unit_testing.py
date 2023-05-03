from webpage.views import index_page
from django.test import RequestFactory
from django.urls import reverse

def test_get_stock_data():
    request = RequestFactory().get(reverse('stocks'))
    response = index_page(request)
    assert response.status_code == 200