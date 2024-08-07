import mlflow

def calculator(a,b,ops = "add"):
    if ops == "add":
        return (a+b)
    if ops == "sub":
        return (a-b)
    if ops == "multiply":
        return (a*b)
    if ops == "divide":
        return (a/b)
    if ops == "%":
        return (a%b)
    

if __name__ == "__main__":
    a,b,ops = 40230, 324344,"divide"
    with mlflow.start_run():
        result = calculator(a,b, ops)
        mlflow.log_param("a",a)
        mlflow.log_param("b",b)
        mlflow.log_param("ops",ops)
        print(f"The result is {result}")
        mlflow.log_param("result",result)