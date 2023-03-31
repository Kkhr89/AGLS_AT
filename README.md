# Pet project for Automation testing of AgileS
## Stack: Pytest + Selenium + Allure
## Database: PostgeSQL
### Done:

 - **users_creator**: Automatic users creation by parsing users.xlsx file with user data
and executing required steps in browser. Can create any amount of users. Password for any user: Godfather1989!
(at the moment, some issues with app when input pass)

### Execution tips:
 - `pytest --show-progress`  -  progress bar (default)
 - `pytest --verbose`  -  detailed progress (default)
 - `pytest --html=reports/full_chrome_report.html --self-contained-html`  -  generate HTML report
 - `pytest --browser chrome/edge/firefox`  -  launch on different browsers (chrome - default)
 - `pytest --reruns 2`  -  re-run failed tests (default)

### Allure:
 - `pytest --alluredir=allure-report/`  -  generate allure report (default)
 - `pytest --screenshot=on --screenshot_path=off`  -  add screenshot to allure report, when test is failed (default)
 - `allure serve allure-report/`  -  open allure report
 - `allure generate --clean`  -  clean allure report
