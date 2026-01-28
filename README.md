# robot-framework-101
This repository is for practicing my automation testing skill with Robot Framework.

## Project structure
```markdown
robot-framework-tests/
│
├── pyproject.toml
├── poetry.lock
├── README.md
├── .gitignore
│
├── test_suites/
│   ├── __init__.robot
│   │
│   ├── api/
│   │   ├── __init__.robot
│   │   ├── auth_tests.robot
│   │   └── user_tests.robot
│   │
│   ├── ui/
│   │   ├── __init__.robot
│   │   ├── login_tests.robot
│   │   └── dashboard_tests.robot
│   │
│   └── db/
│       ├── __init__.robot
│       └── migration_tests.robot
│
├── resources/
│   ├── common.resource
│   ├── variables.resource
│   ├── testdata.resource
│   ├── api_keywords.resource
│   ├── ui_keywords.resource
│   └── db_keywords.resource
│
├── libraries/
│   ├── __init__.py
│   ├── api_client.py
│   ├── db_client.py
│   └── auth_helper.py
│
├── environments/
│   ├── local.env
│   ├── staging.env
│   └── production.env
│
├── scripts/
│   ├── run_local.sh
│   ├── run_ci.sh
│   └── export_env.ps1
│
├── output/
│   ├── log.html
│   ├── report.html
│   └── output.xml
│
└── .github/
    └── workflows/
        └── robot-tests.yml

```


## Run all suite tests
`poetry run robot -d results/ test_suites`

## Run specific test with tags
`poetry run robot -d results/ --include test test_suites`
