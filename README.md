# API Test Automation

This is a simple Python project for testing the Petstore API.

## Project Description

This project tests the Petstore API using Python. It does **CRUD** operations:

- **Create**: Add a new pet.
- **Read**: Get pet information.
- **Update**: Change pet information.
- **Delete**: Remove a pet.

## How to Use

1. **Clone the project**:
   ```
   git clone https://github.com/agkocaman/TestAutomationAPI.git
   ```
   
2. **Go to the project folder**:
   ```
   cd TestAutomationAPI
   ```

3. **Run the code**:
   ```
   python test_petstore_api.py
   ```


## Code Details

- **Create**:
  - `create_positive()`: Adds a pet with valid data.
  - `create_negative()`: Tries to add a pet with invalid data.
  
- **Read**:
  - `get_positive()`: Gets a pet with a valid ID.
  - `get_negative()`: Tries to get a pet with a non-existent ID.
  
- **Update**:
  - `update_positive()`: Updates a pet with valid data.
  - `update_negative()`: Tries to update a pet with invalid data.
  
- **Delete**:
  - `delete_positive()`: Deletes a pet with a valid ID.
  - `delete_negative()`: Tries to delete a pet with a non-existent ID.

## Requirements

- Python 3
- `requests` library

To install the `requests` library, use:
```
pip install requests
```

## Important Notes

- This is a simple project.
- It is for learning purposes.
