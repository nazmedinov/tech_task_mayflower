# Test task for the Mayflower company
UI tests for https://mega.readyscript.ru/ site

## Running tests in docker
1. Go to the project root folder
2. Run the command for starting Docker containers in detached mode:
`docker-compose -p mayflower up -d`
3. Run the command for accessing terminal of tests container:
`docker exec -it mayflower-tests-1 /bin/bash`
4. Run the command for starting tests: 
`pytest`

## Running tests locally
1. Go to the project root folder
2. Run the command to create virtual environment: 
`python3 -m venv venv`
3. Run the command to activate the virtual environment: 
`source venv/bin/activate` for macOS/Linux or `venv\Scripts\activate` for Windows
4. Run the command to install required dependencies for start tests: 
`pip install -r requirements.txt`
5. Run the command for starting tests: 
`pytest --run_env=local`
