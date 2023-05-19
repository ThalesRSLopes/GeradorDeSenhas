import random


class GeradorSenhas:
    limite_inferior_tam = 4
    limite_superior_tam = 20

    def __init__(self, tamanho_senha):
        self.senha = self.gerar_senha(tamanho_senha)

    def gerar_senha(self, tamanho_senha):
        """
        Função retorna uma senha aleatória com a quantidade de caracteres
        especificado no argumento de entrada (padrão = 12)
        """

        # Verificação se o tamanho fornecido realmente é um número inteiro
        if type(tamanho_senha) is not int:
            raise ValueError

        # Verificação se o tamanho é um número entre o limite permitido
        if not GeradorSenhas.limite_inferior_tam <= tamanho_senha <= GeradorSenhas.limite_superior_tam:
            raise TamanhoInvalido(tamanho_senha)

        # Definição de todos os conjuntos de caracteres possíveis
        letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
        letras_maiusculas = letras_minusculas.upper()
        especiais = "!@#$%&"
        numeros = "0123456789"

        # Junção de todos os caracteres possíveis para a senha em uma única string
        caracteres = letras_minusculas + letras_maiusculas + especiais + numeros

        """
        Normalmente as senhas utilizadas exigem pelo menos:
            - uma letra minuscula
            - uma letra maiuscula
            - um número
            - um caractere especial

        Aqui são inseridos de cara um de cada desses elementos para garantir que estarão presentes na senha final.
        """
        senha = random.choice(letras_minusculas) + random.choice(letras_maiusculas) + random.choice(
            especiais) + random.choice(numeros)

        # São selecionados aleatóriamente o restante dos caracteres para complementar a senha.
        # O número de caracteres restantes é o tamanho final da senha menos 4, que são os já escolhidos anteriormente.
        senha += ''.join(random.sample(caracteres, tamanho_senha - 4))

        # É feito o embaralhamento da string para modificar as posições dos 4 primeiros.
        senha = list(senha)
        random.shuffle(senha)

        # A senha é transformada em uma string novamente.
        return ''.join(senha)


class TamanhoInvalido(Exception):
    "Ativado quando o tamanho da senha é um valor fora do limite permitido"

    def __init__(self, message=f"O tamanho da senha deve ser um "
                                        f"número inteiro entre {GeradorSenhas.limite_inferior_tam} e "
                                        f"{GeradorSenhas.limite_superior_tam}"):
        self.message = message
        super().__init__(self.message)


if __name__ == '__main__':
    try:
        tamanho = int(input(f"Digite o tamanho da senha final "
                            f"(entre {GeradorSenhas.limite_inferior_tam} e "
                            f"{GeradorSenhas.limite_superior_tam} caracteres: "))
        print(GeradorSenhas(tamanho).senha)
    except ValueError:
        print("O tamanho deve ser um número inteiro")
    except TamanhoInvalido:
        print(TamanhoInvalido().message)
