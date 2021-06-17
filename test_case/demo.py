__author__ = 'Nancy'

from ptest.assertion import assert_equals, assert_not_none, assert_true
from ptest.decorator import TestClass, Test
from ptest.plogger import preporter
import requests

from common.test_tag import TestType
from common.test_result_send import SendEmail


@TestClass(run_mode='singleline')
class DemoTest:
    @Test(tags=[TestType.smoke])
    def get_weather_api_test(self):
        response = requests.get(url="http://caiyunapp.com/fcgi-bin/v1/apicount.py?_=1623769588738")
        preporter.info(response.json())
        assert_equals(actual=response.status_code, expected=200)

    @Test(tags=[TestType.smoke])
    def post_phone_number_resource_api_test(self):
        body = {
            "data": "06159f611902e66104bee33262801cc1e65d519bab09ac08df958d591b169c799d850258f892bd7d032b49dc94dbe38956eaa2322a65b3af43f90920eb5dc32f3268e336fe2ceed7257875ee8b872695a0557f119637450e7efb68b4e5e9b561",
            "key_id": "47",
            "page": 1,
            "search": "075561008736",
            "sign": "e5fb4d57",
            "size": 10
        }
        headers = {"Content-Type": "application/json"}
        response = requests.post(url="https://haoma.baidu.com/api/v1/search", json=body, headers=headers)

        '''
               print the content of response
        '''
        preporter.info(response.json())
        # add assert,assert status is 200
        assert_equals(actual=response.status_code, expected=200)
        SendEmail.sendtext("test result of post phone number resource api test ", response.json())
