# Pet project for Automation testing of AgileS
## Stack: Python(Pytest) + Selenium + Allure
## Database: PostgreSQL(SQLAlchemy)
### Done:

 - **users_creator**: Automatic users creation by parsing users.xlsx file with user data
and executing required steps in browser. Can create any amount of users. Password for any user: Godfather1989!
(at the moment, some issues with app when input pass). To see/modify users list - users_creator/users.xlsx
 - **ui**: UI automation testing of the web app deployed on local machine(Docker). So far, below features were covered:
   + Sign up page
   + Login page(Standard, Quick Access)
   + Feedback modal window
 - **api**: automation testing of API - TBD
 - **performance**: automation performance testing - TBD

### Execution tips:
 - `pytest --show-progress`  -  progress bar (default)
 - `pytest --verbose`  -  detailed progress (default)
 - `pytest --html=reports/full_chrome_report.html --self-contained-html`  -  generate HTML report
 - `pytest --browser chrome/edge/firefox`  -  launch on different browsers (chrome - default)
 - `pytest --reruns 2`  -  re-run failed tests (default)
 - `-n 2` - run 2 tests in parallel

### Report in Allure:
 - `pytest --alluredir=allure-report/`  -  generate allure report (default)
 - `pytest --screenshot=on --screenshot_path=off`  -  add screenshot to allure report, when test is failed (default)
 - `allure serve allure-report/`  -  open allure report
 - `allure generate --clean`  -  clean allure report
