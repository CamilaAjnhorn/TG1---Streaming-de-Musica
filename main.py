from Streaming.menu import Menu
from Streaming.utils import registrar_erro

def main():
    try:
        menu = Menu()
        menu.menu_principal()
    except Exception as e:
        registrar_erro(f"[Main] Erro ao iniciar sistema: {e}")
        print("Erro ao iniciar sistema")


if __name__ == "__main__":
    main()