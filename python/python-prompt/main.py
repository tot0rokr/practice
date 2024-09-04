from pathlib import Path
from prompt_toolkit import PromptSession, print_formatted_text
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.lexers import PygmentsLexer

hist_file = Path('./sample_history').expanduser()

if not hist_file.exists():
    hist_file.touch()

session: PromptSession = PromptSession(history=FileHistory(str(hist_file)))
session.auto_suggest = AutoSuggestFromHistory()
session.completer = WordCompleter(['rpc_call'])

restricted_global = {}
restricted_local = {}

while True:
    try:
        text = session.prompt('>>> ')
    except KeyboardInterrupt:
        print_formatted_text("Interrupt")
        break
    print_formatted_text(text)
    try:
        exec(text, restricted_global, restricted_local)
    except Exception as e:
        print_formatted_text(f"An error occurred: {e}")
