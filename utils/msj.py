from colorama import init, Fore

init()


def msj_drop_and_create():
	print(Fore.LIGHTCYAN_EX + ">>> ", end="")
	print(Fore.LIGHTBLUE_EX + "DROP all tables and CREATE all tables in database", end="")
	print(Fore.LIGHTCYAN_EX + " <<<" + Fore.RESET)
