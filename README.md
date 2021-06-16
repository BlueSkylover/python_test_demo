# python_test_demo

Repo for all test automation

Pre-Requisites
---------------
* Python >3.5
* Test Runner:[Ptest](https://github.com/KarlGong/ptest/wiki/documentation)

Setup Environment
---------------

Change to repo directory
|cd cn-test-automation|

Install python packages
|pip install -r requirements.txt|

Run tests
-------------------

Run all tests in tests directory, using configuration values in config.ini
|ptest -t tests -p config.ini|

Run all smoke tests in tests directory, using configuration values in config.ini
|ptest -t tests -p config.ini -i smoke|

Test report will be located at test-output folder. Open /test-output/html-report/index.html to view detail html report
