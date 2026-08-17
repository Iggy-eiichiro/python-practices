try:
    with open(r"c:\Users\bro\OneDrive\デスクトップ\R23A2032_Kmg006PDF01_20260424100021834.pdf","rb") as file:
    # with open(r"txt.biscuit","r") as file:
        # end of the run, closed te file automotically 
        # First r(). In oreder to use as a normal character of //. do not interpret this // as aspecial character.
        # Second "r"("rb") is one of the file mode. which mean "read"("read binary").
        data = file.read()
        print(data)

except FileNotFoundError:
    print("Error: file not found")

finally:
    print("File closed")

