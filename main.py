import os
import pytest

if __name__ == '__main__':
    pytest.main(['-s', '-q', './Test_Case/', '--alluredir', './Test_Result/temp'])
    os.system('allure generate ./Test_Result/temp -o ./Test_Report --clean')
