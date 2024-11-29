# LeetCode tasks

__NOTE__ 
This project is for now work in progress for non-full functionality and close to 1% of the completed tasks in [LeetCode](https://leetcode.com/) are not imported 
__NOTE__

Collection of completed LeetCode tasks in various programming languages

In [tasks](tasks/) all tasks that are completed in [LeetCode](https://leetcode.com/) and imported to this repository are.
In the language specific folders (e.g. [python](python/) and [cplusplus](cplusplus/)) there are symbolic links to the respective tasks in the [tasks](tasks/) folder

New tasks are supposed to be added in the [tasks](tasks/) folder, and during committing, a pre-commit hook creates the symbolic link if it does not exists. This is done by looking at the file ending and finding the appropriate folder.

## TODO list
- [ ] README info on below 
- [ ] Import remaning tasks and create tests
- [ ] Create script check if all files are in correct folder
- [ ] pre-commit hook to check if all files are in correct folder
- [ ] Create script that sort files and creates symlinks (if they don't exist)
- [ ] Add documentation for above
- [ ] pre-commit hook to sort files and symlinks (mklink)
- [x] pre-commit hook on formatting
- [x] pre-commit hook on unit tests
- [x] unit tests (from leet code)
- [x] virtual environment and requirements.txt/requirements.in
- [ ] pyright
- [ ] fix coverage, where is the report created, update documentation


#### Install locally

To install the repository locally you can run this command:

```bash
pip install -e .
```

### Virtual environment

To create and activate the virtual environment, install the requirements, run:

```bash
python -m venv ./venv
source venv/bin/activate
#python -m pip install --upgrade pip # Optional step
pip install -r requirements.txt --upgrade

deactivate # To exit the environment
```

### Run unit tests

For every task there are unit tests to check that the implementation works as expected. These test cases are imported from its respective task on [LeetCode](https://leetcode.com/), but in many cases additional test cases are added for more coverage and robust checking of functionality.

To run the test cases, follow the instructions above in [Virtual environment](#virtual-environment) chapter and then run:

```bash
pytest # To simply run the tests
coverage run -m pytest -v tests -Werror --log-level debug # To run the tests and create a report on the code coverage
```

### Pre commit hooks

This repository runs several scripts and checks before a commit can be created. Check [.git-hooks](.git-hooks/) for what is actually run.

To activate the git hooks locally run this command:
```bash
git config --local core.hooksPath .git-hooks
```

### Generate requirements file

The requirements in [requirements.txt](requirements.txt) is created by `pip-compile` command. 

When you add a new package add it to [requirements.in](requirements.in) and then follow the instructions above in [Virtual environment](#virtual-environment) chapter and then run:

```bash
pip-compile --no-emit-index-url --output requirements.txt requirements.in
```