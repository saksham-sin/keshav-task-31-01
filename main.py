from fastapi import FastAPI

app = FastAPI()

# Sample data (dictionary to store employees)
emp = {1: {"emp_name": "Keshav", "salary": 10000}}

# Get an employee by ID
@app.get("/employee/{emp_id}")
def read_item(emp_id: int):
    return emp.get(emp_id, {"error": "Item not found"})

# Create a new emp
@app.post("/employee/{emp_id}")
def create_item(emp_id: int, name: str, salary: float):
    if emp_id in emp:
        return {"error": "Item already exists"}
    emp[emp_id] = {"name": name, "salary": salary}
    return {"message": "Item created", "item": emp[emp_id]}

# Update an existing item
@app.put("/employee/{emp_id}")
def update_item(emp_id: int, emp_name: str, salary: int):
    if emp_id not in emp:
        return {"error": "Item not found"}
    emp[emp_id] = {"name": emp_name, "price": salary}
    return {"message": "Item updated", "item": emp[emp_id]}

# Delete an item
@app.delete("/employee/{emp_id}")
def delete_item(emp_id: int):
    if emp_id not in emp:
        return {"error": "Item not found"}
    del emp[emp_id]
    return {"message": "Item deleted"}