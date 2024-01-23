# test-server-automated-tests


## Automated tests
1. Install dependencies using command

       pip3 install -r requirements.txt


2. Launch test-server on http://localhost:8000 URL

3. Run all tests using command

       python3 -m pytest --alluredir allure_results

4. OR run only smoke tests using command

       python3 -m pytest -v -m "smoke" --alluredir allure_results

5. Generate report using command 

       allure generate -o allure_report -c allure_results

6. Open report using command 

       allure open allure_report

## Manual testing documentation

Checklist with current testing status is located in checklist folder

