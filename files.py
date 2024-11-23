import os

def merge_files_in_directory(directory_path):
    try:
        # Verifica se o diretório existe
        if not os.path.isdir(directory_path):
            print(f"Error: Directory '{directory_path}' does not exist.")
            return

        # Define o nome do arquivo de saída
        output_file = os.path.basename(directory_path.rstrip(os.sep)) + ".dat"

        with open(output_file, "w", encoding="utf-8") as outfile:
            for file_name in os.listdir(directory_path):
                file_path = os.path.join(directory_path, file_name)

                # Ignorar subdiretórios e apenas processar arquivos
                if os.path.isfile(file_path):
                    try:
                        with open(file_path, "r", encoding="utf-8") as infile:
                            content = infile.read()

                        # Adicionar o nome do arquivo e o conteúdo ao arquivo de saída
                        outfile.write(f"{file_name}#{content}|")
                    except Exception as e:
                        print(f"Could not read file '{file_name}': {e}")

        print(f"Output written to: {output_file}")

    except Exception as e:
        print(f"Error: {e}")


def main():
    directory_path = input("Enter the directory path: ").strip()
    merge_files_in_directory(directory_path)


if __name__ == "__main__":
    main()
