from automaton.automaton import AutomatonValidator
from automaton.importer import load_from_jff
import json
import os

def main():
    data_path = "data"
    
    print("Escolha a opção para validar o autômato:")
    print("1. Utilizar um arquivo JFLAP (.jff)")
    print("2. Informar os dados através de uma hash")
    choice = input("Digite 1 ou 2: ")

    if choice == "1":
        file_name = input("Informe o nome do arquivo JFLAP (.jff) na pasta 'data': ").strip()
        file_path = os.path.join(data_path, file_name)
        try:
            automaton_data = load_from_jff(file_path)
            validator = AutomatonValidator(automaton_data)
            print("\nResultado da validação do autômato:")
            print(validator.validate())

            input_file = os.path.join(data_path, "inputs.txt")
            print("\nValidando entradas do arquivo inputs.txt...")
            with open(input_file, "r") as f:
                inputs = [line.strip() for line in f.readlines()]

            for input_string in inputs:
                print(validator.validate_input(input_string))
        except Exception as e:
            print(f"Erro: {e}")

    elif choice == "2":
        file_name = input("Informe o nome do arquivo JSON (hash) na pasta 'data': ").strip()
        file_path = os.path.join(data_path, file_name)
        try:
            with open(file_path, "r") as file:
                automaton_data = json.load(file)
            validator = AutomatonValidator(automaton_data)
            print("\nResultado da validação do autômato:")
            print(validator.validate())

            input_file = os.path.join(data_path, "inputs.txt")
            print("\nValidando entradas do arquivo inputs.txt...")
            with open(input_file, "r") as f:
                inputs = [line.strip() for line in f.readlines()]

            for input_string in inputs:
                print(validator.validate_input(input_string))
        except FileNotFoundError:
            print(f"Erro: O arquivo '{file_name}' não foi encontrado na pasta 'data'.")
        except json.JSONDecodeError:
            print("Erro: Dados inválidos. Certifique-se de que o JSON está correto.")
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")


if __name__ == "__main__":
    main()
