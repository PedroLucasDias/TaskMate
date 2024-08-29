from typing import Any

def validate(obj: Any) -> Any:
    """
    Valida se o objeto é compatível com os tipos JSON aceitos.

    Return: retorna uma cópia profunda do obj caso ele passe na validação.
    """

    if isinstance(obj, dict):
        return {k: validate(v) for k, v in obj.items()}

    if isinstance(obj, list):
        return [validate(i) for i in obj]

    if isinstance(obj, (str, int, float, bool, type(None))):
        return obj

    raise ValueError("Tipo de dados JSON inválido")
