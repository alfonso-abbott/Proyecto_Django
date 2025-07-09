#!/usr/bin/env python3
"""Script auxiliar para ejecutar el servidor y abrir el navegador."""

import subprocess
import webbrowser
from threading import Timer


def main() -> None:
    """Inicia el servidor Django y abre la página principal."""
    # Ejecutamos ``manage.py runserver`` en un subproceso
    proc = subprocess.Popen(["python", "manage.py", "runserver"])

    # Tras unos segundos, abrimos el navegador por defecto
    Timer(2, lambda: webbrowser.open("http://127.0.0.1:8000/")).start()

    try:
        proc.wait()
    except KeyboardInterrupt:
        proc.terminate()


if __name__ == "__main__":
    main()
