import allure
from ddt import *
from unittest import TestCase

from request.getRequest import dataFromWeb
from src.Core.WorkWithCsv import WorkWithCsv


@ddt
class TestData(TestCase):
    def setUp(self):
         allure.attach.file("../files/testData.csv","test_data.csv",attachment_type=allure.attachment_type.CSV)

    @data(*WorkWithCsv.get_csv_data("../../getPostPython/files/testData.csv"))
    @unpack
    def testRequest(self,Route , StatusCode):
        statuscode = dataFromWeb.getData(self , Route)
        self.assertEqual(str(StatusCode) , str(statuscode))



