
def gauss_sum(n: int):
    """Using Gauss sum"""
    return int((n+1)*n/2)

# Defining main function
def main():
    print("Resultado da soma:", gauss_sum(int(input("Digite um numero: "))) )


# __name__
if __name__=="__main__":
	main()